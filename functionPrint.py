from os.path import exists

def sum(a, b):
    print int(a) + int(b)

def print_a_line(line_number, f):
    print line_number, f.readline()

# a = raw_input("enter a number: ")
# b = raw_input("enter a number: ")
# sum(a,b)

filename = raw_input("Enter file name: ")
if(exists(filename)):
    f = open(filename)
else:
    print "File doesn't exist"
    exit(0)

line = raw_input("Enter line number to seek: ")

f.seek(int(line))
print f.readline()

print len(f.read())

f.seek(0)

for i in range(4):
    print_a_line(i, f)
    i = i + 1

f.close()
