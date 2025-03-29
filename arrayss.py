import math
arr=[]
def maximum(arr,n):
    maxi  = arr[0]
    for i in range(n):
        if arr[i]>maxi:
            maxi=arr[i]
    return maxi
def minimum(arr,n):
    mini  = arr[0]
    for i in range(n):
        if arr[i]<mini:
            mini=arr[i]
    return mini
n = input("array length: ")
n = int(n)
for i in range(n):
    val = input('enter value: %d ' %i)
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
print('maximum is :', max)
min= minimum(arr,n)
print('minimum is :', min)
for i in range(n):
    for j in range(n - 1):
        if a[j]>a[j+1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j+1]=temp
print()
print('sorted')
print(a)