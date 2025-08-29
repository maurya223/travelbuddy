# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Django project

import os
import sys

# Add your project directory to the sys.path
path = '/home/maurya223/travelsbuddy-a-website-for-tourist-/login'
if path not in sys.path:
    sys.path.append(path)

# Set environment variables to point to your project
os.environ['DJANGO_SETTINGS_MODULE'] = 'login.settings'

# Import the Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
