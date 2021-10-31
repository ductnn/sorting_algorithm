# Merge Sort

def merge_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr

    mid = n // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    left_idx = right_idx = 0
    left_length = len(left)
    right_length = len(right)

    for _ in range(left_length + right_length):

        if left_idx < left_length and right_idx < right_length:

            if left[left_idx] <= right[right_idx]:
                sorted_arr.append(left[left_idx])
                left_idx += 1
            else:
                sorted_arr.append(right[right_idx])
                right_idx += 1

        elif left_idx == left_length:
            sorted_arr.append(right[right_idx])
            right_idx += 1

        elif right_idx == right_length:
            sorted_arr.append(left[left_idx])
            left_idx += 1

    return sorted_arr

random_arr = [5, 2, 1, 8, 4]  
random_arr = merge_sort(random_arr)  
print(random_arr)

