def sorting(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                
def binary_search(array, element, left, right): 
    if left > right:
        print('Число не входит в интервал значений списка')
        return False
    middle = (right+left) // 2
    if array[middle] < element <= array[middle + 1]: 
        print('Номер позиции элемента, который меньше введенного числа, а следующий за ним больше или равен этому числу:\n', middle+1)
        return middle 
    elif element < array[middle]: 
        return binary_search(array, element, left, middle-1)
    else:
        return binary_search(array, element, middle+1, right)


while True:
    try:
        input_list = list(map(float, input('Введите через пробел список чисел и нажмите Enter \n').split()))
        input_num = float(input('Введите любое число и нажмите Enter \n'))
    except ValueError as e:
        print("Введите цифры, а не буквы!")
    else:
        sorting(input_list)
        print('Отсортированный список:\n', input_list)
        l = 0
        r = len(input_list) - 1
        binary_search(input_list, input_num, l, r)
