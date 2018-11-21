import csv
from os.path import isfile
import requests
import numpy
import json


# Global Variables.
dataFileInfo = ""
readFileName = ""
writeFileName = ""
globalURL = ''
tickerURL = ""
request = ""
globalMarketCap = ""
meanPrice = ''
stdPrice = ''
data = []
coins = []
prices = []


def readConfigurationFile(configFile):
    # Read Configuration file and populate variables.
    global dataFileInfo, readFileName, writeFileName
    dataFileInfo = CSV_Read(configFile)
    readFileName = dataFileInfo[2][0]
    writeFileName = dataFileInfo[2][1]

    # Base URLs.
    global globalURL, tickerURL
    globalURL = str(dataFileInfo[2][2][0])
    tickerURL = str(dataFileInfo[2][3][0])
    return

def welcomeMessage(globalURL):
    # User menu
    dataFromMarket(globalURL)
    print("The current Global Market Cap is at $" + str(globalMarketCap))
    print("Enter 'all' or 'name of crypto' to see the name of the top 100 currencies or a specific currency")
    userChoice = chose()
    decider(userChoice)
    return


def chose():
    choice = input("Your choice: ")
    return choice


def decider(choice):
    global tickerURL, request, data
    if choice == "all":
        request = requests.get(tickerURL)
        data = request.json()
        for x in data:
            symbol = x['symbol']
            coins.append(symbol)
            price = x['price_usd']
            prices.append(price)
            print(symbol + ":\t\t$" + price)
        # meanPrice = numpy.mean([float(i) for i in prices])
        # stdPrice = numpy.std([float(i) for i in prices])
    else:
        tickerURL += '/'+choice+'/'
        request = requests.get(tickerURL)
        data = request.json()

        ticker = data[0]['symbol']
        price = data[0]['price_usd']

        print(ticker + ":\t\t$" + price)
        print()
    return [data, meanPrice, stdPrice]


def dataFromMarket(globalURL):
    global request, data, globalMarketCap
    request = requests.get(globalURL)
    data = request.json()
    globalMarketCap = data['total_market_cap_usd']
    return


def CSV_Read(FileName):
    with open(FileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                Header = row
                lstf = [[] for i in range(len(Header))]
            else:
                index = 0
                for item in row:
                    lstf[index].append(item)
                    index += 1
            line_count += 1
    return [line_count - 1, Header, lstf]


def CSV_Write(FileName, Data, Header):
    new = not isfile(FileName)  # checks if the file exists
    # Potential improvement: if the file exists use your CSV_Read function to ensure the number of columns in Data match number of columns in file.
    with open(FileName, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if new:    writer.writerow(Header)
        resortedData = [[Data[i][r] for i in range(len(Data))] for r in
                        range(len(Data[0]))]  # Convert the elements of the list from columns to rows
        for r in resortedData:
            writer.writerow(r)









