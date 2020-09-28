from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile('../instance/config.py')

# Register Blueprints
from .views.users import user
from .views.geocoding import geocoding
app.register_blueprint(user)
app.register_blueprint(geocoding)