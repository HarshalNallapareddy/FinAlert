# FinAlert
Set custom stock alerts simply by sending an SMS message. Messaging serviced through Twilio, and Webhook/Web-app hosted using Flask and Ngrok. 

<hr>

<h2>Setup Guide</h2>
Create a free account on <a href="https://www.twilio.com/"> Twilio </a>, and follow the instructions to obtain Account SID, Auth Token, and Twilio phone number. Additionally, create an <a href="https://ngrok.com/">Ngrok </a> account, and configure your ngrok agent with your unique Authtoken. 

Finally create `keys.py` file to store all sensitive information as follows. 
```python
account_sid = 'YOUR_ACC_SID' # <--- from Console on Twilio.com
auth_token = 'YOUR_AUTH_TOKEN' # <--- from Console on Twilio.com

twilio_number = 'TWILIO_PHONE_NUMBER' # <--- from Console on Twilio.com. Include the country code
target_number = 'TARGET_PHONE_NUMBER' # <--- The phone number you want to send/receive messages. Include the country code
```

Run `ResponseHandler.py` and copy the ngrok URL, and paste it into the "A Message comes in" field under Messaging when you click on your active Twilio Phone Number. Click the "Save" button, and the alerter should be up and running. 

<hr>

<h2>Usage</h2>

To set a custom alert, simply send an as SMS message to the Twilio Phone Number in the following format: `[Ticker] over/under [Alert_Price]`. For example, `SPY over 400` sets an alert that will activate when SPY is at or above 400. 

To view the price of a stock, simply type `[Ticker] price`, and you will receive a message with the specified stock's current price (rounded to 2 decimal places). 

To view all alerts, type `list`, and a list of all active alerts will be displayed. An alert will be removed from this list when triggered.
