#Copyrights - Lirim Krosa
import urllib.request
import csv
import requests
from bs4 import BeautifulSoup    
import datetime
import re
from PIL import Image
import io
import pytesseract

qyteti = input("Ne cilin qytet doni te kerkoni?: ")
pagenum = int(input("Shtyp Numrin e Faqeve: "))
linku = "https://www.merrjep.com/shpalljet/{}".format(qyteti)

filename = "Merrjep_" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")+".txt"

with open(filename, "w+", encoding='utf-8') as f:

    writer = csv.writer(f)
    i = 1
    while i <= pagenum:

        r = requests.get(linku,"?Page={}".format(i))
        #content = r.content

        soup = BeautifulSoup(r.text, "html5lib")
        x = soup.find_all("div", {'class': 'row row-listing'})

        for thumbnail in x:
            urlpostimet = thumbnail.find('a')['href']
            strs = urlpostimet.replace('/shpallja/', 'https://merrjep.com/shpallja/')
            writer.writerow([strs])
            linqet = strs.split('\n')
            #print(strs)

            for lines in linqet:
                req = urllib.request.Request(lines)
                resp = urllib.request.urlopen(req)
                respData = resp.read().decode('utf-8')
                imgs = re.findall(r'<img src="/Listing/AdDetail/(.*?)" />',str(respData))
                
                for imazhet in imgs:
                    imazhi = imazhet
                    #print(imazhi + "  -  " + lines)
                    allimazet = imazhi.split('\n')

                    for krejta in allimazet:
                       # potestojm = krejta.split("/")
                        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
                        (spliti1,spliti12) = [(s) for s in krejta.split('/')]
                        numri1 = ("px"+spliti12+"="+ spliti1+"; domain=www.merrjep.com; expires=Sun, 17-Nov-2019 19:23:25 GMT; path=/; secure")
                        headers = {'cookie': "VisitorTest1=0ad64cdb-e963-490a-9b1a-88ce53bec6eb; __auc=395944fe16a303f29f8ecf54798; _ga=GA1.2.69928819.1555587607; _fbp=fb.1.1555587607685.277393115; __gads=ID=24dc86f6302cd678:T=1555587625:S=ALNI_MYb1BIbL72ZeStONAZlFS_C9-J3MQ; trc_cookie_storage=taboola%2520global%253Auser-id%3D0100c058-944c-48f6-ad78-ee25c678bf6b-tuct362f997; RecentCat3=; __atuvc=1%7C46; __atssc=google%3B1; _gid=GA1.2.1177526465.1573953467; SetAdCreateId=; RecentCat1=; RecentCat2=; RecentCat3=; RecentCat1=3227; RecentCat2=3013; __asc=0628a32316e7ba6a62f246ee1aa; _gat=1; LastLocation=184; px"+ spliti12 + "=" + spliti1}
                        perfund = ("https://www.merrjep.com/Listing/AdDetail/"+krejta)
                        response = requests.get(perfund, headers=headers)
                        #print( response )
                        img = Image.open(io.BytesIO(response.content))
                        text = pytesseract.image_to_string(img)
                        print( text ) 

                    
            
        i += 1
