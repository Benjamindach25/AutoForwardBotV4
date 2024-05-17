import os

class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6487620358:AAE4iz1l7VIALr0mUVdMp5GDhlNM5DEqQfM")
      API_ID = int(os.environ.get("APP_ID", "27610252"))
      API_HASH = os.environ.get("API_HASH", "73e16fc08192ba7c1d52d4dc9fa2b220")
      CHANNEL = list(x for x in os.environ.get("CHANNEL_ID", "-1002097469844:-1002129887393").replace("\n", " ").split(' '))
