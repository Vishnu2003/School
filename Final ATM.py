#Data Sets
acc_no = {12345: 1234,
          23451: 2341,
          34512: 3412,
          45123: 4123,
          51234: 4321}


acc_bal = {12345: 364734,
           23451: 5637564,
           34512: 552753,
           45123: 7275,
           51234: 58245}

#This function is to list the account numbers
def accounts():
    count = 0
    print('S.no  Account Number')
    for i in acc_no.keys():
        count += 1
        print(count,'   ',i)

#This function contains Main Source code
def run():
    while True: #To get the account number from the user
        accountno = int(input('Enter your account number: '))
        if accountno in acc_no.keys():
            user = accountno
            break
        else:
            print('Enter the correct account number: ')
            continue

    while True: #To check the pin
        pin = int(input('Enter your pin code: '))
        if acc_no[user] == pin:
            break
        else:
            print('Pin code is wrong try again: ')

#Shows diffrent action it can do
    print('Select an action')
    print('Select 1 to check balance')
    print('Select 2 withdraw')
    print('Select 3 to deposit')
    print('Select 4 to transfer')

    while True: #To check balance
        usr_actn = int(input('Enter the action: '))
        if usr_actn == 1:
            print('The amount in your account is: ', acc_bal[user])
            print('THANK YOU!!!...')
            break
        elif usr_actn == 2: #to withdraw amount
            print('The amount in your account is: ', acc_bal[user])
            withdraw = int(input('Enter the amount you want to withdraw: '))
            while True:
                acc_bal[user] = acc_bal[user] - withdraw
                if acc_bal[user] < 0:
                    print('Balance is insufficient')
                    acc_bal[user] = acc_bal[user] + withdraw
                    break
                else:
                    print('Current balance: ', acc_bal[user])
                    print('THANK YOU!!!...')
                    break
            break
        elif usr_actn == 3: #To deposit amount
            print('The amount in your account is: ', acc_bal[user])
            deposit = int(input('Enter the amount you want to deposit: '))
            acc_bal[user] = acc_bal[user] + deposit
            print('Current balance: ', acc_bal[user])
            print('THANK YOU!!!...')
            break
        elif usr_actn == 4: #to transfer from one user to another
            print('The amount in your account is: ', acc_bal[user])
            while True:
                t_acnt = int(input('Enter the account you want to transfer: '))
                if t_acnt in acc_no.keys() and t_acnt != user:
                    print('The amount in the transfer account: ', acc_bal[t_acnt])
                    t_amt = int(input('Enter the amount you want to transfer: '))
                    while True:
                        acc_bal[user] = acc_bal[user] - t_amt
                        if acc_bal[user] < 0:
                            print('Balance is insufficient')
                            acc_bal[user] = acc_bal[user] + t_amt
                            break
                        else:
                            acc_bal[t_acnt] = acc_bal[t_acnt] + t_amt
                            print('Current balance: ', acc_bal[user])
                            print('The amount in the transferees account: ', acc_bal[t_acnt])
                            print('THANK YOU!!!...')
                            break
                    break
                else:
                    print('Enter transfer account number correctly')
                    continue
            break
        else:
            print('Enter the option given in the menu')

#Calling the functions
accounts()
run()

#To repeat the program as per user
while True:
    rep = input('Do you wan to run again y/n ? : ')
    if rep == 'y':
        accounts()
        run()
    else:
        break
