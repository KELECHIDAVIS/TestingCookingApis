import requests
import json 


#*** COMPLEX SEARCH ON SPOONCACULAR API HAS MORE OPTIONS SUCH AS CUISINE AND TYPE OF MEAL LIKE BAKING OR DINNER AND STUFF LIKE THAT 


api_key = '0743aa96ec2d4a709255ee8800b01157'
ingredients = 'cheese,chicken,corn,rice'
returnMax =20  # the max amount of recipes returned ; this value can be between 1-100
ranking = 2  # this is what determines the ranking for recipes; 1 means that it tries to maximize used ingredient 2 means it minimizes missing ingredients 
url = f'https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&apiKey={api_key}&number={returnMax}&ranking={ranking}'

cuisine='' # you can also outline a specific cuisine preference 

response = requests.get(url)

with open('spooncacularData.json', 'w') as f:
    json.dump(response.json(), f)


textFile = open("recipesInTextFormat.txt" , 'w') 


    

#print recipe names 

print("**THIS PROGRAM ASSUMES THAT YOU HAVE TYPICAL PANTRY ITEMS LIKE: WATER, SALT, AND FLOUR**\n")

print("Recipes for the ingredients: {}".format(ingredients.split(',')))

textFile.write("**THIS PROGRAM ASSUMES THAT YOU HAVE TYPICAL PANTRY ITEMS LIKE: WATER, SALT, AND FLOUR**\n\n")

textFile.write("Recipes for the ingredients: {}\n\n".format(ingredients.split(',')))
print()
if response.status_code == 200:
    recipes = response.json()
    for recipe in recipes:
        recipeName =recipe['title']+": "+str(recipe["missedIngredientCount"])+" missed ingredients\n"
        print(recipeName , end="")
        textFile.write(recipeName)
        
else:
    print(f'Error: {response.status_code}')
    
textFile.close() 
