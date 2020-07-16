#!/usr/bin/env python3

## ===== IMPORT MODULES ===== ##
import requests, time
from bitcoin import *

def executeScript():

    def create_addr():
            priv = random_key()
            pub = privtopub(priv)
            addr = pubtoaddr(pub)
            electrumPKey = encode_privkey(priv, 'wif')
            return addr, priv, electrumPKey
    addr,priv,electrumPKey = create_addr()
    
    base_url = "https://blockchain.info/q/addressbalance/"
    # Comment this line when testing
    check_url = base_url+addr
    # Uncomment these lines for testing with balance:
    # btc_address= "1DaYUJr3STrMmzNN11rQYMBDvJnXRY1cVE"
    # check_url = base_url+btc_address
    # print(check_url)

    # get the balance of the address
    btc_address_balance = requests.get(check_url).json()

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


while True:
    executeScript()
