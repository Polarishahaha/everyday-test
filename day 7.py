# 石头剪刀布程序

# 赛制：五局三胜
import random 

count_player = 0
count_computer = 0
valid_rounds = count_player + count_computer
total_rounds = 0

# 计数

while (count_player < 3) and (count_computer < 3) and (total_rounds < 10) :
# 错误写法：while (count_player < 3) or (count_computer < 3) or (total < 5) or (total_stop < 10) :
# and 遇假即假，全真最后一个真；or 遇真即真，全假最后一个假，因此想要表示'达到一个条件后就停止，应该是有一个假就退出，应用and'

    while True :
        player = input('你选择出：').strip()
        if player in ['石头','剪刀','布'] :   # 错误写法：'石头' or '剪刀' or '布'
           break
        else :
            print('不要捣乱啊喂！')
# 确认输入，获得玩家出拳

    computer = random.choice(['石头','剪刀','布'])

# 获得电脑出拳
    
    if player == computer :
        print ('平局')         # 排除平局
        total_rounds += 1

# 判断输赢

    elif player == '石头' and computer == '剪刀' :   # 第一组
        count_player += 1
        print(f'玩家出{player},电脑出{computer},玩家胜利')
        valid_rounds += 1
        total_rounds += 1

    elif player == '石头' and computer == '布' :     # 第二组
        count_computer += 1
        print(f'玩家出{player},电脑出{computer},电脑胜利')
        valid_rounds += 1
        total_rounds += 1

    elif player == '剪刀' and computer == '布' :    # 第三组
        count_player += 1
        print(f'玩家出{player},电脑出{computer},玩家胜利')
        valid_rounds += 1
        total_rounds += 1

    elif player == '剪刀' and computer == '石头' :  # 第四组
        count_computer += 1
        print(f'玩家出{player},电脑出{computer},电脑胜利')
        valid_rounds += 1
        total_rounds += 1

    elif player == '布' and computer == '石头' :    # 第五组
        count_player += 1
        print(f'玩家出{player},电脑出{computer},玩家胜利')
        valid_rounds += 1
        total_rounds += 1

    elif player == '布' and computer == '剪刀' :    # 第六组
        count_computer += 1
        print(f'玩家出{player},电脑出{computer},电脑胜利')
        valid_rounds += 1
        total_rounds += 1

# 判断输赢 :


if count_player == 3 :
        print(f'共 {valid_rounds} 局，玩家得到 {count_player} 分，电脑得到 {count_computer} 分')
        print('恭喜，是你赢了!')
elif count_computer == 3 :
        print(f'共 {valid_rounds} 局，玩家得到 {count_player} 分，电脑得到 {count_computer} 分')
        print('没关系，下次一定！')
else :
    print('哦不，大家似乎运气相同呢，快去买张彩票吧~')

# 先判断输赢再判断总局数，避免刚好十局结束结果没有得到结果

# 结束


'''
思路：
input:人的石头、剪刀、布
process:1.while true循环判断输入是否为三个，若是break,否则循环（边界条件）
2.computer:random.choice，获得
3.比较：if 6种，3种相同
4.while count_x < 3 or total < 5

'''