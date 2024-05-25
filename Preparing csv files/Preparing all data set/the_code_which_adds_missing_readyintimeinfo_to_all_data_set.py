"""EKSİK PREPARATİON TIME OLAN TARİFLERİN ALLRECİPES/GENİUSKİTCHEN/FOOD.COM SİTESİNDEKİ SAYFALARININ URLSİNİ RECİPEDB'DEN ÇEKEN KOD"... """


import requests
import csv
from bs4 import BeautifulSoup
import concurrent.futures


dataset=[]
header_dataset=["Recipe ID","Recipe Title","Continent","Geocultural Region","Country","ISO-3 Code","GDP per capita ($)","Region","Preparation Time","Cooking Time","Ready In","Preparation Time Text","Calories (kCal)","Protein (g)","Carbohydrates (g)","Total fats (g)","Ingredients","RecipeDB URL","Source Type","Source URL"]
header=["Recipe ID","RecipeDB URL","Source URL","Source Type"]

"""liste={  {id: ... , {"Source Type":...., "Source URL":...   }}

}"""

out_dict={}
with open("v2_17.05.2024_0300.csv","r",encoding="utf-8") as file:
    reader=csv.DictReader(file,fieldnames=header)
    next(reader)
    for satir in reader:
        source_type=satir["Source Type"]
        source_url=satir["Source URL"]
        recipeid=satir["Recipe ID"]

        key_dict={"Source Type": source_type,"Source URL":source_url}
        out_dict[recipeid]=key_dict

bilgiler=[]
with open("READY IN DEĞERİ OLMAYANLAR.csv","r",encoding="utf-8") as infile:
    reader=csv.DictReader(infile,fieldnames=header_dataset)
    next(reader)
    for satir in reader:
        if satir["Recipe ID"] in out_dict.keys():
            value=out_dict[satir["Recipe ID"]]
            satir["Source Type"]=value["Source Type"]
            satir["Source URL"]=value["Source URL"]
            bilgiler.append(satir)
        else:
            bilgiler.append(satir)
with open("v2_READY_IN_DEGERİ_OLMAYANLAR.csv","w",newline="",encoding="utf-8") as outfile:
    writer=csv.DictWriter(outfile,fieldnames=header_dataset)
    writer.writeheader()
    for satir in bilgiler:
        writer.writerow(satir)


dataset=[]

header=['Recipe ID', 'Recipe Title', 'Continent', 'Geocultural Region', 'Country', 'ISO-3 Code', 'GDP per capita ($)', 'Region', 'Preparation Time', 'Cooking Time', 'Ready In', 'Preparation Time Text', 'Calories (kCal)', 'Protein (g)', 'Carbohydrates (g)', 'Total fats (g)', 'Ingredients', 'RecipeDB URL', 'Source Type', 'Source URL']
sozluk={}
output_csv="17.05.2024_0300.csv"

with open("READY IN DEĞERİ OLMAYANLAR.csv","r",encoding="utf-8") as infile:
   reader=csv.DictReader(infile,fieldnames=header)
   next(reader)
   for satir in reader:
       if satir["Source URL"] =="NaN":
           dataset.append(satir)

for element in dataset:
    sozluk[element["Recipe ID"]]=element["RecipeDB URL"]

for key in sozluk.keys():
    url=sozluk[key]

def scrape(recipeid):
    print(recipeid)
    url=sozluk[recipeid]

    response=requests.get(url)
    if response.status_code==200:
        soup=BeautifulSoup(response.text,'html.parser')
        collection_li=soup.find('ul',class_='collection')

        if collection_li:
            link_elements=collection_li.find_all('li', class_="collection-item avatar")
            if len(link_elements)>2:
                link_element=link_elements[2]
                a_tag = link_element.find('a')
                if a_tag:
                    source_url=a_tag["href"]
                    link_text = a_tag.get_text(strip=True).replace('\n', '').replace('  ', ' ')


                    if source_url:
                        if link_text:
                            with open(output_csv,"a",newline="",encoding="utf-8") as file:
                                writer=csv.writer(file)
                                writer.writerow([recipeid,url,source_url,link_text])

                        else:
                            with open(output_csv,"a",newline="",encoding="utf-8") as file2:
                                writer2=csv.writer(file2)
                                writer2.writerow([recipeid,url,source_url,"NaN"])

                    else:
                        if link_text:
                            with open(output_csv,"a",newline="",encoding="utf-8") as file3:
                                writer3=csv.writer(file3)
                                writer3.writerow([recipeid,url,"NaN",link_text])

                        else:
                            with open(output_csv,"a",newline="",encoding="utf-8") as file4:
                                writer4=csv.writer(file4)
                                writer4.writerow([recipeid,url,"NaN","NaN"])

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(scrape, sozluk.keys())




