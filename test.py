print("hello world!"),
print("你好，世界！"),
if False == True:
    print("True!"),
else:
    print("False!"),
# x = input("请输入，结束之后按下enter")
# print(x)
# print(x+x)
# print("GoodBye!")

animal = ["dog", "pig", "duck"]
animaltwo = []
for index in range(len(animal)):
    print(animal[index])
animaltwo = range(len(animal))
print(animaltwo)

flag = 1
row = 5
print("打印实心正方形")  # 打印实心正方形
for i in range(0, row):
    for j in range(0, row):
        print("*", end="  ")
    print("")
print("打印空心正方形")  # 打印空心正方形
for i in range(0, row):
    for j in range(0, row):
        if i == 0 or i == row - 1 or j == 0 or j == row - 1:
            print("*", end="  ")
        else:
            print(" ", end="  ")
    print("")
print("打印空心菱形")  # 打印空心菱形
for i in range(0, row):
    for j in range(0, row):
        if i > row // 2 and (j == row // 2 + row - 1 - i or j == row // 2 + i - row + 1):
            print("*", end=" ")
        elif i <= row // 2 and (j == row // 2 + i or j == row // 2 - i):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")
print("打印实心菱形")  # 打印实心菱形
for i in range(0, row):
    for j in range(0, row):
        if i > row // 2 and (j <= row // 2 + row - 1 - i and j >= row // 2 + i - row + 1):
            print("*", end=" ")
        elif i <= row // 2 and (j <= row // 2 + i and j >= row // 2 - i):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")

import random

x = random.random()
print(x)

print(r"a\na"), print("a\na")
print("hello time is {0:x>4d}:{1:x>4d}:{2:x>4d}".format(21, 22, 23))
print("hello time is %2d:" % 21, "%2d:" % 22, "%2d" % 23)
site = {"name": "好的搜索引擎", "url": "www.google.com"}
print("网站名：{name}, 地址 {url}".format(**site))
hi = """hello
here"""
print(repr(hi))
print(hi)
a = []
list.append(a, 1)
list.extend(a, [2, 3, 4, 5])
a.append(6)
print(a)
list.clear(a)
dict = {'Name': 'Zara', 'Name': 7, 'Class': 'First'}
print(len(dict))

import time

print(time.asctime(time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.mktime(time.localtime()))

import calendar

print(calendar.month(2018, 9))


def switchnum(a: object, b: object) -> object:
    "交换a和b的值"
    temp = a
    a = b
    b = temp
    return a, b


a = 1;
b = 2
print(a, " ", b)
print(switchnum(a, b))

globvar=0

def set_globvar_to_one():
    global globvar  # 使用 global 声明全局变量
    globvar = 1
    var=2
    print(globals())
    print(locals())


def print_globvar():
    print(globvar)  # 没有使用 global


set_globvar_to_one()
print(globvar)  # 输出 1
print_globvar()  # 输出 1，函数内的 globvar 已经是全局变量


try:
    fh = open("testfile", "w")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print("关闭文件")
        fh.close()
except IOError:
    print("Error: 没有找到文件或读取文件失败")


def mye( level ):
    if level < 1:
        raise Exception("Invalid level!")
        # 触发异常后，后面的代码就不会再执行
try:
    mye(0)            # 触发异常
except Exception as err:
    print(1,err)
else:
    print(2)


def fibinapi(num):
    '''返回给定的数字长度的分拨纳妾数列'''
    if num <= 2:
        raise Exception("num太少了，请输入一个大于等于3的数字")
    fibi = [0, 1]
    def nextfibi(a, b):
        return a+b
    i = 2
    while(i < num):
        fibi.append(nextfibi(fibi[i-2], fibi[i-1]))
        i += 1
    return fibi

print(fibinapi(10))


# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except ValueError as err:
        print ("参数没有包含数字\n", err)

# 调用函数
#temp_convert("xyz");

class myIter:
    def __init__(self, init):
        self.a = init

    def __iter__(self):
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

iterTest = myIter(2)
print(next(iterTest))
print(next(iterTest))
print(next(iterTest))
print(next(iterTest))
print(next(iterTest))

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(matrix)
newmatric = [[row[i] for row in matrix] for i in range(4)]
print([[row[i] for row in matrix] for i in range(4)])

print("Complex:%d"%10+"+%dj"%5)

class Classname:
    @staticmethod
    def fun():
        print('静态方法')

    @classmethod
    def a(cls, s):
        cls.s=s
        print('类方法%s'%cls.s)

    # 普通方法
    def b(self):
        print('普通方法')

Classname.fun()
Classname.a("呵呵")

C = Classname()
C.fun()
C.a("hehe")
C.b()


import datetime
meetday = datetime.datetime(2016, 6, 18, 13, 14, 0)
togetherTime = datetime.datetime.now() - meetday

print(togetherTime.days)


import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
    # print("matchObj.group(3) : ", matchObj.group(3))  IndexError: no such group
else:
    print("No match!!")

import re
s="i Am a gOod boy  baby!!"
result=re.findall(r'\b[a-z][a-zA-Z]*',s)
print(result)
print("小写字母开头的单词个数：",len(result))

import xml.sax

class MovieHandler ( xml.sax.ContentHandler ):
    def __init__(self):
        self.type = ''
        self.format = ''
        self.year = ''
        self.rating = ''
        self.description = ''
        self.current = ''

    #读取xml内容
    def characters(self, content):
        super().characters(content)
        if self.current == 'type':
            self.type = content
        elif self.current == 'format':
            self.format = content
        elif self.current == 'year':
            self.year = content
        elif self.current == 'rating':
            self.rating = content
        elif self.current == 'description':
            self.description = content

    def startElement(self, name, attrs):
        super().startElement(name, attrs)
        self.current = name
        if self.current == 'movie':
            print("*****Movie****")
            print("title:%s"%attrs['title'])


    def endElement(self, name):
        super().endElement(name)
        if self.current == 'type':
            print("type:"+self.type)
        elif self.current == 'format':
            print("format:"+self.format)
        elif self.current == 'year':
            print("year:" + self.year)
        elif self.current == 'rating':
            print("rating:" + self.rating)
        elif self.current == 'description':
            print("description:" + self.description)
        self.current = ''

parser = xml.sax.make_parser()
xmlhandler = MovieHandler()
parser.setContentHandler(xmlhandler)
parser.parse("movies.xml")

import unittest
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

class TestStatisticalFunctions( unittest.TestCase ):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, a)

unittest.main() # Calling from the command line invokes all tests

