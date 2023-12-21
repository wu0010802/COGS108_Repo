def merge_sort(arr):
    if len(arr) > 1:
        # 找到中間的索引來將陣列分割成兩半
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # 遞迴分割左右兩半直到只剩下單一元素
        merge_sort(left_half)
        merge_sort(right_half)

        # 合併階段
        i = j = k = 0

        # 將兩個有序陣列合併成一個有序陣列
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # 檢查是否還有剩餘的元素
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


# 測試程式碼
unsorted_array = [38, 27, 43, 3]
sorted_array = merge_sort(unsorted_array)
print(sorted_array)
