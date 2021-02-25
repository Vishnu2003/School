#start
#importing prerequsites
import mysql.connector as mysql

con = mysql.connect(host="localhost", user="root", passwd="myhome", database='atm') #establishing a connection with sql database
cur = con.cursor()

def initial(): #intial login or sign up prompt
    while True:
        try:
            sel=int(input("1. Login \n2. signup\n\nYour option: "))
            if sel == 1:
                login()
                break
            if sel == 2:
                signup()
                break
            if sel != 1 or sel != 2:
                print('Enter the correct option!!...')
        except:
            print('Enter the correct option!!...')

def login(): #function to login to aaccount
    global acc_no
    acc_no = int(input('\nAccount Number: '))
    try:
        cur.execute('select password from users where accno = {}'.format(acc_no))
        pass_chk = cur.fetchall()

        while True:
            passwd = input('Password: ')
            if pass_chk[0][0] == passwd:
                actions()
                break
            else:
                print('Enter the correct password!...try again\n')  
    except:
        print('Enter the correct Account Number!...Login Expierd...try again\n')
        login()  

def signup(): #function to signup an account
    acc_no = int(input('Enter your required Account Number : '))
    pass_ch = input('Enter your password : ')   
    pass_chk = input('Enter your password Again : ')
    if pass_ch == pass_chk:
        cur.execute('insert into users(accno, password, balance) values({}, {}, 0)'.format(acc_no, pass_chk))
        con.commit()
        print('Account creation successful!... You may proceed to login...\n')
        initial()
    else:
        print('Password does not match try again!...')
        signup()

def actions(): #prompts users with diffrent actions
    print('Select an action')
    print('Select 1 to check balance')
    print('Select 2 withdraw')
    print('Select 3 to deposit')
    print('Select 4 to transfer')
    while True:
        usr_optn=int(input('Input your action: '))
        if usr_optn==1:
            chk_balance()
            break
        if usr_optn==2:
            withdraw()
            break
        if usr_optn==3:
            deposit()
            break
        if usr_optn==4:
            transfer()
            break
        else:
            print('Enter the correct option')
        
def chk_balance(): #function to find the balance of an account
    cur.execute('select balance from users where accno = {}'.format(acc_no))
    bal_sql = cur.fetchall()
    print('Your current balance is: {}'.format(bal_sql[0][0]))
    rep = input('Do you want to use atm again (y/n) ? : ')
    if rep == 'y':
        actions()


def deposit(): #function to deposit ammount into account
    dep_money=int(input('Enter the ammount you want to deposit: '))
    cur.execute('update users set balance=balance+{} where accno={}'.format(dep_money, acc_no))
    con.commit()
    chk_balance()
    rep = input('Do you want to use atm again (y/n) ? : ')
    if rep == 'y':
        actions()

def withdraw(): #function to withdraw ammout from account
    with_money=int(input('Enter the ammount you want to deposit: '))
    cur.execute('update users set balance=balance-{} where accno={}'.format(with_money, acc_no))
    con.commit()
    chk_balance()
    rep = input('Do you want to use atm again (y/n) ? : ')
    if rep == 'y':
        actions()

def transfer(): #function to transfer ammount from one account to another
    trans_accno=int(input('Enter the account number you want to transfer: '))
    trans_money=int(input('Enter the ammount you want to transfer: '))
    cur.execute('update users set balance=balance-{} where accno={}'.format(trans_money, acc_no))
    cur.execute('update users set balance=balance+{} where accno={}'.format(trans_money, trans_accno))
    con.commit()
    chk_balance()
    rep = input('Do you want to use atm again (y/n) ? : ')
    if rep == 'y':
        actions()

con.close() #closing the established sql connection
initial()
#end