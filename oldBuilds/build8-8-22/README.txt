Microblog Read Me:

To prep for first run:
- python3 -m venv venv
- source venv/bin/activate
- pip install flask
- export FLASK_APP=microblog.py
- pip install flask-wtf
- pip install flask-sqlalchemy
- pip install flask-migrate
- pip install flask-login
- pip install email-validator

To prep for additional runs:
- python3 -m venv venv
- source venv/bin/activate
- pip install flask
- export FLASK_APP=microblog.py

To run:
- flask run
- ctrl + c to stop running
- link is provided in command line out put of
  flask run to where the program is being ran

To enter debug mode:
- While in venv: export FLASK_ENV=development
- If running on windows command prompt use set instead of export
- Running program while in debug mode is the same

To exit debug mode:
- While in venv export FLASK_ENV=production
- If running on windiws command prompt use set instead of export

What to do next:
- pagination of blog posts
