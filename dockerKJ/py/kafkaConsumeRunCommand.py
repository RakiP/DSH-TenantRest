# -*- coding: utf-8 -*-
import json
import argparse
from kafka import KafkaProducer, KafkaConsumer
import subprocess
from TenantRestConfig import *

parser = argparse.ArgumentParser()
parser.add_argument("-V", "--version", help="show program version", action="store_true")
parser.add_argument("--topic", "-t", help="give tenant name, also same as topic on kafka")

# read arguments from the command line
args = parser.parse_args()

def main():

    if args.version:
        print("Ask rakesh.partapsing@kpn.com")

    if args.topic:
        topic = args.topic

        # To consume latest messages and auto-commit offsets
        consumer = KafkaConsumer(topic, group_id='run-group', bootstrap_servers=[kafkaServer])
        for message in consumer:
            # message value and key are raw bytes -- decode if necessary!
            # e.g., for unicode: `message.value.decode('utf-8')`
            #print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
            #                                      message.offset, message.key,
            #                                      message.value))
            runCommand = str(message.value.decode('utf-8')).split(' ')[1]
            if str(message.value.decode('utf-8')).split(' ')[0] == 'RUN' :
                print('Execute testcase(s) {} from Testcases '.format(runCommand))
                tResults = os.path.join(dMountedDisk, 'Testresults', runCommand)
                tCases = os.path.join(dMountedDisk, 'Testcases')

                if runCommand == 'All':
                    subprocess.run(['/bin/bash', '-c', 'docker run -v {0}:/robot/Testcases -v {1}:/robot/Testresults -w /robot --net=host rpartapsing/dsh:part1 /bin/bash -c ./runscript.sh '.format(tCases, tResults)])
                else:
                    print('else')
                    tCasesChosen = os.path.join(tCases, runCommand)
                    subprocess.run(['/bin/bash', '-c', 'docker run -v {0}:/robot/Testcases -v {1}:/robot/Testresults -w /robot --net=host rpartapsing/dsh:part1 /bin/bash -c ./runscript.sh '.format(tCasesChosen, tResults)])

                print('Convert xml to json')
                fXML = os.path.join(tResults, 'output.xml')
                fJSON = os.path.join(tResults, 'output.json')
                subprocess.run(['/bin/bash', '-c', 'sudo chmod 777 {}'.format(tResults)])
                subprocess.run(['/bin/bash', '-c', 'python3 xmlToJson.py {}'.format(fXML)])

                print('Put json on kafka')
                jData = json.load(open(fJSON))
                producer = KafkaProducer(bootstrap_servers=kafkaServer, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

                producer.send(topic, key=b'Testresults', value=jData)

                #print('Remove xml and html files')
                #subprocess.run(['/bin/bash', '-c', 'rm -f /home/rakeshlaptop/Documents/dockerRF/mountedDisk/Testresults/out*'])
                #subprocess.run(['/bin/bash', '-c', 'rm -f /home/rakeshlaptop/Documents/dockerRF/mountedDisk/Testresults/*.html'])

        # consume earliest available messages, don't commit offsets
        KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)

 
if __name__ == "__main__":
    main()
