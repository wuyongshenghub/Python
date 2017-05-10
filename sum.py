#encoding:utf-8

# 不使用关键字break/continue,跳出for或while循环

total = 0
isflag = True
while isflag:
    num = raw_input("pls your number: ")
    if num == 'pc' or  not num:
        isflag = False
    else:
        total = total + int(num) 
print "total is %s" %total
