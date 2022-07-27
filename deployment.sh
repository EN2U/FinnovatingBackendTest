docker-compose build
docker-compose up -d db 
docker-compose run --rm app python manage.py makemigrations
docker-compose run --rm app python manage.py migrate
docker-compose up -d app
docker container exec -i backend_db_1 psql -U cinemauser cinema < data/sampleData.sql