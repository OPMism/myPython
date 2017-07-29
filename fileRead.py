from sys import argv
script, filename = argv
txt = open(filename)
print "Reading text file"
print txt
print txt.read()
print "." * 10
print "Truncate text file"
txt = raw_input("Enter file name")
text = open(txt, 'w')
text.truncate()
print "." * 10
print "Writing to text file"
txt = raw_input("Enter file name")
text = open(txt, 'a')
text.write("New line")
print "." * 10
print "Reading one line from text file"
text = open(txt)
print text.readline()
