#coding:utf-8

'''
#尝试寻找data_Samples的格式
from sklearn.datasets import fetch_20newsgroups
dataset = fetch_20newsgroups(shuffle=True, random_state=1,
                             remove=('headers', 'footers', 'quotes'))
data_samples = dataset.data[:1] #截取需要的量，n_samples=2000
for content in data_samples:
    print(content+'\n')
#print(dataset)

#print("now is data_sample\n")

#print(data_samples)
'''


#正式编辑
#import sys, io
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') # Change default encoding to utf8
import os
import zipfile
import codecs
content = ''
path2 = 'E:/data_temp' #解压后文件储存路径
#path = 'E:\github_data'
for (root,dirs,files) in os.walk("E:/test"): #files对应目录下所有文件，这里为zip
    for filename in files:
        fullname = root+'/'+filename
        name2 = path2+'/'+filename
        #print(fullname+'\n')
        #print(name2+'\n')
        #print(root)
        if zipfile.is_zipfile(fullname):
            azip = zipfile.ZipFile(fullname)
            azip.extractall(path2)
            f = zipfile.ZipFile(fullname)
            flist = f.namelist()
            #print(flist)
            for i in flist:
                if '.java' in i:
                    i = path2+'/'+i
                    print("i:",i)
                    f1 = codecs.open(i,"r",encoding = 'utf8')
                    temp = f1.read()
                    #print(temp)
                    content = content+'\n'+temp
                    f1.close()

print(content)
f2 = codecs.open('github_data.txt',"w",'utf-8')
f2.write(content)
f2.close()


'''
import os
import zipfile
'''
'''
#尝试获取zip路径名字
for (root,dirs,files) in os.walk("C:/Users/林子豪/Desktop/test"):
    for filename in files:
        filename2 = root+'/'+filename
        print(filename2)
        if not zipfile.is_zipfile(filename2):
            print('not a zip file')
'''

'''
#尝试从文件列表获取.java路径名字
import os
import zipfile
root = 'C:/Users/林子豪/Desktop/test'
#path = 'C:/Users/林子豪/Desktop/test/1Sheeld-Android-App-master.zip'
if zipfile.is_zipfile(path):
    print('get the zip')
    f = zipfile.ZipFile(path)
    files = f.namelist()
    for i in files:
        if '.java' in i:
            i = root+'/'+i
            print(i)
            
'''

'''
#合并两个.java内容
path1 = 'C:/Users/林子豪/Desktop/1.txt'
path2 = 'C:/Users/林子豪/Desktop/2.txt'
path3 = 'C:/Users/林子豪/Desktop/test/2ch-Browser-master.zip/src/android/httpimage/Base64.java'
f1 = open(path1,"r")
f2 = open(path2,"r")
f3 = open(path3,"r")
content1 = f1.read()
content2 = f2.read()
content3 = content1 +'\n'+ content2

content4 = f3.read()
print(content1)
print('\n')
print(content2)
print('\n')
print(content3)
print('\n')
print(content4)
f1.close()
f2.close()
f3.close()
'''

'''
#zip压缩操作尝试
import zipfile
path = 'C:/Users/林子豪/Desktop/test/2ch-Browser-master.zip'
azip = zipfile.ZipFile(path)
azip.extractall('C:/Users/林子豪/Desktop/test')

'''





'''
import zipfile

if zipfile.is_zipfile('3D-Compass-master.zip'): #is_zipfile() 判断是否zip文件
    print('yes')


for filename in ['print_name.py', '3D-Compass-master.zip', 'uwsgi', 'admin']:
    print('%20s %s' % (filename, zipfile.is_zipfile(filename)))
'''

'''
import codecs
import re
f = codecs.open('github_data.txt',"r",encoding = 'utf-8')
content = f.read()
content.replace('*','')
content.replace('/','')
content.replace('{','')
content.replace('}','')
content.replace('(','')
content.replace(')','')
a = content.splitlines()
print(len(a))
'''
