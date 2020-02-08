'''
    快速排序: 
      通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
      然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列
'''

nums = [2, 4, 1, 3, 5, 6, 8, 7, 10, 9]

# nums = [ 2, 4, 1, 3, 5, 6, 8, 7, 10, 9 ]
# nums = [ 2, 1, 4, 3, 5, 6, 8, 7, 10, 9 ]
# nums = [ 2, 1, 3, 4, 5, 6, 8, 7, 10, 9 ]
# nums = [ 1, 2, 3, 4, 5, 6, 8, 7, 10, 9 ]
# nums = [ 1, 2, 3, 4, 5, 6, 8, 7, 10, 9 ]
# .....


def quickSortByDesc(array):
  if len(array) < 2:
    return array  # 基线条件:空或只包含一个元素的数组是“有序”的
  else:
    pivot = array[0] # 递归条件
    # 由所有小于基准值的元素组成的子数组
    less = [i for i in array[1:] if i <= pivot]
    # 由所有大于基准值的元素组成的子数组
    greater = [i for i in array[1:] if i > pivot]

    print(greater, less)
  return quickSortByDesc(less) + [pivot] + quickSortByDesc(greater)
  # index, pos = 0, 0
  # count = 0
  # while index < len(nums): 
  #   count += 1
  #   if nums[index] < nums[pos] :
  #     pos += 1
  #     nums[index], nums[pos] = nums[pos], nums[index]
  #     quickSortByDesc(nums)
  #   else: 
  #     index += 1

    
  #   print(nums, 'nums')
  
  # print(count, 'count')
  # return nums


def insertionSortByAsc(nums):
  pass


if __name__ == "__main__":

    result = quickSortByDesc(nums)
    print(result)
    # result = insertionSortByAsc(nums)
    # print(result)
