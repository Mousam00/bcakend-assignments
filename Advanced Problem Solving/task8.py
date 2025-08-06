
def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # base case

    mid=len(arr)//2
    left_arr=arr[:mid]
    right_arr=arr[mid:]

    left_half=merge_sort(left_arr)
    right_half=merge_sort(right_arr)

    return merge(left_half,right_half)

def merge(left,right):
    result=[]
    i=j=0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

unsorted_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(unsorted_list)
print("Sorted list:", sorted_list)



# Time Complexity: O(n log n) in all cases (best, average, worst)

# Space Complexity: O(n) due to extra space used for merging