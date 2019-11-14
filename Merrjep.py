#Copyrights - Lirim Krosa

import csv
import requests
from bs4 import BeautifulSoup    
import datetime


pages = int(input("Shtyp Numrin e Faqeve: "))
qyteti = input("Ne cilin qytet doni te kerkoni?: ")
linku = "https://www.merrjep.com/shpalljet/{}".format(qyteti)

end_page_num = pages

filename = "Merrjep_" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")+".csv"
with open(filename, "w+", encoding='utf-8') as f:

    writer = csv.writer(f)
    writer.writerow(["Descriere","Data"])
    i = 1
    while i <= end_page_num:

        r = requests.get(linku,"?Page={}".format(i))
        content = r.content

        soup = BeautifulSoup(r.text, "html5lib")
        x = soup.find_all("div", {'class': 'row row-listing'})

        for thumbnail in x:
            descriere = thumbnail.find('a')['href']
            strs = descriere.replace('/shpallja/', 'https://merrjep.com/shpallja/')
            writer.writerow([strs])
            print(strs)
        i += 1
