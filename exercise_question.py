def printstr(str):
    numbers = str[1::2]
    strings = str[::2]
    output=""
    if len(numbers) == len(strings):
        for i in range(len(numbers)):
            output = output + strings[i]*int(numbers[i])
        return output
inputstring = raw_input("Enter a string: ")
print(printstr(inputstring))
