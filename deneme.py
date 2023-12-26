import yfinance as yf

x = yf.Ticker("XU030.IS").fast_info
y = yf.Ticker("XU030.IS").info

print(x["lastPrice"])
print(x["previousClose"])
print(x["exchange"])

last = x["lastPrice"]
previous = y["previousClose"]

print((last - previous) / previous * 100)
x = yf.Ticker("THYAO.IS").info

print(x["currentPrice"])
print(x["previousClose"])




x = yf.Ticker("USDTRY=X").fast_info
print(x)