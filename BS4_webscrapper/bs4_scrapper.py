from bs4 import BeautifulSoup
import requests, openpyxl
import pandas as pd

excel = openpyxl.Workbook()
# print(excel.sheetnames)
sheet = excel.active
sheet.title = 'Top rated movies'
# print(print(excel.sheetnames))
sheet.append(['Product Name', 'Price', 'rating'])


def get_data(main_soup):
    data = []
    for item in main_soup:
        prod_name = item.find("a",class_="title").text
        price = item.find("h4", class_="price float-end card-title pull-right").text
        rating= item.find("p", {"data-rating": True})["data-rating"]
        # print(rating)
        # print(prod_name)
        # print(price)
        data.append([prod_name,price,rating])
        sheet.append([prod_name,price,rating])
    return data

def get_main_soup(url,index):
    final_url = url+"?page="+str(index+1)
    source = requests.get(final_url)
    soup = BeautifulSoup(source.text , 'html.parser')
    main_soup = soup.find_all('div' , class_ = "product-wrapper card-body")

    return main_soup
    

try:
    base_url = 'https://webscraper.io/test-sites/e-commerce/static/computers/tablets'
    source = requests.get(base_url)    # response is saved in source variable
    # print(source.text)
    print(source.status_code)           # status code 
    # print(source.raise_for_status)      # raise to get an alert for incorrect urls

    soup = BeautifulSoup(source.text , 'html.parser')
    
    page_count_soup = soup.find('ul' , class_ = "pagination")
    
    page_child = page_count_soup.findChildren()
    out_data =[]
    if len(page_child)>2:
        for i in range(len(page_child)-2):
            main_soup = get_main_soup(base_url, i)
            out_data.extend(get_data(main_soup))
    
except Exception as e:
    print("Got execption:" ,e)

excel.save('bs4_webscrapper_data.xlsx')