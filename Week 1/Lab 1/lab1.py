def linear_search(a, b):
    for i in range(0, len(b)):
        if a == b[i]:
            return i

def linear_search_multi(a, b):
    output = []
    for i in range(0, len(b)):
        if a == b[i]:
            output.append(i)
    return output

# print(linear_search(8, [6, 2, 8, 4]))
# print(linear_search(4, [6, 2, 8, 4]))
# print(linear_search(5, [6, 2, 8, 4]))

# print(linear_search_multi(8, [6, 2, 8, 4, 8, 7]))
# # [2, 4]
# print(linear_search_multi(4, [6, 2, 8, 4, 8, 7]))
# # [3]
# print(linear_search_multi(5, [6, 2, 8, 4, 8, 7]))
# # []


def binary_search(a, b):
    b.sort()
    new_list = b
    
    min_index = 0
    max_index = len(new_list) - 1
    
    while min_index <= max_index:
        middle_index =  (max_index + min_index) // 2
        
        print('middle_index', middle_index)
        
        if (a > new_list[max_index]) or (a < new_list[min_index]):
            return
        
        # print(new_list[middle_index])
        
        if a == new_list[middle_index]:
            return middle_index
        elif a > new_list[middle_index]:
            min_index = middle_index + 1
        elif a < new_list[middle_index]:
            max_index = middle_index
    return

# print(binary_search(4, [2, 4, 6, 8, 98, 99, 100, 101, 102, 103, 104]) == 1)

# print(binary_search(8, [2, 4, 6, 8]) == 3)

# print(binary_search(2, [2, 4, 6, 8]) == 0)

# print(binary_search(1, [2, 4, 6, 8]) == None)

# print(binary_search(99, [2, 4, 6, 8]) == None)
# print(binary_search(4, [2, 4, 6, 8, 98, 99, 100, 101, 102, 103, 104]) == 1)

# print(binary_search(103, [2, 4, 6, 8, 98, 99, 100, 101, 102, 103, 104]) == 9)

def binary_search_multi(a, b):
    b.sort()
    new_list = b
    
    min_index = 0
    max_index = len(new_list) - 1
    
    output = []
    while min_index <= max_index:
        middle_index =  (max_index + min_index) // 2
        
        print('middle_index', middle_index)
        
        if (a > new_list[max_index]) or (a < new_list[min_index]):
            return
        
        print(new_list[middle_index])
        
        if a == new_list[middle_index]:
            output.append(middle_index)
            i = middle_index
            
            while i > min_index:
                i -= 1
                if new_list[i] == new_list[middle_index]:
                    output.append(i)
                else:
                    break
            
            i = middle_index
            while i < max_index:
                i += 1
                if new_list[i] == new_list[middle_index]:
                    output.append(i)
                else:
                    break
            output.sort()
            return output
        
        elif a > new_list[middle_index]:
            min_index = middle_index + 1
        elif a < new_list[middle_index]:
            max_index = middle_index
    return
            
print(binary_search_multi(5, [1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 5]))
# [3, 4, 5]