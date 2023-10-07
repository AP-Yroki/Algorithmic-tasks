array = [4, 1, 7, 3, 6, 2, 9, 10, 8]
n = len(array)

for i in range(0, n - 1):
    for j in range(0, n - 1 - i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]


print(array[-1])

# Решение 2
# max_num = array[0]
#
# for num in array:
#     if num > max_num:
#         max_num = num
#
# print(max_num)
