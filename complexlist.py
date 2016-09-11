#noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
#print noprimes

#sentence = "This is a private party"
#print sentence[::-1]
#words = sentence.split()
#reversed = [word[::-1] for word in words]
#print reversed

#def prime(num):
#    if num > 1:
#        for i in range(2,num):
#            if (num % i) == 0:
#                print(num,"is not a prime number")
#                print(i,"times",num//i,"is",num)
#            else:
#                print(num,"is a prime number")
#    else:
#       print(num,"is not a prime number")
#
#number = int(raw_input("Enter a number: "))
#prime(number)

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
