#imports
import matplotlib.pyplot as plt
import pandas as pd
from fpdf import FPDF

#index for csv insertion
def index():
    with open('<FILE-PATH>/stock.csv', 'r') as index:
        ID = list(index.readlines()[-1].split(','))[0]
    
    return ID

#candlestick update 
def graph():
    data = pd.read_csv('<FILE-PATH>/stock.csv')
    data_stock = data[['Company_Name', 'Date', 'Time', 'Open', 'Close', 'High', 'Low']]
    length = len(data)
    Company_name_label = list(data_stock.Company_Name[length - 8:length + 1])
    Date_label = list(data_stock.Date[length - 8:length + 1])
    Time_label = list(data_stock.Time[length - 8:length + 1])
    Open_candlestick = list(data_stock.Open[length - 8:length + 1])
    Close_candlestick = list(data_stock.Close[length - 8:length + 1])
    High_candlestick = list(data_stock.High[length - 8:length + 1])
    Low_candlestick = list(data_stock.Low[length - 8:length + 1])
    plt.style.use('ggplot')
    for i in range(0, 8):
        plt.plot([0, 0], [High_candlestick[i], Low_candlestick[i]], linewidth=2, color='black')
        if Open_candlestick[i] > Close_candlestick[i]:
            plt.plot([0, 0], [Open_candlestick[i], Close_candlestick[i]], linewidth=7, color='green')
            plt.legend([str(Low_candlestick[i]) + ' - ' + str(High_candlestick[i]),
                        str(Close_candlestick[i]) + ' - ' + str(Open_candlestick[i])], loc="lower right")
        else:
            plt.plot([0, 0], [Open_candlestick[i], Close_candlestick[i]], linewidth=7, color='red')
            plt.legend([str(Low_candlestick[i]) + ' - ' + str(High_candlestick[i]),
                        str(Open_candlestick[i]) + ' - ' + str(Close_candlestick[i])], loc="lower right")
        plt.xlim(-5, 5)
        plt.plot([-0.25, 0.25], [High_candlestick[i], High_candlestick[i]], linewidth=2, color='black')
        plt.plot([-0.25, 0.25], [Low_candlestick[i], Low_candlestick[i]], linewidth=2, color='black')
        plt.title(label=Company_name_label[i])
        if Time_label[i] == ' ':
            plt.xlabel(Date_label[i])
        else:
            plt.xlabel(Date_label[i] + ' at ' + Time_label[i])
        plt.savefig(f'<FILE-PATH>/{i+1}.png')
        plt.clf()

    return print("GRAPHS PRODUCED SUCCESSFULLY")

#pdf creation
def pdf_graph():
    pdf = FPDF(orientation='L', unit='mm', format='A4')
    pdf.add_page()
    pdf.image('<FILE-PATH>/1.png', 5, -4, 140, 105)
    pdf.image('<FILE-PATH>/2.png', 150, -4, 140, 105)
    pdf.image('<FILE-PATH>/3.png', 5, 102, 140, 105)
    pdf.image('<FILE-PATH>/4.png', 150, 102, 140, 105)
    pdf.add_page()
    pdf.image('<FILE-PATH>/5.png', 5, -4, 140, 105)
    pdf.image('<FILE-PATH>/6.png', 150, -4, 140, 105)
    pdf.image('<FILE-PATH>/7.png', 5, 102, 140, 105)
    pdf.image('<FILE-PATH>/8.png', 150, 102, 140, 105)
    pdf.output('check.pdf')

    return print("PDF PRODUCED SUCCESSFULLY")
    
