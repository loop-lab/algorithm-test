def get_sym(arr):
    if len(arr) == 1:
        return True
    if len(arr) == 0:
        return False

    xoy = {}
    left = arr[0][0]
    right = arr[0][0]
    left_y = arr[0][1]
    right_y = arr[0][1]
    for i in range(0, len(arr)):
        if arr[i][1] not in xoy:
            xoy[arr[i][0]] = []
        (xoy[arr[i][1]]).append(arr[i][0])
        if arr[i][0] < left:
            left = arr[i][0]
            left_y = arr[i][1]
        if arr[i][0] > right:
            right = arr[i][0]
            right_y = arr[i][1]

    if left_y != right_y:
        return False

    middle = (left + right) / 2

    for i in range(0, len(xoy)):
        if xoy[i] != []:
            sum_xoy = 0
            count = len(xoy[i])
            sum_xoy = sum(xoy[i])
            if sum_xoy / count != middle:
                return False

    return True

print(get_sym([(0, 0), (5, 0), (3, 0), (1, 1), (4, 1)]))
print(get_sym([(0, 0), (5, 0), (2.5, 0), (1, 1), (4, 1)]))
print(get_sym([(0, 0), (5, 0), (2.5, 0), (1, 1), (5, 1)]))
print(get_sym([(3, 0)]))
print(get_sym([]))