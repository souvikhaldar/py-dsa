def insertion_sort(unsorted_list):
    for i in range(1,len(unsorted_list)):
        j = i - 1
        value = unsorted_list[i]
        while unsorted_list[j]> value and j>=0:
            unsorted_list[j+1] = unsorted_list[j]
            j -= 1
        unsorted_list[j+1] = value
    return unsorted_list

# python3 insertion_sort.py
# [1, 2, 3, 3, 5, 6, 9, 12, 32, 43, 66, 98]