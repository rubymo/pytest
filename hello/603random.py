# -*- coding: utf-8 -*-
# @Time    : 2021/10/19 14:33
# @Author  : Ruby
# @FileName: 603random.py
# @Software: PyCharm


price = 12  # 每次乘车票价
days = 22  # 每月乘车天数
times = 2  # 每天乘车次数
MountCost = 0  # 累计消费

# range 会产生从1开始到 days*times + 1 之间的连续整数
for i in range(1, days*times + 1):
    # f+{} 打印变量
    print(f'第{i}天')
    if MountCost < 100:
        MountCost = price + MountCost
    elif MountCost < 150:
        MountCost = price * 0.8 + MountCost
    elif MountCost < 300:
        MountCost = price * 0.5 + MountCost
    else:
        MountCost = MountCost + price
    print(f'当前累计消费{MountCost}')

print(MountCost)
