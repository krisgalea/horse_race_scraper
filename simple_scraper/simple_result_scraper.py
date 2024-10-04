from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import os
import re

directory = "../horse_racing_data/2018-03-19/"

ordinal_dict = {}

for filename in os.listdir(directory):

    with open(directory + filename) as html_doc:
        print filename
        doc = BeautifulSoup(html_doc, "html.parser")

        horses = doc.find_all(class_="hr-racing-runner-position-container")

        for horse in horses :
            try:
                position = int(re.sub("[A-Za-z]", "", horse.find(class_="ordinal").text))
                odds = re.sub("[A-Za-z]", "", horse.find(class_="hr-racing-runner-betting-info").text)
                if position not in ordinal_dict.keys():
                    ordinal_dict[position] = []

                odds_numerator = float(odds.split("/")[0])
                odds_denominator = float(odds.split("/")[1])
                decimal_odds = odds_numerator / odds_denominator
                print position, " ", decimal_odds

                ordinal_dict[position].append(decimal_odds)

                # xs.append(position)
                # ys.append(decimal_odds)
            except Exception as ex:
                print "skipping"

# print xs, "\n", ys
print ordinal_dict[10]
plt.hist(ordinal_dict[1])
plt.show()
