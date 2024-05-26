import requests, openpyxl
from bs4 import BeautifulSoup

# Creating excel file 

excel = openpyxl.Workbook()
print(excel.sheetnames) ### Nmae of sheet
sheet = excel.active
sheet.append(['Movie Name' , 'Movie Rank' , 'Movie Year'])
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'


try: 
    headers = {'user-agent' :USER_AGENT }
    source = requests.get("https://www.imdb.com/chart/top/", headers=headers)
    # print(source.text) 
    print(source.status_code)  ## status code
    # print(source.raise_for_status)    ## raise to get an alert for incorrect urls

    soup = BeautifulSoup(source.text, 'html.parser')

    movies = soup.find('ul', class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 eBRbsI compact-list-view ipc-metadata-list--base").find_all('li')
    result = []
    for movie in movies:
        name = movie.find('h3' , class_="ipc-title__text").text
        rank = movie.find('span', class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating").text
        # rank.attrs['aria-label']
        year = movie.find('span', class_="sc-b189961a-8 kLaxqf cli-title-metadata-item").text
        result.append((name,rank,year))
        print(name)
        print(rank)
    #     # rating = movie.find()
        sheet.append([name,rank,year])
    print(result)
        

except Exception as e:
    print(e) 

excel.save('IMDB_MoviewRating.xlsx')


