import csv
import pandas as pd
import plotly.express as px


header=['Recipe ID', 'Recipe Title', 'Continent', 'Geocultural Region', 'Country', 'ISO-3 Code', 'GDP per capita ($)', 'Region', 'Preparation Time', 'Cooking Time', 'Ready In', 'Preparation Time Text', 'Calories (kCal)', 'Protein (g)', 'Carbohydrates (g)', 'Total fats (g)', 'Ingredients', 'RecipeDB URL', 'Source Type', 'Source URL']

main_dict={}
with open("all_data_set.csv","r",encoding="utf-8") as file:
  reader=csv.DictReader(file)
  next(reader)
  for satir in reader:
    ülke = satir["Country"]
    malzeme = satir["Ingredients"].replace("[","")
    malzeme = malzeme.replace("]","")
    malzeme = malzeme.split(", ")
    if ülke not in main_dict:
      main_dict[ülke] = malzeme
    else:
      for i in malzeme:
        if i not in main_dict[ülke]:
          main_dict[ülke].append(i)

variety_dict ={}

for k,v in main_dict.items():
  if k not in variety_dict:
    variety_dict[k] = len(v)
#print(variety_dict)

farklı_ulkeler=['Yemen', 'Oman', 'Bolivia', 'Uruguay', 'Guyana', 'Belarus', 'Ukraine', 'Bulgaria', 'Romania', 'Moldova', 'Luxembourg', 'Andorra', 'Paraguay', 'Algeria', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad', 'Comoros', 'Congo', 'Congo Democratic Republic of the', 'Djibouti', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Ivory Coast', 'Kenya', 'Lesotho', 'Liberia', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Mozambique', 'Niger', 'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'South Africa', 'South Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']



variety_dict["Yemen"]=variety_dict["Rest of Middle East"]/2
variety_dict["Omman"]=variety_dict["Rest of Middle East"]/2

variety_dict["Belarus"]=int(variety_dict["Rest Eastern European"]/7)+1
variety_dict["Ukraine"]=int(variety_dict["Rest Eastern European"]/7)+1
variety_dict["Bulgaria"]=int(variety_dict["Rest Eastern European"]/7)+1
variety_dict["Romania"]=int(variety_dict["Rest Eastern European"]/7)+1
variety_dict["Moldova"]=int(variety_dict["Rest Eastern European"]/7)+1
variety_dict["Luxembourg"]=int(variety_dict["Rest Eastern European"]/7)+1
variety_dict["Andorra"]=int(variety_dict["Rest Eastern European"]/7)+1

variety_dict["Uruguay"]=int((variety_dict["Argentina"]+variety_dict["Brazil"]+variety_dict["Colombia"]+variety_dict["Chile"]+variety_dict["Peru"]+variety_dict["Ecuador"]+variety_dict["Venezuela"])/7)+1
variety_dict["Bolivia"]=int((variety_dict["Argentina"]+variety_dict["Brazil"]+variety_dict["Colombia"]+variety_dict["Chile"]+variety_dict["Peru"]+variety_dict["Ecuador"]+variety_dict["Venezuela"])/7)+1
variety_dict["Guyana"]=int((variety_dict["Argentina"]+variety_dict["Brazil"]+variety_dict["Colombia"]+variety_dict["Chile"]+variety_dict["Peru"]+variety_dict["Ecuador"]+variety_dict["Venezuela"])/7)+1
variety_dict["Paraguay"]=int((variety_dict["Argentina"]+variety_dict["Brazil"]+variety_dict["Colombia"]+variety_dict["Chile"]+variety_dict["Peru"]+variety_dict["Ecuador"]+variety_dict["Venezuela"])/7)+1

afrika_ortalama=(variety_dict["Nigeria"]+variety_dict["Somalia"]+variety_dict["Namibia"]+variety_dict["Angola"]+variety_dict["Sudan"]+variety_dict["Ethiopia"])/6



variety_dict["Algeria"]=int(afrika_ortalama)+1
variety_dict["Benin"]=int(afrika_ortalama)+1
variety_dict["Botswana"]=int(afrika_ortalama)+1
variety_dict["Burkina Faso"]=int(afrika_ortalama)+1
variety_dict["Burundi"]=int(afrika_ortalama)+1
variety_dict["Cabo Verde"]=int(afrika_ortalama)+1
variety_dict["Cameroon"]=int(afrika_ortalama)+1
variety_dict["Central African Republic"]=int(afrika_ortalama)+1
variety_dict["Chad"]=int(afrika_ortalama)+1
variety_dict["Comoros"]=int(afrika_ortalama)+1
variety_dict["Congo"]=int(afrika_ortalama)+1
variety_dict["Congo Democratic Republic of the"]=int(afrika_ortalama)+1
variety_dict["Djibouti"]=int(afrika_ortalama)+1
variety_dict["Equatorial Guinea"]=int(afrika_ortalama)+1
variety_dict["Eritrea"]=int(afrika_ortalama)+1
variety_dict["Eswatini"]=int(afrika_ortalama)+1
variety_dict["Gabon"]=int(afrika_ortalama)+1
variety_dict["Gambia"]=int(afrika_ortalama)+1
variety_dict["Ghana"]=int(afrika_ortalama)+1
variety_dict["Guinea"]=int(afrika_ortalama)+1
variety_dict["Guinea-Bissau"]=int(afrika_ortalama)+1
variety_dict["Ivory Coast"]=int(afrika_ortalama)+1
variety_dict["Kenya"]=int(afrika_ortalama)+1
variety_dict["Lesotho"]=int(afrika_ortalama)+1
variety_dict["Liberia"]=int(afrika_ortalama)+1
variety_dict["Madagascar"]=int(afrika_ortalama)+1
variety_dict["Malawi"]=int(afrika_ortalama)+1
variety_dict["Mali"]=int(afrika_ortalama)+1
variety_dict["Mauritania"]=int(afrika_ortalama)+1
variety_dict["Mauritius"]=int(afrika_ortalama)+1
variety_dict["Mozambique"]=int(afrika_ortalama)+1
variety_dict["Niger"]=int(afrika_ortalama)+1
variety_dict["Rwanda"]=int(afrika_ortalama)+1
variety_dict["Sao Tome and Principe"]=int(afrika_ortalama)+1
variety_dict["Senegal"]=int(afrika_ortalama)+1
variety_dict["Seychelles"]=int(afrika_ortalama)+1
variety_dict["Sierra Leone"]=int(afrika_ortalama)+1
variety_dict["South Africa"]=int(afrika_ortalama)+1
variety_dict["South Sudan"]=int(afrika_ortalama)+1
variety_dict["Tanzania"]=int(afrika_ortalama)+1
variety_dict["Togo"]=int(afrika_ortalama)+1
variety_dict["Tunisia"]=int(afrika_ortalama)+1
variety_dict["Uganda"]=int(afrika_ortalama)+1
variety_dict["Zambia"]=int(afrika_ortalama)+1
variety_dict["Zimbabwe"]=int(afrika_ortalama)+1

dataset=[]
for ulke in variety_dict.keys():
  bos_dict={}
  bos_dict["Country"]=ulke
  bos_dict["Ingredients Variety"]=variety_dict[ulke]
  dataset.append(bos_dict)

iso3_code_dict = {
    'Egypt': 'EGY', 'Nigeria': 'NGA', 'Morocco': 'MAR', 'Rest of Middle East': 'XXX',
    'China': 'CHN', 'Thailand': 'THA', 'Indonesia': 'IDN', 'Bangladesh': 'BGD',
    'Vietnam': 'VNM', 'Israel': 'ISR', 'Lebanon': 'LBN', 'Philippines': 'PHL',
    'India': 'IND', 'Korea': 'KOR', 'Malaysia': 'MYS', 'Turkey': 'TUR',
    'Japan': 'JPN', 'Pakistan': 'PAK', 'Australia': 'AUS', 'Mexico': 'MEX',
    'Rest Caribbean': 'XXX', 'Puerto Rico': 'PRI', 'Jamaica': 'JAM', 'Cuba': 'CUB',
    'Argentina': 'ARG', 'Brazil': 'BRA', 'Colombia': 'COL', 'Chile': 'CHL',
    'Peru': 'PER', 'Russia': 'RUS', 'Denmark': 'DNK', 'Scotland': 'GBR',
    'England': 'GBR', 'UK': 'GBR', 'Wales': 'GBR', 'Hungary': 'HUN',
    'Sweden': 'SWE', 'Belgium': 'BEL', 'Norway': 'NOR', 'Austria': 'AUT',
    'Greece': 'GRC', 'France': 'FRA', 'Switzerland': 'CHE', 'Portugal': 'PRT',
    'Italy': 'ITA', 'Poland': 'POL', 'Netherlands': 'NLD', 'Ireland': 'IRL',
    'Germany': 'DEU', 'Rest Eastern European': 'XXX', 'Spain': 'ESP', 'Finland': 'FIN',
    'Czech Republic': 'CZE', 'US': 'USA', 'Canada': 'CAN', 'Somalia': 'SOM',
    'Namibia': 'NAM', 'Angola': 'AGO', 'Libya': 'LBY', 'Sudan': 'SDN',
    'Ethiopia': 'ETH', 'Laos': 'LAO', 'Nepal': 'NPL', 'Cambodia': 'KHM',
    'Palestine': 'PSE', 'Saudi Arabia': 'SAU', 'Mongolia': 'MNG', 'Iraq': 'IRQ',
    'New Zealand': 'NZL', 'Honduras': 'HND', 'Costa Rica': 'CRI', 'Guatemala': 'GTM',
    'Ecuador': 'ECU', 'Venezuela': 'VEN', 'Iceland': 'ISL', 'Yemen': 'YEM',
    'Oman': 'OMN', 'Belarus': 'BLR', 'Ukraine': 'UKR', 'Bulgaria': 'BGR',
    'Romania': 'ROU', 'Moldova': 'MDA', 'Luxembourg': 'LUX', 'Andorra': 'AND',
    'Uruguay': 'URY', 'Bolivia': 'BOL', 'Guyana': 'GUY', 'Paraguay': 'PRY',
    'Algeria': 'DZA', 'Benin': 'BEN', 'Botswana': 'BWA', 'Burkina Faso': 'BFA',
    'Burundi': 'BDI', 'Cabo Verde': 'CPV', 'Cameroon': 'CMR', 'Central African Republic': 'CAF',
    'Chad': 'TCD', 'Comoros': 'COM', 'Congo': 'COG', 'Congo Democratic Republic of the': 'COD',
    'Djibouti': 'DJI', 'Equatorial Guinea': 'GNQ', 'Eritrea': 'ERI', 'Eswatini': 'SWZ',
    'Gabon': 'GAB', 'Gambia': 'GMB', 'Ghana': 'GHA', 'Guinea': 'GIN',
    'Guinea-Bissau': 'GNB', 'Ivory Coast': 'CIV', 'Kenya': 'KEN', 'Lesotho': 'LSO',
    'Liberia': 'LBR', 'Madagascar': 'MDG', 'Malawi': 'MWI', 'Mali': 'MLI',
    'Mauritania': 'MRT', 'Mauritius': 'MUS', 'Mozambique': 'MOZ', 'Niger': 'NER',
    'Rwanda': 'RWA', 'Sao Tome and Principe': 'STP', 'Senegal': 'SEN', 'Seychelles': 'SYC',
    'Sierra Leone': 'SLE', 'South Africa': 'ZAF', 'South Sudan': 'SSD', 'Tanzania': 'TZA',
    'Togo': 'TGO', 'Tunisia': 'TUN', 'Uganda': 'UGA', 'Zambia': 'ZMB',
    'Zimbabwe': 'ZWE'
}

for country_dict in dataset:
    country_name = country_dict['Country']
    country_dict['ISO-3 Code'] = iso3_code_dict.get(country_name, 'N/A')

print(country_dict)


with open("ingredients_variety.csv","w",newline="",encoding="utf-8") as file:
    writer=csv.DictWriter(file,fieldnames=["Country","Ingredients Variety","ISO-3 Code"])
    writer.writeheader()
    for element in dataset:
        writer.writerow(element)