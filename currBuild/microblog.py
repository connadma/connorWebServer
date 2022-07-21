from app import app, db
from app.models import User, Post

#creates shell context that adds database instance and models to the session
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
