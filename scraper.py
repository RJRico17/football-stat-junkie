from bs4 import BeautifulSoup
import requests
import pandas as pd
import sys

page_to_scrape = requests.get('https://matchroompool.com/players/?_gl=1*qek46d*_up*MQ..*_ga*MTI4Nzk4MDczMi4xNzQyOTY3NDQ1*_ga_N5ZWBCJD2K*MTc0Mjk2NzQ0My4xLjAuMTc0Mjk2NzQ0My4wLjAuMA..')
soup = BeautifulSoup(page_to_scrape.text, "html.parser")


main_div = soup.find("div", attrs={"data-type":"players"})
firsts = main_div.find_all("span", {"class":"first"})
lasts = main_div.find_all("span", {"class":"last"})
countrys = main_div.find_all("div", {"class":"country"})
ranks = main_div.find_all("div", {"class":"rank"})

for rank, first, last, country in zip(ranks, firsts,lasts,countrys):
    print(rank.text + ": " + first.text + " " + last.text + " - " + country.text)
    print('https://www.azbilliards.com/person/'+first.text+"-"+last.text)


df = pd.read_csv('seahawks_roster.csv')
print(df)