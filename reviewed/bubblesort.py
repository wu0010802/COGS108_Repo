def bubble_sort(arr):
    n = len(arr)
    # 遍歷所有數組元素
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # 遍歷數組從0到n-i-1
            # 交換如果元素e大於e+1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 測試數據
arr = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(arr)

print("排序後的數組:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")