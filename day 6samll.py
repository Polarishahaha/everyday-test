# 判断2到100内的素数
'''
思路:输入(2,101),处理过程:先用for遍历,然后对每一个看有没有除了1和自己以外的因子,如果有就break(离开当前循环进入下面的流程)
如果没有,则认为是
'''
count = 0

for N in range(2,101) :
    prime = True  # 定义素数

    for i in range(2,N) :
        if N % i == 0 :
            prime = False  # 判定为不是素数
            break  # 跳出循环  

# 注意:要跳出内循环,否则所有非因子的数都会让N输出一次,
# 因为每一个非因子得出一个prime = True,就会进入下面的双if循环,导致一直输出

    if prime == True  :  # 回到外循环,处理N
        count += 1
        print(f'{N:<8}',end='')
        if count % 7 == 0 :
            print()














