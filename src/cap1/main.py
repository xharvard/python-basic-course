#coding: utf-8

'''
Created on 2016年6月21日
第1章： 基础知识
1.1 安装python

- windows系统: 从官网下载安装包， 一步一步安装即可。
- Linux/unix系统: 通过系统的包管理器安装即可。 (Debian Linux: apt-get install python)

还有一些其他语言实现的python版本: Jython(java) 和 IronPython(C#)

1.2 python解释器 
安装好了，在命令行输入 python 即可进入python解释器模式，可以输入代码互动。

1.3 基础介绍 
- #: 表示注释

'''

#import math: 引入math模块，可以调用math的方法
import math
import cmath

# input():  获取用户输入  如果输入字符串，必须要加""号
#input("please input your name: ")

# raw_input():  获取用户输入, 输入原始的即可，推荐使用。
#raw_input("please input you address: ")

#str():  将值转换成字符串
print(str("333"))

#repr(): 与str()相反，以python的形式显示
print(repr("333"))

#长字符串:  使用三个引号代替普通引号。  可以跨多行
print '''
这是长字符串，
可以跨多行
'''
#原始字符串: 比如\n， 会被解释器当做换行。所以必须要用\(\\n)来转义。或者使用r'' 的形式
print "hello \n world"
print "hello \\n world"
print r'hello \n world \b' 
print r"hello \n world \t"

#Unicode字符串:  u'' 将字符串以Unicode存储，特别是中文字符的时候必须这么写
print u'中国'

print(math.pow(2, 3))
print(cmath.sqrt(4))