#!/usr/bin/env python
# coding: utf-8

# # 第三部分 字符串
# ## 1.字符串常用操作
# - 字符串是以两个单引号或两个双引号包裹起来的文本
# - 截取字符串（切片）
#   - str = '0123456789'
#   - print(str[0:3]) #截取第一位到第三位的字符
#   - print(str[:]) #截取字符串的全部字符
#   - print(str[6:]) #截取第七个字符到结尾
#   - print(str[:-3]) #截取从头开始到倒数第三个字符之前
#   - print(str[2]) #截取第三个字符
#   - print(str[-1]) #截取倒数第一个字符
#   - print(str[::-1]) #创造一个与原字符串顺序相反的字符串
#   - print(str[-3:-1]) #截取倒数第三位与倒数第一位之前的字符
#   - print(str[-3:]) #截取倒数第三位到结尾
#   - print(str[:-5:-3]) #逆序截取
# - 去掉空格和特殊符号
#   - name.strip()  去掉空格和换行符
#   - name.lstrip()  去掉左边的空格和换行符
#   - name.rstrip()  去掉右边的空格和换行符  
# - 字符串的搜索和替换
#   - name.count('x')  查找某个字符在字符串里面出现的次数
#   - name.capitalize()  首字母大写
#   - name.center(n,'-')   把字符串放中间，两边用- 补齐
#   - name.find(‘x’)   找到这个字符返回下标，多个时返回第一个；不存在的字符返回-1,一般用返回值是否等于-1作为判断条件
#   - name.index('x') 找到这个字符返回下标，多个时返回第一个；不存在的字符报错
#   - name.replace(oldstr, newstr)  字符串替换
# - 字符串的测试和替换函数
#   - S.startswith(prefix[,start[,end]]) #是否以prefix开头 
#   - S.endswith(suffix[,start[,end]]) #以suffix结尾 
#   - S.isalnum() #是否全是字母和数字，并至少有一个字符
#   - S.isalpha() #是否全是字母，并至少有一个字符 
#   - S.isdigit() #是否全是数字，并至少有一个字符 
#   - S.isspace() #是否全是空白字符，并至少有一个字符 
#   - S.islower() #S中的字母是否全是小写 
#   - S.isupper() #S中的字母是否全是大写 
#   - S.istitle() #S是否是首字母大写的
# - 字符串的分割
#   - name.split()  默认是按照空格分割
#   - name.split(',')   按照逗号分割
# - 连接字符串
#   - “+”连接字符串
#   - ‘-’.join(slit)      用-连接slit 变成一个字符串，slit 可以是字符，列表，字典（可迭代的对象）。int 类型不能被连接
# - 字符串中字母大小写转换
#   - S.lower() #转换为小写 
#   - S.upper() #转换为大写 
#   - S.swapcase() #大小写互换 
#   - S.capitalize() #首字母大写 
# - 是否包含指定字符串
#   - in 
#   - not in 
# - 字符串长度
#   - len(s)
# 

# In[1]:


a='    hello    '
b=a.strip()
c=a.lstrip()
d=a.rstrip()

a='hello world'
print(a.count('or'))
print(a.capitalize())
print(a.center(20,'-'))
print(a.find('or'))
print(a.find('ore'))
if a.find("or")==-1:
    print("不存在")
else:
    print("存在")
b=a.replace("o","oo")
print(b)

a='AdfsdfsdfS23'
print(a.startswith("He"))
print(a.endswith('23'))
print(a.isalnum())
print(a.isalpha())
print(a.isdigit())
print(a.isspace())
print(a.islower())
print(a.isupper())
print(a.istitle())

name="hello,world,hello,world"
name.split(',')

a="hello"
b="world"
print(a+b)
c=["hello","world"]
d="".join(c)
print(d)
d="-".join(c)
print(d)

a='Hello World'
print(a.lower())
print(a.upper())
print(a.swapcase())
print(a.capitalize())

a='hello world'
print('hello' in a)
print('123' not in a)
if "123" in a:
    print("in")
else:
    print("not in")


# In[2]:


# 将字符串作为迭代对象，使用for循环取每一个元素
# 请输出name变量中的值"Q的索引的位置
# 将name变量对应的值变成小写，并输出结果
# 移除name变量对应值的两边的空格，并输出移除后的内容
# 判断name变量对应的值是否以"go"开头，并输出结果
# 判断name变量对应的值是否以"Q"结尾，并输出结果
# 将name变量对应的值中的"o"，替换为"p"，并输出结果
# 将name变量对应的值根据"o"分割，并输出结果
# 请输出name变量对应值的后2个字符
# 请输出name变量对应的值的前三个字符
# 请输出name变量对应的值的第二个字符获取子序列，仅不包含最后一个字符，如：woaini则获取woain  root则获取roo
# 利用下划线将字符串的每一个元素拼接成字符串  li = "gouguoqi"
# 利用下划线将列表的每一个元素拼接成字符串  li = ['gou', 'guo', 'qi']


# ## 2.字符串练习

# *1.计算用户输入的内容中有几个十进制小数？几个字母？

# In[ ]:

inputValue=input("请输入要输入的内容")
num,zm=0,0
for var in inputValue:
    if var.isalpha()==True:
        zm+=1
    elif var.isdecimal()==True:
        num+=1
print("宁输入的内容中有{0}个字母，{1}个数字".format(zm,num))



# *2.开发敏感词语过滤程序，提示用户输入内容，如果用户输入的内容中包含特殊的字符，请替换

# In[ ]:
inputValue=input("请输入要输入的内容")
badList=["傻逼","王怡波","肖战","闪电五连鞭"]
for var in badList:
    varLen=len(var)
    if inputValue.find(var) != -1:
        change = ''
        print(var+'内循环输出')
        while varLen!=0:
            change=change+'*'
            varLen=varLen-1
        inputValue = inputValue.replace(var, change)
print('过滤后的结果是：'+inputValue)




# *3.将字符串作为迭代对象，使用for循环取每一个元素

# In[ ]:
inputValue=input('请输入字符串')
for var in inputValue:
    print(var)
# *4.将name变量对应的值变成小写，并输出结果

# In[ ]:
name=input('请输入字符串')
print(name.lower())




# *5.移除name变量对应值的两边的空格，并输出移除后的内容

# In[ ]:
name=input('请输入:')
print(name.strip())




# *6.接收用户输入的一个字符串，判断是否为纯数字

# In[ ]:
inputStr=input('请输入字符串：')
if inputStr.isdigit():
    print("是纯数字")
else:
    print('不是纯数字')



# *7.接受用户输入的一个字符串，如果是正整数就判断是否能同时被3和7整除

# In[ ]:
inputStr=input('请输入：')
if inputStr.isdigit():
    inputNum=int(inputStr)
    if isinstance(inputNum,int):
        if (inputNum%3==0) and (inputNum%7==0):
            print('输入的是正整数且可以同时被3和7整除')
        else:print('不能同时被3和7整除')
    else:print('输入的不是正整数')
else:print('输入的不是纯数字')




# *8.如果将一句话作为一个字符串，那么这个字符串中必然会有空格，比如"How   are you."，但有的时候，会在两个单词之间多打一个空格。现在的任务是，如果一个字符串中有连续的两个或多个空格，请把它删除，仅保留一个空格。

# In[ ]:
inputStr=input('输入的字符串')
# s = 'How      are you '
word = inputStr.split()
new_s = " ".join(word)
print(new_s)



