#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = 123
print (n)

# In[ ]:

f=456.21389
print (f)


# In[ ]:


s1 = 'Hello,World'
print (s1)


# In[ ]:


# string前面加上‘r’表示就按原先字符串输出，里面的转义字符不用生效
s3=r'Hello,"Bart"'
print (s3)


# In[ ]:


s32='Hello,"Bart"'
print (s32)


# In[ ]:


# 三引号是多行字符串，可以直接输入回车，而不需要用\n来表示
s4=r'''Hello,
Lisa!'''
print (s4)


# In[ ]:


# 输入半径求圆的周长和面积
r=int(input("输入半径求圆的周长和面积"))
pi=3.14
S=pi*r*r
C=pi*2*r
print ("圆的周长是%s圆的面积是%s"%(S,C))


# In[ ]:





# In[ ]:


# 判断是否为闰年（被4整除，不能被一百整除，能被四倍整除）
try:
    year=int(input("请输入年份："))
    if (year%4)==0 and (year%100)!=0 or (year)%400==0:
        print("{0}是闰年".format(year))
    else:
        print("{0}不是闰年".format(year))
except ValueError:
    print("{0}不是正确的年份格式".format(year))


# In[ ]:


# 输入3条边，判断是否为三角形，是就求三角形面积
try:
    a1=float(input("输入第一条边:"))
    a2=float(input("输入第二条边:"))
    a3=float(input("输入第三条边:"))
    if (a1<=0)or(a2<=0)or(a3<=0):
        print("边长应该大于0！")
    elif (a1+a2)>a3 and (a1+a3)>a2 and (a2+a3)>a1:
        s = (a1 + a2 + a3) / 2
        area = (s * (s - a1) * (s - a2) * (s - a3)) ** 0.5
        print("三条边可以组成三角形,且三角形面积为{0}".format(area))
    else:
            print("三条边不能组成三角形，两条边的和应该大于第三边")
except ValueError:
    print("边长应该为数字！")


# In[ ]:


# 把百分之转换成等级制
try:
    stestcore = float(input("请输入你的成绩："))
    if 100>=stestcore>=90:
        print("A")
    elif 90>stestcore>=80:
        print("B")
    elif 80>stestcore>=70:
        print("C")
    elif 70>stestcore>=60:
        print("D")
    elif 60>stestcore>=0:
        print("E")
except ValueError:
    print("输入成绩格式错误")
        


# In[ ]:


# 从1加到100
a=1
sumvalue = 0
while a<101:
    sumvalue=sumvalue+a
    a+=1
print(sumvalue)


# In[ ]:


# 1到100所有的偶数相加结果
a=1
sumvalue = 0
while a<101:
    if a%2==0:
        sumvalue=sumvalue+a
    a+=1
print(sumvalue)


# In[ ]:


# 一颗骰子摇60000次统计各个数字出现的次数，验证随机数是否可靠
import random
is1,is2,is3,is4,is5,is6=0,0,0,0,0,0
times=0
point=0
while times<60001:
    point=random.randint(1,6)
    if point == 1:
        is1+=1
    elif point == 2:
        is2+=1
    elif point == 3:
        is3+=1
    elif point == 4:
        is4+=1
    elif point == 5:
        is5+=1
    elif point == 6:
        is6+=1
    times+=1
print("1出现的次数是{0}，2出现的次数是{1},3出现的次数是{2},4出现的次数是{3},5出现的次数是{4},6出现的次数是{5}".format(is1,is2,is3,is4,is5,is6))
if is1==is2==is3==is4==is5==is6:
    print("随机数是不可靠的")
else:
    print("随机数是可靠的")


# In[7]:


# 计算机随机出1到100的一个数，有人来猜，猜对了，显示（恭喜你，猜对了）、猜大猜小了都有提示；如果猜7次以上提示“智商捉急”
import random
randomNum=random.randint(1,100)
print(randomNum)
times=0
yourNum=float(input("输入你要猜的数字:"))
while times<7:
    if yourNum > randomNum:
        print("猜大了，请继续猜")
        yourNum=float(input("输入你要猜的数字:"))
        times=times+1
    elif yourNum < randomNum:
        print("猜小了，请继续猜")
        yourNum=float(input("输入你要猜的数字:"))
        times=times+1   
    elif yourNum == randomNum:
        break  
if times==8:  
    print("智商捉急")
else:
    print("猜对了")


# In[ ]:


# 判断一个数是不是素数（除了1和自身，不能被其他数整除）
try:
    inputNum = int(input("输入要验证是否为素数的数："))
    i=2
    times=0
    while i<inputNum:
        if (inputNum%i) == 0:
            times+=1
            i+=1
        else:
            i+=1
    if times == 0:
        print("输入的数是素数")
        print("times:{0}".format(times))
    else:
        print("输入的数不是素数")
        print("times:{0}".format(times))
except ValueError:
    print("请正确输入一个数")


# In[8]:


# 找出10000以内的完美数
def numbers(number):
    sum=0
    d=list()
    for i in range(1,number):#range(1,6)
        if number%i==0:
            d.append(i)
        else:
            continue
    for i in d:
        sum+=i
    if sum==number:
        print(number)

for i in range(6,10001):
    numbers(i)
    


# In[14]:


# 九九乘法表
i=1
while i<10:
    j=1
    while j<=i:
        s=j*i
        print("{0}*{1}={2}".format(j,i,s), end=' ')
        j+=1
    print("")
    i+=1


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




