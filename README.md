Run

  docker-compose build
  
  docker-compose up -d
  
  docker-compose exec web python manage.py makemigrations
  
  docker-compose exec web python manage.py migrate
  
  docker-compose exec web python manage.py createsuperuser
  
  http://127.0.0.1/
