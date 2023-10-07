array = [13, 5, -8, 7, 16, 3, 1, 9, 2]
n = len(array)

for i in range(0, n - 1):
    for j in range(0, n - 1 - i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)