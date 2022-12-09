import sys
import logging

logging.basicConfig(level=logging.DEBUG, filename='/var/www/projectoni/projectoni.com/logs/projectoni.log', format='%(asctime)s %(message)s')
sys.path.insert(0, "/var/www/projectoni/projectoni.com")
sys.path.insert(0, "/var/www/projectoni/venv/lib/python3.8/site-packages")
from projectoni import app as application
