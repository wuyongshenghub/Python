#encoding:utf-8
# 逆转字符串——输入一个字符串，将其逆转并输出。


c = raw_input("input your character: ")
#print c
arr = list(c)
output = ''
for i in range(1,len(c)+1):
    output += c[-i]
print output 

