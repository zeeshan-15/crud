import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crud_class_base.settings')

application = get_wsgi_application()
