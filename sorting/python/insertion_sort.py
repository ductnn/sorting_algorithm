# Insertion Sort

def insertion_sort(arr):
    n = len(arr)

    for i in range(n):
        item_insert = arr[i]
        pos = i

        while pos > 0 and arr[pos-1] > item_insert:
            arr[pos] = arr[pos-1]
            pos -= 1

        arr[pos] = item_insert

    return arr

if __name__ == "__main__":
    random_arr = [5, 2, 1, 8, 4]
    insertion_sort(random_arr)  
    print(random_arr)

