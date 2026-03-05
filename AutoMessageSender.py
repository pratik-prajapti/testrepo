import pywhatkit
import time

phone_number = "+91xxxxxxxxxx"   # Enter number with country code
message = "Sorry"

for i in range(100):
    pywhatkit.sendwhatmsg_instantly(phone_number, message, wait_time=15, tab_close=True)
    time.sleep(4)   
