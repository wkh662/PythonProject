# 注释 ctrl+/
print("shabi")
print(100)
print(True)
#------------
#变量--动态类型语言，一个变量可以存储不同类型变量（项目中不建议）
num=114.514
print(num)
num+=1
print(num)
num="cao"
print(num)
a,b=10,10.5
print(a,b)
我=1
print(我)
#-----------
#数据类型
int#整数
float#浮点数
str#字符串
bool#布尔
#--------------
#NoneType#空值 只有None
print(type(10))
print(type(num))
#---------------
#isinstance---判断是否为某一类型----返回值bool类型
print(isinstance(num,int))
#---------------
#双引号定义
s1="hallo"

#单引号定义
s2='fuck'

#当内部有单引号的时候
# 转义字符
# \'
# \"
# \n
#\t---缩进
s4='it\'s good'



#多行定义--三引号会直接输出内容
s3="""
history
你好
故事
"""
print(s1)
print(s2)
print(s3)
print(s4)
#----------

#字符串拼接
s1="人生苦短"
s2="我用python"
print("python之父："+s1+","+s2)
#----------------------

#字符串与字符串拼接
name="王康骅"
age=18
pro="计算机"
hobby="python"
print("你好，我是:"+name+"今年"+str(age)+"专业是"+pro+"喜欢"+hobby)
#----------------------

#格式化占位符
print("大家好我是%s今年%d"%(name,age))
print(f"大家好，我是{name},今年{age}学的是{pro}会用{hobby}")
#{}里面可以是表达式或变量名，前面的f不能少
#------------------

#输入---无论键盘输入什么类型，都默认是字符串类型
s=input("请输入姓名：")
print(f"欢迎您┭┮﹏┭┮ {s}")
#--------------------

#案例
total=10000
cot=input("请输入密码：")
output=input("请输入取款金额：")
remain=total-int(output)
print(f"余额{remain}")
#------------

#多行注释
"""
 asdafaf
        asfavdav
       
"""
