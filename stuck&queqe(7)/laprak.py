# membuat stack
from collections import deque
# stk = []

# # memasukan data 1
# stk.append(1)
# # masukan data 2
# stk.append(2)
# # memasukan data 3
# stk.append(3)
# # memasukan data 4
# stk.append(4)

# print(stk)


# # pop stack
# stk = [1, 2, 3, 4]
# print('data yang keluar', stk.pop())
# print(stk)
# print('data yang keluar', stk.pop())
# print(stk)


# # queque

nomortogel = deque([1, 2, 3, 4, 9])
nomortogel.append(6)
print(nomortogel)
print(nomortogel.popleft())
print(nomortogel.popleft())
print(nomortogel)
