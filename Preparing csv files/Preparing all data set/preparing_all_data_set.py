import requests
from bs4 import BeautifulSoup
import pandas as pd

""" Hello everyone, this is the final version of the code. You need to change start and finish points which be assigned you. """
""" After the code finished to run, the .csv file with name recipedb_data_(startpoint)_(finishpoint).csv is expected to created in the content file in panel at the left"""
""" You need to upload this .csv file to our drive file where you can find that PROJ201 > Data > RecipeDB Data """

def recipe_data_scrape(recipe_id):
  recipe_db_url="https://cosylab.iiitd.edu.in/recipedb/search_recipeInfo/" + str(recipe_id)
  response=requests.get(recipe_db_url)
  if response.status_code == 200:
    soup=BeautifulSoup(response.text, 'html.parser')

    #Recipe Name
    recipe_name=soup.find('center').text.strip()

    #Region
    region_element = soup.find('ul', class_="collection").find_all('li', class_='collection-item avatar')[0]
    recipe_region = region_element.find('p').text.strip()

    #Dietary style
    dietary_element=soup.find_all('li', class_='collection-item avatar')[1]
    dietary_style=dietary_element.find('p',id="dietary-text").text.strip()

    #Prep and cooking time
    prep_time_element=soup.find('ul',class_="collection").find_all('li', class_='collection-item avatar')[2]
    prep_time_text=prep_time_element.find('p').text.strip()


    # Nutritional Information
    nutritional_table = soup.find('table', class_='highlight striped')
    nutritional_data_show_less = {}
    nutritional_data_show_more = {}
    for row in nutritional_table.find_all('tr'):
      columns = row.find_all('td')
      if len(columns) == 2:
        nutrient = columns[0].strong.text.strip()
        quantity = columns[1].text.strip()
        if 'bigRows' in row['class']:
          nutritional_data_show_more[nutrient] = quantity
        else:
          nutritional_data_show_less[nutrient] = quantity

    protein = nutritional_data_show_less.get("Protein (g)", "")
    kalori = nutritional_data_show_less.get("Energy (kCal)", "")
    karbonhidrat = nutritional_data_show_less.get("Carbohydrates (g)", "")
    yag = nutritional_data_show_less.get("Total fats (g)", "")

  # Ingredients
    ingredients_data = []
    ingredient_response = requests.get(recipe_db_url + "#ingredient_nutri")
    if ingredient_response.status_code == 200:
      ingredient_soup = BeautifulSoup(ingredient_response.text, 'html.parser')
      ingredient_table = ingredient_soup.find('table', id='myTable')
      for row in ingredient_table.find('tbody').find_all('tr'):
        row_data = [td.text.strip() for td in row.find_all('td')]
        ingredients_data.append(row_data[0])

      recipe_dict = {
            'Recipe ID': recipe_id,
            'Recipe Title': recipe_name,
            'Region': recipe_region,
            'Dietary Style': dietary_style,
            'Preparation Time Text': prep_time_text,
            "Calories (kCal)": kalori,
            "Protein (g)": protein,
            "Carbohydrates (g)": karbonhidrat,
            "Total fats (g)": yag,
            "Ingredients": ingredients_data,
            'RecipeDB URL': recipe_db_url,
        }
      print(f"Recipe ID: {recipe_id}")
      print(f"Recipe_name:{recipe_name}")
      print(f"\nRegion: {recipe_region}")
      print(f"Dietary Style: {dietary_style}")
      print(f"Preparation Time: {prep_time_text}")
      print(f"\nCalories (g): {kalori}")
      print(f"Protein (g): {protein}")
      print(f"Carbohydrates (g): {karbonhidrat}")
      print(f"Total fats (g): {yag}")
      print(f"\ningredients_data: {ingredients_data}")
      print(f"\nRecipeDB URL: {recipe_db_url}")
      print("\n")
      return recipe_dict
  else:
    print(f"Error: {response.status_code}")
    return False

#---------
all_recipe_data=[]
#upper bound: 149192
startPoint = 2610
finishPoint = 149192
for i in range(startPoint, finishPoint):
  recipe_data=recipe_data_scrape(i)
  if recipe_data:
    all_recipe_data.append(recipe_data)
  if i%1000 == 0 and i != startPoint and recipe_data != False:
    dataframe=pd.DataFrame(all_recipe_data)
    dataframe.to_csv("recipedb_data_" + str(startPoint) + "_" +str(i) + "_sub_save_file.csv",index=False)
    print(dataframe)

dataframe=pd.DataFrame(all_recipe_data)
dataframe.to_csv("all_data_set")
print(dataframe)