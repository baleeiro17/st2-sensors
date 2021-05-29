import requests
import json
from st2reactor.sensor.base import PollingSensor


class portal_sensor(PollingSensor):

    def setup(self):
        self.logger = self.sensor_service.get_logger(
            name=self.__class__.__name__)
        self.address_portal = self._config['simulation_portal']['address']
        self.logger.info("got dashboard address: %s", self.address_portal)

    def poll(self):
        try:
            url = self.address_portal + "/reservations"
            self.logger.info("polling at url %s", url)
            header = {"Content-Type": "application/json"}
            job_data = requests.get(url, timeout=10, headers=header).json()

            # dispatch trigger
            self.sensor_service.dispatch(
                trigger="test.start_trigger",
                payload={
                    "ssh_key": str(job_data['sshkeys']['ssh_public_key'])
                }
            )
        except Exception as e:
            self.logger.exception("Failed to poll(): %s", str(e))

    # Sensor Interface Methods #

    def cleanup(self):
        # called when st2 goes down
        pass

    def add_trigger(self, trigger):
        # called when trigger is created
        pass

    def update_trigger(self, trigger):
        # called when trigger is updated
        pass

    def remove_trigger(self, trigger):
        # called when trigger is deleted
        pass
