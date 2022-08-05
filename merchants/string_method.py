import re

text = ""

with open('merchants.txt') as f:
    for i in f:
        text = str(i)

prepared_txt = re.split("[<>]", text)

print(prepared_txt[2])

list_rapport = ["Surprise Chest", "Sky Reflection Oil", "Chain War Chronicles", "Chain War Chronicles",
                "Chain War Chronicles", "Shy Wind Flower Pollen", "Angler's Fishing Pole",
                "Fine Gramophone", "Vern's Founding Coin", "Sirius's Holy Book", "Sylvain Queens' Blessing",
                "Fargar's Beer", "Red Moon Tears", "Oreha Viewing Stone", "Necromancer's Records"]
