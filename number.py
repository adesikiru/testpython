def add(a,b,c):
    z = a + b + c
    print("number one {0} number two {1} number three {2} addition {3}".format(a,b,c,z));
num1 = input("enter number one: ");
num1 = int(num1);
num2 = input("enter number two: ");
num2 = int(num2);
num3 = input("enter number three: ");
num3 = int(num3);
print("number one {0} number two {1} number three {2}".format(num1, num2, num3));
add(num1, num2, num3);