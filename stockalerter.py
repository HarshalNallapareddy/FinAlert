import yfinance as yf
import time

active_alerts = {}


def getActiveAlerts():
    alerts = []
    for ticker, details in active_alerts.items():
        direction = details[0]
        price = details[1]
        alert = str(ticker) + " " + str(direction) + " " + str(price)
        alerts.append(alert)

    return alerts
        
def getCurrentPrice(ticker):
    stock = yf.Ticker(ticker)
    currentPrice = stock.info['regularMarketPrice']
    return round(currentPrice, 2)

def alert(formattedAlert):

    ticker = formattedAlert[0]
    direction = formattedAlert[1]
    trigger_price = formattedAlert[2]

    active_alerts[ticker] = (direction, trigger_price)

    while (True):

        time.sleep(1)
        current_price = getCurrentPrice(ticker)
        if (direction == 'over' and current_price > trigger_price):
            print( "********** %s is %s %d **********" % (ticker, direction, trigger_price))
            del active_alerts[ticker]
            break
        elif (direction == 'under' and current_price < trigger_price):
            print( "********** %s is %s %d **********" % (ticker, direction, trigger_price))
            del active_alerts[ticker]
            break

    return True