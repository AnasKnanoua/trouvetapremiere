#!/usr/bin/env python
"""Django's command-line utility for administrative tasks.
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ttp.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
"""
import sys, os

cwd = os.getcwd()
INTERP = cwd+'/venv/bin/python'
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(cwd)
sys.path.append(cwd + '/venv')

sys.path.insert(0,cwd+'/venv/bin')
sys.path.insert(0,cwd+'/venv/lib/python3.5/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "mysite.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
