#!/usr/bin/python

# Demonstration of list functionality & string splicing

var1 = 'Hello World!';
var2 = "Python Practise";
list1 = [var1, var2, 2010, 2014];
list2 = [1, 2, 3, 4, 5, 6, 7 ];

print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]
print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]
print "Value available : "
print list1[0:2];

list1[2] = 2020;
list1[1]="Testing";

print "New value available : "
print list1[0:2];
