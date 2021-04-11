from gtts import gTTS
from urllib.parse import urlparse
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from pip._vendor import requests
import os
def menu_teller(pk, text):
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = path + "/static/file/record_"+str(pk)+".mp3"
    tts = gTTS(text=text, lang='ko')
    tts.save(path)

def menu_crawling_teller(pk):
    url = "https://dapi.kakao.com/v2/local/search/category.json?category_group_code=CE7&radius=350&y=37.550950&x=126.941017"
    result = requests.get(urlparse(url).geturl(),
                          headers={"Authorization": "KakaoAK "})
    # 본인 api 키 입력
    driver = webdriver.Chrome(executable_path=r'D:\capstone1\test\chromedriver.exe')  # 본인 크롬 드라이버 위치 입력
    driver.implicitly_wait(3)

    json_obj = result.json()
    market_list = json_obj.get("documents")

    text = ""
    market_count = 0
    for market in market_list:

        try:
            driver.get(market.get("place_url"))
            menu_list = driver.find_element_by_class_name("list_menu").find_elements_by_class_name("loss_word")# 에러 처리 안되어있어서 조금만 class name 바뀌면 에러남. 나중에 시간나면 고칠 예정
            text = text + market["place_name"] + "에는 다음과 같은 메뉴가 있습니다."
            for i in menu_list:
                text = text + " " + i.text
        except:
            break
        market_count += 1
        text = text + "."


    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = path + "/static/file/menu_" + str(pk) + ".mp3"
    text = "주변의 식당은 총" + str(market_count) + "개 있습니다." + text
    tts = gTTS(text=text, lang='ko')
    tts.save(path)