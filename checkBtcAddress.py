#!/usr/bin/env python
# To start the script in the background use: nohup ./checkBtcAddress.py &
# To see the process again use: ps ax | grep test.py


## ===== IMPORT MODULES ===== ##
import requests, time
from bitcoin import *

# Run the script with the help of a timer (see below for timer settings)
starttime=time.time()
while True:
    def create_addr():
                priv = random_key()
                pub = privtopub(priv)
                addr = pubtoaddr(pub)
                electrumPKey = encode_privkey(priv, 'wif')
                return addr, priv, electrumPKey
    addr,priv,electrumPKey = create_addr()

    base_url = "https://www.bitgo.com/api/v1/address/"
    # Comment this line when testing
    check_url = base_url+addr
    # Uncomment these lines for testing with balance:
    # btc_address= "17A16QmavnUfCW11DAApiJxp7ARnxN5pGX"
    # check_url = base_url+btc_address
    # print(check_url)

    # get the balance of the address
    get_json = requests.get(check_url).json()
    btc_address_balance = get_json['balance']

    # Print output to console
    print("BTC Address: " + addr)
    print("Electrum Import Key: " + electrumPKey)
    print("Private Key: " + priv)
    print("Amount on address: " + str(btc_address_balance))
    print('=============================================================================')

    # Actions taken when address with balance is found
    if btc_address_balance > 0:
        # Send message with Telegram
        def telegram_bot_sendtext(bot_message):
            
            # Enter your bot token and bot chat ID here for warnings with Telegram
            bot_token = ''
            bot_chatID = ''
            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
            response = requests.get(send_text)
            return response.json()
            
        telegramtext = telegram_bot_sendtext("Found BTC Address: " + addr + " - Private key: " + priv + " - Electrum key: " + electrumPKey + " - with: " + str(btc_address_balance) + " satoshi")
        
        # Write output to comma separated file
        text_file = open("foundSatoshi.csv", "a+")
        text_file.write(str(btc_address_balance) + "," + addr + "," + electrumPKey + "," + priv)
        text_file.write("\n")
        text_file.close()
    
    # Set the timer to run the script every 5 seconds
    time.sleep(5.0 - ((time.time() - starttime) % 5.0))