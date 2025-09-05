# Travel Buddy Deployment Checklist ✅

## Pre-Deployment Verification

### ✅ Environment Setup
- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] All dependencies installed: `pip install -r requirements.txt`
- [ ] Django version: 5.2.4

### ✅ Configuration Check
- [ ] `DEBUG = False` in settings.py
- [ ] `ALLOWED_HOSTS` includes 'maurya223.pythonanywhere.com'
- [ ] `SECRET_KEY` is set (consider using environment variable in production)
- [ ] Database configured (SQLite3 for development, consider MySQL/PostgreSQL for production)

### ✅ Static Files
- [ ] `STATIC_ROOT` configured to PythonAnywhere path
- [ ] Static files collected: `python manage.py collectstatic`
- [ ] Static files directory exists at: `/home/maurya223/travelsbuddy-a-website-for-tourist-/static`

### ✅ Database
- [ ] Migrations applied: `python manage.py migrate`
- [ ] Superuser created if needed: `python manage.py createsuperuser`
- [ ] Database file exists and is accessible

## PythonAnywhere Deployment Steps

### ✅ Web App Configuration
1. [ ] Log in to PythonAnywhere dashboard
2. [ ] Go to Web tab
3. [ ] Click "Add a new web app"
4. [ ] Choose "Manual configuration" (not Django)
5. [ ] Select Python version 3.8 or higher

### ✅ WSGI Configuration
1. [ ] Open WSGI configuration file in PythonAnywhere
2. [ ] Replace content with:
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

### ✅ Static Files Configuration (PythonAnywhere Web Tab)
- [ ] URL: `/static/`
- [ ] Directory: `/home/maurya223/travelsbuddy-a-website-for-tourist-/static`

### ✅ Final Steps
- [ ] Click "Reload" button in PythonAnywhere Web tab
- [ ] Wait for application to reload (usually takes 30-60 seconds)

## Post-Deployment Verification

### ✅ Website Accessibility
- [ ] Open: http://maurya223.pythonanywhere.com/
- [ ] Home page loads without errors
- [ ] Static files (CSS, JS, images) load correctly
- [ ] All links and navigation work properly

### ✅ Functionality Testing
- [ ] User registration works
- [ ] User login works
- [ ] Booking functionality works
- [ ] My bookings page works
- [ ] Contact form works (if applicable)

### ✅ Error Checking
- [ ] Check PythonAnywhere error logs in Web tab
- [ ] No 500 errors in browser console
- [ ] No 404 errors for static files
- [ ] Database operations work correctly

## Troubleshooting Common Issues

### ❌ Application not loading
- Check PythonAnywhere error logs
- Verify WSGI configuration path is correct
- Ensure all dependencies are installed in virtual environment

### ❌ Static files not loading
- Verify `collectstatic` was run
- Check static files configuration in PythonAnywhere Web tab
- Ensure static files directory exists and has correct permissions

### ❌ Database errors
- Check if migrations were applied
- Verify database file exists and is accessible
- Check database permissions

### ❌ 500 Internal Server Error
- Check PythonAnywhere error logs for detailed error message
- Verify `DEBUG = False` in production
- Check if secret key is properly set

## Deployment Success Indicators ✅

- ✅ Website loads at http://maurya223.pythonanywhere.com/
- ✅ No errors in browser console
- ✅ All functionality works as expected
- ✅ Static files (CSS, images) load properly
- ✅ Forms submit without errors
- ✅ Database operations work correctly

## Quick Test Commands

```bash
# Run verification script
python deployment_verification.py

# Collect static files
python manage.py collectstatic

# Apply migrations
python manage.py migrate

# Create superuser (if needed)
python manage.py createsuperuser

# Test development server
python manage.py runserver
```

## Support Resources

- PythonAnywhere documentation: https://help.pythonanywhere.com/
- Django deployment checklist: https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/
- Error logs: PythonAnywhere Web tab → Error log section

---
*Last verified: [Date]*  
*Deployment status: ✅ SUCCESSFUL / ⚠️ NEEDS ATTENTION / ❌ FAILED*
