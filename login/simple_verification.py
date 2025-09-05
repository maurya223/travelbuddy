#!/usr/bin/env python3
"""
Simple Deployment Verification for Travel Buddy
Checks basic configuration without full Django setup
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check Python version"""
    print("🔍 Checking Python version...")
    version = sys.version_info
    print(f"Python {version.major}.{version.minor}.{version.micro}")
    return version.major == 3 and version.minor >= 8

def check_requirements():
    """Check if requirements are installed"""
    print("\n🔍 Checking requirements...")
    
    try:
        # Try to import Django
        import django
        django_version = django.VERSION
        print(f"✅ Django {django_version[0]}.{django_version[1]}.{django_version[2]} is installed")
        return True
    except ImportError:
        print("❌ Django not installed")
        return False

def check_config_files():
    """Check configuration files"""
    print("\n🔍 Checking configuration files...")
    
    files_to_check = [
        ('settings.py', 'login/login/settings.py'),
        ('wsgi.py', 'login/wsgi.py'),
        ('pa_wsgi.py', 'login/pa_wsgi.py'),
        ('requirements.txt', 'login/requirements.txt')
    ]
    
    all_exist = True
    for file_name, file_path in files_to_check:
        if Path(file_path).exists():
            print(f"✅ {file_name} exists")
        else:
            print(f"❌ {file_name} missing")
            all_exist = False
    
    return all_exist

def check_settings_config():
    """Check settings.py configuration"""
    print("\n🔍 Checking settings configuration...")
    
    try:
        with open('login/login/settings.py', 'r') as f:
            content = f.read()
        
        checks = [
            ('DEBUG = False', 'DEBUG mode is production-ready'),
            ("'maurya223.pythonanywhere.com'", 'PythonAnywhere domain in ALLOWED_HOSTS'),
            ('STATIC_ROOT', 'STATIC_ROOT is configured')
        ]
        
        all_good = True
        for search_term, message in checks:
            if search_term in content:
                print(f"✅ {message}")
            else:
                print(f"❌ {message} not found")
                all_good = False
        
        return all_good
        
    except FileNotFoundError:
        print("❌ settings.py not found")
        return False

def check_wsgi_config():
    """Check WSGI configuration"""
    print("\n🔍 Checking WSGI configuration...")
    
    try:
        with open('login/pa_wsgi.py', 'r') as f:
            content = f.read()
        
        if '/home/maurya223/travelsbuddy-a-website-for-tourist-/login' in content:
            print("✅ PythonAnywhere path configured in WSGI")
            return True
        else:
            print("❌ PythonAnywhere path not found in WSGI")
            return False
            
    except FileNotFoundError:
        print("❌ pa_wsgi.py not found")
        return False

def main():
    """Main verification function"""
    print("=" * 60)
    print("🚀 Simple Travel Buddy Deployment Verification")
    print("=" * 60)
    
    checks = [
        check_python_version,
        check_requirements,
        check_config_files,
        check_settings_config,
        check_wsgi_config
    ]
    
    results = []
    for check in checks:
        try:
            result = check()
            results.append(result)
        except Exception as e:
            print(f"❌ Error during check: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    print("📊 VERIFICATION SUMMARY")
    print("=" * 60)
    
    success_count = sum(results)
    total_checks = len(results)
    
    print(f"Checks passed: {success_count}/{total_checks}")
    
    if success_count == total_checks:
        print("🎉 All basic checks passed! Configuration looks good.")
        print("\nNext steps for deployment:")
        print("1. Run: python manage.py collectstatic")
        print("2. Run: python manage.py migrate")
        print("3. Deploy to PythonAnywhere following deployment_guide.md")
    else:
        print("⚠️  Some checks failed. Please review the issues above.")
        print("\nCommon solutions:")
        print("- Install Django: pip install Django==5.2.4")
        print("- Check file paths and configurations")
        print("- Review deployment_guide.md for setup instructions")

if __name__ == "__main__":
    main()
