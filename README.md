# FinAlert
Set custom stock alerts simply by sending an SMS message. Messaging serviced through Twilio, and Webhook/Web-app hosted using Flask and Ngrok. 

<hr>

<h2>Twilio Setup</h2>
Create a free account on <a href="https://www.twilio.com/"> Twilio </a>, and follow the instructions to obtain Account SID, Auth Token, and Twilio phone number. Additionally, create an <a href="https://ngrok.com/">Ngrok </a> account, and configure your ngrok agent with your unique Authtoken. Finally create a `keys.py` file to store all sensitive information as follows. 
