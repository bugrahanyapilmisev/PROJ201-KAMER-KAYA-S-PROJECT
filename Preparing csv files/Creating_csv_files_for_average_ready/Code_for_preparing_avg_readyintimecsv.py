import pandas as pd
import csv

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
    'Zimbabwe': 'ZWE' }

tobeadded=['Yemen', 'Oman', 'Bolivia', 'Uruguay', 'Guyana', 'Belarus', 'Ukraine', 'Bulgaria', 'Romania', 'Moldova', 'Luxembourg', 'Andorra', 'Paraguay', 'Algeria', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad', 'Comoros', 'Congo', 'Congo Democratic Republic of the', 'Djibouti', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Ivory Coast', 'Kenya', 'Lesotho', 'Liberia', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Mozambique', 'Niger', 'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'South Africa', 'South Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']
csv_path=r"all_data_set.csv"

def calculate_average_per_countries(csv_path):
    df = pd.read_csv(csv_path)
    df['Ready In'] = pd.to_numeric(df['Ready In'], errors='coerce')
    df = df.dropna(subset=['Ready In'])
    country_ready_in_avg = df.groupby('Country')['Ready In'].mean()
    country_ready_in_avg_dict = country_ready_in_avg.to_dict()
    return country_ready_in_avg_dict

def ozel_csv_hazırla(csv_path, country_readyin):
    df = pd.read_csv(csv_path, usecols=['Country', 'ISO-3 Code'])
    country_iso3 = df.drop_duplicates().set_index('Country').to_dict()['ISO-3 Code']

    dataset = []
    for country, avg_ready_in in country_readyin.items():
        if country in country_iso3:
            dataset.append({
                'Country': country,
                'ISO-3': country_iso3[country],
                'Avg Ready In': avg_ready_in
            })

    header_kucuk = ["Country", "ISO-3", "Avg Ready In"]
    with open("average_readyin_by_countries.csv", "w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=header_kucuk)
        writer.writeheader()
        for element in dataset:
            writer.writerow(element)

def rest_ulkeler_add(iso3_code_dict,tobeadded):
    header=["Country","ISO-3","Avg Ready In"]
    dataset=[]
    with open("average_readyin_by_countries.csv","r",encoding="utf-8") as file:
        reader=csv.DictReader(file,fieldnames=header)
        next(reader)
        for satir in reader:
            dataset.append(satir)
    for element in tobeadded:
        bossozluk={}
        bossozluk["Country"]=element
        if element in iso3_code_dict.keys():
            bossozluk["ISO-3"]=iso3_code_dict[element]
        else:
            bossozluk["ISO-3"]="NaN"
        bossozluk["Avg Ready In"]="NaN"
        dataset.append(bossozluk)

    rest_middle_east_ready=0
    rest_eastern_europe_ready=0
    for element in dataset:
        if element["Country"]=="Rest of Middle East":
            rest_middle_east_ready=element["Avg Ready In"]
        elif element["Country"]=="Rest Eastern European":
            rest_eastern_europe_ready=element["Avg Ready In"]
    rest_eastern_europe_ready=88
    rest_middle_east_ready=145

    for element in dataset:
        if element["Country"]=="Yemen":
            element["Avg Ready In"]=rest_middle_east_ready
        elif element["Country"]=="Oman":
            element["Avg Ready In"]=rest_middle_east_ready
        elif element["Country"]=="Belarus":
            element["Avg Ready In"]=rest_middle_east_ready
        elif element["Country"] == "Ukraine":
            element["Avg Ready In"] = rest_eastern_europe_ready
        elif element["Country"]=="Bulgaria":
            element["Avg Ready In"]=rest_eastern_europe_ready
        elif element["Country"]=="Romania":
            element["Avg Ready In"]=rest_eastern_europe_ready
        elif element["Country"]=="Moldova":
            element["Avg Ready In"]=rest_eastern_europe_ready
        elif element["Country"]=="Luxembourg":
            element["Avg Ready In"]=rest_eastern_europe_ready
        elif element["Country"]=="Andorra":
            element["Avg Ready In"]=rest_eastern_europe_ready

    bas=["Country","ISO-3","Avg Ready In"]
    with open("Avg_Ready_In_26_Mayıs.csv","w",newline="",encoding="utf-8") as outfile:
        writer=csv.DictWriter(outfile,fieldnames=bas)
        writer.writeheader()
        for element in dataset:
            writer.writerow(element)

def x():
    afrika = ["Algeria",
              "Benin",
              "Botswana",
              "Burkina Faso",
              "Burundi",
              "Cabo Verde",
              "Cameroon",
              "Central African Republic",
              "Chad",
              "Comoros",
              "Congo",
              "Congo Democratic Republic of the",
              "Djibouti",
              "Equatorial Guinea",
              "Eritrea",
              "Eswatini",
              "Gabon",
              "Gambia",
              "Ghana",
              "Guinea",
              "Guinea-Bissau",
              "Ivory Coast",
              "Kenya",
              "Lesotho",
              "Liberia",
              "Madagascar",
              "Malawi",
              "Mali",
              "Mauritania",
              "Mauritius",
              "Mozambique",
              "Niger",
              "Rwanda",
              "Sao Tome and Principe",
              "Senegal",
              "Seychelles",
              "Sierra Leone",
              "South Africa",
              "South Sudan",
              "Tanzania",
              "Togo",
              "Tunisia",
              "Uganda",
              "Zambia",
              "Zimbabwe"]
    header=["Country","ISO-3","Avg Ready In"]
    dataset2=[]
    with open("Avg_Ready_In_26_Mayıs.csv","r",encoding="utf-8") as file:
        reader=csv.DictReader(file,fieldnames=header)
        next(reader)
        for satir in reader:
            if satir["Country"] in afrika:
                satir["Avg Ready In"]=156
                dataset2.append(satir)
            else:
                dataset2.append(satir)
    for element in dataset2:
        if element["Country"]=="Bolivia":
            element["Avg Ready In"]=177
        elif element["Country"]=="Uruguay":
            element["Avg Ready In"] = 177
        elif element["Country"]=="Guyana":
            element["Avg Ready In"] = 177
        elif element["Country"]=="Paraguay":
            element["Avg Ready In"] = 177

    with open("latest_avg_ready_in.csv","w",newline="",encoding="utf-8") as file:
        writer=csv.DictWriter(file,fieldnames=["Country","ISO-3","Avg Ready In"])
        writer.writeheader()
        for element in dataset2:
            writer.writerow(element)





country_readyin=calculate_average_per_countries(csv_path)
ozel_csv_hazırla(csv_path, country_readyin)
rest_ulkeler_add(iso3_code_dict,tobeadded)
x()