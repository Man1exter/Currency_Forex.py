# pip install forex-python !
from forex_python.converter import CurrencyRates

print("..Currency Converter From Forex..")

cash = CurrencyRates()   # creating instance

r = cash.convert("USD","INR",1)

print("Convert USD to INR =======> ",r)
