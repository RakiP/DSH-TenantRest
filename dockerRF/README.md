# RobotFramework inside Docker

Summary for usage:
1. Clone this repo
2. Put all your tests into folders inside 'Testcases' folder
3. cd into projectfolder
4. execute: make
5. execute: make runkafka (if no kafka was running) Skip this if you are not
performing tests which need kafka
6. make runonce 
7. Empty the 'Testresults' folder
8. execute: make run

Errors:<br>
if any error occurs with paths, execute sudo make down

Additional info of how to use pybot
- Have a docker with virtualenv installed
- go cd into top project directory (e.g. DSH)
- run : source venv/bin/activate
- cd into folder where tests are located
- run : pybot test.robot

Note: <br>
robotframework-mqttlibrary has no python 3 support therefore we use python 2.7