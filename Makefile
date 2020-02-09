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