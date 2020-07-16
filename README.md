# BitcoinLottery

Python script to generate random BTC adresses. If you find an address with wallet balance, you win!
Script is based on Linux systems with Python3 installed.

## Requirements

The following Python modules have to be installed:
* sudo apt install python-pip3
* sudo pip3 install bitcoin [*](https://pypi.org/project/bitcoin/)
* sudo pip3 install requests

## Downloading the BitcoinLottery Python script

Clone or download the code to your computer:

```bash
git clone https://github.com/Willemstijn/BitcoinLottery.git
```

Or download and extract:

https://github.com/Willemstijn/BitcoinLottery/archive/master.zip

## Setting up a Telegram bot

Follow the procedure below to create a channel for signalling found Satoshi's:

* Open and login to [Telegram Web interface](https://web.telegram.org).
* Search @ BotFather and send him a "/start" message.
* To create a new bot, send the "/newbot" message.
* Provice the bot a channel name and user name.
* Telegram provides you with a token for accessing the bot though the HTTP API (Keep this token safe!).
* Search your bot (by the link you just got - e.g. t.me/<botname>), press the “Start” button or send a “/start” message.
* Open a new tab with your browser, enter https://api.telegram.org/bot<yourtoken>/getUpdates. 
* Type ``/start`` to start the bot. You should see something like this:

```json
{"ok":true,"result":[{"update_id":846954168,
"message":{"message_id":2,"from":{"id":6XXXXXXXXX,"is_bot":false,"first_name":"YourFirstName","username":"YourUserName","language_code":"nl"},"chat":{"id":6XXXXXXX,"first_name":"YourFirstName","username":"Yourname","type":"private"},"date":15267434115,"text":"/start","entities":[{"offset":0,"length":6,"type":"bot_command"}]}}]}
```

* Look for “id”, for instance, 6xxxxxxx above is the chat id in this case. 
* Use this "id" and your "token" in the BitcoinLottery script.

## Running the script

### Daemonize
This script will be daemonized.

### Linux

You can run the script in your terminal with this command:

```bash
./run_lottery.py
```

### Windows

Just run the line below in a command prompt in the directory of the script:

```bash
py ./run_lottery.py
```

## Running in the background

### Linux

To let the script run in the background, use the following command:

```bash
nohup ./run_lottery.py &
```

OPTIONAL: Another method is running it in a virtual terminal:

```bash
# Create a new virtual terminal
screen -dmS btcl

# Connect to the virtual screen
screen -r btcl

# Run the script
./run_lottery.py
```

Close your terminal screen. The BitcoinLottery PID belongs to the virtual terminal and keeps running.  
To check the script, run ''screen -r btcl'' again

### Windows

Have not found a way yet and no rush to find one because I use Linux. Guess you'll have to leave a terminal session open during the lottery.

## Addendum

The url's below provide API's to check the balance of a bitcoin address. 
These url's come from: https://bitcointalk.org/index.php?topic=1605809.0

**Confirmed**:

https://blockchain.info/q/addressbalance/<address>
https://www.bitgo.com/api/v1/address/<address>


Unconfirmed:****

http://btc.blockr.io/api/v1/address/info/
https://blockexplorer.com/api/addr/
https://bitcoin.toshi.io/api/v0/addresses/
https://chain.api.btc.com/v3/address/
https://api.blocktrail.com/v1/btc/address/1NcXPMRaanz43b1kokpPuYDdk6GGDvxT2T?api_key=MY_APIKEY
https://api.blockcypher.com/v1/btc/main/addrs/1DEP8i3QJCsomS4BSMY2RpU1upv62aGvhD/balance
https://api-r.bitcoinchain.com/v1/address/1Chain4asCYNnLVbvG6pgCLGBrtzh4Lx4b
https://api.kaiko.com/v1/addresses/3Nt1smucEdFks8uYQhyGvXGBuocTcMSmsT
https://chainflyer.bitflyer.jp/v1/address/1LDWeSRJukN7zWXDBpuvB2WGsMxYE7UTnQ
https://insight.bitpay.com/api/addr/1NcXPMRaanz43b1kokpPuYDdk6GGDvxT2T/?noTxList=1
https://api.coinprism.com/v1/addresses/1dice97ECuByXAvqXpaYzSaQuPVvrtmz6
