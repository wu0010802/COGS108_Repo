def topKFrequent(nums,k):
    nums_dict = {}
    nums_tuple = set()
    nums_list = []
    result_list = []
    
    result = []
    

    for num in nums:
        nums_tuple.add(num)
    for num in nums:
        if not num in nums_list:
            nums_list.append(num)
    for i in range(len(nums)):
        if nums[i] != nums[i-1]:
            num_count = 0
        if nums[i] in nums_tuple:
            
            num_count += 1
        nums_dict[nums[i]] = num_count
    
    for i in nums_dict:
        result_list.append(nums_dict[i])

    temp = result_list.copy()
    # return result_list
    
    for _ in range(k):
        max_value = max(temp)  # 找到當前最大值
        max_index = result_list.index(max_value)  # 找到該最大值在原始列表中的索引
        result.append(nums_list[max_index])
        
        temp.remove(max_value)

    return result

nums = [1,3]
k = 2

print(topKFrequent(nums,k))