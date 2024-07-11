
arr = [2, 7, 5, 4, 4, 3]
max_l = 0
max_r = 0
max_length = 0
current_l = 0
current_r = 0
current_length = 0
asc = True

for i in range(1, len(arr)):
    if arr[i] > arr[i-1] and asc:
        current_r += 1
        current_length += 1
    elif arr[i] < arr[i-1] and not asc:
        current_r += 1
        current_length += 1
    else:
        asc = not asc
        if current_length > max_length:
            max_length = current_length
            max_l = current_l
            max_r = current_r
        if arr[i] != arr[i-1]:
            current_length = 1
            current_l = i-1
            current_r = i
        else:
            current_length = 0
            current_l = i
            current_r = i

if current_length > max_length:
    max_length = current_length
    max_l = current_l
    max_r = current_r

print([max_l, max_r])