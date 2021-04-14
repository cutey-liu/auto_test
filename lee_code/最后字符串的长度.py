"""
题目描述
计算字符串最后一个单词的长度，单词以空格隔开。

输入描述:
输入一行，代表要计算的字符串，非空，长度小于5000。

输出描述:
输出一个整数，表示输入字符串最后一个单词的长度。
"""

def count_final_num():
    str = input("请输入字符串：")
    for i in range(1,len(str)+1):
        if str[-i] == " ":
            text = str[-1:-i:-1]
            lens = len(text)
            # print(text)
            # print(lens)
            break
        else:
            lens = len(str)
    return lens



if __name__ == '__main__':
    print(count_final_num())
