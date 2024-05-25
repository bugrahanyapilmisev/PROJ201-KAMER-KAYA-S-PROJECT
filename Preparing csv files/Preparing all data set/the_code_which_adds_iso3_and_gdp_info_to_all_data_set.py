import csv

def gdp_data_sozluk_dondur(data):
    liste = []
    for key in data:
        sozluk = {}
        sozluk["Country"] = key[0]
        sozluk["Country Code"] = key[1]
        sozluk["GDP per capita ($)"] = list(data[key].values())[0]
        sozluk["Year"] = list(data[key].keys())[0]
        liste.append(sozluk)
    return liste

def gdp_data_csv_yaz(output_csv, gdp_country_csv_icin_dondurulen_liste):
    with open(output_csv, "w", newline="", encoding="utf-8") as file:
        header = ["Country", "Country Code", "GDP per capita ($)", "Year", "ISO-3"]
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        for element in gdp_country_csv_icin_dondurulen_liste:
            element['ISO-3'] = element['Country Code']  # ISO-3 kodunu dolduruyoruz
            writer.writerow(element)
    print(output_csv, "isimli dosya başarıyla oluşturuldu")

def ana_dataset_guncelle(main_dataset_csv, gdp_country_csv_icin_dondurulen_liste, output_csv):
    # GDP verilerini country ismine göre kolay erişim için yeniden düzenliyoruz
    gdp_per_capita_basit_sozluk = {item['Country']: item for item in gdp_country_csv_icin_dondurulen_liste}

    with open(main_dataset_csv, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames + ['GDP per capita ($)', 'ISO-3']
        rows = [row for row in reader]

    for row in rows:
        country = row['Country']
        if country in gdp_per_capita_basit_sozluk:
            row['GDP per capita ($)'] = gdp_per_capita_basit_sozluk[country]['GDP per capita ($)']
            row['ISO-3'] = gdp_per_capita_basit_sozluk[country]['Country Code']
        else:
            row['GDP per capita ($)'] = None
            row['ISO-3'] = None

    with open(output_csv, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(output_csv, "isimli dosya başarıyla güncellendi")

# Örnek kullanım
data = {
    ('Angola', 'AGO'): {'2022': '3000.44423053173'},
    ('Argentina', 'ARG'): {'2022': '13650.6046294524'},
    ('Australia', 'AUS'): {'2022': '65099.8459118981'},
    ('Austria', 'AUT'): {'2022': '52084.6811953372'},
    ('Bangladesh', 'BGD'): {'2022': '2688.30550090738'},
    ('Belgium', 'BEL'): {'2022': '49926.8254295305'},
    ('Brazil', 'BRA'): {'2022': '8917.67491057495'},
    ('Cambodia', 'KHM'): {'2022': '1759.60802346044'},
    ('Canada', 'CAN'): {'2022': '55522.445687688'},
    ('Rest Caribbean', 'CSS'): {'2022': '12639.7046226653'},
    ('Chile', 'CHL'): {'2022': '15355.4797401048'},
    ('China', 'CHN'): {'2022': '12720.2163182363'},
    ('Colombia', 'COL'): {'2022': '6624.16539269075'},
    ('Costa Rica', 'CRI'): {'2022': '13365.3563992692'},
    ('Cuba', 'CUB'): {'2020': '9499.57250428248'},
    ('Czech Republic', 'CZE'): {'2022': '27226.6156386023'},
    ('Denmark', 'DNK'): {'2022': '67790.0539923276'},
    ('Ecuador', 'ECU'): {'2022': '6391.28248430643'},
    ('Egypt', 'EGY'): {'2022': '4295.40749561014'},
    ('Ethiopia', 'ETH'): {'2022': '1027.58591095964'},
    ('Finland', 'FIN'): {'2022': '50871.9304508821'},
    ('France', 'FRA'): {'2022': '40886.2532680273'},
    ('Germany', 'DEU'): {'2022': '48717.9911402128'},
    ('Greece', 'GRC'): {'2022': '20867.2690861087'},
    ('Guatemala', 'GTM'): {'2022': '5473.20856444589'},
    ('Honduras', 'HND'): {'2022': '3040.17304596842'},
    ('Hungary', 'HUN'): {'2022': '18390.1849993244'},
    ('Iceland', 'ISL'): {'2022': '73466.7786674708'},
    ('India', 'IND'): {'2022': '2410.88802070689'},
    ('Indonesia', 'IDN'): {'2022': '4787.99930771921'},
    ('Iraq', 'IRQ'): {'2022': '5937.19546600271'},
    ('Ireland', 'IRL'): {'2022': '103983.29133582'},
    ('Israel', 'ISR'): {'2022': '54930.9388075096'},
    ('Italy', 'ITA'): {'2022': '34776.423234274'},
    ('Jamaica', 'JAM'): {'2022': '6047.2164567796'},
    ('Japan', 'JPN'): {'2022': '34017.2718075024'},
    ('Korea', 'KOR'): {'2022': '32422.5744864287'},
    ('Laos', 'LAO'): {'2022': '2054.43078086496'},
    ('Lebanon', 'LBN'): {'2021': '4136.14657516013'},
    ('Libya', 'LBY'): {'2022': '6716.09598462328'},
    ('Malaysia', 'MYS'): {'2022': '11993.1876132994'},
    ('Mexico', 'MEX'): {'2022': '11496.5228716049'},
    ('Rest of Middle East', 'MEA'): {'2022': '8973.86258463759'},
    ('Mongolia', 'MNG'): {'2022': '5045.50470031666'},
    ('Morocco', 'MAR'): {'2022': '3441.99145507813'},
    ('Namibia', 'NAM'): {'2022': '5031.11503011478'},
    ('Nepal', 'NPL'): {'2022': '1336.54604729847'},
    ('Netherlands', 'NLD'): {'2022': '57025.01245598'},
    ('New Zealand', 'NZL'): {'2022': '48418.5916631992'},
    ('Nigeria', 'NGA'): {'2022': '2162.63373428577'},
    ('Norway', 'NOR'): {'2022': '108729.18690323'},
    ('Pakistan', 'PAK'): {'2022': '1588.8798287911'},
    ('Peru', 'PER'): {'2022': '7125.82993135746'},
    ('Philippines', 'PHL'): {'2022': '3498.5098055874'},
    ('Poland', 'POL'): {'2022': '18688.0044867103'},
    ('Portugal', 'PRT'): {'2022': '24515.2658507319'},
    ('Puerto Rico', 'PRI'): {'2022': '35208.6371888414'},
    ('Russia', 'RUS'): {'2022': '15270.7060546875'},
    ('Saudi Arabia', 'SAU'): {'2022': '30447.8837074473'},
    ('Somalia', 'SOM'): {'2022': '592.103121972088'},
    ('Spain', 'ESP'): {'2022': '29674.5442864413'},
    ('Sudan', 'SDN'): {'2022': '1102.146484375'},
    ('Sweden', 'SWE'): {'2022': '56424.2846986686'},
    ('Switzerland', 'CHE'): {'2022': '93259.9057183024'},
    ('Thailand', 'THA'): {'2022': '6909.9562847948'},
    ('Turkey', 'TUR'): {'2022': '10674.5041731531'},
    ('UK', 'GBR'): {'2022': '46125.2557513568'},
    ('US', 'USA'): {'2022': '76329.5822652029'},
    ('Venezuela', 'VEN'): {'2014': '15975.7293753361'},
    ('Vietnam', 'VNM'): {'2022': '4163.51429874522'},
    ('Palestine', 'PSE'): {'2022': '3789.32796575153'},
    ("Scotland", "GBR"): {"2022": '46125.2557513568'},
    ("England", "GBR"): {"2022": '46125.2557513568'},
    ("Wales", "GBR"): {"2022": "46125.2557513568"},
    ("Rest Eastern European", "NA"): {"2022": "14800.00"}
}

gdp_country_csv_icin_dondurulen_liste = gdp_data_sozluk_dondur(data)
output_csv = "main dataset.csv"
main_dataset_csv = ".csv"

gdp_data_csv_yaz(output_csv, gdp_country_csv_icin_dondurulen_liste)
ana_dataset_guncelle(main_dataset_csv, gdp_country_csv_icin_dondurulen_liste, output_csv)
