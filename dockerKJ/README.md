# DSH Testframework for Tenants

This docker allows you to execute robot framework tests from a git repo.
The Git repo is first cloned to your harddisk (later to be changed into a persistent storage). Make sure you figure out in which folder you want to clone it to.
A run command is given through kafka and the testresults are also put on kafka.

1. Clone repo
2. Open changeme.sh and <br>
- If required change the path of mountedDisk. You may also leave the default. <br>
- DO change the name of the topic to your tenant name.
- Make sure the credentialsId matches up with the jenkins you are connecting to. (JENKINS_HOME/credentials.xml, id-tag)
3. execute: make runonce
4, execute: make
5. execute: make runkafka (if no kafka was running)
6. execute: make runall

The runall command will: 
1. Open up a GUI where you have to log into your tenant environment and give in the url to your git repo where the tests are located. <br>
- A job is created on Jenkins which pushes your testcases from git into the mounted disk <br>
- When is selected which folder to execute, a job is created on jenkins which sends a run command on kafka to your tenant name topic.
Templates for the jobs are located inside the templates folder.

2. Start up a listener which listens on your tenant name topic to observe if a run command passed by. If so:
- A docker is run that executes the testcases located inside mounted disk. and save the results into the mountedDisk/Testresults folder.
- Whenever there is a new output.xml there, the xml is parsed into json.
- The output.json is put on kafka under tenant topic name

3. ensures docker.sock can be used (run docker inside docker)

All commands are run as daemon. For no daemon you may execute
"make runnod" and "make listennod"