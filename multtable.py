size=int(raw_input("Enter a number: "))
row = []
table = []
for i in range(1, size+1):
    for j in range(1, size+1):
        row.append(i*j)
    print ("%d |" %i)
    print(row)
    row = []
