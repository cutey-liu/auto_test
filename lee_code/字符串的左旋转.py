"""
1.字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，
该函数将返回左旋转两位得到的结果"cdefgab"。
"""
def reverse_num(str,num):
    num = int(num)
    str_1 = str[0:num]
    str_2 = str[num:]
    # print(str_1)
    # print(str_2)
    str_3 = str_2 + str_1
    return (str_3)

if __name__ == '__main__':
    str = input("请输入要翻转的字符串：")
    num = input("请输入数字：")
    print(reverse_num(str, num))