# Selection Sort

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i

        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        swap(arr, i, min_idx)

    return arr

if __name__ == "__main__":
    random_arr = [5, 2, 1, 8, 4]  
    selection_sort(random_arr)  
    print(random_arr)

