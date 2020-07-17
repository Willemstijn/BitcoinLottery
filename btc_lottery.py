#!/usr/bin/env python3
import requests
from bitcoin import *
import time

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

def check_balance(addr):
    """
    This function checks the balance of the address and
    returns the result for further processing.
    """
    url = "https://blockchain.info/q/addressbalance/"
    api_check = url+str(addr)
    balance = requests.get(api_check).json()
    
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
            bot_token = ''
            bot_chatID = ''
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

def main():
    """
    Main function for running the script.
    Does the following:
    - Creates a bitcoin address, private keys etc. (create_addr)
    - Checks if the keys contain balance (check_balance)
    - Warns if it does and writes the information to a file
    """
    # create bitcoin address
    priv, pub, addr, electrumPKey = create_addr()
    
    # Check the balance of the Bitcoin address
    balance = check_balance(addr)

    # Write to log if amount > 0
    log_addr(balance, priv, pub, addr, electrumPKey)

    # Send notification through Telegram if amount > 0
    telegram(balance, priv, pub, addr, electrumPKey)

    # Print output to console for visual check of script running.
    print(str(balance) + " satoshi has been found on BTC address: " + str(addr) + ". Keep trying!!")
    # print('=============================================================================')
    # print("BTC Address: " + str(addr))
    # print("Pub Address: " + str(pub))
    # print("Private Key: " + str(priv))
    # print("Electrum Import Key: " + str(electrumPKey))
    # print("Amount on address: " + str(balance))
    # print('=============================================================================')

if __name__ == '__main__':
    while True:
        main()
        time.sleep(5)
