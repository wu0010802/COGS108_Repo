def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # 選擇中間值作為基準點
        left = [x for x in arr if x < pivot]  # 小於基準點的元素
        middle = [x for x in arr if x == pivot]  # 等於基準點的元素
        right = [x for x in arr if x > pivot]  # 大於基準點的元素
        return quick_sort(left) + middle + quick_sort(right)

# 測試數據
array = [3, 6, 8, 10, 1, 2, 1]
sorted_array = quick_sort(array)
print(sorted_array)