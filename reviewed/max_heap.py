import heapq

# 初始化一個空的Min Heap
min_heap = []

# 想要實現的Max Heap中的元素
max_heap_elements = [100, 90, 80, 50, 60, 70, 20, 30, 40]

# 將Max Heap的元素取負後加入Min Heap
for element in max_heap_elements:
    heapq.heappush(min_heap, -element)

# 現在Min Heap中存的是Max Heap元素的負值
# 取出時再取負，即可得到Max Heap的行為
while min_heap:
    max_element = -heapq.heappop(min_heap)
    print(max_element, end=' ')