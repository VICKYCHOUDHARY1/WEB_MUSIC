from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB_URI
from ..logging import LOGGER
import sys

LOGGER(__name__).info("Connecting to your Mongo Database...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_['YM']  # or mongodb = _mongo_async_.get_database('YM')
    LOGGER(__name__).info("Connected to your Mongo Database.")
except ConnectionRefusedError:
    LOGGER(__name__).error("Connection to MongoDB was refused. Check that MongoDB is running.")
    sys.exit(1)
except Exception as e:
    LOGGER(__name__).error(f"Failed to connect to your Mongo Database: {e}")
    sys.exit(1)