#!/usr/bin/env python3
# Do not start this file. Start "run_lottery.py"!
import requests
from bitcoin import *
import time
import config

# Set timer to 15 seconds due to rate-limit on blockchain.com
# Set timer to 20 seconds due to rate-limit on https://www.blockcypher.com/dev/bitcoin/#rate-limits-and-tokens
timer=20

def create_addr():
    """ 
    This function creates a private key, bitcoin public address 
    (based on the private key) and a electrum wif key for importing 
    into the electrum Bitcoin wallet.
    """
    priv = random_key()
    pub = privtopub(priv)
    addr = pubtoaddr(pub)
    electrumPKey = encode_privkey(priv, 'wif')

    return priv, pub, addr, electrumPKey

def check_balance_blockchain_com(addr):
    """
    This function checks the balance of the address and
    returns the result for further processing.
    """
    url = "https://blockchain.info/q/addressbalance/"+str(addr)
    balance = requests.get(url).json()
    ## Placeholder variables
    # balance = 0
    return balance

def check_balance_blockcypher_com(addr):
    """
    This function checks the balance of the address and
    returns the result for further processing.
    """
    url = "https://api.blockcypher.com/v1/btc/main/addrs/"+str(addr)+"/balance"
    balance = requests.get(url).json()
    ## Placeholder variables
    # balance = 0
    return balance

def telegram(balance, priv, pub, addr, electrumPKey):
    """
    This function sends an alarm via Telegram that an address
    with balance has been found.
    """
    if balance > 0:
        def telegram_bot(bot_message):
             # Enter your bot token and bot chat ID here for warnings with Telegram
            bot_token = config.token
            bot_chatID = config.chatID
            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

            response = requests.get(send_text)
            return response.json()        
        
        bot_message = "Found BTC Address: " + str(addr) + " - Private key: " + str(priv) + " - Electrum key: " + str(electrumPKey) + " - with: " + str(balance) + " satoshi."
        
        telegram_bot(bot_message)

def log_addr(balance, priv, pub, addr, electrumPKey):
    """
    This function logs the address, amount and private key(s)
    if balance on address is greater than 0.
    """
    if balance > 0:
        text_file = open("foundSatoshi.csv", "a+")
        text_file.write("\n" + str(balance) + "," + str(addr) + "," + str(electrumPKey) + "," + str(priv) + "," + str(pub))
        text_file.close()

def countdown(timer):
    while timer >= 0:
        print(timer, end=' ')
        time.sleep(1)
        timer -= 1
    # create bitcoin address
    priv, pub, addr, electrumPKey = create_addr()

    # try: # Try exception block chatches errors when checking balance on address

    # Check the balance of the Bitcoin address
    balance = check_balance_blockchain_com(addr)

    # Write to log if amount > 0
    log_addr(balance, priv, pub, addr, electrumPKey)

    # Send notification through Telegram if amount > 0
    telegram(balance, priv, pub, addr, electrumPKey)

    # Print output to console for visual check of script running.
    print("\n" + str(balance) + " satoshi ound on BTC address: " + str(addr))

def main():
    countdown(timer)

if __name__ == '__main__':
    while True:
        main()
        # time.sleep(15)
