'''
    插入排序:每步将一个待排序的记录，按其关键码值的大小插入前面已经排序的文件中适当位置上，直到全部插入完为止。
'''

nums = [2,4,1,3,5,6,8,7,10,9]

# nums = [ 2, 4, 1, 3, 5, 6, 8, 7, 10, 9 ]
# nums = [ 1, 2, 4, 3, 5, 6, 8, 7, 10, 9 ]
# nums = [ 1, 2, 3, 4, 5, 6, 8, 7, 10, 9 ]
# nums = [ 1, 2, 3, 4, 5, 6, 8, 7, 10, 9 ]
# .....

def insertionSortByDesc(nums):
    length = len(nums)
    if length == 0:
        print('nums must more than 1')
    elif length == 1:
        return nums
    else:
        for i in range(0, length ):
            for j in range(0, i):
                if(nums[j] < nums[i]) :
                    nums[i],nums[j]=nums[j],nums[i]
            print('第{0}次执行结果{1}'.format(i,nums))
        return nums


def insertionSortByAsc(nums):
    length = len(nums)
    if length == 0:
        print('nums must more than 1')
    elif length == 1:
        return nums
    else:
        for i in range(0, length ):
            for j in range(0, i):
                if(nums[j] > nums[i]) :
                    nums[j],nums[i]=nums[i],nums[j]
            print('第{0}次执行结果{1}'.format(i,nums))
        return nums

if __name__ == "__main__":
    
    result = insertionSortByDesc(nums)
    print(result)
    # result = insertionSortByAsc(nums)
    # print(result)
