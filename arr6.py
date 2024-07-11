# def equal(arr, k):
#     n = len(arr)
#     count = 0
#     left = 0
#     right = 1

#     while right < n:
#         if arr[right] - arr[left] >= k:
#             count += n - right
#             left += 1
#         else:
#             right += 1

#     return count

# print(equal([1, 2, 3, 4, 5], 3))
# print(equal([1, 1, 3, 4], 2))
# print(equal([], 0))
# print(equal([1,1,3,4], 20))
