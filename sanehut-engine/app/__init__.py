from flask import Flask

app = Flask(__name__)
 
from app.user.controller import user
app.register_blueprint(user, url_prefix='/api/v1')
 
