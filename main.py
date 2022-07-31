import requests
import bs4

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}
url_index = "https://habr.com/post/"
url = "https://habr.com/ru/all/"
keyWords =['Процессоры', 'массах ядра', 'При']
if __name__ == '__main__':
    text = requests.get(url, headers=headers).text
    soup = bs4.BeautifulSoup(text, features='html.parser')
    flag = []
    flagf = []
    for article in soup.find_all("article"):
        id = article.attrs["id"]
        snippset = []
        for i in article.find_all(class_="tm-article-snippet__hubs-item-link"):
            snippset += [i.find("span").text]
        time_article = article.find("time").text
        url_index_id = url_index + id
        title_article = article.find(class_="tm-article-snippet__title-link").find("span").text
        text_id = requests.get(url_index_id, headers=headers).text
        soup_id = bs4.BeautifulSoup(text_id, features='html.parser')
        articl_text = ""
        print(snippset)
        for paragraph in soup_id.find_all("p"):
            articl_text += paragraph.text
        for i in keyWords:
            if articl_text.find(" "+i+" ") > -1:
                flag += [[time_article, title_article, url_index_id]]
                break
        for i in keyWords:
            for j in snippset:
                if i == j:
                    flagf += [[time_article, title_article, url_index_id]]
                    break
    print('Статьи по совпадению в ключевых словах')
    print(flagf)
    print('Статьи по совпадению в тексте')
    print(flag)

