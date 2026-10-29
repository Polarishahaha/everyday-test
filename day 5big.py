N = input('请输入总样本数：')  # 总样本数为N
B = input('请输入批次大小：')  # 批次大小为B

# 明天写一些边界条件优化，包括：输入的不是数、输入的N和B<=0 等情况

ful_count = 0
left_count = 0  
remaining = N  # 赋初始值


while remaining >= B :  # 用while循环模拟分批过程
        remaining -= B
        ful_count = ful_count + 1
# 获得完整批次

if remaining > 0 :
    left_count = left_count + 1

total_count = ful_count + left_count

# 开始输出结果：

print('='*4,'','训练批次报告','','='*4)
print(f'总样本数    ：{N}')
print(f'批次大小    ：{B}')
print(f'总 batch 数 ：{total_count}')
print(f'完整 batch 数 ：{ful_count}')
print(f'最后 batch  ：{remaining}')
print(f'是否整除    ：{remaining == 0 }')
print('='*24)

# 完成 ^_^










