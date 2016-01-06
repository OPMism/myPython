#Answer to http://sites.fas.harvard.edu/~qr20/assignments/assign2.html
#Program to print the acronym (based upon case)
def printAcro(x):
        finaltext = ""
        abbrev=[item[:1] for item in x.split()] #Loop the input string & split to words
        for character in abbrev:        #Group only the upper case characters
                if character.isupper():
                        finaltext = finaltext + character       #Prepare the final string
        print finaltext         #Print the prepared string
        
acronym = printAcro(raw_input("Enter an String: "))
