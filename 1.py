from urllib import request
import re
import os


f=request.urlopen('https://www.zhihu.com/question/31299495')
webPage=f.read()
webPage=webPage.decode()

Links=re.compile(r'src=\"http.+?\.jpe?g') # a wrong R.E

L=Links.findall(webPage)

index=1

s1=set()

for link in L:
    if len(link)<=75 & len(link)>=65:
        if link in s1:
            continue
        s1.add(link)
        filename='newFolder/'+str(index)+'.jpg'
        index+=1
        fp= open(filename,'wb')
        target=request.urlopen(link[5:])
        print(link[5:])
        fp.write(target.read())
        fp.close()








