import os
from os.path import expanduser

home = expanduser("~")

absFilePath = os.path.dirname(os.path.abspath(__file__))
dMountedDiskClient = os.path.join(absFilePath,'mountedDisk')
fKafkaRunCommand = os.path.join(absFilePath,'kafkaProduceRunCommand.py')
templatePushMDisk =  os.path.join(absFilePath,'templates','push-mountedDisk.xml')
templateExecKafkaRunCommand = os.path.join(absFilePath,'templates','executeProduceRunCommand.xml')

####TENANT SPECIFIC#########
kafkaServer = '172.22.0.1:9092'
topic = 'vialis'
dMountedDiskHost = r'/home/rakeshlaptop/Documents/projects/DSH/mountedDisk'