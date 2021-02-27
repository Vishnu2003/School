#importing modules
import mysql.connector as mysql
import datetime as dt

#Establishing sql connection with python
con = mysql.connect(host="localhost",
                    user="root",
                    password="myhome",
                    database="atm")

cur = con.cursor()

#function to login
def login():
    #Username and password list
    cred = {'admin': '1234'}
    while True:
        username = input('Username: ')
        if username in cred.keys():
            user = username
            break
        else:
            print('Username Does not Exist...Try Again')
            continue

    while True:
        password = input('Password: ')
        if cred[user] == password:
            break
        else:
            print('Wrong Password...Try Again')
    
#using time module to get the current date
def date_today():
    global today
    today = dt.datetime.today().strftime('%Y-%m-%d')
    print(today)
   
#to recieve the attendence from th user
def values():
    #assigning attend, stds lists as a global variable to use it outside the function
    global attend
    global stds
    attend = []
    cur.execute('desc attendance')
    x = cur.fetchall()
    n = len(x)
    stds = []

    for i in range(1, n):
        stds.append(x[i][0])
        value = input('{} (p/a): '.format(x[i][0]))

        if value == 'p' or value == 'present':
            attend.append('Present')

        if value == 'a' or value == 'absent':
            attend.append('Absent')

#function to update the table with attendance with user entered data
def query():
    login()
    date_today()
    n = 0
    
    try:
        cur.execute("insert into attendance(Date) values (\'{}\')".format(today))
        con.commit()
        values()
    except:
        print('Attendance Already Exists For Today...Come Back Tommorow')
        input('Press Enter To Exit')
    try:
        for i in stds:
            cur.execute("update attendance set {}= \'{}\' where Date = \'{}\'".format(stds[n], attend[n], today))
            con.commit()
            n += 1
        print('Thank You!!...Come Back Tommorow')
        input('Press Enter To Exit')
    except:
        pass

#calling the initial function query where the other functions called inside it
# query()

def attend_chk():
    while True:
        usr_name=input('Enter the name of the student you want to check the attendance: ')
        usr_date=input('Enter the date you want check the attendance for(yyyy-mm-dd): ')
        try:
            cur.execute("select {} from attendance where Date = \'{}\'".format(usr_name, usr_date))
            atd_chk = cur.fetchall()
            print('\nThe student {} was {} on {}'.format(usr_name, atd_chk[0][0], usr_date))
            break
        except:
            print('\nThe Student name or date is Incorrect!...try again!...\n')

def attend_chng():
    login()
    while True:
        usr_name=input('Enter the name of the student you want to update the attendance:  ')
        usr_date=input('Enter the date you want Update the attendance for(yyyy-mm-dd): ')
        usr_attnd=input('The student {} (p/a):'.format(usr_name))
        if usr_attnd == 'p':
            usr_attnd='Present'
        if usr_attnd == 'a':
            usr_attnd='Absent'
        try:
            cur.execute("update attendance set {}= \'{}\' where Date = \'{}\'".format(usr_name, usr_attnd, usr_date))
            con.commit()
            cur.execute("select {} from attendance where Date = \'{}\'".format(usr_name, usr_date))
            atd_chk = cur.fetchall()
            print('\nThe student {} was {} on {}'.format(usr_name, atd_chk[0][0], usr_date))
            break
        except:
            print('\nError updating attendance!...try again!...\n')

def mainloop():

    """Function to control the flow of the code"""

    # To print the header of the project in ascii

    print('1. Enter attendance for today')
    print('2. Check attendance')
    print('3. Update attendance')
    
    while True:
        usr_option = int(input('Enter the option: '))

        #To check wether the options are entered correctly
        if usr_option in (1, 2, 3):
            break
        else:
            print('Select correct option...Try Again...\n')
    
    #Calling the functions according to user entered option

    #When user selects option 1
    if usr_option == 1:
        query()
    #When user selects option 2
    if usr_option == 2:
        attend_chk()
    #When user selects option 3
    if usr_option == 3:
        attend_chng()
    
    # To ask the user to run the code again

    while True: 
        loop = input('Do you want to run the program again (y/n)?')

        #When user wants to run the code again
        if loop == 'yes' or loop == 'y':
            #Calling the mainloop function to run again
            mainloop() 

        #When user wants Quit the code
        elif loop == 'no' or loop == 'n':
            exit()

mainloop()
