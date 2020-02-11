
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# # Series(支持数组与字典) 一维空间
# x1 = Series([1, 2, 3, 4])
# x2 = Series(data=[1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# print(x1)
# print(x2)


# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# x3 = Series(d)
# print(x3)

# data = {'Chinese': [66, 95, 93, 90, 80], 'English': [
#     65, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
# df1 = DataFrame(data)
# df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun',
#                              'HuangZhong', 'DianWei'])
# df3 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun',
#                              'HuangZhong', 'DianWei'], columns=['English', 'Math', 'Chinese'])
# print(df1)
# print(df2)
# print(df3)



# 读 存 Excel 
# score = DataFrame(pd.read_excel('data.xlsx'))
# score.to_excel('data1.xlsx')
# print(score)


# data = {'Chinese': [ '$66', '$66' ,  '95' ,  '$93' ,   '90'  , '80'  ], 'English': [
#     65, 65, 85, 92, 88, 90], 'Math': [30, 30, 98, 96, 77, 90]}
# df2 = DataFrame(data, index=['ZhangFei','ZhangFei', 'GuanYu', 'ZhaoYun',
#                              'HuangZhong', 'DianWei'], columns=['English', 'Math', 'Chinese'])
# # drop 删除
# # df2 = df2.drop(columns="Chinese")
# # print(df2)
# # df2 = df2.drop(index="ZhangFei")
# # print(df2)

# # 重命名列名 columns
# df2.rename(columns={'Chinese': 'YuWen', 'English': 'Yingyu'}, inplace=True)
# # 去除重复行
# df2 = df2.drop_duplicates()  
# # print(df2)

# # 更改数据格式
# # 不能用chinese 因上面有更新Key值
# df2['YuWen'].astype('str')
# # df2['YuWen'].astype(np.int64)
# # print(df2['YuWen'].astype('str'))

# # print(type(df2['YuWen']))


# # # 删除左右两边空格
# # df2['YuWen'] = df2['YuWen'].astype('str').map(str.strip)
# # print(df2)
# # # 删除左边空格
# # df2['YuWen'] = df2['YuWen'].astype('str').map(str.lstrip)
# # # 删除右边空格
# # df2['YuWen'] = df2['YuWen'].astype('str').map(str.rstrip)

# # 去某个字符
# df2['YuWen'] = df2['YuWen'].str.strip('$')

# # print(cldf2)


# # 全部大写
# df2.columns = df2.columns.str.upper()
# # df2.index = df2.index.str.upper()
# print(df2)
# # 全部小写
# df2.columns = df2.columns.str.lower()
# print(df2)
# # 首字母大写
# df2.columns = df2.columns.str.title()

# print(df2)


# 查找空值

# data = {'Chinese': [ '66', '$66' ,  '95' ,  '$93' ,   '90'  , '80'  ], 'English': [
#     65, 65, 85, 92, 88, 90], 'Math': [ 30, 30, None, 96, 77, 90], 'Name': ['test1', 'test1', 'test3', 'test4', 'test5', 'test6'], }
# df2 = DataFrame(data, index=['ZhangFei','ZhangFei', 'GuanYu', 'ZhaoYun',
#                              'HuangZhong', 'DianWei'], columns=['English', 'Math', 'Chinese', 'Name'])

# df2['Chinese'] = df2['Chinese'].str.strip('$')
# df2['Chinese'] = df2['Chinese'].astype(np.int64)

# df2 = df2.drop_duplicates()

# print(df2)

# # isnull() 函数进行查找None的数据
# print(df2.isnull())
# # .isnull().any() 哪列存在空值
# print(df2.isnull().any())

# # Name 列的数值都进行大写转化
# df2['Name'] = df2['Name'].apply(str.upper)
# # print(df2)

# # print(df2['Chinese'])

# def double_df(x): return 2*x

# # 语文成绩是原来的两倍
# df2['New_Chinese'] = df2['Chinese'].apply(double_df)

# # print(df2)


# def plus(df, n, m): 
#   df['new1'] = (df[u'Chinese']+df[u'English']) * m
#   df['new2'] = (df[u'Chinese']+df[u'English']) * n
#   return df

# df2 = df2.apply(plus, axis=1, args=(2, 3,))
# 不计算None的值
# print(df2.count())
# min() 某列 最小值  max() 某列 最大值
# print(df2.min())
# print(df2.max())
# sum() 某列之和
# print(df2.sum())


# describe() 统计 count, mean, std, min , 25% ,50% 75% max
# df1 = DataFrame(
#     {'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})
# print(df1.describe())


# df1 = DataFrame(
#     {'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})
# df2 = DataFrame(
#     {'name': ['ZhangFei', 'GuanYu', 'A', 'B', 'C'], 'data2': range(5)})
# # 基于指定列进行连接
# df3 = pd.merge(df1, df2, on='name')

# print(df3)
# # inner 内连接 inner 内链接是 merge 合并的默认情况，inner 内连接其实也就是键的交集
# df4 = pd.merge(df1, df2, how='inner')
# print(df4)

# # left 内连接 左连接是以第一个 DataFrame 为主进行的连接，第二个 DataFrame 作为补充
# df5 = pd.merge(df1, df2, how='left')
# print(df5)

# # right 内连接 右连接是以第二个 DataFrame 为主进行的连接，第一个 DataFrame 作为补充
# df6 = pd.merge(df1, df2, how='right')
# print(df6)
# # outer 外连接 外连接相当于求两个 DataFrame 的并集
# df7 = pd.merge(df1, df2, how='outer')
# print(df7)


# 练习

data = {
  '语文':[66, 95,95, 90,80,80],
  '英文': [65,85,93,88, 90,90],
  '数学': [None, 98,96,77,90,90]
}


df = DataFrame(data, index=['张飞','关羽','赵云','黄忠','典韦','典韦'])

def sum(df):
  df['总和'] = df['语文'] + df['英文'] + df['数学']
  # df['平均分'] = df.av
  return df

# 去除重复项
df = df.drop_duplicates()
# 替换na为0 或用 平均值补全
# df = df.fillna(0) 
df['数学'].fillna(df['数学'].mean(), inplace = True)

# print(df)
# 添加一列总和
df = df.apply(sum(df), axis=1)

df['总和'] = df.sum(axis=1)
print(df)
# # 排序
# print(df.sort_values(by='总和'))
# print(df.sort_values(by='总和', ascending=[False]))
# print(df.mean())
# print(df.describe())
print(df.isnull().min())



