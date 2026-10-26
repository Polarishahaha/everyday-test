# 练习1 布尔值判断

print(5>3)
print(5 == 5.0)
print('abc' < 'abd')
print(3 > 2 and 4 < 5)
print(3 >2 or 4 > 5)
print(0 and 5,0 or 5,'' or 'hi',bool(0) ,bool('') ,bool('False'))


# 易错：字符串'False'和'0'都是True！负数也是True
# False结果：False，None，0/0.0/0j, 空字符串''，空列表[]， 空字典{}， 空元组(), 空集合set()

# 练习2 判断闰年
year = eval(input('请输入年份:'))

if (year %4 == 0 and year %100 != 0) or (year %400 == 0) :
    print('闰年')
else :
    print('不是闰年') 


# 练习3 判断是否构成三角形
a = float(input('请输入边长a:'))
b = float(input('请输入边长b:'))
c = float(input('请输入边长c:'))
d = a+b>c and a+c>b and b+c>a
print(f'能否构成三角形：{d}')

# 练习4 登录密码
user_name = input('请输入用户名：')
password = eval(input('请输入登录密码:'))
success = user_name == 'admin' and password == 123456
if success :
    print('Welcome back!')
else:
    print('Sorry,we cannot let you sign in.')
# 练习5 短路求值
x = 5;y = 0
print(x > 0 and y != 0)
print(x < 0 or y == 0)

# 练习6 短路求值
print(False and (1 / 0))
print(True or (1 / 0))