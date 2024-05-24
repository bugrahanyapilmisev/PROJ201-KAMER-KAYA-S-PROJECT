# PROJ201-KAMER-KAYA-S-PROJECT
In this project, we aimed to visualize the cuisines of different regions, their time spent on preparing food, and also the GDP per capita information of countries. We used choropleth maps to visualize these correlations.


Steps:
#DATA COLLECTION
-We have gathered the info about recipes, geographical info, nutrition info, and preparation info from the website "https://cosylab.iiitd.edu.in/recipedb/" and printed out them on a single .csv file.
-Since some of the recipes in recipe_info.csv have blank info about ready-in-time info, we wrote a code that detects the recipes with missing ready-in-time info and opens the page which has info about prep-time and given in the corresponding recipe's "https://cosylab.iiitd.edu.in/recipedb/" page, and adds the prep-time info to our recipe_info.csv.
-We have directly downloaded GDP_per_capita.csv file from "https://www.imf.org/en/Data](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD".
-We have manually collected ISO-3 code of countries from "https://tr.wikipedia.org/wiki/ISO_3166-1_alpha-3" website and added them to our recipe_info.csv to print out choropleth maps on plotly.

#CREATING CHOROPLETH MAPS
-With the help of a plotly modulo called "express", we created 3 different choropleth maps which are about average ready-in-time per country, variety of ingredients used in recipes by countries, and general GDP_per_capita per country.



Challenging parts in the project:
-Since some of the countries, have no name column in recipe_info.csv, for example, Angola's name in our csv file was just "Rest of Africa". So, while creating sub .csv files to create maps we manually added the names of countries that have the same problem.
