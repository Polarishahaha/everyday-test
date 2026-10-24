'''
思路:
1.获取信息(input)
2.计算BMI
3.输出

'''

name=input('请输入姓名:')
age=int(input('请输入年龄:'))
height=float(input('请输入身高:'))
weight=float(input('请输入体重:'))
BG=float(input('请输入血糖:'))
#已逐步获取信息

BMI=weight/(height/100)**2
#已完成BMI计算

print('===== 检验报告 =====')
print('姓名      :%-10s'%name)
print('年龄      :{:>3}岁'.format(age))
print(f'身高      :{height:^8.1f}cm')
print(f'体重      :{weight:^8.1f}kg')
print(f'BMI      :{BMI:^8.2f}')
print(f'血糖      :{BG:^8.2f}mmol/L')
print('='*20)
#已完成输出

height=170;name='张三';weight=float(60)
print(type(weight))
print(f'身高：{height:>8.2f}cm')
print('姓名：%-10s      %8.2f'%(name,weight))

'''
今日出错：
1.格式化输出姓名,应该%s,表示字符串
2.'姓名：%s'%name    不要丢了后面的赋值！
3.f'{}'类型里,{:>}表示对齐,>右<左^居中,{:.2f}表示精确度,如果去掉.,则为默认六位精确度,合起来：{:>3.2f}
4.'%d,%s'等形式,后面应为%(a,b),一个%带一个(),()里多个变量用,连接
5.'{}{}{}'.format(a,b,c)的格式里,不必一一对应,从a 开始,以0 为序号往后排索引顺序,
  ★不能用负数索引,
  ★合规操作:1.a =10;b=1
               print('{0}{1}'.format(a,b))
             2.a =10;b=1
               print('{a}{b}'.format(a=10,b=1))
'''