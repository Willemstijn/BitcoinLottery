#!/usr/bin/python
from subprocess import Popen
#import sys
import logging
from datetime import datetime

# Use sys.argv[1] if you want to use this file like this "run_lottery.py <filename>"
# filename = sys.argv[1]
filename = 'btc_lottery.py'

logging.basicConfig(filename='report.log' ,level=logging.DEBUG)

while True:
    print("\nStarting " + filename)
    p = Popen("python " + filename, shell=True)
    sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S ')
    message = 'Started Bitcoin Lottery: '
    logging.info(message + sttime)
    p.wait()
