import mysql.connector as mysql
import datetime as dt

def login():
    cred = {'admin': 'admin'}
    while True:
        u_name = input('Username: ')
        if u_name in cred.keys():
            user = u_name
            break
        else:
            print('Username Does not Exits...Try Again')
            continue

    while True:
        passwd = input('Password: ')
        if cred[user] == passwd:
            break
        else:
            print('Wrong Password...Try Again')
    
def sql():
    global con
    global cur
    con = mysql.connect(host="localhost",
                              user="root",
                              passwd="passwd",
                              database="vishnu")
    cur = con.cursor()
    
def date_today():
    global today
    today = dt.datetime.today().strftime('%Y-%m-%d')
    
def values():
    global attendance
    global stds
    attendance = []
    cur.execute('desc attend')
    x = cur.fetchall()
    n = len(x)
    stds = []
    for i in range(1, n):
        stds.append(x[i][0])
        value = input('Is {} present? (y/n): '.format(x[i][0]))
        if value == 'y' or value == 'yes':
            attendance.append('Present')
        elif value == 'n' or value == 'no':
            attendance.append('Absent')
    attendance  = tuple(attendance)
    stds = tuple(stds)

def query():
    login()
    sql()
    date_today()
    n = 0
    
    try:
        cur.execute("insert into attend(Date) values (\'{}\')".format(today))
        con.commit()
        values()
    except:
        print('Attendance Already Exists For Today....Come Back Tommorow')
        input('Press Enter To Exit')

    try:
        for i in stds:
            cur.execute("update attend set {} = \'{}\' where Date = \'{}\'".format(stds[n], attendance[n], today))
            con.commit()
            n += 1
        print('Thank You!!....Come Back Tommorow')
        input('Press Enter To Exit')
    except:
        print()

query()



    




    


