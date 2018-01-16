#!/bin/bash

#CHANGE THESE VARS
: "${mountedDisk:="$HOME/Documents/projects/DSHTesting/mountedDisk"}"
IP=`ifconfig | grep inet | grep -v inet6 | head -1 | awk '{print $2}' | cut -d':' -f2`
topic='vialis'
CREDENTIALSID='546bf002-fbb8-48e8-ba3c-8a6f10ae5f74'

#CODE
if [ ! -d "$mountedDisk" ]; then
  mkdir $mountedDisk
  chmod 777 $mountedDisk
fi

sed -i -e "s/IPADDRESS/$IP/g" "py/TenantRestConfig.py"
sed -i -e "s#PATHTOMOUNTEDDISK#$mountedDisk#g" "py/TenantRestConfig.py"
sed -i -e "s/TOPIC/$topic/g" "py/TenantRestConfig.py"
sed -i -e "s/IPADDRESS/$IP/g" "makefile"
sed -i -e "s#PATHTOMOUNTEDDISK#$mountedDisk#g" "makefile"