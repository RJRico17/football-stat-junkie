from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get('https://matchroompool.com/players/?_gl=1*qek46d*_up*MQ..*_ga*MTI4Nzk4MDczMi4xNzQyOTY3NDQ1*_ga_N5ZWBCJD2K*MTc0Mjk2NzQ0My4xLjAuMTc0Mjk2NzQ0My4wLjAuMA..')
soup = BeautifulSoup(page_to_scrape.text, "html.parser")


main_div = soup.find("div", attrs={"data-type":"players"})
firsts = main_div.find_all("span", {"class":"first"},limit=5)
lasts = main_div.find_all("span", {"class":"last"},limit=5)
countrys = main_div.find_all("div", {"class":"country"},limit=5)
ranks = main_div.find_all("div", {"class":"rank"},limit=5)

for first, last in zip(firsts,lasts):
    player_scrape = requests.get('https://en.wikipedia.org/wiki/'+first.text+"_"+last.text)
    soup = BeautifulSoup(player_scrape.text, "html.parser")
    bdays = soup.find("span",attrs={"class":"bday"})

for rank, first, last, country, bday in zip(ranks, firsts,lasts,countrys,bdays):
    print(rank.text + ": " + first.text + " " + last.text + " - " + country.text + " - " + bday.text)
    print('https://www.azbilliards.com/person/'+first.text+"-"+last.text)
    