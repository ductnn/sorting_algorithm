# Bubble Sort

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def bubble_sort(arr):
    n = len(arr)
    is_swapped = True

    while is_swapped:
        is_swapped = False

        for i in range(n-1):
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)
                is_swapped = True
    
    return arr

if __name__ == "__main__":
    random_arr = [5, 2, 1, 8, 4]  
    bubble_sort(random_arr)  
    print(random_arr)

