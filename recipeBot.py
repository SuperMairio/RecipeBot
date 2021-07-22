import random
import csv
from typing import List
#import discord
#from discord.ext import commands

recipesList = []

def ListRecipes():
    with open("recipes.csv") as recipes: 
        reader = csv.reader(recipes, delimiter=',')
        for row in reader:
            recipesList.append(row)
        
    print(f"There are {len(recipesList)} recipes")
        
    for r in recipesList:
        print(r[0])

def ShuffleRecipes():
    recipe = ""
    return recipe

def GetRecipe():
    recipe = ""
    return recipe

ListRecipes()