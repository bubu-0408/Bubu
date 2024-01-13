list = [1, 2, 5, 6, 8, 7, 9, 5, 46, 12, 3]
# list.sort()#python内置排序
# target = 7
# # 顺序查找
# for i in list:
#     if i == target:
#         print(list.index(i))
#
#
# # # # 二分查找前提有序列表
# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         guess = arr[mid]
#         if guess == target:
#             return mid  # 找到目标，返回其索引
#         if guess > target:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None  # 没有找到目标，返回None
#
#
# print(binary_search(list, target))
#
#
# # # 冒泡排序
# def bubble_sort(list):
#     for i in range(len(list) - 1):
#         for j in range(len(list) - i - 1):
#             if list[j] > list[j + 1]:
#                 list[j], list[j + 1] = list[j + 1], list[j]
#     return list
#
#
# print(bubble_sort(list))
#
#
# # # 简单选择排序
# def select_sort_simple(list):
#     new_list = []
#     for i in range(len(list)):
#         min_val = min(list)
#         new_list.append(min_val)
#         list.remove(min_val)
#     return new_list
#
#
# print(select_sort_simple(list))
#

# # 选择排序
# def select_sort(list):
#     for i in range(len(list) - 1):
#         min_loc = i
#         for j in range(i + 1, len(list)):
#             if list[j] < list[min_loc]:
#                 min_loc = j
#         list[i], list[min_loc] = list[min_loc], list[i]
#     return list
#
#
# print(select_sort(list))

# 插入排序
# def insert_sort(list):
#     for i in range(1, len(list)):  # 表示摸到的数下标
#         target = list[i]
#         j = i - 1  # 手里数下标
#         while  target < list[j] and j >= 0:
#             list[j + 1] = list[j]
#             j -= 1
#         list[j+1]= target
#     return list
# list = [1, 2, 5, 6, 8, 7, 9, 5, 46, 12, 3]
# print(insert_sort(list))

# 快速排序
# def partition(list, left, right):
#     """
#     将列表就地围绕基准元素（选择最左边的元素）进行分区。
#
#     参数:
#     - list: 待分区的列表。
#     - left: 待分区子数组的左索引。
#     - right: 待分区子数组的右索引。
#
#     返回:
#     分区完成后基准元素的索引。
#     """
#     tmp = list[left]  # 选择最左边的元素作为基准
#     while left < right:
#         # 从右侧找到比基准小的数
#         while left < right and list[right] >= tmp:#从右边找比tmp小的数
#             right -= 1#往左走一步
#         list[left] = list[right]
#
#         # 从左侧找到比基准大的数
#         while left < right and list[left] <= tmp:
#             left += 1
#         list[right] = list[left]
#     # 将基准元素放置到正确的位置
#     list[left] = tmp
#     return left
#
#
# def quick_sort(list, left, right):
#     """
#     实现快速排序算法，对给定的列表进行原地排序。
#
#     参数:
#     - list: 待排序的列表。
#     - left: 待排序子数组的左索引。
#     - right: 待排序子数组的右索引。
#
#     返回:
#     排序后的列表。
#     """
#     if left < right:
#         # 分区列表并获取基准的索引
#         mid = partition(list, left, right)
#
#         # 递归地对基准左右两侧的子数组进行排序
#         quick_sort(list, left, mid - 1)
#         quick_sort(list, mid + 1, right)
#
#     return list
#
# print(quick_sort(list,0,len(list)-1))

#堆排序
# def sift(list, low, high):
#     """
#     :param list:列表
#     :param low:堆的根节点位置
#     :param high:堆的最后一个元素位置
#     :return:
#     """
#     i = low  # i最开始指向根节点
#     j = 2 * i + 1  # j开始是左孩子
#     tmp = list[low]  # 把堆顶存起来
#     while j <= high:
#         if list[j + 1] > list[j] and j + 1 <= high:
#             j = j + 1  # j指向右孩子
#         if list[j] > tmp:
#             list[i] = list[j]
#             i = j    #往下看一行
#             j = 2 * i + 1
#         else:        #tmp更大，把tap放在i的位置
#             list[i]=tmp #把tmp放在某一级根节点
#             break
#     else:
#         list[i]=tmp #把tmp放在叶子节点
#
# def heap_sort(list):
#     #建堆
#     n=len(list)
#     for i in range(n-2//2,-1,-1):#i表示建堆时调整的部分根节点下标
#         sift(list,i,n-1)
#     for i in range(n-1,-1,-1):
#         #i指向当前最后一元素
#         list[0],list[i]=list[i],list[0]#交换堆顶和当前最后一个
#         sift(list,0,i-1)#i-1是新的high
#     return list
# print(heap_sort(list))

#堆排序内置对象
# import heapq
# heapq.heapify(list)
# for i in range(len(list)):
#     print(heapq.heappop(list),end=" ")
