#imports
import csv
import datetime
import json
import pytz
from kafka import KafkaConsumer
import temp

#consumer class
class Consumer:
    
    #consumer_property
    consumer = KafkaConsumer("first_topic",
            bootstrap_servers='localhost:9092',
            auto_offset_reset='latest')
    
    print("starting the consumer")
   
    #data update            
    for msg in consumer:
        
        receive_data = json.loads(msg.value)
       
        if receive_data['isUSMarketOpen']:
            date = datetime.datetime.now(pytz.timezone('America/New_York')).strftime("%Y-%m-%d")
            current_time = datetime.datetime.strptime(receive_data['latestTime'], "%I:%M:%S %p").strftime("%H:%M:%S")
            company_name = receive_data['companyName']
            company_open = receive_data['iexOpen']
            company_close = receive_data['iexClose']
            company_high = receive_data['iexAskPrice']
            company_low = receive_data['iexBidPrice']
        
        else:
            date = datetime.datetime.strptime(receive_data['latestTime'],'%B %d, %Y').strftime('%Y-%m-%d')
            current_time = ' '
            company_name = receive_data['companyName']
            company_open = receive_data['open']
            company_close = receive_data['close']
            company_high = receive_data['high']
            company_low = receive_data['low']

        ID = int(temp.index())
        SQL = [ID + 1, company_name, date, current_time, company_open, company_close, company_high, company_low]
        print(SQL)
              
        with open('C:/Users/VK/Desktop/1 Project/stock.csv', 'a', newline='') as data_store:
            writer = csv.writer(data_store)
            writer.writerow(SQL)
       