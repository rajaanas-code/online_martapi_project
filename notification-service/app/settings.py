from starlette.datastructures import Secret
from starlette.config import Config

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()

BOOTSTRAP_SERVER = config("BOOTSTRAP_SERVER", cast=str)
DATABASE_URL = config("DATABASE_URL", cast=Secret)
# TEST_DATABASE_URL = config("TEST_DATABASE_URL", cast=Secret)

<<<<<<< HEAD
KAFKA_ORDER_TOPIC = config("KAFKA_ORDER_TOPIC", cast=str)
=======
KAFKA_ORDER_TOPIC = config("KAFKA_ORDER_TOPIC", cast=str, default="order-events")
>>>>>>> 37deb645b9f12e3aa90dee167739129606757f1e
MAILJET_API_KEY = config("MAILJET_API_KEY", cast=str)
MAILJET_SECRET_KEY = config("MAILJET_SECRET_KEY", cast=str)