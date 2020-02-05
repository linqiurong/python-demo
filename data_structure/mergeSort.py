'''
    归并操作的工作原理如下：
    第一步：申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
    第二步：设定两个指针，最初位置分别为两个已经排序序列的起始位置
    第三步：比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
    重复步骤3直到某一指针超出序列尾
    将另一序列剩下的所有元素直接复制到合并序列尾
'''

nums = [2,4,1,3,5,6,8,7,10,9]

# .....

def merageAsc(left, right):
    l, r=0, 0
    result=[]
    while l<len(left) and r<len(right):
        # print('aaa')
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    # print(result, 'result')
    result += left[l:]
    result += right[r:]
    return result

def merageDesc(left, right):
    l, r=0, 0
    result=[]
    while l<len(left) and r<len(right):
        if left[l] >= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    # print(result, 'result')
    result += left[l:]
    result += right[r:]
    return result


def mergeSort(nums, order_type='asc'):
    length = len(nums)
    if length == 0:
        print('nums must more than 1')
    elif length == 1:
        return nums
    else:
        # 获取中间元素
        middle_index = int (length / 2)
       
        if order_type == 'asc':
            left = mergeSort(nums[:middle_index]) 
            right = mergeSort(nums[middle_index:])
            # print(left, right)
            return merageAsc(left, right)
        else:
            left = mergeSort(nums[:middle_index], 'desc') 
            right = mergeSort(nums[middle_index:], 'desc')
            return merageDesc(left, right)


if __name__ == "__main__":
    
    result = mergeSort(nums)
    print(result)
    # result = mergeSort(nums, 'desc')
    # print(result)
