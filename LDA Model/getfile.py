import os
import fnmatch
import zipfile
import re
#-*- coding:utf-8 -*-
def iterfindfiles(path, fnexp):
    for root, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files, fnexp):
            yield os.path.join(root, filename)
result=""
for filelist in iterfindfiles("C:\Users\林子豪\Desktop\javafile", "*.zip"):
    z = zipfile.ZipFile(filelist, "r")
for file in z.namelist():
    result=result+file+"\n"
    print("以下内容是压缩包所包含文件：")
    print(result+"\r\n")
unicodepage=result.decode("utf-8")
myItems=re.findall("([\w\d]*?.txt)",unicodepage,re.S)
items=[]
print("以下是获取所有以. txt结束的文本")
for item in myItems:
    items.append(item.replace("\r\n",""))

print (items)


