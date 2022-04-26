# KAFKA BASED STOCK UPDATES

## Aim
The project is created to fetch stock live updates using Apache Kafka and updating MySQL data repository. Also a visual representation of stock of different companies are made as candlestick chart and stored in PDF format.  

## Table of contents
* [Introduction](#Introduction)
* [Technologies](#Technologies)
* [Screenshots](#Screenshots)
* [Setup](#Setup)
* [Launch](#Launch)
* [Additional](#Additional)

## Introduction
In this project the stock live updates are fetched using Apache Kafka and then the extracted data is processed and cleansed to later store it in a flat file, here, a CSV file. The processed data is also stored in MySQL database locally in this case, but can also be stored in the global version. And finally, the visual representation of desired data is presented using candlestick chart and it is locally stored in PDF format. The stock data is fetched using IEX cloud api key.
> NOTE: To access the Kafka topic using Python, it was already created using CLI. ALso a desired databse was pre-selected in MySQL to store the data. 

## Technologies
Project is created with:
* Apache Kafka
* Python 3
* MySQL
* kafka-python library
* pyEX library
* pandas library
* fpdf library
* mysql library
* matplotlib library

## Screenshots
* Apache Kafka
![Kafka](https://github.com/Vishal-HubGit/kafka-based-stock-updates/blob/main/visuals/kafka.png)
* Python script
![Kafka-Python](https://github.com/Vishal-HubGit/kafka-based-stock-updates/blob/main/visuals/kafka-python.png)
* MySQL
![MySQL](https://github.com/Vishal-HubGit/kafka-based-stock-updates/blob/main/visuals/MySQL.png)

## Setup
To run this project, the following programs are required:
* Apache Kafka
* Python 3
* MySQL

## Launch
To launch this project, the following packages are required in Python:
* kafka-python library
```
pip install kafka-python
```
* pyEX library
```
pip install pyex
```
* pandas library
```
pip install pandas
```
* fpdf library
```
pip install fpdf
```
* mysql-connector library
```
pip install mysql-connector-python
```


## Additional
In addition to stock updates, there are other methods also available to fetch company logo or company information inside the IEX_Cloud.py .
