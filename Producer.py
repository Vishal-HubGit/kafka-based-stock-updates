#imports
import json
import time
from kafka import KafkaProducer
from IEX_Cloud import IEX

#producer class
class Producer:
    
    #producer_config
        
    #encoder
    def json_serialize(data):
        return json.dumps(data).encode("utf-8")
    
    #producer_properties
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=json_serialize)
    
    #standalone
    if __name__ == "__main__":
        
        symbol = ['AAPL', 'AMZN', 'FB', 'GOOGL', 'MSFT', 'NFLX', 'TSLA', 'TWTR']
        token = "pk_3e9ccc33732e44ce83989833101f9ff3"
        
        for sym in symbol:
            data = IEX(token, sym)
            send_data = data.stock_quote()
            print(send_data)
            producer.send("first_topic", send_data)
            time.sleep(2)
