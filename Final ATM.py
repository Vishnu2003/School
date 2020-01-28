acc_no={12345:1234,
        23451:2341,
        34512:3412,
        45123:4123,
        51234:4321}

acc_bal={12345:364734,
        23451:5637564,
        34512:552753,
        45123:7275,
        51234:58245}


def run():
    while True:
        accountno = int(input('Enter your account number: '))
        if accountno in acc_no.keys():
            user = accountno
            break
        else:
            print('Enter the correct account number: ')
            continue

    while True:
        pin = int(input('Enter your pincode: '))
        if acc_no[user] == pin:
            break
        else:
            print('Pincode is wrong try again: ')


    print('select an action ')
    print('select 1 to check balence')
    print('select 2 withdraw')
    print('select 3 to deposit')
    print('select 4 to transfer')

    usr_actn=int(input('Enter the action: '))
    if usr_actn == 1:
        print('The ammount in your account is: ', acc_bal[user])
        print('THANK YOU!!!...')
    elif usr_actn == 2:
        print('The ammount in your account is: ', acc_bal[user])
        withdraw=int(input('Enter the ammount you want to withdraw: '))
        acc_bal[user]=acc_bal[user]-withdraw
        print('Current balence: ',acc_bal[user])
        print('THANK YOU!!!...')
    elif usr_actn == 3:
        print('The ammount in your account is: ', acc_bal[user])
        deposit = int(input('Enter the ammount you want to deposit: '))
        acc_bal[user] = acc_bal[user] + deposit
        print('Current balence: ', acc_bal[user])
        print('THANK YOU!!!...')
    else:
        print('The ammount in your account is: ', acc_bal[user])
        while True:
            t_acnt = int(input('Enter the account you want to transfer: '))
            if t_acnt in acc_no.keys():
                print('The ammount in the transfer account: ',acc_bal[t_acnt])
                t_amnt = int(input('Enter the ammount you want to transfer: '))
                acc_bal[user] = acc_bal[user]-t_amnt
                acc_bal[t_acnt] = acc_bal[t_acnt]+t_amnt
                print('Current balence: ', acc_bal[user])
                print('The ammont in the transferd account: ',acc_bal[t_acnt])
                print('THANK YOU!!!...')
                break
            else:
                print('Enter transfer account number correctly')
                continue


run()

while True:
    rep = input('Do you wan to run again y/n ? : ')
    if rep == 'y':
        run()
    else:
        break







