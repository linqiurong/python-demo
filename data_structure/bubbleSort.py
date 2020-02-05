'''
    冒泡排序 它重复地走访过要排序的元素列，依次比较两个相邻的元素，如果顺序（如从大到小、首字母从从Z到A）
    错误就把他们交换过来。走访元素的工作是重复地进行直到没有相邻元素需要交换，也就是说该元素列已经排序完成。
'''

nums = [2,4,1,3,5,6,8,7,10,9]

def bubbleSortByDesc(nums):
    '''
        从大到小排序 
    '''
    length = len(nums)
    if length == 0:
       print('nums must more than 1')
    elif length == 1:
        return nums
    else:
        for i in range(0, length ):
            for j in range(i, length ): 
                if nums[i] > nums[j]:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
            print('第{0}次执行结果{1}'.format(i,nums))
        return nums


def bubbleSortByAsc(nums):
    '''
        从小到大排序 
    '''
    length = len(nums)
    if length == 0:
       print('nums must more than 1')
    elif length == 1:
        return nums
    else:
        for i in range(0, length ):
            for j in range(i, length ): 
                if nums[i] < nums[j]:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
            print('第{0}次执行结果{1}'.format(i,nums))
        return nums

if __name__ == "__main__":

    result = bubbleSortByDesc(nums)
    print(result)
    result = bubbleSortByAsc(nums)
    print(result)
        