```
1. Create an account on https://www.pythonanywhere.com/

2. Create a Repository on GitHub 

3. Push your project to GitHub

4. Test Django web app and create Django requirements files
       i)  python manage.py runserver
       ii) python -m pip freeze (type gather then. YouTube doesn't allow to write gather than symble ) requirements.txt

5. git clone 

6. mkvirtualenv --python=/usr/bin/python3.9 venv 

7. pip install -r requirements.txt

8. Setting up your Web app and WSGI file
        Source code: /home/nongareshop/ecommerce
        Working directory: /home/nongareshop/
        Virtual Environtment Path: /home/nongareshop/.virtualenvs/env

         # Paths
         /static/ /home/nongareshop/ecommerce/static/

         /media/ /home/nongareshop/ecommerce/media_root/

9. WSGI
import os
import sys
path = os.path.expanduser('~/ecommerce')
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'ecproject.settings'

from django.core.wsgi import get_wsgi_application

from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
```