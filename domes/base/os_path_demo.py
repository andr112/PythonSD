import os

# os.system("notepad.exe")  # 打开记事本
# os.system("calc.exe")  # 打开计算器

# os.startfile("C:\Windows\System32\\calc.exe")
# os.startfile("C:\\Program Files (x86)\\Tencent\\WeChat\\WeChat.exe")

print("--------os---------------------")
print(os.getcwdb())
lst = os.listdir()
print(lst)
# os.makedirs("A/B")
os.mkdir("C")
print(os.listdir())
# os.removedirs("A/B")
os.rmdir("C")
print(os.listdir())
os.chdir("..\\")
cur_path = os.getcwdb()
print("cur_path: " + str(cur_path))
print("listdir: " + str(os.listdir()))
lst_files = os.walk(cur_path)
for dirPath, dirNames, fileNames in lst_files:
    print(dirPath)
    print(dirNames)
    print(fileNames)
    print("-----next-----------")

print("--------os.path---------------------")
basePath = os.path.abspath("bases_demo.py")
print(basePath)
print(os.path.isdir(basePath))
print(os.path.dirname(basePath))
print(os.path.basename(basePath))
basePath, name = os.path.split(basePath)
print("os.path.split >  basePath: " + basePath + " , name: " + name)
print(os.path.isdir(basePath))
print(os.path.exists(basePath))
print(os.path.join(basePath, name))
