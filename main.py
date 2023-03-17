import Parser
url = 'https://omsk.hh.ru/search/vacancy?text=python&area=68'
if __name__ == '__main__':
    try:
        Parser.parse(url)
    except:
        print("Ошибка")


