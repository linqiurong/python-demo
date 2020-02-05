''' 2020 02 03 '''
'''
    # 给定一个整数数组 nums 和一个目标值 target 请你在该数组中找出和为目标值的那两个数
    # 并返回他们的数组下标
    # 例 nums = [2, 7, 11, 15] , target = 9
'''

nums = [2, 7, 11, 15]
target = 13

def getIndexClose(nums, target) :
    # 获取数组长度
    length = len(nums)
    # 数组必须大于2位
    if length < 2 :
        print('nums must more than 2 numbers')
        return
    # 临时变量 获取当前位置
    tmp_index = 0
    while tmp_index < length - 1 :
        # 如果前一个数与后一个数相加等于目标值 则返回当前的位置信息
        if nums[tmp_index] + nums[tmp_index+1] == target :
            return [tmp_index, tmp_index+1 ]
        tmp_index += 1


def getIndexNotClose(nums, target) : 
    # 获取长度
    length = len(nums)
    if length < 2 :
        print('nums must more than 2 numbers')
        return
    # tmp_index = 0
    for i in range(0, length) :
        for j in range(1, length) :
            if nums[i] + nums[j] == target : 
                return [ i, j ]
    
    print('end')
    

if __name__ == "__main__":
    
    result = getIndexClose(nums, target)
    label = ''

    if result == None :
        label = u'未找到结果'
    else :
        label = u'找到结果'

    print(label, result)

    label = ''
    result = getIndexNotClose(nums, target)
    if result == None :
        label = u'未找到结果'
    else :
        label = u'找到结果'
    print(label, result)



