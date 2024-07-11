def maxOnes(arr):
    left = 0
    right = 0
    max_length = 0

    while right < len(arr):
        if arr[right] == 1:
            right += 1
            max_length = max(max_length, right - left-1)
        else:
            if left == right:
                right += 1
            else:
                right += 1
                max_length = max(max_length, right - left - 1)
                left += 1

    return max_length


print(maxOnes([0, 0])); #0
print(maxOnes([1, 0])); #1
print(maxOnes([0, 1])); #1
print(maxOnes([1, 0, 1, 1, 0, 1, 1, 1])) #5
print(maxOnes([1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1])); #5
print(maxOnes([1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1])); #6
print(maxOnes([1, 1, 1, 1, 0, 0])); #4
print(maxOnes([1, 1, 1, 1, 1])); #4