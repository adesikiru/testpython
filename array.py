arr=[]
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
print("addition ", suma)