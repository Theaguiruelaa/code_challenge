shopper= input("Hi Shopper, Welcome! ")
grocery = input("\nDid you buy a grocery: (Yes/No) ") 

if grocery.lower() == "yes":

    item = input("Name of the Item: ")

    itemprice = eval(input("Price of the Item: "))

    age = eval(input("Age: "))

    hmamount = eval(input("Amount given: "))

    discount = round((hmamount * 0.052), 2)

    discountprice = round((hmamount - discount), 2)

    tax = round((itemprice * 0.123), 2)

    taxprice = round((itemprice + tax), 2)

    if age >= 60: 

        print(f"\nHi consumer, you purchased a {item}, with a price of {itemprice} php minus a 5.2% discount({discount} php) to your total purchase. ")

        print(f"\nTotal of: {round((itemprice - discount), 2)}")

        print(f"\nChange: {round((hmamount - discountprice), 2)}")

        print("\nThank you for shopping. ")

    elif age >= 18 and age <= 60:
        print(f"\nHi consumer, you purchased a {item}, with a price of {itemprice} php plus a 12.3% tax({tax} php) to your total purchase. ")
    
        print(f"\nTotal of: {round((itemprice + tax), 2)}")

        print(f"\nChange: {round((hmamount - taxprice), 2)}")

        print("\nThank you for shopping. ")

else: 

    print("Thank you for dropping by. See you again.")