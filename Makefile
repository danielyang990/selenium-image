build:
	docker-compose build selenium

up:
	docker-compose up -d
	docker-compose ps

down:
	docker-compose down

ps:
	docker-compose ps

test:
	docker-compose exec test bash

push:
	docker tag centos7-python36-selenium:latest firewolf990/centos7-python36-selenium:latest
	docker push firewolf990/centos7-python36-selenium:latest