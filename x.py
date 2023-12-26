from flask import Flask, render_template
import yfinance as yf

app = Flask(__name__)


@app.route('/')
def hello_world():
    list_of_stocks = ["THYAO.IS","KRDMB.IS","TUPRS.IS","EREGL.IS","TOASO.IS","TTRAK.IS","XU030.IS","USDTRY=X"]
    stock_dict = {}

    for stock in list_of_stocks:
        if stock == "XU030.IS" or stock == "USDTRY=X":
            ticker = yf.Ticker(stock).fast_info
            ticker_x = yf.Ticker(stock).info
            st = {
            "Fiyat": round(ticker["lastPrice"],2),
            "Dunku Kapanis": round(ticker_x["previousClose"],2),
            "Yuzdelik Degisim": round((ticker["lastPrice"] - ticker_x["previousClose"]) / ticker_x["previousClose"] * 100,2)
            }
            stock_dict[stock] = st
            continue
        ticker = yf.Ticker(stock).info
        
        
        st = {
            "Fiyat": ticker["currentPrice"],
            "Dunku Kapanis": ticker["previousClose"],
            "Yuzdelik Degisim": round((ticker["currentPrice"] - ticker["previousClose"]) / ticker["previousClose"] * 100,2)
        }
        stock_dict[stock] = st

    return render_template('stocks.html', stock_dict=stock_dict)

if __name__ == '__main__':
    app.run(debug=True)
