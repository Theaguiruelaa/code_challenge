goon = True
count = 0
total = 0

while goon:
    number = int(input("Enter a number: "))

    
    if number == 0:
        print("\nLoop has now stopped.")
        print(f"You have entered {count} numbers.")
        print(f"The sum of all the numbers given is: {total}")
        break

    count += 1
    total += number

    continue