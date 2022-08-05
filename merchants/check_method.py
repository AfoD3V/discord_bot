import re

merchant_list = ["Lucas", "Morris", "Mac", "Jeffrey", "Dorella",
                 "Malone", "Burt", "Oliver", "Nox", "Aricer", "Rayni",
                 "Ben", "Peter", "Laitir", "Evan"]

merchant_location = ["Yudia", "East Luterra", "Anikka", "Shushire", "Feiton", "West Luterra",
                     "Tortoyk", "Arthetine", "Rohendel", "Punika", "Rethramis", "North Vern",
                     "Yorn", "South Vern"]

merchant_set = []

item_list = ["Prideholme Potato", "Necromancer's Records", "Oreha Viewing Stone", "Red Moon's Tears", "Fargar's Beer",
             "Sylvain Queens' Blessing", "Sirius's Holy Book", "Vern's Founding Coin", "Fine Gramophone",
             "Angler's Fishing Pole", "Shy Wind Flower Pollen", "Chain War Chronicles", "Sky Reflection Oil",
             "Surprise Chest"]

with open('html.txt', 'r') as f:
    for line in f:
        text = str(line)
        prepared_string = re.split("[<>]", text)

        if 'td b-gk0zvrar9a=""' in prepared_string:
            continue
        elif len(merchant_set) == 5:
            if merchant_set[4] in item_list:
                print(f"{merchant_set[0]} in {merchant_set[1]} - {merchant_set[2]}")
                print(f"{merchant_set[4]}")
                print(f"{merchant_set[3]}")
                print("\n")
                merchant_set = []
            else:
                merchant_set = []

        else:
            for merchant in merchant_list:
                if merchant in prepared_string:
                    merchant_set.append(merchant)
            for location in merchant_location:
                if location in prepared_string:
                    merchant_set.append(location)
                    # Zone prepare
                    zone = prepared_string[9].split(" ")

                    try:
                        zone = re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', zone[3])
                    except IndexError:
                        None
                    merchant_set.append(" ".join(zone))

                    # Link prepare
                    try:
                        link = prepared_string[11].split('"')
                        merchant_set.append("https://lostmerchants.com/" + link[5])
                    except IndexError:
                        None

            for item in item_list:
                if item in prepared_string:
                    merchant_set.append(item)

            print(merchant_set)
