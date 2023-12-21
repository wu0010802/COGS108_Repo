def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid  # 找到目標值，返回其索引
        elif mid_val < target:
            left = mid + 1  # 目標值在右半部分，移動左邊界
        else:
            right = mid - 1  # 目標值在左半部分，移動右邊界

    return -1  # 如果未找到目標值，返回 -1


# 測試數列和目標值
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 15

# 執行二分搜尋
result = binary_search(arr, target)

if result != -1:
    print(f"元素在索引 {result} 處找到")
else:
    print("數列中未找到該元素")
