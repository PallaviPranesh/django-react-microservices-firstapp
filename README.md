This is simple microservices project with django and react.

To run the frontend react app:

npm install react-scripts@latest
npm start
http://localhost:3000/


django Commands:
to start app:
py manage.py runserver

to migrate any changes in db and models:
py manage.py makemigrations <appname>
py manage.py migrate

to start django post server:
navigate to posts folder and run the commans
py manage.py runserver
in browser type
http://localhost:8000/api/posts

to start django comment server:
py manage.py runserver 8001
in browser type 
http://localhost:8001/api/comments