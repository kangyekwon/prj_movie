
from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time

options = webdriver.ChromeOptions()

options.add_argument('lang=ko_KR')
driver = webdriver.Chrome('./chromedriver.exe', options=options)

# 랭킹 > 아우터 , 바지 ,신발
# review_xpath = '//*[@id="goodsRankList"]/li[1]/div[3]/div[1]/a/img'
# review_number_xpath =  '//*[@id="estimate_type"]/button[3]'
# review_button_xpath = '//*[@id="estimate_list"]/div/div[3]/div[4]/div[1]'                   #review button
# # #                      //*[@id="movieEndTabMenu"]/li[6]/a
# # your_year = 2 # 아우터 2, 바지 3, 신발 5
review_number_xpath = '//*[@id="estimate_goods"]'
review_button_xpath = '//*[@id="estimate_goods"]'
# review_page = '//*[@id="pagerTagAnchor2"]review_page'


# your_year = 2017 # 할당받은 연도로 수정하세요
for i in range(1, 3): # 3
    url = 'https://www.musinsa.com/ranking/best?period=month&age=ALL&mainCategory=002&subCategory=&leafCategory=&price=&golf=false&kids=false&newProduct=false&exclusive=false&discount=false&soldOut=false&page={}&viewType=small&priceMin=&priceMax='.format(i)

    titles = []
    reviews = []
    try:

        for j in range(1, 11):  # 우선 상품 10가지만
            driver.get(url)
            time.sleep(0.5)
            outer_title_xpath = '//*[@id="goodsRankList"]/li[{}]/div[3]/div[2]/p[2]/a'.format(j)
            try:
                title = driver.find_element("xpath", outer_title_xpath).text
                driver.find_element("xpath", outer_title_xpath).click()
                time.sleep(0.5)
                driver.find_element('xpath', review_button_xpath).click()
                time.sleep(0.5)
                review_range = driver.find_element('xpath', review_number_xpath[7:13]).text
                review_range = review_range.replace(',', '')
                review_range = (int(review_range) -1) // 10 + 2
                print(review_range)
                # exit()
                for k in range(1, review_range):
                    review_page_button_xpath = '//*[@id="estimate_type"]/button[3]'.format(k)
                    try:
                        driver.find_element('xpath', review_page_button_xpath).click()
                        for l in range(1, 11):
                            back_flag = False
                            review_title_xpath = '//*[@id="estimate_list"]/div/div[{}]/div[4]/div[1]'.format(l)
                            try:
                                review = driver.find_element('xpath', review_title_xpath).click()
                                back_flag = True
                                time.sleep(0.5)
                                review = driver.find_element('xpath', review_xpath).text
                                titles.append(title)
                                reviews.append(review)
                                driver.back()
                            except:
                                if back_flag:
                                    driver.back()
                                print('review', i, j, k, l)
                        driver.back()
                    except:
                        print('review page', i, j, k)
            except:
                print('movie', i, j)
        df = pd.DataFrame({'title':titles, "reviews":reviews })
        df.to_csv('./crawling_data/reviews_{}_{}page.csv'.format(i),index=False)
    except:
        print('page', i)




driver.close()