# 练习用for和while循环写九九乘法表

# for循环

# 思路：for嵌套，实现j由i控制。注意：end='\t'空格

fact = 1
for i in range(1,10) :
    for j in range(i,10) :
        fact = i * j
        result = f'({i}*{j})={fact}'
        if j < 9 :
            print(f'{result:<12}',end='')
        else :
            print(f'({i}*{j})={fact}')
# 这好像是一个倒着的表？

# 给它正过来

fact = 1
for i in range(1,10) :
    for j in range(1,i+1) :
        fact = i * j 
        result = f'({i}*{j})={fact}'
        if j < i :
            print(f'{result:<12}',end='')
        else :
            print(f'{result:<12}')





