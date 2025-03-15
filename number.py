def add(a,b,c):
    z = a + b + c
    print("number one {0} number two {1} number three {2} addition {3}".format(a,b,c,z));
def mult(a,b,c):
    z = a * b * c
    print("number one {0} number two {1} number three {2} multiplication {3}".format(a,b,c,z));
def hcf(a,b,c):
    hcf1 (a,b);
def largest(a,b,c):
    if a > b: 
        large = a
    else:
        large = b
    if c > large:
        largest = c
    else:
        largest = large
    print("the largest number is:", largest);
def smallest(a,b,c):
    if a < b: 
        small = a
    else:
        small = b
    if c < small:
        smallest = c
    else:
        smallest = small
    print("the smallest number is:", smallest);
num1 = input("enter number one: ");
num1 = int(num1);
num2 = input("enter number two: ");
num2 = int(num2);
num3 = input("enter number three: ");
num3 = int(num3);
print("number one {0} number two {1} number three {2}".format(num1, num2, num3));
add(num1, num2, num3);
mult(num1, num2, num3);
largest(num1, num2, num3);
smallest(num1, num2, num3);
hcf(num1, num2, num3);