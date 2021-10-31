# Quick Sort

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def partition(arr, low, high):
    mid = (low + high) // 2
    piv = arr[mid]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < piv:
            i += 1

        j -= 1
        while arr[j] > piv:
            j -= 1

        if i >= j:
            return j

        swap(arr, i, j)

def quick_sort(arr):

    def _quick_sort(items, low, high):
        if low < high:
            split_idx = partition(items, low, high)
            _quick_sort(items, low, split_idx)
            _quick_sort(items, split_idx + 1, high)

    _quick_sort(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    random_arr = [5, 2, 1, 8, 4, 9, 100, 2]
    quick_sort(random_arr)  
    print(random_arr)

