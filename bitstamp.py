import pysher
import sys
import time
import json
import csv


import logging
root = logging.getLogger()
root.setLevel(logging.INFO)

pusher = pysher.Pusher('de504dc5763aeef9ff52')

# Store all messages in a list to loop over later
def my_func(messages):
    messages = json.loads(messages)
    # separated the bid and asks
    bids = messages["bids"]
    asks = messages["asks"]
    # csv writer function open here
    with open(r'bitstamp.csv', 'a') as f:
      writer = csv.writer(f)
      # looping through the each bids and asks and adding them to csv file
      for i in range(0,len(bids)):
        fields = asks[i] + bids[i]
        fields = [ str(i) for i in fields ]
        print(fields)
        writer.writerow(fields)
    f.close()


def connect_handler(data):
    channel = pusher.subscribe('order_book')
    channel.bind('data', my_func)

pusher.connection.bind('pusher:connection_established', connect_handler)
pusher.connect()

while True:
	time.sleep(1)
