#判断语句
n=int(input("输入一个整数："))
if n>=20:
        print(f"{n}是大于20的数")
        print("你真牛逼")
print("-----------------")
#没有缩进则不属于if代码块
#-------------------

#案例
true_name = "1111"
true_cod = "1111"
name = input("账号：")
cod = input("密码：")
if cod == true_cod and name == true_name:
    print("登陆成功")
    print("你真牛逼")
else:
    print("登陆失败")
    print("你真傻逼")

year=int(input("今年是："))
if (year%100!=0 and year%4==0) or year%400==0:
    print("是闰年")
else:
    print("不是闰年")
#--------------------
year=int(input("今年是："))
if year%100!=0 and year%4==0:
    print("是闰年")
elif year%400==0:
    print("是闰年")
else:
    print("不是闰年")
    pass#不做任何操作--为了语法工整的占位符

pay = float(input("请输入月收入："))
if pay <= 2000:
    z = 0
elif pay <= 3000:
    z = (pay - 2000) * 0.05
elif pay <= 4000:
    z = (pay - 3000) * 0.15 + 50
elif pay <= 5000:
    z = (pay - 4000) * 0.25 + 200
else:
    z = (pay - 5000) * 0.35 + 450
print(f"月收入{pay:.2f}，调节税为{z:.2f}")