def account(name, initial_deposit = 0):
    account_name = name
    balance = initial_deposit
    print(f"Bank Account Created For {account_name} with Initial Deposit of {balance}")

def denomination(amount):
    thou = amount // 1000 
    tsukli = amount % 1000

    fhund = amount // 500
    fsukli = amount % 500

    thund = amount // 200
    tsukli = amount % 200


    ohund = amount // 100
    osukli = amount % 100

    fifty = amount // 50
    ftsukli = amount % 50

    twenty = amount // 20
    twensukli = amount % 20

    ten = amount // 10
    tensukli = amount % 10

    five = amount // 5
    fivesukli = amount % 2