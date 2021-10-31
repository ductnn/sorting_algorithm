import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim


# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    is_swapped = True

    while is_swapped:
        is_swapped = False

        for i in range(n-1):
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)
                is_swapped = True
    
            yield arr


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

        yield arr


# Quick Sort
def quick_sort(arr, low, high):
    if low >= high:
        return

    piv = arr[high]
    piv_idx = low

    for i in range(low, high):
        if(arr[i] < piv):
            swap(arr, i, piv_idx)
            piv_idx += 1
        yield arr

    swap(arr, high, piv_idx)

    yield arr
    yield from quick_sort(arr, low, piv_idx - 1)
    yield from quick_sort(arr, piv_idx + 1, high)


# Selection Sort
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i

        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        swap(arr, i, min_idx)
        yield arr


# Merge Sort
def merge_sort(arr, low, high):
    if (high <= low) :
        return

    elif (low < high):
        mid = (low + high) // 2

        yield from merge_sort(arr, low, mid)
        yield from merge_sort(arr, mid + 1, high)
        yield from merge(arr, low, mid, high)
        yield arr


def merge(arr, low, mid, high):
    sorted_arr = []
    i = low
    j = mid+1

    while (i <= mid and j <= high):
        if (arr[i] < arr[j]):
            sorted_arr.append(arr[i])
            i += 1
        else:
            sorted_arr.append(arr[j])
            j += 1

    if (i > mid):
        while (j <= high):
            sorted_arr.append(arr[j])
            j += 1
    else:
        while(i <= mid):
            sorted_arr.append(arr[i])
            i += 1

    for i, val in enumerate(sorted_arr):
        arr[low + i] = val
        yield arr


# Swap
def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

#===================== Visualize =====================

n = int(input("Enter the number of elements:"))
print(
    "\n 1. Bubble"
    "\n 2. Insertion"
    "\n 3. Quick"
    "\n 4. Selection"
    "\n 5. Merge Sort"
    "\n"
)

al = int(input("Choose algorithm: "))
array = [i + 1 for i in range(n)]
random.shuffle(array)

if (al == 1):
    title = "Bubble Sort"
    algo = bubble_sort(array)

elif (al == 2):
    title = "Insertion Sort"
    algo = insertion_sort(array)

elif (al == 3):
    title = "Quick Sort"
    algo = quick_sort(array, 0, n-1)

elif (al == 4):
    title = "Selection Sort"
    algo = selection_sort(array)

elif (al == 5):
    title = "Merge Sort"
    algo = merge_sort(array, 0, n-1)

else:
    print("Please enter a number from f**king list")

# Initialize fig
fig, ax = plt.subplots(figsize=(16, 8))
ax.set_title(title)

bar_rec = ax.bar(range(len(array)), array, align='edge')

ax.set_xlim(0, n)
ax.set_ylim(0, n * 1.1)

text = ax.text(0.02, 0.95, "", transform = ax.transAxes)

counter = [0]


def update_plot(array, rec, counter):
    for rec, val in zip(rec, array):
        rec.set_height(val)
        rec.set_color("#07eb0b")
    
    rec.set_color("#e80027")

    counter[0] += 1
    text.set_text("No.of operations :{}".format(counter[0]))


anima = anim.FuncAnimation(
    fig,
    func=update_plot,
    fargs=(bar_rec, counter),
    frames=algo,
    interval=1000./60,
    repeat=False
)

plt.show()
