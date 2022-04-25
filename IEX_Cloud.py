#imports
import pyEX as p
import requests

# IEX class
class IEX:

    #constructor creation
    def __init__(self, token, symbol):
        self.base_url = 'https://cloud.iexapis.com/stable'
        self.token = token
        self.symbol = symbol

    #get stock updates
    def stock_quote(self):
        stock = p.Client(api_token=self.token, version='stable')
        sym = self.symbol
        df = stock.quote(symbol=sym)
        
        return df
    
    #get company logo
    def company_logo(self):
        url = f'{self.base_url}/stock/{self.symbol}/logo?token={self.token}'
        req = requests.get(url)
        
        return req.json()['url']
    
    #get company information
    def company_info(self):
        url = f'{self.base_url}/stock/{self.symbol}/company?token={self.token}'
        req = requests.get(url)
        
        return req.json()
