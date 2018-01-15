import requests  # Библиотека для отправки запросов
from fake_useragent import UserAgent  # fake user agent
from bs4 import BeautifulSoup  # Чудесный суп!

minValue = 1  # Минимальное значение, откуда начинаются поиски. Устанавливается эмпирическим путём
idVk = 'idVK'  # id пользователя (только цифры)

pageLink = 'https://vk.com/doc' + idVk + '_'

for i in range(minValue, 457457887):
    response = requests.get(pageLink + str(i), headers={'User-Agent': UserAgent().chrome})
    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        obj = soup.find('div', attrs={'class': 'message_page_title'})
        if str(obj) != '<div class="message_page_title">Ошибка</div>':
            print('https://vk.com/doc' + idVk + '_' + str(i))
    i += 1
