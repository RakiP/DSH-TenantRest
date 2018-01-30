import os
from os.path import expanduser

home = expanduser("~")

absFilePath = os.path.dirname(os.path.abspath(__file__))
dMountedDiskClient = os.path.join(absFilePath,'mountedDisk')
fKafkaRunCommand = os.path.join(absFilePath,'kafkaProduceRunCommand.py')
templatePushMDisk =  os.path.join(absFilePath,'templates','push-mountedDisk-pipeline.xml')
templateExecKafkaRunCommand = os.path.join(absFilePath,'templates','executeProduceRunCommand-pipeline.xml')
#templatePushMDisk =  os.path.join(absFilePath,'templates','push-mountedDisk.xml')
#templateExecKafkaRunCommand = os.path.join(absFilePath,'templates','executeProduceRunCommand.xml')

portJenkins = 80
portKafka = 9092

####TENANT SPECIFIC#########
ipAddress = 'IPADDRESS'
topic = 'TOPIC'
dMountedDiskHost = r"PATHTOMOUNTEDDISK"
##JENKINS
ipAddressJenkins = ipAddress
crId = 'CREDENTIALSID' # this is the id tag of credentials.xml. This can be found in JENKINS_HOME dir.