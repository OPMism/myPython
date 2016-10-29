def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

var1 = make_multiplier_of(10)
print var1(4)
