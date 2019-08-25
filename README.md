# cgi-hackathon


Assignment
==========
    1. clone repo at https://github.com/BasavarajuUS/cgi-hackathon.git


Project Setup
-------------
    1. Change to project folder

    2. Create virtual environment (command - 'virtualenv assignment')

    3. Activate installed virtualenv 'assignment' (command - 'source assignment/bin/activate')

    4. Install the project requirements using requirement.txt (command - 'pip install -r requirements.txt')

    5. create django project name as 'games_listing'

    6. create django app name as 'games'

    7. Setup database (command - 'python manage.py db migrate')

    8. Create superuser (command - 'python manage.py createsuperuser')

    9. Run the application (command - 'python manage.py runserver')

    10. Access the application in browser - http://127.0.0.1:8000

    11. Access the application Admin interface in browser - http://127.0.0.1:8000/admin using superuser credentials created at step 8


Application
-----------
    1. Admin - http://127.0.0.1:8000/admin
    2. Get All games using the API - http://127.0.0.1:8000/api/v1/games/
    3. Get perticular game by passing game id as argument using the API - http://127.0.0.1:8000/api/v1/games/1/
    4. Search the games by using the API http://127.0.0.1:8000/api/v1/games/search/ using payload {'name': "title", "value": 'NH3'}
