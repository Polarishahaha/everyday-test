# 练习1

print(5>3)
print(5 == 5.0)
print('abc' < 'abd')
print(3 > 2 and 4 < 5)
print(3 >2 or 4 > 5)
print(0 and 5,0 or 5,'' or 'hi',bool(0) ,bool('') ,bool('False'))


# 易错：字符串'False'和'0'都是True！负数也是True
# False结果：False，None，0/0.0/0j, 空字符串''，空列表[]， 空字典{}， 空元组(), 空集合set()

# 练习2
year = int(input('请输入年份:'))
is_leap = (year %4 == 0 and year %100 != 0) or (year %400 == 0)
print(year)



# 练习3
a = float(input('请输入边长a:'))
b = float(input('请输入边长b:'))
c = float(input('请输入边长c:'))
d = a+b>c and a+c>b and b+c>a
print(f'构成三角形为：{d}')

# 练习4
user_name = input('请输入用户名：')
password = int(input('请输入登录密码:'))
success = user_name == 'admin' and password == 123456
print(success)

# 练习5
x = 5;y = 0
print(x > 0 and y != 0)
print(x < 0 or y == 0)

# 练习6
print(False and (1 / 0))
print(True or (1 / 0))