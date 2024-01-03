import yfinance as yf
import tqdm as tqdm

def get_stock_info_dict(stock_list):

    if stock_list == None:
        return None
    
    stock_dict = {}

    for stock in tqdm.tqdm(stock_list, desc=f"Getting stock info", unit="stock"):
        
        try:
            ticker = yf.Ticker(stock).info
            
            #if ticker not have current price key try fast_info
            if "currentPrice" not in ticker:
                ticker_fast = yf.Ticker(stock).fast_info
                st = {
                "price": round(ticker_fast["lastPrice"],2),
                "previousClose" : round(ticker["previousClose"],2),
                "rate": round((ticker_fast["lastPrice"] - ticker["previousClose"]) / ticker["previousClose"] * 100,2)
                }
                stock_dict[stock] = st
                continue

            st = {
                "price": ticker["currentPrice"],
                "previousClose": ticker["previousClose"],
                "rate": round((ticker["currentPrice"] - ticker["previousClose"]) / ticker["previousClose"] * 100,2)
            }
            stock_dict[stock] = st



        except Exception as e:
            print(f"Error occured while getting info for {stock}")
            print(e)
            continue

    return stock_dict