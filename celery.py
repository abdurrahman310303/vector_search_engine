import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vector_search.settings')

app = Celery('vector_search')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()