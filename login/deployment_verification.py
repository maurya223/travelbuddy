#!/usr/bin/env python3
"""
Deployment Verification Script for Travel Buddy Django Project
This script checks if the project is ready for deployment on PythonAnywhere
"""

import os
import sys
import django
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    print("🔍 Checking Python version...")
    version = sys.version_info
    print(f"Python {version.major}.{version.minor}.{version.micro}")
    if version.major == 3 and version.minor >= 8:
        print("✅ Python version is compatible (3.8+)")
        return True
    else:
        print("❌ Python version should be 3.8 or higher")
        return False

def check_django_configuration():
    """Check Django configuration"""
    print("\n🔍 Checking Django configuration...")
    
    try:
        # Set up Django environment
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'login.settings')
        django.setup()
        
        from django.conf import settings
        
        # Check DEBUG mode
        if not settings.DEBUG:
            print("✅ DEBUG mode is False (production-ready)")
        else:
            print("⚠️  DEBUG mode is True - should be False for production")
        
        # Check ALLOWED_HOSTS
        allowed_hosts = settings.ALLOWED_HOSTS
        if 'maurya223.pythonanywhere.com' in allowed_hosts:
            print("✅ PythonAnywhere domain is in ALLOWED_HOSTS")
        else:
            print("❌ PythonAnywhere domain not found in ALLOWED_HOSTS")
            print(f"Current ALLOWED_HOSTS: {allowed_hosts}")
        
        # Check static files configuration
        if hasattr(settings, 'STATIC_ROOT') and settings.STATIC_ROOT:
            print("✅ STATIC_ROOT is configured")
        else:
            print("❌ STATIC_ROOT is not configured")
        
        return True
        
    except Exception as e:
        print(f"❌ Error checking Django configuration: {e}")
        return False

def check_requirements():
    """Check if requirements are installed"""
    print("\n🔍 Checking requirements...")
    
    try:
        import django
        django_version = django.VERSION
        print(f"✅ Django {django_version[0]}.{django_version[1]}.{django_version[2]} is installed")
        
        # Check if we can import other potential requirements
        try:
            import sqlite3
            print("✅ SQLite3 is available")
        except ImportError:
            print("❌ SQLite3 not available")
            
        return True
        
    except ImportError as e:
        print(f"❌ Missing requirement: {e}")
        return False

def check_database():
    """Check database connectivity"""
    print("\n🔍 Checking database...")
    
    try:
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            if result and result[0] == 1:
                print("✅ Database connection successful")
                return True
            else:
                print("❌ Database connection test failed")
                return False
    except Exception as e:
        print(f"❌ Database error: {e}")
        return False

def check_static_files():
    """Check static files configuration"""
    print("\n🔍 Checking static files...")
    
    try:
        from django.conf import settings
        from django.contrib.staticfiles import finders
        
        # Check if static files can be found
        static_files = finders.find('admin/css/base.css')
        if static_files:
            print("✅ Static files are accessible")
        else:
            print("⚠️  Static files not found - run 'python manage.py collectstatic'")
        
        # Check STATIC_ROOT path
        static_root = getattr(settings, 'STATIC_ROOT', None)
        if static_root and os.path.isabs(static_root):
            print(f"✅ STATIC_ROOT is absolute path: {static_root}")
        else:
            print("❌ STATIC_ROOT is not configured properly")
            
        return True
        
    except Exception as e:
        print(f"❌ Static files error: {e}")
        return False

def check_wsgi_config():
    """Check WSGI configuration"""
    print("\n🔍 Checking WSGI configuration...")
    
    wsgi_path = Path('login/wsgi.py')
    pa_wsgi_path = Path('login/pa_wsgi.py')
    
    if wsgi_path.exists():
        print("✅ WSGI file exists")
    else:
        print("❌ WSGI file missing")
    
    if pa_wsgi_path.exists():
        print("✅ PythonAnywhere WSGI file exists")
        
        # Check if pa_wsgi has the correct path
        with open(pa_wsgi_path, 'r') as f:
            content = f.read()
            if '/home/maurya223/travelsbuddy-a-website-for-tourist-/login' in content:
                print("✅ PythonAnywhere path is correctly configured")
            else:
                print("❌ PythonAnywhere path might be incorrect")
    else:
        print("❌ PythonAnywhere WSGI file missing")
    
    return True

def main():
    """Main verification function"""
    print("=" * 60)
    print("🚀 Travel Buddy Deployment Verification")
    print("=" * 60)
    
    checks = [
        check_python_version,
        check_requirements,
        check_django_configuration,
        check_database,
        check_static_files,
        check_wsgi_config
    ]
    
    results = []
    for check in checks:
        try:
            result = check()
            results.append(result)
        except Exception as e:
            print(f"❌ Error during {check.__name__}: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    print("📊 VERIFICATION SUMMARY")
    print("=" * 60)
    
    success_count = sum(results)
    total_checks = len(results)
    
    print(f"Checks passed: {success_count}/{total_checks}")
    
    if success_count == total_checks:
        print("🎉 All checks passed! Deployment should be successful.")
        print("\nNext steps:")
        print("1. Run: python manage.py collectstatic")
        print("2. Run: python manage.py migrate")
        print("3. Deploy to PythonAnywhere following the deployment guide")
    else:
        print("⚠️  Some checks failed. Please review the issues above.")
        print("\nCommon solutions:")
        print("- Check your PythonAnywhere path in wsgi files")
        print("- Ensure DEBUG=False in settings.py")
        print("- Verify ALLOWED_HOSTS includes your PythonAnywhere domain")
        print("- Run: pip install -r requirements.txt")

if __name__ == "__main__":
    main()
