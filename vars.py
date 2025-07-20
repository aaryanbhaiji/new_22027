#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "23537514"))
API_HASH = environ.get("API_HASH", "c5ec016af7d2cb637278b715f4f5a389")
BOT_TOKEN = environ.get("BOT_TOKEN", "8096925495:AAETA-B20WZ6mb_PY6-oacWheor8jcDgLCs")

OWNER = int(environ.get("OWNER", "953685850"))
CREDIT = environ.get("CREDIT", "@bindasboy010")

TOTAL_USER = os.environ.get('TOTAL_USERS', '953685850').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '953685850').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
