#Start Of Code
import mysql.connector as mysql
import matplotlib.pyplot as plt
from tabulate import tabulate

def sql():
    global data
    global brand_data
    global os_data
    global con
    global cur
    con = mysql.connect(host="localhost",
                              user="root",
                              passwd="passwd",
                              database="vishnu")
    cur = con.cursor()
    cur.execute("select brand,count(*) from users group by brand")
    brand_data = cur.fetchall()
    cur.execute("select os,count(*) from users group by os")
    os_data = cur.fetchall()

sql()

def brand_pie():
    l_brand_lab = []
    l_brand_val = []

    for x,y in brand_data:
        l_brand_lab.append(x)
        l_brand_val.append(y)

    plt.figure(0, figsize=(5,5))
    plt.pie(l_brand_val, labels=l_brand_lab, autopct = "%1.1f%%")
    plt.title('Pie Chart of Brands')
    plt.show()

def os_pie():
    l_os_lab=[]
    l_os_val=[]

    for x,y in os_data:
        l_os_lab.append(x)
        l_os_val.append(y)

    plt.figure(0, figsize=(5,5))
    plt.pie(l_os_val, labels=l_os_lab, autopct = "%1.1f%%")
    plt.title('Pie Chart of OS')
    plt.show()

def usr_brand():
    while True:
        inp_brand =input('Enter the Required brand you want: ')
        cur.execute("select cus_name, os from users where brand = '{}'".format(inp_brand))
        brand = cur.fetchall() 
        if brand != []:
            print('\nDetail of the Customers who are using {} Brand\n'.format(inp_brand))
            print(tabulate(brand, headers = ['cus_name', 'os'], tablefmt='psql'))
            break
        else:
            print('Brand Does not Exist!...Try Again...')

def usr_os():
    while True:
        inp_os =input('Enter the Required OS you want: ')
        cur.execute("select cus_name, brand from users where os = '{}'".format(inp_os))
        os = cur.fetchall() 
        if os != []:
            print('\nDetail of the Customers who are using {} OS\n'.format(inp_os))
            print(tabulate(os, headers = ['cus_name', 'brand'], tablefmt='psql'))
            break
        else:
            print('OS Does not Exist!...Try Again...')

def usr():
    while True:
        name_cus = input('Enter the Name of the Customer: ')
        cur.execute("select cus_name, brand, os from users where cus_name = '{}'".format(name_cus))
        cus = cur.fetchall() 
        if cus != []:
            print('\nDetails of the Customers {}\n'.format(name_cus))
            print(tabulate(cus, headers = ['cus_name', 'brand', 'os'], tablefmt='psql'))
            break
        else:
            print('Customer Does not Exist!...Try Again...')
            
def all_usr():
    print('Names of all the Customers\n')
    cur.execute("select cus_name from users")
    users = cur.fetchall()
    print(tabulate(users, headers = ['Customer Names'], tablefmt='psql'))

def mainloop():
    print('Select The Required Output\n')
    print('1. Display pie chart of all Brands')
    print('2. Display pie chart of all OS')
    print('3. Display Customers By Brand')
    print('4. Display Customers by OS')
    print('5. Display the details of the Customer')
    print('6. Display all Customers\n')
    while True:
        x = (input('Enter Here: '))
        if x == '1':
            brand_pie()
            break
        elif x == '2':
            os_pie()
            break
        elif x == '3':
            usr_brand()
            break
        elif x == '4':
            usr_os()
            break
        elif x == '5':
            usr()
            break
        elif x == '6':
            all_usr()
            break
        else:
            print('Select the required output within the given options!...Try Again...')
    
    while True:
        loop = input('Do you want to run the program again (y/n)?')
        if loop == 'yes' or loop == 'y':
            mainloop()
        elif loop == 'no' or loop == 'n':
            print('Thank You!...')
            exit()

mainloop()
    
#End of Code
    
     
OUTPUT:-
https://ibb.co/J7Mt3YH
https://ibb.co/DtNBxRh
https://ibb.co/5nYW0FZ
https://ibb.co/9yzqbqF
https://ibb.co/pfLxpT1
https://ibb.co/tq1SvDw
https://ibb.co/64df7CH








