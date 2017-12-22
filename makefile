build:
	@docker build -t dockerrfpy27 --network=host .

run:
	@docker-compose up -d

stop:
	@docker stop dockerrfpy27

down:
	@docker-compose down

stopkafka:
	@docker stop dkafka && docker rm dkafka

listen: 
	@cd py && python3 kafkaConsumeRunCommand.py &

jenkins:

	@cd py && python3 jenkinsCreateJobs.py &


