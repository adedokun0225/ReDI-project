from bs4 import BeautifulSoup
import requests


web_doc = requests.get('https://www.ooyyo.com/germany/used-cars-for-sale/c=CDA31'
                       'D7114D3854F111BFE6FB7A03C53CCA2160101D386601D0FD36FB0447B53C2791A7EC8D49161301F/').text
soup = BeautifulSoup(web_doc, "lxml")

Used_cars = soup.find_all('a', class_="car-card-1")


for Used_car in Used_cars:
    with_discount = Used_car.find('div', class_='price-stat').text.replace('\n', ' ')
    if 'N/A' in with_discount:
         name_of_car = Used_car.find('div', class_="mob-heading").text.replace('\n', " ")
         Mileage = Used_car.find('div', class_='mileage').text.replace('\n', ' ')
         Price = Used_car.find('span', class_='_js-hook-main-price').text
         without_discount = Used_car.find('div', class_='label').text
         picture_of_car = Used_car.find('img')['data-src']

         print(f'''
         The picture of care is {picture_of_car}
         name_of_car:{name_of_car}
         with {Price}
         mileage with{Mileage}
          ''')
    # print(f'picture:{picture_of_car.strip()}')
    # print(f'name of car:{name_of_car.strip()}')

        #with open('document.txt','a') as doct:
         #   doct.write(Documents)








#print(with_discount)




