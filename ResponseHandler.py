from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from flask_ngrok import run_with_ngrok
from twilio.rest import Client

import keys, stockalerter, time, sys

client = Client(keys.account_sid, keys.auth_token)
message = client.messages.create(
        body= "\nLevel Alerter Activated. Set triggers in the following format: [ticker] [over/under] [trigger price]",
        from_= keys.twilio_number,
        to = keys.target_number
)   

app = Flask(__name__)
run_with_ngrok(app)

@app.route('/')
def hello():
    return "Placeholder Homepage"

#formats user-input into tuple with ticker, direction, and trigger_price 
def formatAlert(user_input):
    user_input_split = user_input.split(" ")

    ticker = str(user_input_split[0]).upper() #converts Spy to SPY
    direction = str(user_input_split[1]).lower() #converts Under to under

    if direction != 'under' and direction != 'over':
        return None

    trigger_price = round(float(user_input_split[2]), 2)

    return (ticker, direction, trigger_price)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    body = request.values.get('Body', None)
    resp = MessagingResponse()

    if "list" in body:
        alerts = stockalerter.getActiveAlerts()
        alert_string_builder = ""
        for alert in alerts:
            alert_string_builder += ("- " + alert + "\n")

        resp.message("\nHere are the active alerts:\n" + alert_string_builder)

    elif "price" in body:
        price_query = body.split(" ")
        ticker = price_query[0].upper()

        resp.message("The price of %s is %f" % (ticker, stockalerter.getCurrentPrice(ticker)))

    else:

        formatted_alert = formatAlert(body)
        if formatted_alert is not None:

            ticker = formatted_alert[0]
            direction = formatted_alert[1]
            trigger_price = formatted_alert[2]
                        
            if stockalerter.alert(formatted_alert):
                resp.message("\n***%s is at the %f level***" % (ticker, trigger_price))
        else:
            resp.message("\nInvalid input")

    return str(resp)

if __name__ == "__main__":
    app.run()