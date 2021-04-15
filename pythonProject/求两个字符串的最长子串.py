'''
求两个字符串的最长子串'''
li = []
str_1 = "1111111111111ggggg11哈ha"
str_2 = "hah嘿ah嘿gggggg"
li = []
for i in range(0,len(str_1)+1): #1~18  2~19
    for j in range(1,len(str_1)):
        # print(str_1[i:j+1],end=" ")
        if  str_1[i:j+1] in str_2 and str_1[i:j+1]!="":
            li.append(str_1[i:j+1])
        elif str_1[0] in str_2 and str_1[i:j+1]!="":
            li.append(str_1[0])
try:
    res = max(li, key=len)
    print(res)
except:
    print("没有重复的子串")
