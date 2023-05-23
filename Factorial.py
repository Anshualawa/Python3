def Factorial(x):
    if x<=0:
        return 1
    else:
        return (x * Factorial(x-1))

# Calling Function 

x = 5
print(Factorial(x))

# another way

def factorial2(x):
    y=1
    for i in range(1,x+1):
        y *=i
    return y

print(factorial2(5))