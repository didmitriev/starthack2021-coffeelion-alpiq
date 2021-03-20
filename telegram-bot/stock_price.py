# Get Gamestop Stock Price and send
import yfinance as yf

symbol = 'GME'


def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data['Close'][0]
    

print(get_current_price('GME'))

# print(get_current_price('GME'))