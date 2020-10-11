from bs4 import BeautifulSoup
from selenium import webdriver
import time
import dload

driver = webdriver.Chrome('chromedriver')
driver.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%B0%95%EB%8F%99%EC%9B%90") # 여기에 URL을 넣어주세요
time.sleep(5)

req = driver.page_source
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(req, 'html.parser')

###################################
thumbnails = soup.select('#_sau_imageTab > div.photowall._photoGridWrapper > div.photo_grid._box > div > a.thumb._thumb > img')
i = 1
for thumbnail in thumbnails:
    img = thumbnail['src']
    print(img)
    dload.save(img, f'img2/{i}.jpg')
    i += 1
###################################

driver.quit() # 끝나면 닫아주기