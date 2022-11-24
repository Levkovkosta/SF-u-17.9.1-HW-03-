def buble_sort (array = []):

    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:

        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

arr = list(map(int, input('Введите числа через пробел: ').split()))

x = int(input('Введите число в рамках последовательности: '))

while x:
    if x <= min(arr) or x >= max(arr):
        print('Некорректное число')
        x = int(input('введите число в рамках последовательности: '))
    else:
        break

arr.append(x)
buble_sort(arr)
print (arr)
find = (binary_search(arr, x, 0, len(arr) - 1))
print(f'Индекс числа меньше введенного - {find-1}, индекс числа больше либо равного введенному - {find}')
