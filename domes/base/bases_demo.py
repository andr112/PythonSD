import math

a, b, c = 1, 2, 3
d = a < b <= c
print(d)

dd = b"0cc0x23"  # 字节串字面值要加前缀 'b' 或 'B'；生成的是类型 bytes 的实例
ee = rb"0cc0x23"
print(type(dd), " , ", dd, " , ", ee == dd)
ss = 'abc\tdefg'
rss = r'abc\tdefg'
print(type(ss), " , ", ss, " , ", rss)
print(type(ss), " , ", ss, " , ", rss)
print(f"format str : {type(ss)} , {ss} ,{rss}")

e = 1 + 2 - 3 * 2 / 3 + 2 // 3 + 2 ** 2 + 5 % 3
print(e)

f = sum(x * x for x in range(10))
print(f)

r10 = range(10)
print(type(r10))

r1_10 = range(1, 10, 2)
print(list(r1_10))

# 列出模块中的函数
# 用import导入模块后，可使用函数dir（m）列出模块的所有函数，import是导入模块的命令，m是模块名


print("\nmath模块的所有函数")
print(dir(math))

# 查看完整的python内置函数清单
print("\n完整的python内置函数清单")
print(dir(__builtins__))

# 查看某个函数的文档帮助信息
print(" math.ceil(3.5) : ", math.ceil(3.5))
print(type(math.ceil))
print(" math.ceil 函数的文档帮助信息 ")
print(help(math.ceil))
