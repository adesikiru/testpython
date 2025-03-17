def hcf1(a,b):
    x = a
    y = b
    while y != 0 :
        z = x % y
        x=y
        y=z
    return x
def hcf(a,b,c):
    h1=  hcf1 (a,b)
    h2 = hcf1(h1, c)
    print("the HCF is", h2)

def lcm1(a,b):
    # LCM = (a*b)/HCF(a,b)
    return (a * b) // hcf1(a,b)

def lcm(a,b,c):
    # Find LCM of first two numbers
    l1 = lcm1(a,b)
    # Find LCM of the result and the third number
    l2 = lcm1(l1, c)
    print("the LCM is", l2)
    return l2

num1 = input("enter number one: ")
num1 = int(num1)
num2 = input("enter number two: ")
num2 = int(num2)
num3 = input("enter number three: ")
num3 = int(num3)

# Call both HCF and LCM functions to show their results
hcf(num1, num2, num3)
lcm(num1, num2, num3)