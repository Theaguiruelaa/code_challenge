for a in range(1,6):
    for b in range(6, a,-1):
        print(" ", end= " ")
    for c in range(a, 0, -1):
        print(c, end=" ")
    for d in range(1, a+1):
        print(d, end= " ")
    print()    
    
for a in range(4, 0, -1):
    for b in range(6, a, -1):
        print(" ", end= " ")
    for c in range(a, 0, -1):
        print(c, end=" ")
    for d in range(1, a+1):
        print(d, end= " ")
    print() 