'''
1.选定 Pivote中心轴
2.将大于 Pivot的数字放在Pvot的右边
3.将小于 Pivot的数字放在 Pivote的左边
4.分别对左右子序列重复前三步操作
'''
def quick_sort():
    li = [8,1,5,6,2]
    pivote = li[0]

    for i in range(0,len(li)):
        r_sign = len(li) - i-1
        l_sign = i
        # print(r_sign)
        # print(l_sign)
        if li[r_sign] < pivote:

            i = i + 1


if __name__ == '__main__':
    quick_sort()




