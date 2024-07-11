ints = []

def dep(arr):
    if len(arr) == 0:
        return ""

    arr.sort()
    result = []
    left = arr[0] # 8
    right_prev = arr[0] # 8
    right = 0 # 11
    i = 1

    while i < len(arr):
        right = arr[i]
        if right - right_prev != 1:
            if left == right_prev:
                result.append(str(left))
            else:
                result.append(str(left) + "-" + str(right_prev))
            left = right
        right_prev = right
        i += 1

    if left == right_prev:
        result.append(str(left))
    else:
        result.append(str(left) + "-" + str(right_prev))

    return ','.join(result)

print(dep([4, 1, 7, 11, 2, 8, 3]))
print(dep(ints))
print(dep(ints))
print(dep(ints))
print(dep(ints))