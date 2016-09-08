import requests
import os

print requests.__version__
print os.system('curl -iLX GET http://google.com')
