#!/usr/bin/env python3
# Do not start this file. Start "run_lottery.py"!
import requests
from cryptos import *
from bitcoin import *
import time
import config
from bs4 import BeautifulSoup

# Set timer to 15 seconds due to rate-limit on blockchain.com
# Set timer to 20 seconds due to rate-limit on https://www.blockcypher.com/dev/bitcoin/#rate-limits-and-tokens
timer = 1

# Use crypto modules for determining amount
b = Bitcoin()

def create_addr():
    """ 
    This function creates a private key, bitcoin public address 
    (based on the private key) and a electrum wif key for importing 
    into the electrum Bitcoin wallet.
    """
    priv = random_key()
    pub = privtopub(priv)
    addr = pubtoaddr(pub)
    # Address for testing purposes
    # addr = '3LtmPDgAQhpMkuDKpEXbWmMkvq6WKWLatj'
    electrumPKey = encode_privkey(priv, 'wif')

    return priv, pub, addr, electrumPKey

def check_balance_crypto_mod(addr):
    """
    This function checks the balance of the address
    through the crypto module and
    returns the result for further processing.
    """
    print(f"Public address: {addr}")

    inputs = b.unspent(addr)
    tx = b.mktx(inputs)
    # print(json.dumps(tx, indent=4))
    # Balance (amount) is nested in a json list and dictionary
    # print(tx)
    balance = tx['ins'][0]['amount']
    # print(balance)

    return balance

def check_balance_blockchain_com(addr):
    """
    This function checks the balance of the address and
    returns the result for further processing.
    """
    url = "https://blockchain.info/q/addressbalance/"+str(addr)
    balance = requests.get(url).json()

    return balance

def check_balance_blockchain_com_beautifulsoup(addr):
    """
    This function checks the balance of the address with beautifulsoup 
    and returns the result for further processing.
    """
    url = "https://www.blockchain.com/btc/address/"
    
    result = requests.get(f"{url}{addr}")
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    
    # get balance from site and print tag value
    tags = soup.find_all(class_="sc-1ryi78w-0 gCzMgE sc-16b9dsl-1 kUAhZx u3ufsr-0 fGQJzg")
    balance_list = tags[4].string.split()
    balance_str = balance_list[0]
    balance = float(balance_str)
    
    return balance

def check_balance_blockcypher_com(addr):
    """
    This function checks the balance of the address and
    returns the result for further processing.
    """
    url = "https://api.blockcypher.com/v1/btc/main/addrs/"+str(addr)+"/balance"
    balance = requests.get(url).json()

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

    try: 
            # Check the balance of the Bitcoin address
            balance = check_balance_crypto_mod(addr)

            # Write to log if amount > 0
            log_addr(balance, priv, pub, addr, electrumPKey)

            # Send notification through Telegram if amount > 0
            telegram(balance, priv, pub, addr, electrumPKey)

            # Print output to console for visual check of script running.
            print("\n" + str(balance) + " satoshi found on BTC address: " + str(addr))

    except(IndexError) as e:
        print("No amount on address.")
    # balance = check_balance_blockchain_com_beautifulsoup(addr)
    # IndexError: list index out of range


def main():
    countdown(timer)

if __name__ == '__main__':
    while True:
        main()
        # time.sleep(15)
