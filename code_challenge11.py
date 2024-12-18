for z in range(1,5):
    for y in range(5, z, -1):
        print(" ", end = " ")

    for x in range(1, z+1):
        print("+", end=" ")

    for a in range(1, z+1):
        print("$", end =" ")
    print()


for z in range(1,5):
    for y in range(3, z + 1):
        print(" ", end = " ")

    for x in range(z, 4, -1):
        print("+", end= " ")

    for a in range(z, 4, -1):
        print("$", end = " ")
    print()