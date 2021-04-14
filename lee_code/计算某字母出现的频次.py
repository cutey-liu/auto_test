"""
题目描述
写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字母，然后输出输入字符串中该字母的出现次数。不区分大小写。

输入描述:
第一行输入一个由字母和数字以及空格组成的字符串，第二行输入一个字母。

输出描述:
输出输入字符串中含有该字符的个数。
"""

def count_num():
    str1 = input()
    str2 = input()
    count = 0
    str1 = str1.lower()
    str2 = str2.lower()
    for i in str1:
        if str2 == i:
            count = count+1
    print(count)


if __name__ == '__main__':
    count_num()