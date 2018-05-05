# -*- coding: utf-8 -*-
# @Author: shubhambansal
# @Date:   2018-05-06 03:27:19
# @Last Modified by:   shubhambansal
# @Last Modified time: 2018-05-06 04:02:29
from bitmex_websocket import BitMEXWebsocket
import logging
from time import sleep
import csv

# Basic use of websocket.
def run():
    logger = setup_logger()

    # Instantiating the WS will make it connect. Be sure to add your api_key/api_secret.
    ws = BitMEXWebsocket(endpoint="https://testnet.bitmex.com/api/v1", symbol="XBTUSD",
                         api_key='-H4GmpGWNC505KogaaKyxoch', api_secret='GBM8hOsE9PYnKj374IHqv7M096sEpRSfoLZvA3hvY6oIHizJ')

    logger.info("Instrument data: %s" % ws.get_instrument())

    # Run forever
    while(ws.ws.sock.connected):
        # print("test")
        logger.info("Ticker: %s" % ws.get_ticker())
        data = ws.get_ticker()
        data = [ str(data[k]) for k in data ]
        with open(r'bitmex.csv', 'a') as f:
          writer = csv.writer(f)
          writer.writerow(data)
        f.close()
        # if ws.api_key:
        #     logger.info("Funds: %s" % ws.funds())
        # logger.info("Market Depth: %s" % ws.market_depth())
        # logger.info("Recent Trades: %s\n\n" % ws.recent_trades())
        sleep(10)


def setup_logger():
    # Prints logger info to terminal
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Change this to DEBUG if you want a lot more info
    ch = logging.StreamHandler()
    # create formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # add formatter to ch
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


if __name__ == "__main__":
    run()
