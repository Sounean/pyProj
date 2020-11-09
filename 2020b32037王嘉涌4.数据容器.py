#!/usr/bin/env python
# coding: utf-8

# # 第四部分 数据容器类型
# ## 1.列表
# - 列表（list）是一个有序的序列结构，序列中的元素可以是不同的数据类型
# - 将列表中的各元素用逗号分隔开，并用中括号将所有元素包裹起来
# - 序列中的每个元素都分配一个索引，第一个索引是0，第二个索引是1，依此类推。
# - 负数索引表示从右边往左数，最右边的元素的索引为-1，倒数第二个元素为-2.
# - 列表可以根据需要增长或缩短（长度可变），并且可以包含任何类型的对象，并支持任意的嵌套。
# - 列表可以进行一系列序列操作，如索引、切片、加、乘和检查成员等
# 

# In[10]:


list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]
list4=[]


# - 列表切片
#   - 切片操作需要提供起始索引位置和最后索引位置，然后用冒号 : 将两者分开  
#     $$ 列表名称[起始位置：终止位置：步长] $$
#   - 如果未输入步长，则默认步长为 1
#   - 切片操作返回一系列从起始位置开始到最后位置结束的数据元素
#   - 需要注意的是，起始位置的值包含在返回结果中，而最后索引位置的值不包含在返回结果中
# 

# In[11]:


list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print(list1[0])
print(list2[1:5])
print(list2[-5:-2])
print(list2[:-2])
print(list2[:])
print(list2[::-1])
print(list2[:-1])
print(list2[-1:-5:-2])
print(list1[0][1])


# - 列表操作
#   - 列表的长度: len(list)
#   - 合并列表: list1+list2
#   - 重复列表: list1*3
#   - 添加: list1.append(obj),list1.insert(index,obj)
#   - 删除 : list1.remove(obj),list1.pop(index)
#   - 查找位置: list1.index(obj)
#   - 统计元素的次数：list1.count(obj)
#   - 反转：list1.reverse()
#   - 清空：list1.clear()
#   - 排序：list1.sort()
#   - 拼接两个列表：list1.extend(list2)
#   - 列表的最大值: max(list)
#   - 列表的最小值: min(list)
#   - 转换为列表: list(other)
# 

# In[12]:


list1 = ["I", "am", "a", "Pupil", ".","am"]
list2=['physic','chemistry',1997,2000]
list3=[1,2,3,4,5]
list4=['a','b','c','d']
print(len(list1))
print(list1+list2)
print(list1*2)
list1.append('good')
print(list1)
list1.insert(3,'good')
print(list1)
list1.remove('am')
print(list1)
list1.pop(-1)
print(list1)
print(list1.index("I"))
print(list1.count("am"))
list1.reverse()
print(list1)
list1.sort()
print(list1)
list1.clear()
print(list1)

a=[1,2,3]
b=['a','b','c']
print(a+b)
a.extend(b)
print(a)
a.append(b)
print(a)
a=[1,2,3]
print(len(a))
print(max(a))
print(min(a))


# - 列表的包含  
# 使用in可以检查列表中是否包含某个值，返回True，False
# 
# 

# In[13]:


list1 = ["I", "am", "a", "Pupil", ".","am"]
list2=['physic','chemistry',1997,2000]
if 'am' in list1:
    print("yes")
else:
    print("no")


# - 列表推导式
#   - 在list内部使用for循环来构造list的方法。
#   - 这些方法将让我们更加美观可读、方便简洁地实现一些功能。
#   - [表达式 for 变量 in 列表]    
#   - [表达式 for 变量 in 列表 if 条件]
# 
# 

# In[14]:


list1 = [1,2,3,4,5,6,7,8,9] 
list2 = [x**2 for x in list1]
list3 = [x**2 for x in list1 if x>5] 
print(list3)
multiples = [i for i in range(30) if i % 3 is 0] 
print(multiples) 

vec=[2,4,6]
vec2=[4,3,-9]
sq = [vec[i]+vec2[i] for i in range(len(vec))]
print(sq)


# In[ ]:


#例1:  过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']    
new = [name.upper() for name in names if len(name)>3] 
print(new)


# In[ ]:


#零均值处理，对列表中每个数值逐个减去均值
import random
li=[random.randint(0,100) for i in range(30)]
print(li)
avg=sum(li)/len(li)
newli=[i-avg for i in li]
print(newli)


# ## 2.元组
#   - 元组（tuple）数据结构与列表类似，其中元素可以有不同的类型，不同之处在于元组的元素不能修改。
#   - 元组使用小括号，列表使用方括号。
#   - 但是元组中的元素是不可变的，即一旦初始化之后，就不能够再做修改
#   - 元组对象没有append()、insert()和remove()这样的方法。
# 

# In[ ]:


tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
tup4 = ()
tup5 = (50,)


# - 元组操作
#   - 元组的长度: len(list)
#   - 合并元组: list1+list2
#   - 重复元组: list1*3
#   - 查找位置: list1.index(obj)
#   - 统计元素的次数：list1.count(obj)
#   - 反转：list1.reverse()
#   - 清空：list1.clear()
#   - 排序：list1.sort()
#   - 拼接两个列表：list1.extend(list2)
#   - 元组的最大值: max(list)
#   - 元组的最小值: min(list)
#   - 转换为元组: tuple(other)
# 

# In[ ]:


tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print(tup1[0])
print(tup2[1:5])
tup3 = tup1 + tup2
len((1, 2, 3))
tup4=(1, 2, 3) + (4, 5, 6)
tup5=('Hi!',) * 4
print(tup5)
for x in (1, 2, 3): 
    print( x)


# ## 3.字典
#   - 字典的创建使用大括号 {} 包含键值对，并用冒号 : 分隔键和值，形成 键:值 对
#   - 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
#   - 字典中的数据元素是无序的，并不会按照初始化的顺序排列。不同键所对应的值可以相同，但是字典中的键必须是唯一的
#   - 键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一。
#   - 利用for循环和zip()函数创建字典
#     - zip()函数用于将多个序列（列表、元组等）中的元素配对，产生一个如 [(列表1元素,列表2元素),(,)] 的新的元组列表；
#     - for循环用于重复执行将值放入键中的操作。
# 
# 

# In[ ]:


dict1 = {'a': 1, 'b': 2, 'b': '3'}
print(dict1['b'])
dict2={}

key=[1,2,3,4]
value=["a","b","c"]
for i,j in zip(key,value):
    dict2[i]=j
print(dict2)


# - 字典操作
#   - 字典的访问，通过字典的键进行访问
#   - 如果不太确定字典中有哪些键或者值，我们可以使用 keys() 方法或者values()方法
#   - 通过 in 判断是否存在某个键，其语法跟在列表和元组中判断是否存在某个值是相同的
#   - 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对
#   - 使用 items() 方法，该方法将返回所有键值对，并将其保存在一个元组列表
#   - 使用 pop() 方法删除单一元素
#   - 使用 clear() 方法清空词典的所有元素
# 

# In[ ]:


dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict1['Name']) 
#print(dict1['Number'])
keys=dict1.keys()
values=dict1.values()
print(keys)
print(values)
for i in dict1.keys():
    print(i,' : ',dict1[i])
for key,value in dict1.items():
    print(key,' : ',value)
dict1.pop("Age")
print(dict1)
dict1.clear()
print(dict1)


# In[ ]:


# - 两个特殊函数
#   - enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时获得索引和值。
#   - 利用enumerate()可以获得序列的索引和值组成的键值对。


# In[ ]:


for key,value in enumerate(dict1):
    print(key,value)


# ## 4.集合
#   - 集合（set）是一种无序集
#   - 在集合中，重复元素是不被允许的。集合可以用于去除重复值
#   - 集合中每个元素必须都是不可变类型
#   - 集合的创建有两种方式：使用 set() 函数或者使用大括号{}
#   - 需要注意的是，创建空集合，必须使用 set() ，而不是{}，因为{}表示创建一个空的字典

# In[ ]:


s1=set([1,2,3,4,5])
print(s1)
s2={'a','b','c'}
print(s2)
s3=set((1,2,3))
print(s3)
s4=set("hello")
print(s4)


#   - 集合操作
#     - 通过add()添加一个元素，原值修改，无返回值
#     - 通过update()添加一个可迭代对象，可迭代对象可以是列表，元组，字典和字符串，将其迭代添加
#     - remove（） 删除集合中指定的元素,如果删除的元素不存在，则会报错
#     - pop() 随机删除集合的某一个元素
#     - del 删除整个集合
#     - clear()清空集合
#     - 交集：&  或者 intersection
#     - 并集：| 或者 union
#     - 差集：- 或者 difference
#     - 反交集：^ 或者 symmetric_difference
#     - 子集与超集
#     - 去重。把一个列表变成集合，就自动去重了
#     - 关系测试。测试两组数据之前的交集、差集、并集等关系

# In[ ]:


set1=set({'jim','jordan','Spider Man'})
set1.add('Kong Fu Panda')
print(set1) 
set1.update("hello")
print(set1) 
set1.remove('jordan')
print(set1)
set1.pop()
print(set1)
set1.clear()
print(set1)
del set1

set2=set({'jim','jordan','Spider Man','James','Jack'})
for i in set2:
    print(i)

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1 & set2)  # {4, 5}
print(set1.intersection(set2))  # {4, 5}
print(set1 | set2)  # {1, 2, 3, 4, 5, 6, 7,8}
print(set2.union(set1))  # {1, 2, 3, 4, 5, 6, 7,8}
print(set1 - set2)  # {1, 2, 3}
print(set2 - set1) #{8, 6, 7}
print(set1.difference(set2))  # {1, 2, 3}
print(set2.difference(set1)) #{8, 6, 7}
print(set1 ^ set2)  # {1, 2, 3, 6, 7, 8}
print(set1.symmetric_difference(set2))  # {1, 2, 3, 6, 7, 8}


# ## 5.练习
# In[ ]:
import random,string,numpy as np
# 列表  
# *1. 有两个列表：l1 = [11, 22, 33]，l2 = [22, 33, 44]，获取内容相同的元素列表，获取l1中有， l2中没有的元素列表，获取l1 和 l2 中内容都不同的元素
l1=[11,22, 33];l2=[22,33,44]
print("内容相同的元素有：{}".format(set(l1)&set(l2)))
print("l1有，l2没有的元素有{}".format(set(l1)-set(l2)))
print("l1l2内容不同的元素有{}".format(set(l1)^set(l2)))
# In[ ]:


# *2. 创建列表，内容为a-z,A-Z,0-9，并从中随机抽出6个字符作为验证码
print("验证码：{}".format("".join(random.sample(list(string.ascii_letters)+list(string.digits),6))))
# In[ ]:


# *3. 随机生成1000个整数，数字范围[20,100]，升序输出所有不同的数字及其每个数字的重复次数
list1=[random.randint(20,100) for var in range(1000)];list1.sort()
dict1={var:list1.count(var) for var in list1}
print("升序输出所有不同的数字和每个数字重复的次数:\n")
for key in dict1:
    print("{0}重复的次数：{1}".format(key,dict1[key]))
# In[ ]:


# *4. 随机生成100个卡号: 卡号以6102009开头， 后面3位依次是 （001， 002， 003， 100），生成关于银行卡号的字典， 默认每个卡号的初始密码为"redhat";输出卡号和密码信息， 格式如下: 
# 卡号 密码
# 6102009001 000000
print("卡号  密码")
carDict={6102009000+var:"radhat" for var in range(1,101)}
for key in carDict:
    print("{0}\t\t{1}".format(key,carDict[key]))
# In[ ]:


# *5. 根据输入的月份，打印该月份所属的季节。提示: 3,4,5 春季 6,7,8 夏季 9,10,11 秋季 12, 1, 2 冬季。
try:
    inputMonth = int(input("请输入月份："))
    if inputMonth<1 or inputMonth>12:raise ValueError
    seasonsDict = {"春季": [3, 4, 5], "夏季": [6, 7, 8], "秋季": [9, 10, 11], "冬季": [12, 1, 2]}
    for key in seasonsDict:
        if inputMonth in seasonsDict[key]:
            print("输入的是:{}".format(key))
except ValueError:print("请输入正确月份")
# In[ ]:


# *6. 已知names = [‘jane’,‘joe’,‘susan’,‘black’,‘leonaldo’] ，找出上述名字中长度大于4的名字,组成列表打印出来. ( for 循环遍历，与列表推导式 两种方法做)
def forMethod(inputList):
    listOutput=[]
    for var in inputList:
        if len(var)>4:
            listOutput.append(var)
    return listOutput
def otherMethod(inputlist):
    listOutput=[var for var in inputlist if len(var)>4]
    return listOutput
names =['jane','joe','susan','black','leonaldo']
print("for循环遍历出来的：{}".format(forMethod(names)))
print("列表推导出来的：{}".format(otherMethod(names)))
# In[ ]:


# *7.10以内大于4的数写入列表
print("10以内大于4的数构成的列表：{}".format([var for var in range(10) if var>4]))
# In[ ]:


# *8.将10以内所有整数写入列表
print("10以内所有整数构成的列表：{}".format([var for var in range(10) if isinstance(var,int)]))
# In[ ]:


# *9.将10以内所有整数的平方写入列表。
print("10以内所有整数的平方构成的列表：{}".format([var**2 for var in range(10) if isinstance(var,int)]))
# In[ ]:


# *10.100以内所有的偶数写入列表.
print("100以内所有整数构成的列表：{}".format([var for var in range(100) if isinstance(var,int) if var%2==0]))
# In[ ]:


# *11.使用列表推到式得出:0-30间能被3整除的数
print("0-30间能被3整除的数：{}".format([var for var in range(1,31) if var%3==0]))
# In[ ]:
# *12.求M,N中矩阵对应元素的和与元素的乘积    (提示：使用2个for遍历)
# m =[[1,2,3],  [4,5,6],  [7,8,9]] ，n =[[2,2,2],  [3,3,3], [4,4,4]]
# 用两个for遍历的方式：
m =[[1,2,3],  [4,5,6],  [7,8,9]] ;n =[[2,2,2],  [3,3,3], [4,4,4]]
listout=[]
for listindex in range(len(m)):
    listnew=[]
    for var in range(len(m[listindex])):
        listnew.append(m[listindex][var]*n[listindex][var])
    listout.append(listnew)
print(listout)

# In[ ]:
# *13.找到嵌套列表中名字含有两个‘e’的所有名字：names=[['Tom','Billy','Jefferson','Andrew','Wesley','Steven','Joe'],['Alice','Jill','Ana','Wendy','Jennifer','Sherry','Eva']]
names=[['Tom','Billy','Jefferson','Andrew','Wesley','Steven','Joe'],['Alice','Jill','Ana','Wendy','Jennifer','Sherry','Eva']]
print("嵌套列表中名字含有两个'2'的所有名字组成的列表：{}".format([var for i in names for var in i if var.count('e')==2]))
# In[ ]:


# *14.过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
print("转换后的列表中的名字有：{}".format([i for i in names if len(i)>=3]).upper() )
# In[ ]:
# *15.对列表中每个数值逐个减去均值
inputList=[]
flag=True
try:
    while flag:
        inputValue = input("请输入一个数字加入list，输入#结束输入：")
        if inputValue == "#":
            avg = int(sum(inputList) / len(inputList))
            print(avg)
            newli = [i - avg for i in inputList]
            print(newli)
            flag = False
        else:
            inputValue = int(inputValue)
            inputList.append(inputValue)
            print(inputList)
            flag = True
except ValueError:print("你输入的既不是数字也不是#")



# In[ ]:
# *16.按照下面的要求实现对列表的操作：1). 产生一个列表，其中有 40 个元素，每个元素是 50 到 100 的一个随机整数。2). 如果这个列表中的数据代表着某个班级 40 人的分数，请计算成绩低于平均分的学生人数。3). 对上面的列表元素从大到小排序并输出li.sort(reverse=True)   
listOut=[random.randint(50,100) for i in range(40)];listOut.sort()
print("（1）中要的列表为：{}".format(listOut))
print("（2）中问题成绩低于平均分的人数为：{}".format(len([i for i in listOut if i<np.mean(listOut)])))
print("(3)中的问题中所要的从小到大排序为：{}".format(listOut))
# In[ ]:
# *17.编写用户登陆系统，要求如下:
# 系统里面有多个用户，用户的信息目前保存在列表里面users = ['root','westos'], passwd = ['123','456']，用户登陆(判断用户登陆是否成功）
# 1).判断用户是否存在
# 2).如果存在，判断用户密码是否正确，如果正确，登陆成功，退出循环，如果密码不正确，重新登陆，总共有三次机会登陆
# 3).如果用户不存在
# 重新登陆，总共有三次机会
uers=['root','westos'];passwd=['123','456']
class dropExcept(Exception):pass
try:
    for i in range(3):
        inputUser = input("请输入用户名：");inputPasswd = input("请输入密码：")
        for user in uers:
            if user == inputUser:
                if inputPasswd == passwd[inputUser.index(user)]:raise dropExcept
                else:print("密码错误")
            else:print("用户名错误")
    else:print("登陆失败")
except dropExcept:print("登陆成功")
# In[ ]:


# 元组  
# *18. 有以下列表，nums = [2, 7, 11, 15, 1, 8]，请找到列表中任意相加等于9的元素集合，如：[(8, 1), (4, 5)]
nums = [2, 7, 11, 15, 1, 8]
print("满足条件的集合有：{}".format([(nums[i],nums[j]) for i in range(0,len(nums)) for j in range(i,len(nums)) if nums[i] + nums[j] == 9]))
# In[ ]:


# *19.求(x,y)其中x是0-5之间的偶数，y是0-5之间的奇数组成的元祖列表
print("题目所求的元组列表为：{}".format([(x,y) for x in range(5) for y in range(5) if x%2==0 if y%2!=0]))
# In[ ]:


# 字典  
# *20 创建一个空字典，输入学生姓名和成绩，并一一对应，当输入#退出
studentDict={}
def drop(str):
    if str=="#":
        raise dropExcept
class dropExcept(Exception):pass
try:
    while True:
        studentName=input("学生姓名：");drop(studentName)
        studentScore=input("学生成绩:");drop(studentScore)
        studentDict[studentName]=studentScore
except dropExcept:
    print("退出新增学生信息！");
    print("学生姓名\t\t学生成绩")
    for key in studentDict:
        print("{}\t\t\t\t{}".format(key,studentDict[key]))
# In[ ]:


# *21. 有如下值集合[11,22,33,44,55,66,77,88,99,90], 将所有大于66的值保存至字典的第一个key中，将小于66值保存至第二个key的值中.
listInput=[11,22,33,44,55,66,77,88,99,90]
key1List=[]
key2List=[]
for var in listInput:
    if var>66:key1List.append(var)
    else:key2List.append(var)
outDict={'key1':key1List,'key2':key2List}
outDict
# In[ ]:


# *22.统计重复单词的次数：此处认为单词之间以空格为分隔符，并且不包含,和. 要求用户输入一个英文句子，打印出每个单词及其重复的次数
# inputSentense
# inputList=inputSentense
inputList=input("请输入一个英文句子：").replace(',',' ').replace('.',' ').split()
inputDict={}
for var in inputList:
    inputDict[var]=inputList.count(var)
for key in inputDict:
    print("英语单词：{0}出现的次数:{1}".format(key,inputDict[key]))
# In[ ]:


# *23.数字重复统计。随机生成1000个整数，数字的范围[20，100]，升序输出所有的不同的数字及其每个数字重复的次数。
inputList=[random.randint(20,100) for i in range(1000)];inputList.sort()
outputDict={var:inputList.count(var) for var in inputList}
for key in outputDict:
    print("数字:{}重复的次数为：{}".format(key,outputDict[key]))
# In[ ]:


# 集合  
# *24. 明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性,他先用计算机生成了N个1～1000之间的随机整数(N<=1000),N是用户输入的，对于其中重复的数字，只保留一个，把其余相同的数字去掉，不同的数对应着不同的学生的学号，然后再把这些数从小到大排序，按照排好的顺序去找同学做调查，请你协助明明完成“去重”与排序工作. 
try:
    inputN = int(input("请输入小于等于1000的数:"))
    if inputN > 1000 or inputN <= 0: raise ValueError
    listOnput=list(set([random.randint(1,1000) for i in range(inputN)]));listOnput.sort()
    print(listOnput)
except ValueError:print("请输入小于等于1000的正整数")

# In[ ]:

