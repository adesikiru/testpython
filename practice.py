def lcm1(a,b):
    x=a
    y=b
    while y != 0:
        

def lcm(a,b,c):
    l1=lcm1(a,b)
    l2=lcm1(l1,c)
    print("the LCM is", l2);
num1 = input("enter number one: ");
num1 = int(num1);
num2 = input("enter number two: ");
num2 = int(num2);
num3 = input("enter number three: ");
num3 = int(num3);
print("number one {0} number two {1} number three {2}".format(num1, num2, num3));

lcm(num1,num2,num3);