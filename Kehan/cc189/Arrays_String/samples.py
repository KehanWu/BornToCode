# coding=utf-8

# 定义一个function测试一个String是否都是unique characters
def is_unique(input_string):
    if len(input_string) > 256:
        return False
    hash_set = [False] * 256
    for character in input_string:
        ascii_number = ord(character)
        if hash_set[ascii_number]:
            return False
        else:
            hash_set[ascii_number] = True
    return True
# print(is_unique("yuweiyao"))

"""
如何不使用额外空间？
1. brute force，双重循环，每个都比较，n的平方
2. 排序，然后前后两两比较。排序的时间复杂度和空间复杂度参考：https://blog.csdn.net/hust_lmj/article/details/79058542
3. tricky case, 1个int是32位，两个int是64位，理论上4个int可以代替一个size=256的数组。或者假设这个字符串只有a~z，那么一个int就可以完成了.
    位运算的奇淫技巧：https://www.cnblogs.com/blknemo/p/14470610.html
"""

def is_unique_follow_up(input_string):
    checker = 0
    for i in input_string:
        offsite = ord(i) - ord('a')
        #检查checkr第offset位是否为1®
        if (checker & (1 << offsite) != 0):
            return False
        checker = checker | (1 << offsite)
    return True

print(is_unique_follow_up("abcde"))


