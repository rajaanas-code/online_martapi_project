from starlette.datastructures import Secret
from starlette.config import Config

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()

BOOTSTRAP_SERVER = config("BOOTSTRAP_SERVER", cast=str)
DATABASE_URL = config("DATABASE_URL", cast=Secret)
# TEST_DATABASE_URL = config("TEST_DATABASE_URL", cast=Secret)

KAFKA_CONSUMER_GROUP_ID_FOR_PRODUCT = config("KAFKA_CONSUMER_GROUP_ID_FOR_PRODUCT", cast=str)
KAFKA_PRODUCT_TOPIC = config("KAFKA_PRODUCT_TOPIC", cast=str)