a = 10
b = 12
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)



# Note: we need to make use of the ** operator to evaluate the square root as:

# √ (x)  = x(½)

# 1/2 means  0.5  so x raised to power 0.5
# so .....(a ** 2 + b ** 2) is given power of.. 0.5 



# below is pythagoras program for user input

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** 0.5
print("Hypotenuse length is", hypo)
