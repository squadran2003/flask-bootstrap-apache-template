#!/usr/bin/python
import sys
import logging

activate_this = '/var/www/flask-bbotstrap-apache-template/Yourapp/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")

from Yourapp import app as application
application.secret_key = 'Add your secret key'
