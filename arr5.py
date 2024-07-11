arr1 = [[1,2], [5,1], [11,5], [15,7], [17,5], [18,7], [19,5]]
arr2 = [[2,4], [3,6], [8,5], [9,7], [13, 6]]

def sum_cpu(arr1, arr2):
    i1 = 0
    i2 = 0
    result = []

    while i1 < len(arr1) and i2 < len(arr2):
        if arr1[i1][0] <= arr2[i2][0]:
            result.append(arr1[i1])
            i1 += 1
        else:
            result.append(arr2[i2])
            i2 += 1

    if i1 < len(arr1):
        result += arr1[i1:]
    else:
        result += arr2[i2:]
    return result


print(sum_cpu(arr1, arr2))