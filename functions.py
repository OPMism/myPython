def sum_two_numbers(a, b):
    return a + b

num1 = int(raw_input("Enter a number a: "))
num2 = int(raw_input("Enter a number b: "))
print "Value from user input: ", sum_two_numbers(num1, num2)
print "Value from hard-coded input 3 & 5: ", sum_two_numbers(3,5)

# Modify this function to return a list of strings as defined above
def list_benefits():
    benefitlist = ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]
    return benefitlist

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return ("%s is a benefit of functions!" %benefit)

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print build_sentence(benefit)

name_the_benefits_of_functions()
