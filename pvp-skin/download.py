from bs4 import BeautifulSoup
import requests
import os
from selenium import webdriver


class Spider:

    def __init__(self):
        self.header = {'User-Agent': 'Mozilla/5.0'}
        self.start_url = 'https://pvp.qq.com/web201605/herolist.shtml'
        self.base_url = 'https://pvp.qq.com/web201605/'
        self.folder = 'skin'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        
    def __del__(self):
        self.driver.quit()

    def load_msg(self, url):
        driver = self.driver
        driver.get(url)
        html = driver.execute_script("return document.documentElement.outerHTML")
        return html

    def make_folder(self):
        if not os.path.exists(self.folder):
            os.mkdir(self.folder)

    def get_list(self):
        hero_set = set()
        # response = requests.get(self.start_url, self.header)
        # response.encoding = 'gbk'
        html = self.load_msg(self.start_url)
        soup = BeautifulSoup(html, "html.parser")
        try:
            hero_lists = soup.find('ul', class_='herolist clearfix').find_all('a')
            for hero in hero_lists:
                hero_url = hero['href']
                url = self.base_url + hero_url
                hero_set.add(url)
        except Exception as e:
            print(e)
        return hero_set

    def get_detail(self):
        skin_set = set()
        detail_lists = self.get_list()
        for skin in detail_lists:
            html = self.load_msg(skin)
            soup = BeautifulSoup(html, "html.parser")
            try:
                skin_lists = soup.find('ul', class_='pic-pf-list pic-pf-list3').find_all('img')
                for skin_url in skin_lists:
                    name = skin_url['data-title']
                    url = skin_url['src']
                    final_url = 'http:' + url.replace('heroimg', 'skin/hero-info').replace('smallskin', 'bigskin')
                    # print(final_url)
                    # print(name)
                    final_mix = name + '*' + final_url
                    skin_set.add(final_mix)
            except Exception as e:
                print(e)
        return skin_set

    def download(self):
        self.make_folder()
        mix_names = self.get_detail()
        for mix_name in mix_names:
            name = mix_name.split('*')[0]
            url = mix_name.split('*')[1]
            img_name = './skin/' + name + '.jpg'
            response = requests.get(url, self.header)
            with open(img_name, 'wb') as f:
                try:
                    f.write(response.content)
                    print("正在下载皮肤：%s" % name)
                except Exception as e:
                    print(e)


if __name__ == '__main__':
    spider = Spider()
    spider.download()

