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

def GetInput():
    try:
        choice = input("1 = Show all recipes\n2 = Get random recipe\n3 = Get specific recipe link\nq = Quit\nPlease choose one: ")
        if choice == "q" or choice == "Q":
            exit()
        else:
            return choice
    except(ValueError):
        print("Sorry I don't recognise that input")
        return GetInput()

def ListRecipes(recipesList, x):
    print("---------------------------------------")
    if x == 1: 
        print(f"There are {len(recipesList)} recipes")
        for r in recipesList:
            print(r[0])
    elif x == 2:
        ShuffleRecipes(recipesList)

def ShuffleRecipes(recipesList):
    del recipesList[0]
    recipe = random.choice(recipesList)
    print(recipe[0])

def SearchList(recipesList):
    x = 0

    try:
        choice = int(input("1 = Search recipes by letter\n2 = Search recipes by keyword\nPlease choose one: "))
        if choice == 1:
            letter = input("Please enter a letter: ")
            for recipe in recipesList:
                r = recipe[0]
                if r[0] == letter:
                    print(recipe[0])
                    x += 1
            if x == 0:
                print("Sorry there are no recipes starting with that letter")
                SearchList(recipesList)
        elif choice == 2:
            term = input("Please enter a keyword: ")
            for recipe in recipesList:
                if term in recipe[0]:
                    print(recipe[0])
                    x += 1
            if x == 0:
                print("Sorry there are no recipes with that word in them")
                SearchList(recipesList)
                
    except(ValueError):
        print("Sorry I don't recognise that input")
        SearchList(recipesList)

def RunBot():
    x = GetInput()
    
print(" ---------- R E C I P E   B O T ----------")