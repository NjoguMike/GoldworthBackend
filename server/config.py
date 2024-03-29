from flask import Flask
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_admin import Admin, AdminIndexView, form
import os

app = Flask(__name__)

db = SQLAlchemy()


app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE']='sqlalchemy'
app.config['SESSION_SQLALCHEMY']=db
app.config['SECRET_KEY'] = 'no_key'
app.config["IMAGE_UPLOAD_PATH"] = "image_uploads"
app.config["FILE_UPLOAD_PATH"] = "file_uploads"

db.init_app(app)

migrate = Migrate(app, db)
CORS(app)

Session(app)
bcrypt = Bcrypt(app)
mash = Marshmallow(app)
api = Api(app)
admin = Admin(app, name="GoldWorth", index_view=AdminIndexView(url='/'), template_mode='bootstrap4')

