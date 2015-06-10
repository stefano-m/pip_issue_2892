def adder(y):
    def addsome(x):
        return x +y
    return addsome

add1 = adder(1)
add2 = adder(2)
