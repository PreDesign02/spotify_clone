#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spotify_clone.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    
    #get the port env variabeL OR default to 1000
    port=os.environ.get('PORT', '1000')
    
    #if running server command, specify the port
    if sys.argv[1]== 'runserver':
        sys.argv[2]== '0.0.0.0:' + port


if __name__ == '__main__':
    main()
