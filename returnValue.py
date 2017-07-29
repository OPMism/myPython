def add(a,b):
    sum = int(a) + int(b)
    return int(sum)

def sub(a,b):
    diff = int(a) - int(b)
    return int(diff)

def mul(a,b):
    product = int(a) * int(b)
    return int(product)

def div(a,b):
    divison = int(a) / int(b)
    return float(divison)

flag = True
while(flag):
    print """
    Options:
    \t * 1 Add
    \t * 2 Subtract
    \t * 3 Multiply
    \t * 4 Divide
    """
    option = int(raw_input("Enter option: "))
    if(option <= 4) and (option >= 1):
        a = raw_input("Enter first number: ")
        b = raw_input("Enter second number: ")
    else:
        print "Incorrect option selected. Program exiting"

    if (option==1):
        result = add(a,b)
    if (option==2):
        result = sub(a,b)
    if (option==3):
        result = mul(a,b)
    if (option==4):
        result = div(a,b)

    print "Result of the operation: %d" % result

    cont = raw_input("Do you want to continue? Y or N ")
    if(cont == 'Y') or (cont == 'y'):
        flag = True
    elif(cont == 'N') or (cont == 'n'):
        flag = False
    else:
        print "Incorrect option selected. Allowed choices are Y or N"
else:
    print "Program exiting"
