# -*- coding=UTF-8 -*-
# @Time: 2020/9/25 20:13
# @File:spider.py.py
# @Software:PyCharm

from bs4 import BeautifulSoup   #网页解析、获取数据
import re                        #正则表达式、文字匹配
import urllib.request, urllib.error  #获取网络数据
import xlwt                      #excel操作
import sqlite3                   #sqlite数据库操作

# 1、爬取网页
# 2、解析数据
# 3、保存数据

def main():
    baseurl='https://movie.douban.com/top250/?start='
    savepath=''
    savedata(savepath)
    data=getdata(baseurl)
    for i in range (0,250):
        print(i+1,data[i])





def getdata(baseurl):
    head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.63'}
    datalist = []
    for i in range (0,10):
        url=baseurl+str(i*25)
        print(url)
        req=urllib.request.Request(url,headers=head)
        res=urllib.request.urlopen(req)
        # ------------------------------------爬取页面内容----------------------------------------------
        html=res.read().decode('utf-8')
        bs=BeautifulSoup(html,'html.parser')
        movie=bs.find_all('div',class_='item')            #整页所有电影
        # moviename=bs.find_all('span',class_='title')
        for i in range(0,25):
            #正则表达式只能够对于字符串进行操作，所以必须先进行数据类型转换
            name=re.search(r'<span class="title">(.*?)</span>',str(movie[i]))     #检索电影名
            datalist.append(name.group(1))
    return datalist



def savedata(savepath):
    print('save')


if __name__ == '__main__':
    main()
