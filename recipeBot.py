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
    print("\n---------------------------------------\n")
    try:
        choice = input("1 = Show all recipes\n2 = Get random recipe\n3 = Search recipes\nq = Quit\nPlease choose one: ")
        return choice
    except(ValueError):
        print("Sorry I don't recognise that input")
        return GetInput()

def ListRecipes(recipesList):
    print(f"There are {len(recipesList)} recipes")
    for r in recipesList:
        print(r[0])


def ShuffleRecipes(recipesList):
    del recipesList[0]
    recipe = random.choice(recipesList)
    print(recipe[0])

def SearchList(recipesList):
    x = 0

    choice = GetInput()
    while choice.upper() != "Q":
        if choice == "1": #List all
            print("\n---------------------------------------\n")
            ListRecipes(recipesList)
            choice = GetInput()

        elif choice == "2": #Get random
            print("\n---------------------------------------\n")
            ShuffleRecipes(recipesList)
            choice = GetInput()

        elif choice == "3": #Search 
            print("\n---------------------------------------\n")
            searchType = int(input("1 = Search by letter\n2 = Search by keyword\nPlease choose one: "))
            if searchType == 1:
                letter = input("Please enter a letter: ")
                print("\n")
                for recipe in recipesList:
                    r = recipe[0]
                    if r[0] == letter:
                        print(recipe[0])
                        x += 1
                if x == 0:
                    print("Sorry there are no recipes starting with that letter")
            elif searchType == 2:
                term = input("Please enter a keyword: ")
                print("\n")
                for recipe in recipesList:
                    if term in recipe[0]:
                        print(recipe[0])
                        x += 1
                if x == 0:
                    print("Sorry there are no recipes with that word in them")
            choice = GetInput()
    quit()

print(" ---------- R E C I P E   B O T ----------")
recipes = GetRecipe()
SearchList(recipes)