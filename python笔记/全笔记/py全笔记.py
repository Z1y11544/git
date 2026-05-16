# 一--初识python
# 3. Bug
# 遇到Bug怎么办
# 三个多：1）多看 2）多思考 3）多尝试、查询资料、记录
# 3.1 输入错误
# SyntaxError: invalid character  符号错误
# 注意：python中的符号都是用英文模式下的
# 3.2 缩进错误
# IndentationError: unexpected indent 缩进错误
# 3.3 语法错误
# SyntaxError: invalid syntax 语法错误 无效语法
# IndexError 索引错误
# 3.4 命名错误
# NameError 命名错误

# 5.输出函数print（）
# 1.输出多个值，或者多句话时，需要用逗号（英文模式）隔开
# 2.sep就是用来间隔多个值
# 3.end用来设定以...结尾，默认为换行符\n，可以切换成其他字符。
# print（字符串，end=“后面拼接的字符”）最后输出结果：第一个print中的字符串+后面拼接的词+第二个print中的字符串

# 二--变量
#  1.变量的作用
#  计算机中的存储空间
#  2.变量的格式
#  变量名 = 值
#  注意:=是赋值运算符,左右两边打上空格是为了代码的规范,美观性。
# num_1 = 3  # num_1就是一个变量，保存可乐的价格
# num_2 = 10 # num_2也是一个变量，保存冰淇淋的价格
# total = num_1 + num_2 # total也是一个变量，保存总价格
# print(total)
"""加上引号的话会打印引号里面的内容，没有引号就会别识别成变量名，
打印的是变量的值，如果该变量没有赋值，就会报命名错误"""
# 变量只有在赋值以后才会被创建，所以使用变量之前必须赋值

# a = 666
# 解释器做了两件事情
# 1）在内存中创建了一个666的数据
# 2）创建了一个变量a，把666这个数据保存到a变量去
# b = a
# print(b)
# print(a)  # 666
# a = 999  # 同一个变量可以反复赋值
# print(a)  # 999
#
# a = 6.66
# print(a)
# 同一个变量可以反复赋值
# 代码是从上往下运行的

# 2.标识符
# 2.1 含义：程序员定义的变量名，函数名
# 2.2 标识符的规定 （必须要遵守，不遵守就会报错）
# 1.标识符只能由字母、数字和下划线组成。
# python3可以用中文命名，但不推荐
# 标识符包含在（）内对标识符本身没有影响

# 2.标识符第一个字符必须不能是数字。

# 3.标识符不能与Python关键字重名。

# 4.严格区分大小写。

# 2.3 变量命名规则
# 1.见名知意
# 2.下划线分割法
# 3.大驼峰命名法
# 4.小驼峰命名法


# 3.数值类型
# 3.1 int 整型（常用）： 任意大小的整数
# num = 1
# 检测数据类型的方法 type（）
# print(type(num))
# 3.2 float浮点型:小数
# num2 = 1.5
# print(type(num2))
# 3.3 bool布尔型（重点），通常用于判断
# 固定写法，一个为True（真），一个为False（假）
# 注意；严格区分大小写
# 布尔值可以当作整型对待，True相当于整数1，False相当于整数0
# 3.4 complex 复数型(了解)
# 固定写法：z = a + bj ---a是实部，b是虚部，j是虚数单位
# print (type(5 + 6j))

# 4. 字符串str
# 特点：需要加上引号，单双都行，包含多行内容的时候也可以用三引号

# 5.格式化输出
# 5.1占位符
# 生成一定格式的字符串
# 5.2 %
# 1. %s 字符串
# name = 'bingbing'
# print('我的名字是：%s' % name)
# 注意：占位符只是占据位置，并不会被输出
# 2.%d 整数(常用)
# age = 18
# name = 'bingbing'
# print('我的名字：%s，年龄：%d' % (name, age))
# 3.%ad 整数（a是任意整数）
# 数字设置位数，不足前面补空白
# a = 123
# print("%06d"%a) #表示输出的整数显示位数，不足的话用0补全，超出或相同当前位数则原样输出
# 4. %f 浮点数(常用)
# a = 1.2
# print("%f" %a)
# 默认后六位小数，遵循四舍五入原则
# 5. %.af 浮点数
# a设置小数位数
# b = 2.34567
# print("%.7f" %b) #默认显示七位小数
# 6.%%
# print("我是%%的%%" % ())

# 5.3 f格式化
# 格式：f"{表达式}"
# name = "bingbing"
# age = 18
# print(f"我的名字是{name}，我今年{age}岁了")

# 三--运算符
# 1.算数运算符
# 1.1
# print(1/1)  # 注意：使用算数运算符/，商一定是浮点数
# a = 1/1
# print(type(a))
# 1.2 // 取整除 取商的整数部分，向下取整
# 向下取整不管四舍五入的原则，只要后面有小数，就忽略小数
# a = 5
# b = 2
# print(a//b)
# 1.3 % 取余数 只取余数部分
# print(a%b)
# 1.4  幂 m**n：m的n次方
# print(a**b)

# print(7.0//2)  #取整除若有浮点数，结果也会用浮点数
# 优先级排序：幂(最高优先级) > 乘、除、取余、取整数 > 加减
# print(3**2+5/2)

# 2. 赋值运算符
# 2.1 =
# num1 = 5
# num2 = 8
# 将一个变量的值赋给另一个变量
# num3 = num1
# print(num3)
# num4 = num2
# print(num4)
# 将运算的值赋给变量
# total = num3 + num4
# print(total)

# 2.2 +=
# a = 1
# print(a)
# a = a + 1
# a += 1    #等效于a = a + 1
# print(a)

# n1 = 99    #成本
# n2 = 66    #利润
# n1 = n1 + n2    #售价
# n1 += n2    #等效于 n1+n2 = n1
# print(n1)

# 2.3 -=
# b = 1
# print(b)
# b = b-1
# b -= 1
# print(b)
# 赋值运算符必须连着写，中间不能有空格，否则会报错
# n = 5
# n += 10    #n没有被提前定义，所以不能参与加法运算
# print(n)
# print(10+=3)    #纯数字也不能使用，报错语法错误，因为赋值运算符是针对变量存在的

# 3.input()输入函数
# input(prompt)  #prompt是提示，会在控制台中显示
# name = input("请输入姓名：")
# print(name)

# pwd = input("请输入你的密码：")
# print(pwd)

# 4.转义符
# 4.1 \t 制表符  通常表示四个字符，也能缩进
# print('sixs\tar')
# print("姓名\t年龄\t电话")
# 4.2 \n 换行符 表示将当前位置移到下一行开头
# print("哈哈\n嘻嘻")
# 4.3 \r 回车 表示将当前位置移到本行开头
# print("哈哈哈\r嘻嘻嘻")
# 4.4 \\ 反斜杠符号
# print(r'sixs\\tar')        # r原生字符，默认取消转义

# 四--if判断
# 1. if判断基本格式
# if 要判断的条件：
#   条件成立要做的事情
# age = 17
# if age < 18:
#     print('未成年不能上网')
# note = float(input('请输入成绩：'))
# if note == 100:
#     print('你真棒！')
# if note == 60:
#     print('还要继续加油哈')

# 2.运算符
# 2.1 比较运算符
# == 比较的是两个变量是否相等，相等的话就返回为True(真)，不相等的话返回为False(假)
# != 比较的是两个变量是否相等，不相等的话就返回为True(真)，相等的话返回为False(假)
# a = 666
# b = 999
# print(a > b)
# if a < b:
#     print("a小于b")
# 2.2 逻辑运算符
# and 左右两边都符合才为真
# a = '哈哈'
# b = '嘿嘿'
# if a =='哈哈' and b == '嘿嘿':
#     print('a和b都在笑')

# or 左右只需要一边都符合就为真
# fruit = "水蜜桃"
# if fruit == "苹果" or fruit == "水蜜桃" :
#     print("带回来了水果")

# not 表示相反的结果
# print(not 3>9)

# 2.3 三目运算
# 基本格式 ：为真结果 if 判断条件 else 为假结果
# a = 5
# b = 8
# print("a小于等于b") if a <= b else print('a比b大')

# 3.if-else
# 3.1 if-else（二选一）基本格式:
# if 条件:
#     满足条件要做的事
# else:     #else后面不需要添加任何条件
#     不满足条件要做的事

# 3.2 if-elif（多选一）结构:
# if 条件1:
#     满足条件1要做的事
# elif 条件2:
#     满足条件2要做的事
# elif 条件3:
#     满足条件3要做的事
# else可以表示所有条件都不符合的这样一个情况

# 4.if 嵌套(if里面有if)
# if 条件1:
#     事情1
#     if 条件2:
#         事情2
# else:
#     不满足条件做的事情
# 注意:外层，内层的if判断都可以是if-else

# ticket = True
# temp = 36.5  #正常人体温为36.3
# if ticket == True:
#     print('可以进站了-->',end ="")
#     if 35.8 <= temp <= 37.2 :
#         print('体温正常,安心回家')
#     else:
#         print('体温异常,需要隔离')
# else :
#     print('没票不能进站')

# 五--循环语句
# 1. 循环语句
# 重复执行
# 2.while循环
# 2.1基本格式
# 定义初始变量
# while 条件:
#     循环体(条件满足时段做的事情)
#     改变变量

# 死循环:
# while True:
#     循环体(要循环做的事情)

# i = 1   #定义一个初始值，记录循环的次数，i = 1表示从第一次开始
# while i <= 100:
#     print('好好学习,天天向上')
#     i += 1
# 注意:如果没有改变变量,条件一直满足,就会一直循环下去,一直执行。
# 死循环:
# while True:  # 条件只写True,说明一直为真,就会一直执行,从而形成一个死循环
#     print('你好呀')

# 2.2 while循环应用:计算1+2+3...+100的和
# i = 1
# s = 0
# while i <= 100:
#     s += i
#     i += 1
# print(f'计算结果是{s}')

# 3. while循环嵌套
# 3.1含义
# 一个while循环里面还有一个while循环
# 3.2基本格式
# while 条件1:
#     循环体1
#     while 条件2:
#         循环体2
#         改变变量2
#     改变变量1
# 注意:缩进决定层级,严格控制缩进,最好自动缩进

# 4. for 循环
# 4.1基本格式:
# for 临时变量 in 可迭代对象:
#     循环体
# str = 'hellopython'
# 可迭代对象就是去遍历取值的整体,这里的话只需要记住字符串就是可迭代对象
# for i in str:
#     print(i)

# 4.2 range()
# 用来记录循环次数相当于一个计数器
# range(start,stop,step)
# for i in range(1,6):    # 从1开始,从6-1结束,遵循包前不包后原则
#     print(i)
# range()里面只写一个数,这个数就是循环的次数,默认从零开始
# 写两个数,前面的表示开始位置,后面的数字表示结束位置

# 4.3 for循环应用:计算1+2+3+...+100
# s = 0
# for i in range(100):
#     i += 1
#     s += i
# print(f'结果为{s}')

# 5. break和continue
# 都是专门在循环中使用的关键字
# i = 1
# if i <= 5:
#     print('我在吃苹果')
#     break
# 报错,break和continue只能放在循环内
# 5.1 break
# 作用:某一条件满足时,退出循环
# i = 1
# while i <=5:
#     print(f'小红在吃第{i}个苹果')
#     if i == 3:
#         print('吃饱了,不吃了')
#         break
#     i += 1

# 5.2 continue
# 作用:退出本次循环,下一次循环继续执行
# i = 1
# while i <= 5:
#     print(f'小明在吃第{i}个苹果')
#     if i == 3:
#         print('有虫子不吃了')
#         # 在continue之前一定要修改计算器,否则会陷入死循环
#         i += 1
#         continue
#     i += 1

# 六-- 字符串&列表
# 1.字符串编码
# 本质上就是二进制数据与语言文字的一一对应关系
# 1.1 Unicode :所有字符都是两个字节,
# 好处:字符与数字之间的转换速度快一些
# 坏处:占用空间大
#
# 1.2 UTF-8:精准,不同的字符用不同的长度表示
# 优点:节省空间
# 缺点:字符与数字的转换速度较慢,每次都需要计算字符需要多少个字节来表示.

# 1.3 字符串编码转换
# a = 'hello'
# print(a,type(a))
# a1 = a.encode()
# print('编码后',a1)
# print(type(a1))  #bytes,以字节为单位进行处理
# a2 = a1.decode()
# print(a2)
# print(type(a2))
# 注意 : 对于bytes,只需要知道它跟字符串类型相互转换
# st = "我在学习python"
# st1 = st.encode('utf-8')
# print(st1, type(st1),sep = '\n')
# st2 = st1.decode('utf-8')
# print(st2, type(st2),sep = '\n')

# 2.字符串常见操作
# 2.1 + 字符串拼接
# print(10+10)   # 20,整型相加,+是算数计算符
# print("10"+"10")    # 1010,字符串相加,+是字符串拼接
# name1 = '六星'
# name2 = '教育'
# print(name1+name2)
# print(name1,name2 ,sep = "")

# 2.2 * 重复输出
# print('好好学习,天天向上\n'*5)
# 注意: 需要输出多少次就在*后面写多少
# print('&\t'*10)

# 2.3 成员运算符
# 作用 : 检查字符串中是否包含了某个子字符(即某个字符或多个字符)
# in :如果包含的话返回True,不包含返回False
# not in : 如果不包含的话返回True,包含返回False
# name = 'bingbing'
# print('b'in name)
# print('a' in name)
# print('b' not in name)
# print('a'  not in name)

# 2.4 下标
# python中下标从0开始
# 作用 : 通过下标快速找到对应的数据
# 格式 : 字符串[下标值]
# name = 'sixstar'
# 从左往右数,下标从0开始
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[6])
# print(name[7])   #取值不要超出下标范围
# 从右往左数，下标从-1开始。
# print(name[-1])

# 2.5 切片
# 含义 : 绝对操作对象截取其中一部分的操作
# 语法 : [开始位置:结束位置:步长]
# 包前不包后原则
# st = 'abcdefghijk'
# print(st[0:4])      # abcd
# print(st[4:7])      # efg
# print(st[3:])       # defghijk --下标为3之后的全部截取到
# print(st[:7])       # abcdefg --下标为7之前的全部截取到，不包含7
# 从右往左
# print(st[-1:])      # k
# print(st[:-1])      # abcdefghij
# print(st[-1:-5])
# 步长:表示选取间隔,不写步长,则默认是一
# 步长的绝对值大小决定切取的间隔,正负号决定切取方向
# 正数表示从左往右取值,负数表示从右往左
# st = 'abcdefghijk'
# print(st[-1::1])      # k
# print(st[-1::-1])     # kjihgfedcba
# print(st[-1:-5:-1])   # kjih
# print(st[0:7:3])      # aceg

# 3. 字符串常见操作
# 3.1 查找
# 3.1.1find: 检测某子字符串是否包含在字符串中,如果在就返回这个子字符串的下标,否则就返回-1
# find(子字符串,开始位置下标,结束位置下标)
# 注意:结束位置下标可以省略,表示在整个字符串中查找
# name = 'bingbing'
# print(name.find('i'))     # 1--第一个i的下标为1
# print(name.find('bing'))  # 0--检测到第一个bing,b的下标为零
# print(name.find('b',3))   # 4
# print(name.find('b',5))   # -1--超出范围,不包含返回-1
# print(name.find('b',3,5)) # 4--在下标3-5位置范围内查找
# 包前不包后
# print(name.find('b',3,4)) #-1

# 3.1.2 index():检测某子字符串是否包含在字符串中,如果在就返回这个子字符串的下标,否则就返回报错
# index(子字符串,开始位置下标,结束位置下标)
# 注意: 开始和结束位置下标可以省略,表示在整个字符串中查找
# name = '我命由我不由天'
# print(name.index("命"))       # 1
# print(name.index('命',2))     # 报错,从下标2开始找,没有找到
# print(name.index('命',1,3))   # 1
# 同样包前不包后
# 和find的区别:find没找到,返回-1,index没找到就会报错

# 3.1.3 count():返回某个子字符串在整个字符串中出现的次数,没有就返回0
# count(子字符串,开始位置下标,结束位置下标)
# 注意: 开始和结束位置下标可以省略,表示在整个字符串中查找
# name = 'bingbing'
# print(name.count('b'))          # 2
# print(name.count('a'))          # 0
# print(name.count('b',1))        # 1
# print(name.count('b',1,3))      # 0
# print(name.count('b',1,4))      # 0
# 同样包前不包后

# 3.2 判断
# 3.2.1 startswith():是否一某个字符串开头,是--True,不是--False,
#                    如果设置开始和结束位置下标,则在规定范围内检测
# starswith(子字符串,开始位置下标,结束位置下标)
# st = 'sixstar'
# print(st.startswith('six'))        # True
# print(st.startswith('sex'))        # False
# print(st.startswith('s',3,6))      # True
# print(st.startswith('s',2,6))      # False

# 3.2.2 endswith():是否一某个字符串结尾,是--True,不是--False,
#                    如果设置开始和结束位置下标,则在规定范围内检测
# endswith(子字符串,开始位置下标,结束位置下标)
# st = 'sixstar'
# print(st.endswith('er'))           # False

# 3.2.3 isupper():检测字符串中的字符是都为大写,是的话返回True
# st = 'sixstar'
# print(st.isupper())                # False
# print("SIX".isupper())             # True

# 3.3 修改元素
# 3.3.1 replace():替换
# replace(旧内容,新内容,替换次数)
# 注意:替换次数可以省略,默认全部替换
# name = "好好学习,天天向上"
# print(name.replace("天","时"))
# print(name.replace("天","时",1))

# 3.3.2 split():指定分隔符来切割字符串
# st = "hello,python"
# print(st.split(","))         # ['hello', 'python']--以列表的形式返回
# 如果字符串中不包含分割内容，就不进行分割，会作为一个整体
# print(st.split("a"))         # ['hello,python']
# print(st.split("o"))         # ['hell', ',pyth', 'n']
# print(st.split("o",1))       #['hell', ',python']--指定只分割一次

# 3.3.3 capitalize():第一个字符大写,其他都小写
# st = "bingBing"
# print(st.capitalize())         # Bingbing

# 3.3.4 lower():大写字母转为小写
# st = "bingBing"
# print(st.lower())              # bingbing

# 3.3.5 upper():小写字母转为大写
# st = "bingBing"
# print(st.upper())              # BINGBING

# 4.列表
# 基本格式:
# 列表名 = [元素1,元素2,元素3...]
# 注意:
# 所有元素防止中括号内,元素与元素之间用,隔开
# 元素之间的数据类型可以各不相同
# li = [1,2,'a',4]
# print(li,type(li))
# 列表也可以进行切片操作
# print(li[0:3])
# 列表也是可迭代对象,可以for循环遍历取值
# for i in li:
#     print(i)

# 5. 列表的常见操作
# 5.1 添加元素
# append()  extend()  insert()
# li = ["one","two","three"]
# li.append("four")          # append整体添加
# li.extend("four")          # extend 分散添加,将另一个类型的元素逐一添加
# li.insert(3,"four")        # 在指定位置插入元素
# li.insert(0,"four")        # 指定位置如果有元素,那就会原有元素后移
# li.insert("four")          # 报错,没指定下标
# print(li)
# li =[1,2,3]
# li.append(4)
# li.extend(4)                 # 报错,要用可迭代对象
# li.insert(3,4)
# print(li)

# 5.2 修改元素
# 直接通过下标就可以进行修改
# li = [1,2,3]
# li[1] = "a"
# print(li)

# 5.3 查询
# 5.3.1 in :判断元素是否存在列表中，如果存在就返回True，不存在就返回False
#       not in ：判断元素是否不存在列表中，如果不存在就返回True，存在就返回False
# li=['a','b','c','d']
# print('e' in li)

# 用户输入昵称,昵称重复则不能使用
# 定义一个列表,保存已经存在的昵称
# name_list = ['bingbing','susu','ziyi']
# while True:
#     name = input("请输入你的昵称：")
    # 判断昵称是否存在
    # if name in name_list:
    #     print(f"您输入的昵称{name}已经存在了哦")
    # else :
    #     print(f"昵称{name}已经被您使用")
    #     # 把昵称新增到列表
    #     name_list.append(name)
    #     print(name_list)
    #     break

# 5.3.2   index：返回指定数据所在的下标，如果查找的数据不存在就会报错
#         count：统计指定数据在当前列表出现的次数
# 字符串中的用法相同

# 5.4 删除元素
# del
li = ['a','b','c','d']
# del li           # 删除列表
# del li[2]        # 根据下标删除
# print(li)

# pop:删除指定指定下标的数据,python3版本默认删除最后一个元素
# li = ['a','b','c','d']
# li.pop()           # 默认删除最后一个元素
# li.pop('b')        # 报错,不能指定元素删除,只能根据下标删除
# li.pop(5)          # 下标不能超出范围
# li.pop(2)
# print(li)

# remove:根据指定元素的值进行删除
# li = ['a','b','c','d','b']
# li.remove('d')
# li.remove('t')       # 报错,列表中不存在这个元素
# li.remove('b')       # 默认删除最开始的指定元素
# print(li)

# 5.5 排序
# sort: 将列表按特定顺序重新排列,默认从小到大
# reverse: 倒序,将列表倒置(反过来)
# li = [1,5,3,2,4]
# li.sort()              #按照从小到大的顺序排列
# li.reverse()           # 倒序
# print(li)

# 5.6 列表推导式
# 基本写法:
# 格式一:[表达式 for 变量 in 列表]
# 注意: in 后面不仅可以放列表,还可以rnage(),放可迭代对象
# li = [1,2,3,4,5,6]
# [print(i) for i in li]         # 前面的i是表达式
# li = []
# for i in range(1,6):
#     # print(i)
#     li.append(i)
# print(li)

# [li.append(i) for i in range(1,6)]
# print(li)

# 格式二:[表达式 for 变量 in 列表 if 条件]
# 把奇数放进列表里面
# li = []
# for i in range(1,11):
#     if i%2 != 0:
#         print(i)
#         li.append(i)
# print(li)

# li = []
# [li.append(i) for i in range(1,11) if   i%2 != 0]
# print(li)

# 5.7 列表嵌套
# 含义:一个列表表面里面又有一个列表
# li = [1,2,3,[4,5,6]]          # [4,5,6]是里面的列表
# print(li[3])                  # 取出里面的列表
# print(li[3][0])               # 取出内列表的下标为0的元素

# 七--元组&字典&集合
# 1.元组 tuple
# 基本格式:元组名 = (元素1,元素2,元素3...)
# 所有元素包含在小括号内, 元素与元素之间用,隔开, 不同元素也可以是不同的数据类型
# tua = (1,2,3,"a",[1,2,3])
# print(type(tua))              # "tuple"
# tua = ()                      # 定义空元组
# print(type(tua))
# tub = (1,)                    # 只有一个元素的时候,末尾必须要加上,否则返回唯一值的数据类型
# print(type(tub))

# 1.2元组与列表的区别:
#     1.元组只有一个元素时必须加, 列表不需要
# li = [1]
# print(type(li))
#     2.元组只支持查询操作,不支持增删改操作
# li = [1,2,3]
# li[1] = "a"
# print(li)
# tua = (1,2,3)
# print(tua[-1])               # 元组也有下标,从左往右从零开始
# tua[2] = "a"                 # 报错,元组不支持修改操作
# count()、index()、len()跟列表的用法相同
# print(tua.index(2))
# print(tua.count(1))
# print(len(tua))
# print(tua[1:])

# 1.3 应用场景
# 函数的参数与返回值
# 格式化输出后面的()本质上就是一个元组
# name = "bingbing"
# age = 18
# print("%s的年龄是%d" % (name, age))
# info = (name, age)
# print(type(info))
# print("%s的年龄是%d" % info)
# 数据不可以被修改，保护数据的安全

# 2.字典  dict
# 2.1 基本格式:字典名 = {键1:值1,键2:值2...}
# 键值对形式保存,键和值之间用:隔开,每一个键值对之间用,隔开
# dic = {"name":"bingbing",'age':18}
# print(type(dic))
# 字典中的键具有唯一性,但是值可以重复
# dic2 = {"name":"bingbing","name":"susu"}     # 不会报错,键名重复前面的值会被后面的值覆盖
# print(dic2)
# dic3 = {"name":'bingbing',"name2":"bingbing"}
# print(dic3)

# 2.2 字典常见操作
# 2.2.1 查看元素
# 变量名[键名]
# dic = {"name":"bingbing",'age':18}
# print(dic[2])                 # 不可以根据下标.字典中没有下标,查找元素需要根据键名,键名相当于下标
# print(dic["age"])             # 18
# print(dic['six'])             # 报错键名不存在
# 变量名.get(键名)
# dic = {"name":"bingbing",'age':18}
# print(dic.get("name"))          # bingbing
# print(dic.get("tel"))           # None,键名不存在,返回None
# print(dic.get("tel","不存在"))   # 不存在,如果键名不存在,返回自己设置的默认值

# 2.2.2 修改元素
# 变量名[键名] = 值
# dic = {"name":"bingbing",'age':18}
# dic["age"] = 20                 # 列表通过下标修改,字典通过键名修改
# print(dic)

# 2.2.3 添加元素
# 变量名[键名] = 值
# 注意:键名存在就修改,不存在就新增
# dic = {"name":"bingbing",'age':18}
# dic["tel"] = 1244668            # 没有tel键,新增进字典
# print(dic)
# dic['tel'] = 12345              # 此时已经有tel键了,,修改tel对应的值
# print(dic)
# dic["remark"] = "在线征婚"
# print(dic)

# 2.2.4 删除元素
# del
# 删除整个字典 del 字典名
# dic = {"name":"bingbing",'age':18}
# del dic
# print(dic)                      # 报错,已经被删除了,找不到这个字典
# 删除指定键值对,键名不存在就会报错  del 字典名[键名]
# dic = {"name":"bingbing",'age':18}
# del dic['age']
# del dic['tel']                  # 没有指定的键就会报错
# print(dic)

# clear():清空整个字典里面的东西但保留这个字典
# dic = {"name":"bingbing",'age':18}
# dic.clear()
# dic["age"] = 18
# print(dic)

# pop() 删除指定键值对,键不存在就会报错
# dic = {"name":"bingbing",'age':18}
# dic.pop("age")
# dic.pop("tel")                  # 报错，不存在键名
# dic.pop()                         # 报错,没有指定键名
# dic.popitem()
# print(dic)

# 2.3 字典常见操作2
# 2.3.1 len()求长度
# dic = {"name":"bingbing",'age':18,"tel":'123'}
# print(len(dic))                 # 3,字典中有3个键值对
# li = [1,2,3,4]
# print(len(li))
# st = "hello"
# print(len(st))
# 2.3.2 keys():返回字典里面包含的所有键名
# dic = {"name":"bingbing",'age':18}
# print(dic.keys())               # dict_keys(['name', 'age'])
# for循环取出键名
# for i in dic.keys():
#     print(i)

# 2.3.3 values():返回字典里面包含的所有值
# dic = {"name":"bingbing",'age':18}
# print(dic.values())
# for i in dic.values():
#     print(i)

# 2.3.4 item(): 返回字典里面所包含的所以键值对，键值对以元组形式
# dic = {"name":"bingbing",'age':18}
# print(dic.items())
# for i in dic.items():
#     print(i,type(i))

# 2.4 字典的应用场景
# 使用键值对,存储描述一个物体的相关信息

# 3. 集合
# 3.1 基本格式:集合名 = {元素1,元素2,元素3...}
# s1 = {1,2,3}
# s1 = {}                          # 定义空字典
# s1 = set()                       # 定义空集合
# print(s1,type(s1))
# 3.2 集合具有无序性
# s1 = {'a','b','c','d','e','f'}
# print(s1)                        # 每次运行都不一样
# s2 = {1,2,3,4,5,6}
# print(s2)                        # 数字运行结果一样

# 集合无序的实现方法涉及hash表
# print(hash('a'))
# print(hash('b'))
# print(hash('c'))
# 每次运行结果都不同，hash值不同，那么在hash表中的位置也不同，这就实现了集合的无序性
# print(hash(1))
# print(hash(2))
# print(hash(3))
# python中int整型的hash值就是他本身,在hash表中的位置不会发生变化,固顺序不变
# print(hash("1"))
# print(hash("2"))
# print(hash("3"))
# print(hash("4"))
# 用引号括起来整型变成了字符串类型,所以hash值会变
# 无序性:不能修改集合中的值

# 3.3 集合具有唯一性可以自动去重
# s1 = {1,2,4,6,3,2,4}
# print(s1)

# 3.4 集合的常见操作
# 3.4.1 添加元素
# add ：添加的是一个整体
# s2 = {1,2,3,4}
# print(f"原集合:{s2}")
# 集合的唯一性,决定了如果需要添加的元素在原集合已经存在,就不进行任何操作
# s2.add(1)
# s2.add(5)
# s2.add(5,6)           # 报错,一次只能添加一个元素
# s2.add((5,6))
# print(f"现集合:{s2}")

# update:把传入的元素拆分,一个个放进集合中(要可迭代对象)
# s2 = {1,2,3,4}
# print(f"原集合:{s2}")
# s2.update([5,6,7])     # 元素必须是能够被for循环取值的可迭代对象
# print(f"添加后{s2}")

# 3.4.2 删除元素
# remove : 选择删除的元素,如果集合中有就删除，没有就会报错
# s2 = {1,2,3,4}
# s2.remove(3)
# s2.remove(5)          # 报错,集合中没有5这个元素
# print(s2)

# pop:对集合进行无序排列,然后删除左边的第一个元素删除
# s2 = {'a','b','c','d'}
# print("原集合",s2)
# s2.pop()               # 默认删除根据hash表排序的第一个
# print("删除后",s2)

# discard 需要选择要删除的元素,有的话就删除,没有的话不变
# s2 = {1,2,3,4}
# print("原集合",s2)
# s2.discard(3)
# s2.discard(7)
# print("删除后",s2)

# 4. 交集和并集
# 4.1 交集&
# 含义: 共有的部分
# a = {1,2,3,4}
# b = {3,4,5,6}
# b = {5,6,7,8}          # 没有共有的部分返回空集set()
# print(a & b)
# s1 = {'a','b','c'}
# s2 = {'c','d'}
# print(s1 & s2)

# 4.2 并集 |
# 含义 : 把所有的元素都放在一起,重复的不算(集合的唯一性)
# a = {1,2,3,4}
# b = {5,6,7,8}
# print(a | b)
# l = a | b
# print(type(l))      # set

# 八 -- 类型转换&深浅拷贝
# 1.类型转换
# 1.1 int():转换为一个整数,只能转换由纯数字组成的字符串
# float -> int
# a = 1.2
# print(type(a))
# b = int(1.2)
# print(b,type(b))      # 1
# print(int(1.8))
# 浮点型强制转型会去掉小数点及后面的数值，只保留整数部分
# str -> int
# a = int("123")
# print(a,type(a))
# print(int("bingbing"))     # 报错
# 如果字符串中有数字和正负号以外的字符,就会报错
# print(int("-10"))
# +/-写在前面表示正负号,不可以写在后面
# print(int("10+"))            # 报错

# 用户从控制台输入,判断年龄
# age = int(input("请输入您的年龄:"))  # input默认输入str
# print(type(age))
# if age >= 18:
#     print("成年了")

# 1.2 float() : 转换为一个小数
# print(float(11))        # int转换为float，会自动添加小数
# print(float(-11))
# print(float("11.345"))
# print(float("10-"))     # 如果字符串中有正负号,数字和小数点以外的字符,则不支持转换

# 1.3 str() : 转换为字符串类型,任何类型都可以转换成字符串类型
# n = 100
# print(type(n))       # <class 'int'>
# n2 = str(n)
# print(n2,type(n2))   # 100 <class 'str'>
# st = str(-1.80)      # 保留一位小数
# print(st,type(st))   # float转换成str会取出末位0的小数部分
# li = [1,2,3]
# st = str(li)
# print(st,type(st))

# 1.4 eval() : 用来执行一个字符串表达式,并返回表达式的值
# print(10+10)
# print("10"+"10")
# print(eval("10"+"10"))
# print(eval("10+10"))    # 20，执行运算，并返回运算值
# print(eval("10+'10'"))  # 报错,整型和字符串不可以相加
# eval()可以实现list、dict、tuple和str之间的转换
# str -> list
# st1 = "[[1,2],[3,4],[5,6]]"
# print(type(st1))
# li = (eval(st1))
# print(li,type(li))

# str -> dict
# st2 = "{'name':'bingbing','age':'18'}"
# dic = eval(st2)
# print(dic,type(dic))
# eval() 非常强大,但是不够安全,容易被恶意修改数据,不建议使用

# 1.5 list() :将可迭代对象转换成列表
# 支持转换为list的类型: str、tuple、dict、set
# str -> list
# print(list('abcdefg'))
# print(list(12345))         # 报错

# tuple -> list
# print(list((1,2,3,4)))

# dict -> list
# print(list({'name':'bingbing','age':18}))
# 字典转换列表，会取键名作为列表的值

# set -> list
# print(list({1,2,3,4,5}))
# 基本转换成列表，先会去重，再转换

# 2. 深浅拷贝
# 2.1 赋值
# li = [1,2,3,4,5]
# print("前li",li)
# li2 = li          # 将li直接赋值给li2
# print("前li2",li2)
# 给li列表新增元素
# li.append(6)
# print("li",li)
# print("后li2",li2)
# 赋值: 等于完全共享资源,一个值的改变会另一个值也会共享

# 2.2 浅拷贝
# 会创建新的对象,拷贝第一层的数据，嵌套层会指向原来的内存地址
# import copy           # 导入cope模块
# li = [1,2,3,[4,5,6]]       # 定义一个嵌套列表
# li2 = copy.copy(li)
# print(li)
# print(li2)
# 查看内存地址 id（）
# print("li内存地址",id(li))
# print("li2内存地址",id(li2))
# 内存地址不一样，说明不是同一个对象
# li.append(8)
# print(li)
# print(li2)
# 往嵌套列表添加元素
# li[3].append(7)
# print(li)
# print(li2)
# print("li[3]内存地址",id(li[3]))
# print("li2[3]内存地址",id(li2[3]))
# 外层的内存地址不同，但是内层的内存地址相同

# 优点 : 拷贝速度快,拷贝效率高

# 2.3 深拷贝 (数据完全不共享)
# 外层的对象和内部元素都拷贝了一遍
# import copy   # 导入copy模块
# li = [1,2,3,[4,5,6]]
# li2 = copy.deepcopy(li)     # 深拷贝
# print("li:",li,id(li))
# print("li2:",li2,id(li2))
# li.append(8)
# print(li)
# print(li2)
# 在嵌套列表添加元素
# li[3].append(7)
# print(li,id(li[3]))
# print(li2,id(li2[3]))
# 深拷贝数据变化只影响自己本身,跟原来的对象没有关联

# 3.可变类型
# 含义 : 变量对应的值可以修改,但是内存地址不变
# 常见的可变类型 : list,dic,set
# li = [1,2,3,4]
# print("li的原内存地址",id(li))
# li.append(5)
# print(li)
# print("li的现内存地址",id(li))
# dic = {"name":"bingbing","age":18}
# print(dic,id(dic))
# dic["name"] = "susu"   # 修改元素
# print(dic,id(dic))

# set = {1,2,3,4,5}
# print(set,id(set))
# set.remove(3)     # 删除元素
# print(set,id(set))

# 4.不可变对象
# 含义 : 变量对应的值不能被修改,如果修改就会生成一个新的值从而分配新的内存空间
# n = 10      # 整型
# print(n,"原地址:",id(n))
# n = 15
# print(n,"修改后:",id(n))
# 内存地址不一样：修改n的值就会生成新的值，重新赋值给n

# st = "hello"    # 字符串
# print(st,id(st))
# st = "bingbing"
# print(st,id(st))

# tua = (1,2,3)
# print(tua,id(tua))
# # 不支持下周删除和修改操作
# tua = ('a','b','c')
# print(tua,id(tua))

# 注意: 深浅拷贝只针对可变对象

# 九-- 函数基础
# 1.函数
# 1.1 含义:将独立的代码块组织成一个整体,使其具有特殊功能的代码集,在需要的时候再去调用即可
# 1.2 作用: 提高代码的重用性,使整体代码看上去更加简练
# 1.3 基本格式:
# ①定义函数
# def 函数名():
#     函数体
# ②调用函数
# 函数名()
# def login():
#     print("这是登录函数")
#     print("_________")
# login()
# login()
# 调用几次,函数里面的代码就会运行几次,每次调用的时候,函数都会从头开始运行

# 编写一个打招呼的函数并调用它
# def dazhaohu():
#     print("你好")
#     print("bingbing")
#     print("18岁")
# 调用函数前必须保证函数已经存在
# dazhaohu()

# 2. 返回值 return
# 函数执行结束后，最后调用的一个结果
# 作用:
# ① return会给函数执行者返回值
# def buy():
#     return "一桶水果茶"
# buy()
# print(buy())
# 2.函数中遇到了return，表示函数结束，不继续执行
# def buy():
#     return "一桶水果茶",20   # return返回多个值,以元组的形式
#     # return 20            # return下面的代码不会执行
# print(buy())
# 返回值的三种情况总结
#      1.一个返回值也没有,返回的结果是None
#      2.一个返回值,就把值返回给调用者
#      3.多个返回值,以元组的形式返回给调用者
# return和print的区别:
#     1.return表示此函数结束了
# def funa():
    # return 123
    # print(123)
    # print(456)
# funa()
#     2.return是返回计算值,print是打印结果
# def add():
#     a = 1
#     b = 2
#     print(a + b)
# add()

# 3.参数
# 3.1 形参和实参
# 定义格式:
# def 函数名(形参a,形参b):
#     函数体
#     ...(如a=1,b=2)
# 调用格式:
# 函数名(实参1,实参2)
# def add(a,b):
#     return a+b
# print(add(12,13))

# 3.2 函数参数
# 1. 必备参数(位置参数)
# 含义:传递和定义参数的顺序及个数必须一致
# 格式: def func(a,b)
# def funa(name1,name2,name3):
#     print(name1)
#     print(name2)
#     print(name3)
# funa("bingbing","susu","ziyi")   # 写了几个就必须传几个,不可以多传少传

# 2.默认参数
# 含义:为参数提供默认值,调用函数时可不传该默认值
# 注意:所有的位置参数必须出现在默认参数前，包括函数的定义和调用
# 格式:def func(a=12):
# def funb(a=8):
#     print(a)
# funb()
# funb(200)
# 设置默认值，没传就是默认，传了就按传的执行

# 3.可变参数
# 含义:传入的值的数量是可以改变的,可以传多个,也可以不传
# 格式:def func(*args):
# def func(*args):           # 可以吧args改成其他参数名,但是args符合代码的规范性
#     print(args)   # 以元组形式接收
# func("海绵宝宝","派大星")

# 4.关键字参数
# 格式: def func(**kwargs):
# def fund(**kwargs):
#     print(kwargs)        # 以字典形式接收
# fund()    # 空字典
# fund(name="bingbing",age=18)      # 传值的时候,需要采用键=值的形式
# 作用:可以扩展函数的功能

# 4.函数嵌套
# 4.1嵌套调用
# 含义:在一个函数里面调用另一个函数
# def study():
#     print("晚上在学习")
# def course():
#     study()
#     print("python基础")
# 调用
# study()
# course()

# 4.2嵌套定义
# 含义:在一个函数中定义另外一个函数
# def study():        # 外函数
#     print("晚上在学习")
#     def course():   # 内函数
#         print("python基础")
#     course()
# study()

# 十--函数进阶
# 1.作用域
# 1.1 含义：指的是变量的生效范围，分为两种，分别是全局变量和局部变量
# 1.2全局变量
# 函数外部定义的变量，在整个文件中都是有效的
# a = 100     # 全局变量
# def test1():
#     print(f"只是test1中a的值{a}")
# def test2():
#     a = 120     # 局部变量
#     print(f"只是test2中a的值{a}")
# print("调用函数前a的值",a)
# test1()
# test2()
# print("调用函数后a的值",a)
# a的值没有被覆盖是因为函数内部如果要使用变量，会先从函数内部找，有的话就直接使用，没有再到外面找
# 1.3 局部变量
# 函数内部定义的变量,从定义位置开始到函数定义结束位置有效
# def funa():
#     num = 10       # 局部变量
#     print("num:",num)
# funa()
# print("num:",num)     # 报错，局部变量只能在被定义函数中使用，外部不能使用
# 作用:在函数体内部,临时保存数据,即当函数调用完之后,就销毁局部变量
# def funa():
#     num = 10       # 局部变量
#     print("funa中的num:",num)
# funa()
# def funb():
#     num = 20
#     print("funb中的num:",num)
# funb()

# 全局变量和局部变量命名相同
# 在函数内部修改全局变量的值,可以使用global关键字
# 1.4 global
# 将变量声明为全局变量
# 语法格式:global 变量名
# a = 100     # 全局变量
# def test1():
#     print(f"只是test1中a的值{a}")
# def test2():
#     global a    # 声明全局变量
#     a = 120     # 局部变量
#     print(f"只是test2中a的值{a}")
# print("调用函数前a的值",a)
# test1()
# test2()
# print("调用函数后a的值",a)

# def study():
#     global name,age
#     name = "Python基础"   # 局部变量name，age声明为全局变量
#     age = 18
#     print(f"{age}岁的我们在学习{name}")
# study()
# print(name,age)
# def work():
#     print(name)
# work()

# 总结: global关键字可以对全局变量进行修改,也可以在局部作用域中声明一个全局变量

# 1.5 nonlocal--了解
# 用来声明外层局部变量，只能在嵌套函数中使用，在外部函数先进行声明，内部函数进行nonlocal声明
# a = 10        # 全局变量
# def outer():  # 外函数
#     a = 5     # 局部变量
#     def inner():   # 内函数
#         nonlocal a
#         a = 20
#         def inner2():
#             nonlocal a
#             a = 30
#             print("inner2函数中a的值:",a)
#         inner2()
#         print("inner函数中的a的值",a)
#     inner()
#     print("outer函数中a的值:",a)
# outer()
# 总结:nonlocal只能对上一级进行修改

# 2. 匿名函数
# 2.1 基本语法
# 函数名 = lambda 形参 : 返回值(表达式)
# 调用: 结果 = 函数名(实参)

# 普通函数
# def add(a,b):
#     return a+b
# print(add(1,3))
# 匿名函数
# add = lambda a,b:a+b    # a,b就是匿名函数的形参,a+b是返回值的表达式
# lambda 不需要写return来返回值,表达式本身结果就是返回值
# print(add(20086,2))

# 2.2 lambda的参数形式
# 函数名 = lambda 形参 : 返回值(表达式)
# 2.2.1无参数
# funa = lambda : "一桶水果茶"
# print(funa())
# 2.2.2 一个参数
# funb = lambda name : name
# print(funb("bingbing"))
# 2.2.3 默认参数
# func = lambda name,age = 18 : (name,age)
# print(func("bingbing"))
# print(func("bingbing",20))
# fune = lambda a,b,c=12:(a+b+c)
# print(fune(1,2,4))
# print(fune(1,2))
#  默认参数必须写在非默认参数后面
# 2.2.4 关键字参数
# fund = lambda **kwargs:kwargs
# print(fund(age=18,name="bingbing"))
# 2.31 ambda结合if判断
# a = 8
# b = 5
# 格式: 为真结果 if 条件 else 为假结果
# print("a比b小") if a<b else print("a大于等于b")
# comp = lambda a,b : "a比b小" if a<b else "a大于等于b"    # a,b是形参,比较大小
# print(comp(3,8))
# 特点:
# lambda只能实现简单的逻辑，如果逻辑复杂且代码量较大，不建议使用lambda，降低代码可读性，为后期代码维护增加困难

# 3.内置函数
# 3.1查看所有的内置函数
# import builtins
# print(dir(builtins))
# 大写字母开头一般是内置常量名,小写字母开头一般是内置函数名
# 3.2 内置函数一
# 3.2.1 abs():返回绝对值
# print(abs(-10))
# print(abs(10))
# 3.2.2 sum():求和
# print(sum(123))       # 报错,整型不是可迭代对象,sum函数内要放可迭代对象
# 注意:字符串也不行
# print(sum({1.5,3,4}))   # 运算时只要有一个浮点数,那么结果必定是浮点数

# 3.3 内置函数二
# 3.3.1 max():求最大值
# 3.3.2 m(in():求最小值
# print(min(4,1,8))
# print(max(4,1,8))
# print(min(5,-8,key=abs))      # 传入了求绝对值函数，则参数就会先求绝对值再取较大者

# 3.3.3 zip():将可迭代对象作为参数，将对象中对应的元素打包成一个个元组
# li = [1,2,3]
# li2 = ["a","b","c"]
# print(zip(li,li2))
# 提取1:通过for循环
# for i in zip(li,li2):
#     print(i)
#     print(type(i))
# 如果元素个数不一致，就按照长度最短的返回
#  提取2:转换成列表打印
# print(list(zip(li,li2)))     # 转换成列表打印
# 注意:必须是可迭代对象
# print(list(zip(li,3)))

# 3.3.4 map():可以对可迭代对象的每一个元素进行映射,分别去执行
# map(func,iter1):func--自己定义的函数  iterl--要放进去的可迭代对象
# li = [1,2,3]
# def funa(x):
#     return x*5
# funa = lambda x : 5*x
# mp = map(funa,li)        # 注意只需要函数名，不需要小括号
# print(mp)
# for 循环
# for i in mp:
#     print(i)
# 列表
# print(list(mp))

# 3.3.5 reduce():先把对象中的两个元素取出,计算出一个值然后保存着,接下来把这个计算值跟第三个元素计算
# 需要先导包
# from functools import reduce
# reduce(fonction,sequance)   # function--函数:必须是有两个参数的函数,sequance:序列可迭代对象
# li = (1,2,3,4)
# def add(a,b):
#     return a+2*b
# res=reduce(add, li)
# print(res)

# 4. 拆包
# 含义:对于函数的多个返回数据去掉元组,列表直接获取里面数据的过程
# tua = (1,2,3,4)
# print(tua)
# print(tua[0])
# 方法一
# a,b,c,d = tua
# print(a,b,c,d)
# 要求元组内的个数相同，对象内有多个数据就需要定义多少个变量接受
# a,b = tua      # 报错，值错误要拆包的值太多
# print(a,b)
# 一般在获取元组值的时候使用
# 方法二
# a,*b=tua
# print(a,b)
# c,*d = b
# print(c,d)
# 先把单独的给它取完，其他剩下的全部交给带*的变量
# 一般在函数调用时使用
# def funa(a,b,*args):
#     print(a,b)
#     print(args,type(args))
# funa(1,2,3,4,5,6,7)
# arg = (1,2,3,4,5,6,7)
# funa(*arg)

# 十一--异常、模块和包
# 1.异常
# 1.1 含义:程序运行过程中出现的非正常的流程现象
# 1.2 异常处理
# 方式一: 根据控制台的错误提示找出错误点并分析改正
# abc = 666
# print(abc)
# Traceback:异常的追踪信息，可以追踪信息，可以追溯程序异常的具体位置
# XXXError:异常类型，后面会包含异常具体信息

# 方式二:对异常进行捕获处理
# 2. 异常处理,捕获异常
# 2.1 语法格式1
# try:
#     不确定是否能够正常执行的代码
# except :
#     如果检测到异常,就执行这个代码
# try:
#     print(abc)   # 一般try下面只放一行尝试执行的代码
# except (NameError,TypeError):
# 当要捕获多个异常类型时,可以吧要捕获的异常类型的名字(用元组形式)放到except后
#     print("这一行代码有问题!")
# 注意:可以申明捕获异常类型,但是遇到其他异常类型时依然会报错,无法捕获异常
# st = "12345"
# try:
#     print(st[5])
# except Exception as e:
# Exception 万能异常,可以捕获任意异常
# as相当于取别名,e是变量名,可以自定义,as e相当于把异常信息保存到变量e中去
#     print("这一行代码有问题!")
#     print(e)   # 打印输出异常信息

# 2.2 语法格式2
# try:
#     可能会引发异常的代码
# except:
#     出现异常现象的处理代码
# else:
#     没有捕获到异常执行的代码
# try:
#     print("abc")
# except Exception:
#     print("这一行代码有错误哦!")
# else:
#     print("这里是else的代码")
# st = "12345"   # 下标最大值为4
# try:
#     print(st[4])
# except:
#     print("超过下标范围")
# else:
#     print("try里面的代码没有问题")

# 2.3 语法格式三
# try:
#     可能会引发异常的代码
# except:
#     出现异常现象的处理代码
# else:
#     没有捕获到异常执行的代码
# finally:
#     try代码块结束后运行的代码(不管有没有异常，都会执行)
# 注意:可以单独使用try和finall

# 2.4抛出异常  raise
# 步骤:
# 1.创建一个Exception("XXX")对象，XXX——异常同事信息
# 2.raise抛出这个对象
# raise Exception("我抛出了一个异常")
# def funa():
#     raise Exception("有一个异常")
# funa()

# 需求: 密码长度不足6位，就报异常
# def login():
#     longeur = input("请输入您的密码")
#     if len(longeur) >= 6:
#         return "密码输入成功"
#     else:
#         raise Exception("您的密码长度不够,输入失败")
# try:
#     print(login())
# except Exception as e:
#     print(e)
# 捕获异常是为了检测到异常时，代码还能继续往下运行，即程序不会终止

# 3.模块
# 3.1 含义:一个py文件就是一个模块,即导入一个模块本质上就是执行一个py文件
# 3.2 分类
# 3.2.1 内置模块