#!/usr/bin/env python3
import requests, time
from bitcoin import *

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
    # JSON url for checking the balance of the address
    base_url = "https://blockchain.info/q/addressbalance/"
    check_url = base_url+addr
    btc_address_balance = requests.get(check_url).json()
    return btc_address_balance

def telegram():
    pass

def log_addr():
    """
    This function logs the address, amount and private key(s)
    if there is an amount found on the address (Everything > 0).
    """
    print("log_addr: ", btc_address_balance)
    


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
    # print(priv, pub, addr, electrumPKey)
    print("------------------")
    print("BTC Address: " + addr)
    print("Pub Address: " + pub)
    print("Private Key: " + priv)
    print("Electrum Import Key: " + electrumPKey)
    
    # print("Amount on address: " + str(btc_address_balance))
    print('=============================================================================')

    # Check the balance of the Bitcoin address
    check_balance(addr)

    # Log address when amount >0 found
    

if __name__ == '__main__':
    main()
    
