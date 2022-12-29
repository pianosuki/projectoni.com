import sys
import logging
import os

if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(level=logging.DEBUG, filename='./logs/projectoni.log', format='%(asctime)s %(message)s')
sys.path.insert(0, "/var/www/projectoni/projectoni.com")
sys.path.insert(0, "/var/www/projectoni/venv/lib/python3.8/site-packages")
from projectoni import app as application
