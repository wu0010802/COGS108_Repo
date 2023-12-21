def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # 看看左子樹的根是否存在且是否比目前的最大值大
    if l < n and arr[largest] < arr[l]:
        largest = l

    # 同上，改為右子樹
    if r < n and arr[largest] < arr[r]:
        largest = r

    # 如果最大值不是目前的根
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交換

        # 遞迴地繼續構建堆
        heapify(arr, n, largest)

# 主要的函數來進行heap sort
def heapSort(arr):
    n = len(arr)

    # 建立一個maxheap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # 一個個從堆中取出元素
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # 交換
        heapify(arr, i, 0)

# 測試代碼
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print ("排序後的陣列是：")
for i in range(n):
    print ("%d" %arr[i], end=' ')