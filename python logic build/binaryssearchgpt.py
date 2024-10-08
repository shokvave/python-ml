def binary_search(lst, element):
    middle = 0 
    start = 0
    end = len(lst) - 1
    steps = 0 

    while start <= end:
        print("steps", steps, ":", str(lst[start:end+1]))

        steps += 1
        middle = (start + end) // 2

        if element == lst[middle]:
            return middle
        if element < lst[middle]:
            end = middle - 1
        else:
            start = middle + 1 
    return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 9

binary_search(my_list, target)
