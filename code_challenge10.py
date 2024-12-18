for z in range(1,6):
    for y in range(6, z, -1):
        print(" ", end = " ")

    for x in range(1, z+1):
        print("*", end=" ")

    for a in range(1, z+1):
        print("*", end =" ")
    print()


for z in range(1,6):
    for y in range(1, z + 1):
        print(" ", end = " ")

    for x in range(6, z, -1):
        print("*", end= " ")

    for a in range(6, z, -1):
        print("*", end = " ")
    print()