# 自动售货机程序

# 明天修bug，力竭了

# 商品价格

water = 2.0
cola = 3.5
sprite = 3.5
chip = 5.0
chocolate = 6.5

# 给出计数器
count_water = count_cola = count_sprite = count_chip = count_chocolate = 0
number = 0

# 打印菜单

print('='*5,' 商品菜单 ','='*5)
print('矿泉水：{:<4}元'.format(water))
print('可乐：{:<6}元'.format(cola))
print('雪碧：{:<6}元'.format(sprite))
print('薯片：{:<6}元'.format(chip))
print('巧克力：{:<4}元'.format(chocolate))
print('输入 q 结算')

# 进入点单 

order = 0

while order != 'q' :
    while True :
        order = input('请输入所需商品名称(单次只能点一类商品！)：')
        number = input('请输入所需商品数量：')

        if order == 'q' :
            break        # break后面的代码都不执行了

        if number.isdigit() :
            number = int(number)
        else :
            print('商品数量必须为整数！')
            break
        
        if order in ['矿泉水','可乐','雪碧','薯片','巧克力'] :

            if order == '矿泉水' :
                count_water += number
            elif order == '可乐' :
                count_cola += number 
            elif order == '雪碧' :
                count_sprite += number 
            elif order == '薯片' :
                count_chip += number 
            else :
                count_chocolate += number 
            break
        else :
            print('我们没有这种商品哦')
        
# 进入结算

total = count_water + count_cola + count_sprite + count_chip + count_chocolate

money = (water * count_water) + (cola * count_cola) + (sprite * count_sprite) + (chip * count_chip) + (chocolate * count_chocolate)

money = float(f'{money:.2f}')
money = round(money,2)

# 打印结果
print('='*5,' 购物清单 ','='*5)

if count_water + count_cola + count_sprite + count_chip + count_chocolate == 0 :
    print('购物车为空,无需付款')

elif count_water + count_cola + count_sprite + count_chip + count_chocolate != 0 :      
    print(f'商品共 {total} 件，其中矿泉水 {count_water} 件，可乐 {count_cola} 件，雪碧 {count_sprite} 件，薯片 {count_chip} 件，巧克力 {count_chocolate} 件')
    print(f'总价 {money} 元')

# 收款
    while True :
        cash = eval(input(f'请付款 {money:.2f} 元：'))
        
        if str(type(cash)) == "<class 'float'>" or "<class 'int'>":
            cash = round(cash,2)
            print(f'已付款 {cash} 元')
            if cash == money :
                break
            elif cash > money :
                print(f'为您找零 {cash - money} 元')
                break
            else :
                print('当前付款无效，请重试')
        else :
            print('当前付款无效，请重试')

# 结束语

print('谢谢光临！')
            


'''
思路：1.赋值
2.每个商品各自使用一个计数器
3.while items ！= q ：保持循环
4.'请输入所需的商品'；'请输入数量'
5.while True 解决输入正确性，break跳出循环
6.结算'购物清单'
7.找零
'''
