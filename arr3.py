arr = [2, 3, 5, 7, 8]
index=3
k=2
result = []

step = 1
fin = index+k

if len(arr)-k < index or arr[index] - arr[index-1] < arr[index+1] - arr[index]:
    fin = index-k
    step = -1

for i in range(index, fin, step):
    result.append(arr[i])

print(result)