# Python 语法基础
Python 是一门易于学习、功能强大的编程语言
+ python官网 : https://www.python.org/
+ Python3 中文官方文档 : https://docs.python.org/zh-cn/3/
+ 开发工具pycharm : https://www.jetbrains.com/pycharm/

### 标识符和关键字
有效标识符字符为： 大小写字母 A 至 Z、下划线 _ 、数字 0 至 9，但不能以数字开头。长度没有限制，但区分大小写。,不能与关键字相同

### 语句块, 4个空格来表示每级缩进

Python语言利用缩进表示语句块的开始和退出（Off-side规则），而非使用花括号或者某种关键字。增加缩进表示语句块的开始，而减少缩进则表示语句块的退出。

### 数据类型

+ int (整数）
+ float（浮点数）
+ bool (逻辑值:True / False)
+ complex (复数:3+2.7j)
+ bytes（字节,一个由字节组成的不可更改的有序串行)
+ list（列表,可以包含多种类型的可改变的有序串行)
  > list = [4.0，'string'，True]
+ tuple（元组,可以包含多种类型的不可改变的有序串行）
  > tp =（4.0，'string'，True）
+ set，frozenset (与数学中集合的概念类似。无序的、每个元素都是唯一的: )
  > setA = {4.0，'string'，True}
  >
  > frozensetA = frozenset（[4.0，'string'，True]）
+ dict（字典,一个可改变的由键值对组成的无序串行）
  > {'key1'：1.0，3：False}
+ type（类型 : 显示某个值的类型，用type（x）获得）
  > type（1）->int
+ builtin_function_or_method (自带的函数，不可更改也不可增加: print / input)
+ range (按顺序排列的数)

##### str（string/字符串）

使用'（单引号）和"（双引号）来表示单行字符串，用'''（三个连续单引号）和"""（三个连续双引号）表示多行字符串. 出现在字符串中的\（反斜杠）被解释为特殊字符，比如\n表示换行符。表达式前加r指示Python不解释字符串中出现的\
> strA = "abc"

### 控制语句

+ if语句，当条件成立时运行语句块。经常与else，elif（相当于else if）配合使用，称为if-elif-else语句。
+ for语句，遍历列表、字符串、字典、集合等迭代器（容器），依次处理迭代器中的每个元素。有时和else连用，称为for-else语句。
+ while语句，当条件为真时，循环运行语句块。有时和else配合使用，称为while-else语句。
+
try语句，必与except配合使用处理在程序运行中出现的异常情况，称为try-except语句。常与else，finally配合使用，称为try-except-else语句，try-except-finally语句，try-except-else-finally语句
+ class语句，用于定义类型。
+ def语句，用于定义函数和类型的方法。
+ pass语句，表示此行为空，不运行任何操作。
+ assert语句，用于程序调试阶段时测试运行条件是否满足。
+ with语句，Python2.6以后定义的语法，在一个场景中运行语句块。比如，运行语句块前加密，然后在语句块运行退出后解密。
+ yield语句，在迭代器函数内使用，用于返回一个元素。自从Python 2.5版本以后。这个语句变成一个运算符。
+ raise语句，制造一个错误。
+ import语句，导入一个模块或包。
+ from…import语句，从包导入模块或从模块导入某个对象。
+ import…as语句，将导入的对象赋值给一个变量。
+ in语句，判断一个对象是否在一个字符串/列表/元组里。

### 表达式

##### 算数运算

e = 1 + 2 - 3 * 2 / 3 + 2 // 3 + 2 ** 2 # 结果为5.0

+ "+" 加法或者取正
+ "-" 减法或者取负
+ "*" 乘法
+ "/" 除法
+ "//" 整除
+ "**" 乘方
+ "~" 取补
+ "%" 取余

##### 逻辑运算

+ and，or，not : 且 , 或 , 非
+ is，is not用于比较两个变量是否是同一个对象
+ in，not in用于判断一个对象是否属于另外一个对象

##### 支持“列表推导式”（list comprehension），比如计算0-9的平方和：

> sum(x * x for x in range(10))

##### 条件表达式

> y if cond else x

意思是当cond为真时，表达式的值为y，否则表达式的值为x。相当于C++和Java里的cond?y：x。

##### 同时赋值给多个变量

Python区分列表（list）和元组（tuple）两种类型。 list的写法是[1，2，3]， 而tuple的写法是（1，2，3）。 可以改变list中的元素，而不能改变tuple。
在某些情况下，tuple的括号可以省略。tuple对于赋值语句有特殊的处理。
> x, y=1 , 2 # 同时给x,y赋值，最终结果：x=1, y=2
>
> x, y=y, x #最终结果：y=1, x=2

