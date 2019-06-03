from random import *
from time import *

class Hero(object):
  def __init__(self, heroName, health, agility, strength):
    self.heroName = heroName
    self.health = health
    self.agility = agility
    self.strength = strength

  def attack(self, opponentName):
    opponentName.health -= self.strength

class inventoryItems(Hero):
  def __init__(self, itemName, ability, value):
    self.itemName = itemName
    self.ability = ability
    self.value = value

  def buff(self, heroName):
    heroName.strength += self.value
    heroName.health += self.value
    heroName.agility += self.value

  def speedy(self, heroName):
    heroName.agility += self.value

  def commitDie(self, heroName):
    heroName.health = 0

magicMushrooms = inventoryItems('Magic Mushrooms', 'Buff', 400)
Meth = inventoryItems('Meth', 'Commit suicide', 0)
NikeShoes = inventoryItems('Nike Shoes', 'Speed buff', 1000)

print("Welcome to Eric's game called Commit Die Arena!")

userInput = int(input("Enter the number of players: "))
heroes = []
heroNames = []

for i in range(userInput):
  heroName = input("Enter the name of hero #" + str(i+1) + ": ")
  if heroName in heroNames:
    while heroName in heroNames:
      heroName = input("This hero already exists. Enter the name of hero #" + str(i+1) + ": ")
  hero = Hero(heroName, 15000, 700, 1500)
  heroes.append(hero)
  heroNames.append(heroName)

while len(heroes) > 1:
  heroSpeeds = []
  heroesAlive = []

  for i in heroes:
    if i.health > 0:
      heroesAlive.append([i.agility, i])
      heroSpeeds.append(i.agility)

  heroOrder = []
  heroNamesAlive = []

  for i in range(len(heroSpeeds)):
    for j in range(len(heroesAlive)):
      if max(heroSpeeds) in heroesAlive[j]:
        heroOrder.append(heroesAlive[j][1])
        heroNamesAlive.append(heroesAlive[j][1].heroName)
        heroSpeeds.remove(max(heroSpeeds))
        heroesAlive.remove(heroesAlive[j])
        break
  
  order = "\nOrder of attacking: "
  for i in heroNamesAlive:
    if i == heroNamesAlive[-1]:
      order += i
    else:
      order += i + ", "

  print(order)
  sleep(1)

  for i in range(len(heroOrder)):
    if heroOrder[i].health > 0 and len(heroes) > 1:
      print("\nNow it's " + heroOrder[i].heroName + "'s turn.")
      attack = input("Who would you like to attack? ")
      if attack not in heroNames or heroOrder[heroNames.index(attack)].health <= 0:
        while attack not in heroNames:
          attack = input("That is not a valid input. Who would you like to attack? ")
      
      heroAttacked = heroOrder[heroNamesAlive.index(attack)]
      heroOrder[i].attack(heroAttacked)
      if heroAttacked.health > 0:
        print(heroAttacked.heroName + " now has " + str(heroAttacked.health) + " health left.")

      else:
        print(heroAttacked.heroName + " is now ded :(")
        heroes.remove(heroAttacked)
        heroNames.remove(heroAttacked.heroName)
      
      sleep(1)

      print("\n" + heroOrder[i].heroName + " will now spin the wheel to win a free inventory item! Here is a list of all the possible items and their functions:")
      print("Magic Mushrooms: Strength, health, and speed increase by 400")
      print("Meth: Commit suicide")
      print("Nike Shoes: Speed increase by 1000")
      spin = input("Press enter to spin the wheel:")

      sleep(0.5)
      randomNumber = randint(1,4)
      if randomNumber == 1:
        magicMushrooms.buff(heroOrder[i])
        print(heroOrder[i].heroName + " was buffed by magic mushrooms!")
        
      elif randomNumber == 2:
        Meth.commitDie(heroOrder[i])
        heroes.remove(heroOrder[i])
        heroNames.remove(heroOrder[i].heroName)
        print(heroOrder[i].heroName + " has commited die due to meth :(")
        
      elif randomNumber == 3:
        NikeShoes.speedy(heroOrder[i])
        print(heroOrder[i].heroName + " obtained Nike Shoes to increase their agility!")
        
      else:
        print(heroOrder[i].heroName + " did not get an inventory item.")

      print(heroOrder[i].heroName + " has now finished their turn.\n")

    elif heroOrder[i].health <= 0:
      print("Looks like " + heroOrder[i].heroName + " is ded :(")
      sleep(1)
    
    else:
      print("\nNow it's " + heroOrder[i].heroName + "'s turn.")
      print("\n" + heroOrder[i].heroName + " will now spin the wheel to win a free inventory item! Here is a list of all the possible items and their functions:")
      print("Magic Mushrooms: Strength, health, and speed increase by 400")
      print("Meth: Commit suicide")
      print("Nike Shoes: Speed increase by 1000")
      spin = input("Press enter to spin the wheel:")

      sleep(0.5)
      randomNumber = randint(1,4)
      if randomNumber == 1:
        magicMushrooms.buff(heroOrder[i])
        print(heroOrder[i].heroName + " was buffed by magic mushrooms!")
        
      elif randomNumber == 2:
        Meth.commitDie(heroOrder[i])
        heroes.remove(heroOrder[i])
        heroNames.remove(heroOrder[i].heroName)
        print(heroOrder[i].heroName + " has commited die due to meth :(")
        
      elif randomNumber == 3:
        NikeShoes.speedy(heroOrder[i])
        print(heroOrder[i].heroName + " obtained Nike Shoes to increase their agility!")
        
      else:
        print(heroOrder[i].heroName + " did not get an inventory item.")

      print(heroOrder[i].heroName + " has now finished their turn.\n")
  
  if len(heroes) == 1:
    print("The game has ended. " + heroes[0].heroName + " has won Commit Die Arena!")

  elif len(heroes) == 0:
    print("Everyone has miraculously commited die :)")
    
  else:
    print("The round has ended. Let the battles commence again!\n")
    sleep(1)
