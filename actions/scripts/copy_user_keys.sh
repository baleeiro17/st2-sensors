#!/bin/bash

KEY="$1"
USERNAME="$2"
HOST_IP="$3"

echo "$KEY" > ~/tmpkey.pub

RET=0
ssh-copy-id -f -i ~/tmpkey.pub -o userknownhostsfile=/dev/null -o stricthostkeychecking=no "$USERNAME"@"$HOST_IP" || RET=1
rm -f ~/tmpkey.pub

exit $RET