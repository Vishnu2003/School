import requests
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot  as plt
from time import sleep

def live_data():
    global data
    global con_data
    try:
        print('Trying to connect to network...'); sleep(2)
        api = 'https://api.covid19api.com/summary'
        req = requests.get(api).text
        raw_data = bs(req, 'lxml').text
        text = open("data.txt","w")
        text.write(raw_data)
        text.close()
        data = eval(open('data.txt').read())
        con_data = data['Countries']
        print('Connection... Successful...Proceeding...'); sleep(2)
    except:
        print('Network Error...Trying with old data...'); sleep(3)
        try:
            data = eval(open('data.txt').read())
            con_data = data['Countries']
        except:
            print('Cannot retrive the data...Connect to a Network and try again...'); sleep(1)
            input('Press ENTER to exit...')
            exit()
    
def quick_stats():
    gbl_dat = data['Global']
    keys = gbl_dat.keys()
    values = gbl_dat.values()
    plt.bar(keys, values)
    plt.title('Scale : y axis 1 cm = 1000000 units')
    plt.show()

def data_by_code():
    usr_code = input('Enter the Country code which you want the details: ').upper()
    for i in range(len(con_data)):
        if con_data[i]['CountryCode'] == usr_code:
            for key, value in con_data[i].items():
                print(key, ':', value)
            break
                                   
def data_by_con():
    con = input('Enter the Country which you want the details: ').capitalize()
    for i in range(len(con_data)):
        if con_data[i]['Country'] == con:
            for key, value in con_data[i].items():
                print(key, ':', value)
            break
                      
live_data()
#data_by_code()
#data_by_con()
quick_stats()





