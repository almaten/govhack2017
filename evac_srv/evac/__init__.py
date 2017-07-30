from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('evac.config')
db = SQLAlchemy(app)

from evac import evac_api, views, models
