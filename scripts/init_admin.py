# 启动django
import os
import sys
import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NB_Platform.settings')
django.setup()  # 伪造让django启动

from web import models
from utils.encrypt import md5

models.Administrator.objects.create(username='root', password=md5("root"), mobile="16605643102")

