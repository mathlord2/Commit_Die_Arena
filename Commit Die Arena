import random
import time

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

Eric = Hero('Eric', 14000, 700, 1500)
Trevor = Hero('Trevor', 15000, 500, 2000)
Leo = Hero('Leo', 13000, 750, 1250)

magicMushrooms = inventoryItems('Magic Mushrooms', 'Buff', 400)
Meth = inventoryItems('Meth', 'Commit suicide', 0)
NikeShoes = inventoryItems('Nike Shoes', 'Speed buff', 1000)


print("Welcome to Eric's game called Commit Die Arena! Here are your heroes and their stats:")
print("Eric: 14000 health, 700 agility, 1500 strength")
print("Trevor: 15000 health, 500 agility, 2000 strength")
print("Leo: 13000 health, 750 agility, 1250 strength")

while True:
  if Eric.health > 0 and Leo.health > 0 and Trevor.health <= 0:
    a = [Eric.agility, Leo.agility]
  elif Eric.health > 0 and Trevor.health > 0 and Leo.health <= 0:
    a = [Eric.agility, Trevor.agility]
  elif Trevor.health > 0 and Leo.health > 0 and Eric.health <= 0:
    a = [Trevor.agility, Leo.agility]
  elif Eric.health > 0 and Leo.health > 0 and Trevor.health > 0:
    a = [Eric.agility, Leo.agility, Trevor.agility]

  if Eric.agility == max(a) and Eric.health > 0:
    print("\nEric will make the first move.")
    if Trevor.health > 0 or Leo.health > 0:
      while True:
        c = input("Who would you like to attack? ")
        if c.lower() == 'trevor':
          if Trevor.health > 0:
            Eric.attack(Trevor)
            if Trevor.health > 0:
              print("Trevor now has " + str(Trevor.health) + " health left.")
            else:
              print("Trevor is now ded :(")
          else:
            print("Trevor is already dead. You will attack Leo instead.")
            Eric.attack(Leo)
            if Leo.health > 0:
              print("Leo now has " + str(Leo.health) + " health left.")
            else:
              print("Leo is now ded :(")
          break
        elif c.lower() == 'leo':
          if Leo.health > 0:
            Eric.attack(Leo)
            if Leo.health > 0:
              print("Leo now has " + str(Leo.health) + " health left.")
            else:
              print("Leo is now ded :(")
          else:
            if Trevor.health > 0:
              print("Leo is already dead. You will attack Trevor instead.")
              Eric.attack(Trevor)
              if Trevor.health > 0:
                print("Trevor now has " + str(Trevor.health) + " health left.")
              else:
                print("Trevor is now ded :(")
          break
        else:
            print ("That is not a valid input. Please try again.")

    time.sleep(1)
    print("\nEric will now spin the wheel to win a free inventory item! Here is a list of all the possible items and their functions:")
    print("Magic Mushrooms: Strength and health and speed increase by 400")
    print("Meth: Commit suicide")
    print("Nike Shoes: Speed increase by 1000")
    d = input("Press enter to spin the wheel:")
    time.sleep(0.5)
    if random.randint(1,4) == 1:
      magicMushrooms.buff(Eric)
      print("Eric was buffed by magic mushrooms!")
    elif random.randint(1,4) == 2:
      Meth.commitDie(Eric)
      print("Eric has commited die due to meth :(")
    elif random.randint(1,4) == 3:
      NikeShoes.speedy(Eric)
      print("Eric obtained Nike Shoes to increase his agility!")
    else:
      print("Eric did not get an inventory item.")

    print("Eric has now finished his turn.")

    if Trevor.agility > Leo.agility and Trevor.health > 0:
      print("\nNow it's Trevor's turn.")
      if Eric.health > 0 or Leo.health > 0:
        while True:
          c = input("Who would you like to attack? ")
          if c.lower() == 'eric':
            if Eric.health > 0:
              Trevor.attack(Eric)
              if Eric.health > 0:
                print("Eric now has " + str(Eric.health) + " health left.")
              else:
                print("Eric is now ded :(")
            else:
              print("Eric is already dead. You will attack Leo instead.")
              Eric.attack(Leo)
              if Leo.health > 0:
                print("Leo now has " + str(Leo.health) + " health left.")
              else:
                print("Leo is now ded :(")
            break
          elif c.lower() == 'leo':
            if Leo.health > 0:
              Trevor.attack(Leo)
              if Leo.health > 0:
                print("Leo now has " + str(Leo.health) + " health left.")
              else:
                print("Leo is now ded :(")
            else:
              print("Leo is already dead. You will attack Eric instead.")
              Trevor.attack(Eric)
              if Eric.health > 0:
                print("Eric now has " + str(Eric.health) + " health left.")
              else:
                print("Eric is now ded :(")
            break
          else:
            print ("That is not a valid input. Please try again.")
      time.sleep(1)
      print("\nTrevor will now spin the wheel to win a free inventory item! Here is a list of all the possible items and their functions:")
      print("Magic Mushrooms: Strength and health increase by 400")
      print("Meth: Commit suicide")
      print("Nike Shoes: Speed increase by 1000")
      d = input("Press enter to spin the wheel:")
      time.sleep(0.5)
      if random.randint(1,4) == 1:
        magicMushrooms.buff(Trevor)
        print("Trevor was buffed by magic mushrooms!")
      elif random.randint(1,4) == 2:
        Meth.commitDie(Trevor)
        print("Trevor has commited die due to meth :(")
      elif random.randint(1,4) == 3:
        NikeShoes.speedy(Trevor)
        print("Trevor obtained Nike Shoes to increase his agility!")
      else:
        print("Trevor did not get an inventory item.")

      print("Trevor has now finished his turn.")

      if Leo.health > 0:
        print("\nNow it's Leo's turn.")
        if Eric.health > 0 or Trevor.health > 0:
          while True:
            c = input("Who would you like to attack? ")
            if c.lower() == 'eric':
              if Eric.health > 0:
                Leo.attack(Eric)
                if Eric.health > 0:
                  print("Eric now has " + str(Eric.health) + " health left.")
                else:
                  print("Eric is now ded :(")
              else:
                print("Eric is already dead. You will attack Trevor instead.")
                Leo.attack(Trevor)
                if Trevor.health > 0:
                  print("Trevor now has " + str(Trevor.health) + " health left.")
                else:
                  print("Trevor is now ded :(")
              break
            elif c.lower() == 'trevor':
              if Trevor.health > 0:
                Leo.attack(Trevor)
                if Leo.health > 0:
                  print("Trevor now has " + str(Trevor.health) + " health left.")
                else:
                  print("Trevor is now ded :(")
              else:
                print("Trevor is already dead. You will attack Eric instead.")
                Leo.attack(Eric)
                if Eric.health > 0:
                  print("Eric now has " + str(Eric.health) + " health left.")
                else:
                  print("Eric is now ded :(")
              break
            else:
              print ("That is not a valid input. Please try again.")

        time.sleep(1)
        print("\nLeo will now spin the wheel to win a free inventory item! Here is a list of all the possible items and their functions:")
        print("Magic Mushrooms: Strength and health increase by 400")
        print("Meth: Commit suicide")
        print("Nike Shoes: Speed increase by 1000")
        d = input("Press enter to spin the wheel:")
        time.sleep(0.5)
        if random.randint(1,4) == 1:
          magicMushrooms.buff(Leo)
          print("Leo was buffed by magic mushrooms!")
        elif random.randint(1,4) == 2:
          Meth.commitDie(Leo)
          print("Leo has commited die due to meth :(")
        elif random.randint(1,4) == 3:
          NikeShoes.speedy(Leo)
          print("Leo obtained Nike Shoes to increase his agility!")
        else:
          print("Leo did not get an inventory item.")

        print("Leo has now finished his turn.")
    
    else:
      if Leo.health > 0:
        print("\nNow it's Leo's turn.")
        if Eric.health > 0 or Trevor.health > 0:
          while True:
            c = input("Who would you like to attack? ")
            if c.lower() == 'eric':
              if Eric.health > 0:
                Leo.attack(Eric)
                if Eric.health > 0:
                  print("Eric now has " + str(Eric.health) + " health left.")
                else:
                  print("Eric is now ded :(")
              else:
                print("Eric is already dead. You will attack Trevor instead.")
                Leo.attack(Trevor)
                if Trevor.health > 0:
                  print("Trevor now has " + str(Trevor.health) + " health left.")
                else:
                  print("Trevor is now ded :(")
              break
            elif c.lower() == 'trevor':
              if Trevor.health > 0:
                Leo.attack(Trevor)
                if Leo.health > 0:
                  print("Trevor now has " + str(Trevor.health) + " health left.")
                else:
                  print("Trevor is now ded :(")
              else:
                print("Trevor is already dead. You will attack Eric instead.")
                Leo.attack(Eric)
                if Eric.health > 0:
                  print("Eric now has " + str(Eric.health) + " health left.")
                else:
                  print("Eric is now ded :(")
              break
            else:
              print ("That is not a valid input. Please try again.")

        time.sleep(1)
        print("\nLeo will now spin the wheel to win a free inventory item! Here is a list of all the possible items and their functions:")
        print("Magic Mushrooms: Strength and health increase by 400")
        print("Meth: Commit suicide")
        print("Nike Shoes: Speed increase by 1000")
        d = input("Press enter to spin the wheel:")
        time.sleep(0.5)
        if random.randint(1,4) == 1:
          magicMushrooms.buff(Leo)
          print("Leo was buffed by magic mushrooms!")
        elif random.randint(1,4) == 2:
          Meth.commitDie(Leo)
          print("Leo has commited die due to meth :(")
        elif random.randint(1,4) == 3:
          NikeShoes.speedy(Leo)
          print("Leo obtained Nike Shoes to increase his agility!")
        else:
          print("Leo did not get an inventory item.")

        print("Leo has now finished his turn.")

        if Trevor.health > 0:
          print("\nNow it's Trevor's turn.")
          if Eric.health > 0 or Leo.health > 0:
            while True:
              c = input("Who would you like to attack? ")
              if c.lower() == 'eric':
                if Eric.health > 0:
                  Trevor.attack(Eric)
                  if Eric.health > 0:
                    print("Eric now has " + str(Eric.health) + " health left.")
                  else:
                    print("Eric is now ded :(")
                else:
                  print("Eric is already dead. You will attack Leo instead.")
                  Trevor.attack(Leo)
                  if Leo.health > 0:
                    print("Leo now has " + str(Leo.health) + " health left.")
                  else:
                    print("Leo is now ded :(")
                break
              elif c.lower() == 'leo':
                if Leo.health > 0:
                  Trevor.attack(Leo)
                  if Leo.health > 0:
                    print("Leo now has " + str(Leo.health) + " health left.")
                  else:
                    print("Leo is now ded :(")
                else:
                  print("Leo is already dead. You will attack Eric instead.")
                  Trevor.attack(Eric)
                  if Eric.health > 0:
                    print("Eric now has " + str(Eric.health) + " health left.")
                  else:
                    print("Eric is now ded :(")
                break
              else:
                print ("That is not a valid input. Please try again.")

          time.sleep(1)
          print("\nTrevor will now spin the wheel to win a free inventory item! Here is a list of all the possible items and their functions:")
          print("Magic Mushrooms: Strength and health increase by 400")
          print("Meth: Commit suicide")
          print("Nike Shoes: Speed increase by 1000")
          d = input("Press enter to spin the wheel:")
          time.sleep(0.5)
          if random.randint(1,4) == 1:
            magicMushrooms.buff(Trevor)
            print("Trevor was buffed by magic mushrooms!")
          elif random.randint(1,4) == 2:
            Meth.commitDie(Trevor)
            print("Trevor has commited die due to meth :(")
          elif random.randint(1,4) == 3:
            NikeShoes.speedy(Trevor)
            print("Trevor obtained Nike Shoes to increase his agility!")
          else:
            print("Trevor did not get an inventory item.")

          print("Trevor has now finished his turn.")

  elif Trevor.agility == max(a) and Trevor.health > 0:
    print("\nTrevor will make the first move.")
    if Eric.health > 0 or Leo.health > 0:
      while True:
        c = input("Who would you like to attack? ")
        if c.lower() == 'eric':
          if Eric.health > 0:
            Trevor.attack(Eric)
            if Eric.health > 0:
              print("Eric now has " + str(Eric.health) + " health left.")
            else:
              print("Eric is now ded :(")
          else:
            print("Eric is already dead. You will attack Leo instead.")
            Trevor.attack(Leo)
            if Leo.health > 0:
              print("Leo now has " + str(Leo.health) + " health left.")
            else:
              print("Leo is now ded :(")
          break
        elif c.lower() == 'leo':
          if Leo.health > 0:
            Trevor.attack(Leo)
            if Leo.health > 0:
              print("Leo now has " + str(Leo.health) + " health left.")
            else:
              print("Leo is now ded :(")
          else:
            print("Leo is already dead. You will attack Eric instead.")
            Trevor.attack(Eric)
            if Eric.health > 0:
              print("Eric now has " + str(Eric.health) + " health left.")
            else:
              print("Eric is now ded :(")
          break
        else:
          print ("That is not a valid input. Please try again.")
    time.sleep(1)
    print("\nTrevor will now spin the wheel to win a free inventory item! Here is a list of all the possible items and their functions:")
    print("Magic Mushrooms: Strength and health increase by 400")
    print("Meth: Commit suicide")
    print("Nike Shoes: Speed increase by 1000")
    d = input("Press enter to spin the wheel:")
    time.sleep(0.5)
    if random.randint(1,4) == 1:
      magicMushrooms.buff(Trevor)
      print("Trevor was buffed by magic mushrooms!")
    elif random.randint(1,4) == 2:
      Meth.commitDie(Trevor)
      print("Trevor has commited die due to meth :(")
    elif random.randint(1,4) == 3:
      NikeShoes.speedy(Trevor)
      print("Trevor obtained Nike Shoes to increase his agility!")
    else:
      print("Trevor did not get an inventory item.")

    print("Trevor has now finished his turn.")

    if Eric.agility > Leo.agility and Eric.health > 0:
      print("\nNow it's Eric's turn.")
      if Trevor.health > 0 or Leo.health > 0:
        while True:
          c = input("Who would you like to attack? ")
          if c.lower() == 'trevor':
            if Trevor.health > 0:
              Eric.attack(Trevor)
              if Trevor.health > 0:
                print("Trevor now has " + str(Trevor.health) + " health left.")
              else:
                print("Trevor is now ded :(")
            else:
              print("Trevor is already dead. You will attack Leo instead.")
              Eric.attack(Leo)
              if Leo.health > 0:
                print("Leo now has " + str(Leo.health) + " health left.")
              else:
                print("Leo is now ded :(")
            break
          elif c.lower() == 'leo':
            if Leo.health > 0:
              Eric.attack(Leo)
              if Leo.health > 0:
                print("Leo now has " + str(Leo.health) + " health left.")
              else:
                print("Leo is now ded :(")
            else:
              print("Leo is already dead. You will attack Trevor instead.")
              Eric.attack(Trevor)
              if Trevor.health > 0:
                print("Trevor now has " + str(Trevor.health) + " health left.")
              else:
                print("Trevor is now ded :(")
            break
          else:
            print ("That is not a valid input. Please try again.")
    
      time.sleep(1)
      print("\nEric will now spin the wheel to win a free inventory item! Here is a list of all the possible items and their functions:")
      print("Magic Mushrooms: Strength and health increase by 400")
      print("Meth: Commit suicide")
      print("Nike Shoes: Speed increase by 1000")
      d = input("Press enter to spin the wheel:")
      time.sleep(0.5)
      if random.randint(1,4) == 1:
        magicMushrooms.buff(Eric)
        print("Eric was buffed by magic mushrooms!")
      elif random.randint(1,4) == 2:
        Meth.commitDie(Eric)
        print("Eric has commited die due to meth :(")
      elif random.randint(1,4) == 3:
        NikeShoes.speedy(Eric)
        print("Eric obtained Nike Shoes to increase his agility!")
      else:
        print("Eric did not get an inventory item.")

      print("Eric has now finished his turn.")

      if Leo.health > 0:
        print("\nNow it's Leo's turn.")
        if Eric.health > 0 or Trevor.health > 0:
          while True:
            c = input("Who would you like to attack? ")
            if c.lower() == 'eric':
              if Eric.health > 0:
                Leo.attack(Eric)
                if Eric.health > 0:
                  print("Eric now has " + str(Eric.health) + " health left.")
                else:
                  print("Eric is now ded :(")
              else:
                print("Eric is already dead. You will attack Trevor instead.")
                Leo.attack(Trevor)
                if Trevor.health > 0:
                  print("Trevor now has " + str(Trevor.health) + " health left.")
                else:
                  print("Trevor is now ded :(")
              break
            elif c.lower() == 'trevor':
              if Trevor.health > 0:
                Leo.attack(Trevor)
                if Leo.health > 0:
                  print("Trevor now has " + str(Trevor.health) + " health left.")
                else:
                  print("Trevor is now ded :(")
              else:
                print("Trevor is already dead. You will attack Eric instead.")
                Leo.attack(Eric)
                if Eric.health > 0:
                  print("Eric now has " + str(Eric.health) + " health left.")
                else:
                  print("Eric is now ded :(")
              break
            else:
              print ("That is not a valid input. Please try again.")

        time.sleep(1)        
        print("\nLeo will now spin the wheel to win a free inventory item! Here is a list of all the possible items and their functions:")
        print("Magic Mushrooms: Strength and health increase by 400")
        print("Meth: Commit suicide")
        print("Nike Shoes: Speed increase by 1000")
        d = input("Press enter to spin the wheel:")
        time.sleep(0.5)
        if random.randint(1,4) == 1:
          magicMushrooms.buff(Leo)
          print("Leo was buffed by magic mushrooms!")
        elif random.randint(1,4) == 2:
          Meth.commitDie(Leo)
          print("Leo has commited die due to meth :(")
        elif random.randint(1,4) == 3:
          NikeShoes.speedy(Leo)
          print("Leo obtained Nike Shoes to increase his agility!")
        else:
          print("Leo did not get an inventory item.")

        print("Leo has now finished his turn.")
      
    else:
      if Leo.health > 0:
        print("\nNow it's Leo's turn.")
        if Eric.health > 0 or Trevor.health > 0:
          while True:
            c = input("Who would you like to attack? ")
            if c.lower() == 'eric':
              if Eric.health > 0:
                Leo.attack(Eric)
                if Eric.health > 0:
                  print("Eric now has " + str(Eric.health) + " health left.")
                else:
                  print("Eric is now ded :(")
              else:
                print("Eric is already dead. You will attack Trevor instead.")
                Leo.attack(Trevor)
                if Trevor.health > 0:
                  print("Trevor now has " + str(Trevor.health) + " health left.")
                else:
                  print("Trevor is now ded :(")
              break
            elif c.lower() == 'trevor':
              if Trevor.health > 0:
                Leo.attack(Trevor)
                if Leo.health > 0:
                  print("Trevor now has " + str(Trevor.health) + " health left.")
                else:
                  print("Trevor is now ded :(")
              else:
                print("Trevor is already dead. You will attack Eric instead.")
                Leo.attack(Eric)
                if Eric.health > 0:
                  print("Eric now has " + str(Eric.health) + " health left.")
                else:
                  print("Eric is now ded :(")
              break
            else:
              print ("That is not a valid input. Please try again.")
      
        time.sleep(1)
        print("\nLeo will now spin the wheel to win a free inventory item! Here is a list of all the possible items and their functions:")
        print("Magic Mushrooms: Strength and health increase by 400")
        print("Meth: Commit suicide")
        print("Nike Shoes: Speed increase by 1000")
        d = input("Press enter to spin the wheel:")
        time.sleep(0.5)
        if random.randint(1,4) == 1:
          magicMushrooms.buff(Leo)
          print("Leo was buffed by magic mushrooms!")
        elif random.randint(1,4) == 2:
          Meth.commitDie(Leo)
          print("Leo has commited die due to meth :(")
        elif random.randint(1,4) == 3:
          NikeShoes.speedy(Leo)
          print("Leo obtained Nike Shoes to increase his agility!")
        else:
          print("Leo did not get an inventory item.")

        print("Leo has now finished his turn.")

      if Eric.health > 0:
        print("\nNow it's Eric's turn.")
        if Trevor.health > 0 or Leo.health > 0:
          while True:
            c = input("Who would you like to attack? ")
            if c.lower() == 'trevor':
              if Trevor.health > 0:
                Eric.attack(Trevor)
                if Trevor.health > 0:
                  print("Trevor now has " + str(Trevor.health) + " health left.")
                else:
                  print("Trevor is now ded :(")
              else:
                print("Trevor is already dead. You will attack Leo instead.")
                Eric.attack(Leo)
                if Leo.health > 0:
                  print("Leo now has " + str(Leo.health) + " health left.")
                else:
                  print("Leo is now ded :(")
              break
            elif c.lower() == 'leo':
              if Leo.health > 0:
                Eric.attack(Leo)
                if Leo.health > 0:
                  print("Leo now has " + str(Leo.health) + " health left.")
                else:
                  print("Leo is now ded :(")
              else:
                print("Leo is already dead. You will attack Trevor instead.")
                Eric.attack(Trevor)
                if Trevor.health > 0:
                  print("Trevor now has " + str(Trevor.health) + " health left.")
                else:
                  print("Trevor is now ded :(")
              break
            else:
              print ("That is not a valid input. Please try again.")

        time.sleep(1)
        print("\nEric will now spin the wheel to win a free inventory item! Here is a list of all the possible items and their functions:")
        print("Magic Mushrooms: Strength and health increase by 400")
        print("Meth: Commit suicide")
        print("Nike Shoes: Speed increase by 1000")
        d = input("Press enter to spin the wheel:")
        time.sleep(0.5)
        if random.randint(1,4) == 1:
          magicMushrooms.buff(Eric)
          print("Eric was buffed by magic mushrooms!")
        elif random.randint(1,4) == 2:
          Meth.commitDie(Eric)
          print("Eric has commited die due to meth :(")
        elif random.randint(1,4) == 3:
          NikeShoes.speedy(Eric)
          print("Eric obtained Nike Shoes to increase his agility!")
        else:
          print("Eric did not get an inventory item.")

        print("Eric has now finished his turn.")

  elif Leo.agility == max(a) and Leo.health > 0:
    print("\nLeo will make the first move.")
    if Eric.health > 0 or Trevor.health > 0:
      while True:
        c = input("Who would you like to attack? ")
        if c.lower() == 'eric':
          if Eric.health > 0:
            Leo.attack(Eric)
            if Eric.health > 0:
              print("Eric now has " + str(Eric.health) + " health left.")
            else:
              print("Eric is now ded :(")
          else:
            print("Eric is already dead. You will attack Trevor instead.")
            Leo.attack(Trevor)
            if Trevor.health > 0:
              print("Trevor now has " + str(Trevor.health) + " health left.")
            else:
              print("Trevor is now ded :(")
          break
        elif c.lower() == 'trevor':
          if Trevor.health > 0:
            Leo.attack(Trevor)
            if Leo.health > 0:
              print("Trevor now has " + str(Trevor.health) + " health left.")
            else:
              print("Trevor is now ded :(")
          else:
            print("Trevor is already dead. You will attack Eric instead.")
            Leo.attack(Eric)
            if Eric.health > 0:
              print("Eric now has " + str(Eric.health) + " health left.")
            else:
              print("Eric is now ded :(")
          break
        else:
          print ("That is not a valid input. Please try again.")
    
    time.sleep(1)
    print("\nLeo will now spin the wheel to win a free inventory item! Here is a list of all the possible items and their functions:")
    print("Magic Mushrooms: Strength and health increase by 400")
    print("Meth: Commit suicide")
    print("Nike Shoes: Speed increase by 1000")
    d = input("Press enter to spin the wheel:")
    time.sleep(0.5)
    if random.randint(1,4) == 1:
      magicMushrooms.buff(Leo)
      print("Leo was buffed by magic mushrooms!")
    elif random.randint(1,4) == 2:
      Meth.commitDie(Leo)
      print("Leo has commited die due to meth :(")
    elif random.randint(1,4) == 3:
      NikeShoes.speedy(Leo)
      print("Leo obtained Nike Shoes to increase his agility!")
    else:
      print("Leo did not get an inventory item.")

    print("Leo has now finished his turn.")

    if Eric.agility > Trevor.agility and Eric.health > 0:
      print("\nNow it's Eric's turn.")
      if Trevor.health > 0 or Leo.health > 0:
        while True:
          c = input("Who would you like to attack? ")
          if c.lower() == 'trevor':
            if Trevor.health > 0:
              Eric.attack(Trevor)
              if Trevor.health > 0:
                print("Trevor now has " + str(Trevor.health) + " health left.")
              else:
                print("Trevor is now ded :(")
            else:
              print("Trevor is already dead. You will attack Leo instead.")
              Eric.attack(Leo)
              if Leo.health > 0:
                print("Leo now has " + str(Leo.health) + " health left.")
              else:
                print("Leo is now ded :(")
            break
          elif c.lower() == 'leo':
            if Leo.health > 0:
              Eric.attack(Leo)
              if Leo.health > 0:
                print("Leo now has " + str(Leo.health) + " health left.")
              else:
                print("Leo is now ded :(")
            else:
              print("Leo is already dead. You will attack Trevor instead.")
              Eric.attack(Trevor)
              if Trevor.health > 0:
                print("Trevor now has " + str(Trevor.health) + " health left.")
              else:
                print("Trevor is now ded :(")
            break
          else:
            print ("That is not a valid input. Please try again.")
      
      time.sleep(1)
      print("\nEric will now spin the wheel to win a free inventory item! Here is a list of all the possible items and their functions:")
      print("Magic Mushrooms: Strength and health increase by 400")
      print("Meth: Commit suicide")
      print("Nike Shoes: Speed increase by 1000")
      d = input("Press enter to spin the wheel:")
      time.sleep(0.5)
      if random.randint(1,4) == 1:
        magicMushrooms.buff(Eric)
        print("Eric was buffed by magic mushrooms!")
      elif random.randint(1,4) == 2:
        Meth.commitDie(Eric)
        print("Eric has commited die due to meth :(")
      elif random.randint(1,4) == 3:
        NikeShoes.speedy(Eric)
        print("Eric obtained Nike Shoes to increase his agility!")
      else:
        print("Eric did not get an inventory item.")

      print("Eric has now finished his turn.")

      if Trevor.health > 0:
        print("\nNow it's Trevor's turn.")
        if Eric.health > 0 or Leo.health > 0:
          while True:
            c = input("Who would you like to attack? ")
            if c.lower() == 'eric':
              if Eric.health > 0:
                Trevor.attack(Eric)
                if Eric.health > 0:
                  print("Eric now has " + str(Eric.health) + " health left.")
                else:
                  print("Eric is now ded :(")
              else:
                print("Eric is already dead. You will attack Leo instead.")
                Trevor.attack(Leo)
                if Leo.health > 0:
                  print("Leo now has " + str(Leo.health) + " health left.")
                else:
                  print("Leo is now ded :(")
              break
            elif c.lower() == 'leo':
              if Leo.health > 0:
                Trevor.attack(Leo)
                if Leo.health > 0:
                  print("Leo now has " + str(Leo.health) + " health left.")
                else:
                  print("Leo is now ded :(")
              else:
                print("Leo is already dead. You will attack Eric instead.")
                Trevor.attack(Eric)
                if Eric.health > 0:
                  print("Eric now has " + str(Eric.health) + " health left.")
                else:
                  print("Eric is now ded :(")
              break
            else:
              print ("That is not a valid input. Please try again.")

        time.sleep(1)
        print("\nTrevor will now spin the wheel to win a free inventory item! Here is a list of all the possible items and their functions:")
        print("Magic Mushrooms: Strength and health increase by 400")
        print("Meth: Commit suicide")
        print("Nike Shoes: Speed increase by 1000")
        d = input("Press enter to spin the wheel:")
        time.sleep(0.5)
        if random.randint(1,4) == 1:
          magicMushrooms.buff(Trevor)
          print("Trevor was buffed by magic mushrooms!")
        elif random.randint(1,4) == 2:
          Meth.commitDie(Trevor)
          print("Trevor has commited die due to meth :(")
        elif random.randint(1,4) == 3:
          NikeShoes.speedy(Trevor)
          print("Trevor obtained Nike Shoes to increase his agility!")
        else:
          print("Trevor did not get an inventory item.")

        print("Trevor has now finished his turn.")

    else:
      if Trevor.health > 0:
        print("\nNow it's Trevor's turn.")
        if Eric.health > 0 or Leo.health > 0:
          while True:
            c = input("Who would you like to attack? ")
            if c.lower() == 'eric':
              if Eric.health > 0:
                Trevor.attack(Eric)
                if Eric.health > 0:
                  print("Eric now has " + str(Eric.health) + " health left.")
                else:
                  print("Eric is now ded :(")
              else:
                print("Eric is already dead. You will attack Leo instead.")
                Trevor.attack(Leo)
                if Leo.health > 0:
                  print("Leo now has " + str(Leo.health) + " health left.")
                else:
                  print("Leo is now ded :(")
              break
            elif c.lower() == 'leo':
              if Leo.health > 0:
                Trevor.attack(Leo)
                if Leo.health > 0:
                  print("Leo now has " + str(Leo.health) + " health left.")
                else:
                  print("Leo is now ded :(")
              else:
                print("Leo is already dead. You will attack Eric instead.")
                Trevor.attack(Eric)
                if Eric.health > 0:
                  print("Eric now has " + str(Eric.health) + " health left.")
                else:
                  print("Eric is now ded :(")
              break
            else:
              print ("That is not a valid input. Please try again.")
    
        time.sleep(1)
        print("\nTrevor will now spin the wheel to win a free inventory item! Here is a list of all the possible items and their functions:")
        print("Magic Mushrooms: Strength and health increase by 400")
        print("Meth: Commit suicide")
        print("Nike Shoes: Speed increase by 1000")
        d = input("Press enter to spin the wheel:")
        time.sleep(0.5)
        if random.randint(1,4) == 1:
          magicMushrooms.buff(Trevor)
          print("Trevor was buffed by magic mushrooms!")
        elif random.randint(1,4) == 2:
          Meth.commitDie(Trevor)
          print("Trevor has commited die due to meth :(")
        elif random.randint(1,4) == 3:
          NikeShoes.speedy(Trevor)
          print("Trevor obtained Nike Shoes to increase his agility!")
        else:
          print("Trevor did not get an inventory item.")

        print("Trevor has now finished his turn.")

        if Eric.health > 0:
          print("\nNow it's Eric's turn.")
          if Trevor.health > 0 or Leo.health > 0:
            while True:
              c = input("Who would you like to attack? ")
              if c.lower() == 'trevor':
                if Trevor.health > 0:
                  Eric.attack(Trevor)
                  if Trevor.health > 0:
                    print("Trevor now has " + str(Trevor.health) + " health left.")
                  else:
                    print("Trevor is now ded :(")
                else:
                  print("Trevor is already dead. You will attack Leo instead.")
                  Eric.attack(Leo)
                  if Leo.health > 0:
                    print("Leo now has " + str(Leo.health) + " health left.")
                  else:
                    print("Leo is now ded :(")
                break
              elif c.lower() == 'leo':
                if Leo.health > 0:
                  Eric.attack(Leo)
                  if Leo.health > 0:
                    print("Leo now has " + str(Leo.health) + " health left.")
                  else:
                    print("Leo is now ded :(")
                else:
                  print("Leo is already dead. You will attack Trevor instead.")
                  Eric.attack(Trevor)
                  if Trevor.health > 0:
                    print("Trevor now has " + str(Trevor.health) + " health left.")
                  else:
                    print("Trevor is now ded :(")
                break
              else:
                print ("That is not a valid input. Please try again.")
          
          time.sleep(1)
          print("\nEric will now spin the wheel to win a free inventory item! Here is a list of all the possible items and their functions:")
          print("Magic Mushrooms: Strength and health increase by 400")
          print("Meth: Commit suicide")
          print("Nike Shoes: Speed increase by 1000")
          d = input("Press enter to spin the wheel:")
          time.sleep(0.5)
          if random.randint(1,4) == 1:
            magicMushrooms.buff(Eric)
            print("Eric was buffed by magic mushrooms!")
          elif random.randint(1,4) == 2:
            Meth.commitDie(Eric)
            print("Eric has commited die due to meth :(")
          elif random.randint(1,4) == 3:
            NikeShoes.speedy(Eric)
            print("Eric obtained Nike Shoes to increase his agility!")
          else:
            print("Eric did not get an inventory item.")

          print("Eric has now finished his turn.")


  if Eric.health > 0 and Trevor.health <= 0 and Leo.health <= 0:
    print("\nThe game has ended. Eric is the winner of Commit Die Arena!")
    break
  
  elif Trevor.health > 0 and Eric.health <= 0 and Leo.health <= 0:
    print("\nThe game has ended. Trevor is the winner of Commit Die Arena!")
    break

  elif Leo.health > 0 and Eric.health <= 0 and Trevor.health <= 0:
    print("\nThe game has ended. Leo is the winner of Commit Die Arena!")
    break
  
  elif Eric.health <= 0 and Trevor.health <= 0 and Leo.health <= 0:
    print("Everyone has miraculously commited die!")
  
  print ("The next round will begin :)")
