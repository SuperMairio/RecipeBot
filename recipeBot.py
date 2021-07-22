import random
import csv
from typing import List
#import discord
#from discord.ext import commands

recipesList = []

def GetRecipe():
    with open("recipes.csv") as recipes: 
        reader = csv.reader(recipes, delimiter=',')
        for row in reader:
            recipesList.append(row)
    return(recipesList)
    
def ListRecipes(recipesList, all):
    if all == True: 
        print(f"There are {len(recipesList)} recipes")
        for r in recipesList:
            print(r[0])
    else:
        ShuffleRecipes(recipesList)

def ShuffleRecipes(recipesList):
    del recipesList[0]
    recipe = random.choice(recipesList)
    print(recipe[0])


ListRecipes(GetRecipe(), False)