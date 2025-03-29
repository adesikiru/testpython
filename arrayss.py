import math
arr=[]
def mediann(arr, n):
    len = n
    med = 0.0
    if len % 2 ==0:
        med=(arr[(len//2-1)]+arr[(len//2)])/2
    else: med = arr[(len//2)]
    print("median is: ", med)
def binarySearch(arr, n, Item):
    location = 1
    i=0
    j=n-1
    middle=(i+j)//2
    while (i < j):
        if Item < arr[middle]:
            j = middle - 1
        else: 
            i = middle + 1
        middle = (i+j)//2
    if arr[middle] == Item:
        location = middle
        print('{0} is found at {1}'.format(Item, location))
    else:
        print('Item is not found: ')
    
    
    
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
        if arr[j]>arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j+1]=temp
print()
print('sorted')
print(arr)
print()
mediann(arr, n)
print()
Item = input('enter item to be searched: ')
Item = int(Item)
binarySearch(arr,n, Item)