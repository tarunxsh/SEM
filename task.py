# script to simulate SEM Module function
# This will make request to backend server with random pulses
from requests import request
import time
import random
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('SME')

base_url =  "http://127.0.0.1:8000/api/{}/{}"

while 100:
	pulses = random.randint(1,5)	# random pulses
	mtr = random.randint(1,2)		# random meter_id [must exisit on backend]
	url = base_url.format(mtr,pulses)
	logger.info("Send :  mtr={}  pulses={}".format(mtr,pulses))
	res = request(url=url , method="get")
	logger.info("Recv : {}".format(res.json()))
	time.sleep(3)
