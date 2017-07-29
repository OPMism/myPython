# from itertools import combinations
#
# s , n  = raw_input().split()
#
# for i in range(1, int(n)+1):
#     for j in combinations(sorted(s), i):
#         print ''.join(j)
#

def func1():
    print "inside function 1"

def func2(arg1, arg2):
    print arg1 + arg2

func1()
func2(10,20)
