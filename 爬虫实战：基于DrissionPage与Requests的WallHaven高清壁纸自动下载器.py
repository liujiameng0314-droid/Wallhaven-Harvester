import os 
from DrissionPage import Chromium
import requests
from bs4 import BeautifulSoup
import time
import re
def search_wallpapers(tab,keyword):
    url='https://wallhaven.cc'
    tab.get(url)
    search_position=tab.ele('x://input[@type="search"]')
    search_position.input(keyword)
    tab.ele('x://button').click()
    tab.wait(2)
    amount = tab.ele('x://header[@class="listing-header"]/h1').text
    paper_amount=int(re.search('(.*?)Wallpapers',amount).group(1).replace(',', '').strip())
    return paper_amount

def scroll_and_get_link(tab,pages):
    url_list=[]
    for i in range(1,pages):
        tab.scroll.to_bottom()
        tab.wait(2)
    wallpaper_urls_list=tab.eles('x://ul/li/figure/a[@class="preview"]')
    for element in wallpaper_urls_list:
        time.sleep(0.5)
        wallpaper_url=element.attr('href')
        url_list.append(wallpaper_url)
    return url_list

def create_folder(dir,keyword):
    folder_name=os.path.join(dir,keyword)
    os.makedirs(folder_name,exist_ok=True)
    return folder_name

def download_images(url_list,headers,folder_name):
    order=0
    for image_url in url_list:
        
        order+=1
        res=requests.get(image_url,headers=headers)
        image_name=folder_name+'/'+str(order)+'.png'
        if res.status_code==200:
            soup=BeautifulSoup(res.text,'html.parser')
            paper_url=soup.find('img',attrs={'id':'wallpaper'}).get('src')
            res1=requests.get(paper_url,headers=headers)
            with open(image_name,'wb') as f:
                       f.write(res1.content)
def main():
     user_agent=input('请输入你的浏览器user-agent请求字段：')
     headers={'User-Agent':f'{user_agent}'}
     keyword=input("请输入壁纸的关键词：")
     browser=Chromium()
     tab=browser.latest_tab
     print('正在完成壁纸的检索，请稍后....')
     paper_amount=search_wallpapers(tab,keyword)
     print(f'共检索到{paper_amount}张相关壁纸')
     if paper_amount!=0:
         print('正在获取壁纸的链接....')
         pages=int(input('你想要下载几页壁纸：'))
         url_list=scroll_and_get_link(tab,pages)
         dir=input('请选择文件夹位置：')
         folder_name=create_folder(dir,keyword)
         print(f'{folder_name}文件夹已经完成创建，用来放置下载的壁纸')
         print('开始下载壁纸.....')
         download_images(url_list,headers,folder_name)
         print('壁纸下载任务已经完成')
     else:
        print(f'没有检索到任何{keyword}相关壁纸')
     browser.quit()
if __name__=='__main__':
    main()
     

     
    








    