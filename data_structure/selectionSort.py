'''
    选择排序法是一种不稳定的排序算法。它的工作原理是每一次从待排序的数据元素中选出最小（或最大）的一个元素，
    存放在序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    以此类推，直到全部待排序的数据元素排完。
'''

nums = [2,4,1,3,5,6,8,7,10,9]

def selectionSortByDesc(nums):
    length = len(nums)
    if length == 0:
        print('nums must more than 1')
    elif length == 1:
        return nums
    else:
        for i in range(length-1):
            min_index = i
            for j in range(i+1,length):
                if nums[min_index] < nums[j]:
                    min_index=j
            if i != min_index :
                nums[i],nums[min_index]=nums[min_index],nums[i]
            print('第{0}次执行结果{1}'.format(i,nums))
        return nums


def selectionSortByAsc(nums):
    length = len(nums)
    if length == 0:
        print('nums must more than 1')
    elif length == 1:
        return nums
    else:
        for i in range(length-1):
            min_index = i
            for j in range(i+1,length):
                if nums[min_index] > nums[j]:
                    min_index=j
            if i != min_index :
                nums[i],nums[min_index]=nums[min_index],nums[i]
            print('第{0}次执行结果{1}'.format(i,nums))
        return nums


if __name__ == "__main__":
    
    result = selectionSortByDesc(nums)
    print(result)
    result = selectionSortByAsc(nums)
    print(result)
