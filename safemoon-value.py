import requests
import json
import time

########################## INSERT YOUR INFO AS NEEDED BELOW ################################################

#Contract Address - the token you wish to read value from on Bscscan (set to Safemoon, DO NOT CHANGE)
contractAddr = '0x8076C74C5e3F5852037F31Ff0093Eeb8c8ADd8D3'

#Wallet Address - INSERT YOUR PUBLIC WALLET ADDRESS HERE
walletAddr = ''

#API Key for bscscan - MAKE AND ACCOUNT https://bscscan.com/register verify your account then go to https://bscscan.com/myapikey and generate a new API key. INSERT THAT API KEY HERE
bscAPIkey = ''
  
############################################################################################################

###PROGRAM CODE BELOW - DO NOT TOUCH UNLESS YOU KNOW WHAT YOU ARE DOING###

mode = input("Enter 'F' for Full Mode, 'W' for wallet readout only, or 'P' for price readout only: ")
verbose = False
callBSC = True
callPCS = True
if mode == 'W':
    callPCS = False
elif mode == 'P':
    callBSC = False
elif mode == 'V':
    verbose = True
    mode = 'F'

while True:

    if callBSC == True:
        if verbose == True:
            print("calling bscscan...")

        bscResponse = requests.get('https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress=' + contractAddr + '&address=' + walletAddr + '&tag=latest&apikey=' + bscAPIkey)
        bscData = bscResponse.json() if bscResponse and bscResponse.status_code == 200 else None
        safemoonAmount = bscData["result"]
        safemoonAmount = float(safemoonAmount)
        safemoonAmount = safemoonAmount / 1000000000
        print("Safemoon Balance: " + str(safemoonAmount))

    if callPCS == True:
        if verbose == True:
            print("calling pancakeswap...")

        pkResponse = requests.get('https://api.pancakeswap.info/api/tokens')
        pkData = pkResponse.json() if pkResponse and pkResponse.status_code == 200 else None
        safemoonPrice = pkData["data"][contractAddr]["price"]
        print("SafeMoon Price: " + safemoonPrice)
    
    
    if mode == 'F':
        sfValue = safemoonAmount * float(safemoonPrice)
        sfValue = str(sfValue)
        
        print("Your Balance Value: " + sfValue + "\n")

    if verbose == True:
        print("Waiting 10 seconds...")
    time.sleep(10)