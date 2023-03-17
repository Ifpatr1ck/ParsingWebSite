import requests
from bs4 import BeautifulSoup
#Хэдэр, для того, чтоб не получить ошибку 404 и мне не сказали, что я мудак
def parse(url):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    #Запрос
    page = requests.get(url=url,headers=user_agent)
    soup = BeautifulSoup(page.text,"html.parser")
    vakancii = soup.findAll('div', class_='serp-item')
    count = 0
    spisok2 = []
    print(len(vakancii))
    for i in vakancii:
        href = i.find("a",class_="serp-item__title")
        result = href.get("href")
        count+=1
        print(result)
        spisok2.append(result)
    print(count)


    with open("info.txt", 'w', encoding='utf-8') as file:
        for i in range(count):
            file.write(spisok2[i] + '\n')