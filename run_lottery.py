#!/usr/bin/env python3

from subprocess import Popen
import sys
import logging
import time
from datetime import datetime

# Use sys.argv[1] if you want to use this file like this "run_lottery.py <filename>"
# filename = sys.argv[1]
filename = 'checkBtcAddress.py'

logging.basicConfig(filename='report.log',level=logging.DEBUG)

while True:
    print("\nStarting " + filename)
    p = Popen("python " + filename, shell=True)
    sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S ')
    message = 'Started Bitcoin Lottery: '
    logging.info(message + sttime)
    p.wait()
    time.sleep(5)