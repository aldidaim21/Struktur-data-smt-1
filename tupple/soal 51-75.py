# # 51-55
# tuple1 = 'ronaldo', 'the real', 'goat', 'mempunyai', 5, 'piala ucl'
# # 51
# print(tuple1.index('goat'))

# # 52
# print(tuple1.index('ronaldo'))

# # 53
# print((tuple1))

# # 54
# print(tuple1.index('piala ucl'))

# # 55
# print(tuple1.index(5))


# 56-58
# tuple3= (22,19,12,3,13,2,20)

# #56
# print(len(tuple3))

# #57
# print(max(tuple3))

# #58
# print(min(tuple3))


# # 59-61
# tup01 = (30, 41, 20, 12, 3)

# # 59
# print(len(tup01))

# # 60
# print(max(tup01))

# # 61
# print(min(tup01))

# # 62-65

# # 62
# ibudosen = ('Thiodas')
# ulbi = tuple(ibudosen)
# print(ulbi)

# # 63
# abcd = ('Bluelock')
# asepracing = tuple(abcd)
# print(asepracing)

# # 64
# jokowimabar = ('EVANGELION')
# prabowologin = tuple(jokowimabar)
# print(prabowologin)

# # 65
# bekasipanas = ('GABRIELLA')
# bandungtiris = tuple(bekasipanas)
# print(bandungtiris)


# ----------------------------------------------------
# 66-80
tup_odd = 1, 3, 5, 7, 9
tup_odd1 = 11, 13, 15, 17, 19

# 66
tup_odd2 = tup_odd + tup_odd1
print(tup_odd2)

# 67
print(2 in tup_odd)
print(2 in tup_odd1)

# 68
tup_odd3 = tup_odd, tup_odd1
print(tup_odd3)

# 69
print(tup_odd*3)

# 70
print(19 in tup_odd)
print(19 in tup_odd1)

# 71
print(tup_odd1*5)

# 72
print(tup_odd, tup_odd1)

# 73
tup_odd4 = tup_odd2 + tup_odd3
print(tup_odd4)

# 74
print('genap' in tup_odd)
print('genap' in tup_odd1)

# 75
for i in (1, 3, 5, 7, 9):
    print(i, end='')

# 76
for j in (11, 13, 15, 17, 19):
    print(j, end='')

# 77
print(tup_odd[1:5])

# 78
print(tup_odd[-5:-1])

# 79
print(tup_odd1[1:5])

# 80
print(tup_odd1[-5:-1])
