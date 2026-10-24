name=input('请输入溶液名称：')
m=float(input('请输入溶质质量：'))
M=float(input('请输入溶质摩尔质量：'))
V=float(input('请输入溶液体积：'))
# 通过input获得四个信息,先不卡浮点数小数点

n=m/M
c=n/(V/1000)
# 计算物质的量浓度

print('===== 溶液配制报告 =====')
print('溶液名称  :%s'%name)
print('溶质质量  :{:>8.2f} g'.format(m))
print('摩尔质量  :{:>8.2f} g/mol'.format(M))
print(f'溶液体积  :{V:>8.1f} mL')
print(f'物质的量  :{n:>8.4f} mol')
print(f'浓度      :{c:>8.4f} mol/L')
print('='*24)

'''
今日学习:1.数据类型转换注意：文件中提取的数字类型是字符串 int/float(); input()得到的数据是字符串 int/float();需要将数字转换为字符串形式输出 str
2.print输出时,可用','隔开输出多个,输出后在同一行
3.float转int时,会丢失精度,也就是直接舍弃小数而非四舍五入
4.格式化精度控制:.nf后,若n比原来位数少,则四舍五入(与int不同)



'''