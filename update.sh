sudo cp test.yaml /opt/stackstorm/configs/test.yaml
sudo rm -rf /opt/stackstorm/packs/test && sudo cp -r ../st2-sensors /opt/stackstorm/packs/test
st2 run packs.setup_virtualenv packs=test
st2ctl reload --register-all
