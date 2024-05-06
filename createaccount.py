import yaml
import random

username = input("Welcome! what is ur username? ")
generated_key = ""
i = 0
while i < 9:
   key = random.randint(0,9)
   generated_key += str(key)
   i += 1
print(generated_key)
try:
    with open("gamedata.yaml", "r") as file:
        existing_data = yaml.safe_load(file)
except FileNotFoundError:
    existing_data = {}

existing_data[str(username)] = generated_key

with open("gamedata.yaml", "w") as file:
    yaml.safe_dump(existing_data, file)