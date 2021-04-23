# safemoon-tracker


A simple python based tracker for cryptocurrency price, wallet balance and wallet value. 

For use tracking the Safemoon cryptocurrency based on the BSCscan and Pancakeswap API's. Given the inconsistent pricing shown for Safemoon accross exchanges, I made this nifty little tracker to know what the value of my coin is specifically on Pancakeswap. You can use it too!

If you only wish to watch the price and not to track your wallet value, simply enter 'P' when the program prompts you. It pulls straight from the Pancakeswap API, unfortunately their API seems slow to update so you may see repeated values for a while, but rest assured it's not frozen. If you wish to also track your personal wallet balance and value, follow the steps outlined below:

This project does not work out of the box. If you wish to use it to track your own wallet, you must set it up yourself. There are comments within the source code explaining how to do this, it is also outlined below:

1: You must set up your own bscscan API key to access bscscan data. Create an account on bscscan found here: https://bscscan.com/apis

2: Once your account is set up, generate an API key and copy it. Open the source code in your editor of choice (Notepad is ok) and insert the key in the designated variable as outlined by the comments.

3: The other thing you need is your public Safemoon wallet address. You can find this on Trustwallet and Metamask easily, by navigating to the 'receive' page on your wallet and copying your address. Paste it in the designated variable within the source code.

4: You're all set! Double click the file in explorer to run it (must have python3 installed), and watch your balance as it grows! Enter 'P' to see price only, 'W' to track wallet balance only, or 'F' to run the full program and also see the value of your wallet balance in USD. Have fun, and and keep on HODLing!

NOTE: This is not a compiled EXE. It's simply a .py file, so you must have python installed to run it. Also, note that putting your public wallet key into this program is 100% safe. Nobody can access your coin just with your public key. You can see the entire source code, so if you are afraid anything fishy is being pulled go ahead and look through it to see how the program uses your public key.

Thanks for your interest in my little tool!
