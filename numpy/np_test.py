
import numpy as np

'''

'''
# a = np.array([1, 2, 3])

# b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# # 组数组赋值 下标从0开始
# b[1, 1] = 10
# # .shape 获取数组大小 
# print(a.shape)
# #
# print(b.shape)
# # dtype 获取类型
# print(a.dtype)

# print(b)


'''

'''
# dtype 定义结构类型
# S32:表示字符串32位 i:表示数字  f:表示浮点数

# persontype = np.dtype({
#     'names': ['name', 'age', 'chinese', 'math', 'english'],
#     'formats': ['S32', 'i', 'i', 'i', 'f']})

# peoples = np.array([("ZhangFei", 32, 75, 100, 90), ("GuanYu", 24, 85, 96, 88.5),
#                     ("ZhaoYun", 28, 85, 92, 96.5), ("HuangZhong", 29, 65, 85, 100)],
#                    dtype=persontype)

# 类型	    字符代码
# bool	      ?, b1
# int8	      b, i1
# uint8	      B, u1
# int16	      h, i2
# uint16	    H, u2
# int32	      i, i4
# uint32	    I, u4
# int64	      q, i8
# uint64	    Q, u8
# float16	    f2, e
# float32	    f4, f
# float64	    f8, d
# complex64	  F4, F
# complex128	F8, D
# str	        a, S（可以在S后面添加数字，表示字符串长度，比如S3表示长度为三的字符串，不写则为最大长度）
# unicode	    U
# object	    O
# void	      V

# ages = peoples[:]['age']
# # print(ages, 'ages')
# chineses = peoples[:]['chinese']
# maths = peoples[:]['math']
# englishs = peoples[:]['english']
# # mean 求平均数
# print(np.mean(ages))
# print(np.mean(chineses))
# print(np.mean(maths))
# print(np.mean(englishs))

# arange() 类似内置函数 range()，通过指定初始值、终值、步长来创建等差数列的一维数组，默认是不包括终值的。
# x1 = np.arange(1, 11, 2)
# # linspace 是 linear space 的缩写，代表线性等分向量的含义。linspace() 通过指定初始值、终值、元素个数来创建等差数列的一维数组，默认是包括终值的。
# x2 = np.linspace(1, 9, 5)

# print(x1)
# print(x2)
# # 数组加法
# print(np.add(x1,x2))
# # 数组减法
# print(np.subtract(x1,x2))
# # 乘法
# print(np.multiply(x1,x2))
# # 除法
# print(np.divide(x1,x2))
# # n次方
# print(np.power(x1,x2))
# # 取余
# print(np.remainder(x1,x2))


# a = np.array([[6, 1, 1], [4, 2, 3], [7, 8, 5]])

# print(a)
# # 数组中最小值 1,2,3,4,5,6,7,8,9
# print(np.amin(a))
# # 数组中最大值
# print(np.amax(a))
# # amin(a, 0) 是延着axis=0 轴的最小值, axis=0 把元素看成了【1,4,7】[2,5,8],[3,6,9]的最小值
# # 即[1,4,7]的最小值 【2,5,8]的最小值, [,3,6,9]的最小值(某列中的最小值)
# # amin(a, 0) 表示列
# # amin(a, 1) 表示行
# print(np.amin(a, 0))
# # amin(a, 1) 是延着axis=1 轴的最大值, axis=1 把元素看成了【1,2,3】[4,5,6],[7,8,9]的最大值
# # 即[1,2,3]中的最大值 [4,5,6]的最大值 [7,8,9]的最大值(某行中的最大值)
# # amax(a, 0) 表示列
# # amax(a, 1) 表示行
# print(np.amax(a, 1))

# # print(np.amax(a, 0))
# # print(np.amax(a, 1))


# # 统计最大值与最小值之差 ptp()
# 对于相同的数组 a，np.ptp(a) 可以统计数组中最大值与最小值的差，即 9-1 = 8。
# 同样 ptp(a, 0) 统计的是沿着 axis = 0 轴的最大值与最小值之差，即 7-1 = 6
# （当然 8-2 = 6, 9-3 = 6，第三行减去第一行的 ptp 差均为 6），
# ptp(a, 1) 统计的是沿着 axis = 1 轴的最大值与最小值之差，即 3-1 = 2
# （当然 6-4 = 2, 9-7 = 2，即第三列与第一列的 ptp 差均为 2）。

# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(np.ptp(a))
# print(np.ptp(a, 0))
# print(np.ptp(a, 1))


# # 统计数组的百分位数 percentile()
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(np.percentile(a, 50))
# print(np.percentile(a, 50, axis=0))
# print(np.percentile(a, 50, axis=1))

# # 统计数组中的中位数 median()、平均数 mean()
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# #求中位数
# print np.median(a)
# print np.median(a, axis=0)
# print np.median(a, axis=1)
# #求平均数
# print np.mean(a)
# print np.mean(a, axis=0)
# print np.mean(a, axis=1)

# # 统计数组中的加权平均值 average()
# # average() 函数可以求加权平均，加权平均的意思就是每个元素可以设置个权重，
# # 默认情况下每个元素的权重是相同的，所以 np.average(a) = (1+2+3+4)/4 = 2.5，
# # 你也可以指定权重数组 wts = [1, 2, 3, 4]，
# # 这样加权平均 np.average(a, weights=wts) = (1*1+2*2+3*3+4*4)/(1+2+3+4) = 3.0。
# a = np.array([1, 2, 3, 4])
# wts = np.array([1, 2, 3, 4])
# print(np.average(a))
# print(np.average(a, weights=wts))


# # 统计数组中的标准差 std()、方差 var()
# # 方差的计算是指每个数值与平均值之差的平方求和的平均值，即 mean((x - x.mean()) ** 2)。
# # 标准差是方差的算术平方根。
# # 在数学意义上，代表的是一组数据离平均值的分散程度。
# # 所以 np.var(a) = 1.25, np.std(a) = 1.118033988749895。
# a = np.array([1, 2, 3, 4])
# print(np.std(a))
# print(np.var(a))

# sort(a, axis=-1, kind=‘quicksort’, order=None)，默认情况下使用的是快速排序；
# 在 kind 里，可以指定 quicksort、mergesort、heapsort 分别表示快速排序、合并排序、堆排序。
# 同样 axis 默认是 - 1，即沿着数组的最后一个轴进行排序，也可以取不同的 axis 轴，
# 或者 axis = None 代表采用扁平化的方式作为一个向量进行排序。
# 另外 order 字段，对于结构化的数组可以指定按照某个字段进行排序。
a = np.array([[4, 3, 2], [2, 4, 1]])
print(np.sort(a))
print(np.sort(a, axis=None))
print(np.sort(a, axis=0))
print(np.sort(a, axis=1))

