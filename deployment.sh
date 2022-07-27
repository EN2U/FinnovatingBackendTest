export COMPOSE_PROJECT_NAME=backend

docker-compose build
docker-compose up -d db 
docker-compose run --rm app python manage.py makemigrations
docker-compose run --rm app python manage.py migrate
docker-compose up -d app

# replace the following line of code if the script is used on windows
# docker container exec -i backend-db-1 psql -U cinemauser cinema < data/sampleData.sql
docker container exec -i backend_db_1 psql -U cinemauser cinema < data/sampleData.sql