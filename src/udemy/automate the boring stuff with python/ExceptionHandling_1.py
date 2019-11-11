def dividBy(quotient, dividend):
    try:
        return quotient / dividend
    except ZeroDivisionError:
        print("Error you have tried to divide by Zero!!!!")
        return "infinite"





print(dividBy(42, 2))
print(dividBy(42, 1))
print(dividBy(42, 0))
print(dividBy(42, 4))