import investpy
import pandas as pd

#df_klse = investpy.stocks.get_stocks_list(country='malaysia')
df_klse = investpy.stocks.get_stocks(country='malaysia')


df = investpy.get_stock_historical_data(stock='CBMS', country='malaysia', from_date='01/05/2020', to_date='01/06/2020', interval='Monthly')
date = df.index.strftime("%Y/%m/%d").tolist()
df_old =  pd.DataFrame(columns=list(date))
df_old =  pd.DataFrame(columns=['name','symbol'])
x = 0

#for symbol in symbols:
for index, row in df_klse.iterrows():
 df = investpy.get_stock_historical_data(stock=row['symbol'], country='malaysia', from_date='01/06/2016', to_date='01/06/2020', interval='Monthly')
 close = df['Close'].to_list()  #get closed stock price
 date = df.index.strftime("%Y/%m/%d").tolist()  #retrive date from pandas datetimeindex and put into list object

 df_new = pd.DataFrame([close], columns=list(date)) #convert to single row dataframe
 df_new['name'] = row['name']
 df_new['symbol'] = row['symbol']

 df_old = pd.concat([df_old,df_new], axis=0, ignore_index=True) #combine two dataframe regardless of different column names
 x = x + 1
 print(x)
 #if x == 3:
 # break

df_old = df_old.reindex(sorted(df_old.columns), axis=1) #sort the columns
df_old.to_csv("stock_historical.csv")

