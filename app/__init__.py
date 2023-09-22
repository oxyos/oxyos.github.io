from flask import Flask, request, render_template

from config import Config # Import the app's configuration from the config.py file in the main directory

app = Flask(__name__)

app.config.from_object(Config) # Loads the configuration from the config.py file into Flask
app.jinja_env.auto_reload = True

from app import routes
