from st2actions.runners.pythonrunner import Action
import requests
import json
import sys


class ChangeJobStatus(Action):
    def __init__(self, config=None):
        super(ChangeJobStatus, self).__init__(config=config)
        self.address_portal = self._config['simulation_portal']['address']

    def run(self, job_id=None, job_status=None):
        """
        Change reservation status
        """
        try:
            # job_
            headers = {"Content-Type": "application/json"}
            reservation_id = job_id[4:]
            url = self.address_portal + "/reservations/" + reservation_id
            payload = {'status': job_status}
            requests.put(url, data=json.dumps(payload), headers=headers)
        except Exception as e:
            print(e)
            sys.exit(1)
