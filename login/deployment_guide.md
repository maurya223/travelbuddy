# PythonAnywhere Deployment Guide

## Steps to Deploy on PythonAnywhere

### 1. Create PythonAnywhere Account
- Go to https://www.pythonanywhere.com/ and create a free account

### 2. Clone Repository
```bash
git clone https://github.com/maurya223/travelsbuddy-a-website-for-tourist-
cd travelsbuddy-a-website-for-tourist-
```

### 3. Set Up Virtual Environment
```bash
# Create virtual environment
mkvirtualenv --python=/usr/bin/python3.8 travelbuddy-env

# Activate virtual environment
workon travelbuddy-env

# Install dependencies
pip install -r requirements.txt
```

### 4. Database Setup
```bash
# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### 5. Static Files
```bash
# Collect static files
python manage.py collectstatic
```

### 6. Web App Configuration on PythonAnywhere
1. Go to Web tab in PythonAnywhere dashboard
2. Click "Add a new web app"
3. Choose "Manual configuration" (not Django)
4. Select Python version 3.8 or higher
5. In the WSGI configuration file, replace the content with:

```python
import os
import sys

path = '/home/maurya223/travelsbuddy-a-website-for-tourist-/login'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'login.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 7. Configure Static Files
In the Web tab, under "Static files":
- URL: `/static/`
- Directory: `/home/maurya223/travelsbuddy-a-website-for-tourist-/static`

### 8. Reload Web App
Click the reload button in the Web tab to apply changes

## Environment Variables (Optional)
For production, consider setting environment variables for:
- SECRET_KEY (generate a new one for production)
- DEBUG=False
- Database configuration if using MySQL/PostgreSQL

## Troubleshooting
- Check error logs in the Web tab
- Ensure all dependencies are installed
- Verify static files are collected properly
- Check database migrations are applied
