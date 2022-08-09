str1 = 'AA'
str2 = 'AA'

str1 = '.'*len(str1) + str1 + '.'*len(str1)
str2 = '.'*len(str2) \
    + str2 \
    + '.'*len(str2)

print(str1)
print(str2)
