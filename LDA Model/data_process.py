#'''
#正式编辑
#import sys, io
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') # Change default encoding to utf8
import os
import zipfile
import codecs
content = ''
path2 = 'E:/data_temp' #解压后文件储存路径
#path = 'E:\github_data'
for (root,dirs,files) in os.walk("C:/Users/林子豪/Desktop/1files"): #files对应目录下所有文件，这里为zip
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
                    #print("i:",i)
                    f1 = codecs.open(i,"r",encoding = 'utf-8')
                    temp = f1.read()
                    #print(temp)
                    content = content+'\n'+temp
                    f1.close()

print(content)
f2 = codecs.open('github_data.txt',"w",'utf-8')
f2.write(content)
f2.close()
#'''