import math
arr=[]
def maximum(arr,n):
    maxi  = a[0]
    for i in range(n):
        if a[i]>maxi:
            maxi=a[i]
    return maxi
n = input("array length: ")
n = int(n)
for i in range(n):
    val = input('enter value: %d' %i)
    val = int(val)
    arr.append(val)
print(arr)
suma = 0
for i in range(n):
    suma = suma + arr[i]
    print(suma, end= ',')
print()
ave = suma/n
var = 0
for i in range(n):
    var = var +((arr[i]-ave)*(arr[i]-ave))
print('variation is ' , var)
sd = math.sqrt(var)
print('standard deviation', sd)
sd = '{0:.03f}'.format(sd)
ave = '{0:.02f}'.format(ave)
print("average in 2 decimal places is ", ave)
print("standard deviation in 3 decimal places is ", sd)
print("addition ", suma)
max= maximum(arr,n)
print('maximum is :', maxi)