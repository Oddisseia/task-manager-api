import os

from dotenv import load_dotenv
from src import create_app

load_dotenv()

app = create_app(os.getenv("CONFIG_TYPE"))

if __name__ == '__main__':
    app.run()

# This is import is here, so we are able to split the routes from the app.py to its own file
from src.task import urls
