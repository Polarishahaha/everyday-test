# 输入数据
name = input('请输入患者姓名:')
id = input('请输入患者身份证号:')
age = int(input('请输入患者年龄:'))
height = float(input('请输入患者身高:'))
weight = float(input('请输入患者体重:'))
BG = float(input('请输入患者血糖:'))

# 获得非计算数据
birthday = int(id[6:10])

# 获得计算数据
BMI = weight/(height/100)**2

# 进行判断

# 判断年龄段
if 0 <= age <= 17 :
    age_stage='未成年'
elif 18 <= age <= 59:
    age_stage='成年人'
else:
    age_stage='老年人'

# 判断体型
if BMI < 18.5:
    build='偏瘦'
elif 18.5 <= BMI <24:
    build='正常'
elif 24 <= BMI <28:
    build='超重'
else :
    build='肥胖'

# 判断血糖
if 3.9 <= BG <= 6.1:
    BG_situation = '正常'
else:
    BG_situation = '异常'

# 输出报告
print('===== 门诊初步评估报告 =====')
print('姓名: %s'%name)
print('出生年份: {}'.format(birthday))
print(f'身高: {height:.1f} cm')
print(f'体重: {weight:.1f} kg')
print(f'BMI: {BMI:.2f}')
print(f'体型: {build:}')
print(f'血糖: {BG:}'+' mmol/L')
print(f'血糖状态: {BG_situation}')
print('========================')

'''
收获：1.对齐符号<>后面如果没有宽度就是无效的
2.智能计算年龄：
from datetime import datetime

id_card = input('请输入身份证号:')
birth_year = int(id_card[6:10])
birth_month = int(id_card[10:12])
birth_day = int(id_card[12:14])

today = datetime.now()
age = today.year - birth_year

# 如果今年生日还没到，年龄减 1
if (today.month, today.day) < (birth_month, birth_day):
    age -= 1

print(f'年龄：{age}')
'''