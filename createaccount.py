import yaml
import sys

def create_instance(username, hunger, water, life):
   try:
      with open("gamedata.yaml", "r") as file:
         existing_data = yaml.safe_load(file)
   except FileNotFoundError:
      existing_data = {}

   if username in existing_data:
      print("Username Taken. Try another!")
      sys.exit()

   if existing_data is None:
      existing_data = {}

   existing_data[username] = {
      "hunger": hunger,
      "water": water,
      "life": life
    }
   with open("gamedata.yaml", "w") as file:
      yaml.safe_dump(existing_data, file)
new_hunger,new_water,new_life = 100,100,100
new_username = input("Hello there! What is your name?")
create_instance(new_username, new_hunger, new_water, new_life)
