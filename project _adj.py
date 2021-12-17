from bs4 import BeautifulSoup
import requests

#class cars:
    #def __init__(self, web_doc):
        #self.web_doc = web_doc

def stream_Url(web_Url):
    web_doc = requests.get(web_Url).text
    soup = BeautifulSoup(web_doc, "lxml")
    return soup


def find_cars(soup):
    x = soup.find_all('a', class_="car-card-1")
    return x


def Extract_info(soup):
    with_discount = soup.find('div', class_='price-stat').text.replace('\n', ' ')

    if "N/A" in with_discount:
        name_of_car = soup.find('div', class_="mob-heading").text.replace('\n', " ")
        Mileage = soup.find('div', class_='mileage').text.replace('\n', ' ')
        Price = soup.find('span', class_='_js-hook-main-price').text
        without_discount = soup.find('div', class_='label').text
        picture_of_car = soup.find('img')['data-src']

        return f"The cars is:  {name_of_car} \n and the Mileage is:  {Mileage} \n the picture is  {picture_of_car} \n with a discount of {without_discount}"

def Extract_next(soup):
    extract_link = soup.find('a', class_="btn btn-lg btn-block btn-warning")
    return "https://www.ooyyo.com" + extract_link["href"]

def print_car_list(html_data):
    car_list = find_cars(html_data)
    for car in car_list:
        info = Extract_info(car)
        print(info)



if __name__ =="__main__":
    for i in range(1301, 3301, 1000):
        start_Url = f"https://www.ooyyo.com/germany/used-cars-for-sale/c=CDA31D7114D3854F111BFE6FB7A03C53CCA2160101D386601D0FD36FB0447B53C2791A7EC8D4916{i}F/"
        html_data = stream_Url(start_Url)
        print_car_list(html_data)


    #next_link = Extract_next(html_data)
    #while next_link in start_Url:
    #    html_data2 = stream_Url(next_link)
    #    print_car_list(html_data2)







# Documents = (f'''print(f'name of car:{name_of_car}')

        # The picture of care is {picture_of_car}
        # name_of_car:{name_of_car}
        # with {Price}
        # mileage with{Mileage}
        # ''')
        # with open('document.txt','a') as doct:
        #   doct.write(Documents)