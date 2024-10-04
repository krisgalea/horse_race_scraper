from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
import re
import os
from matplotlib import pyplot as plt


def freq_dist(items):
    dist = {}
    for item in items:
        if item not in dist.keys():
            dist[item] = 0
        dist[item] += 1
    return dist


performance_dict = {}
directory = "../horse_racing_data/2018-03-23/horses/"
for filename in os.listdir(directory):
    try:
        html_doc = open(directory + filename)
        doc = BeautifulSoup(html_doc, 'html.parser')

        fouled = doc.find(class_="full-date").text
        races = doc.find(class_="default-table horse-profile-results-table")

        # 5th March 2016
        fouled = re.sub("(rd|st|th|nd)", "", fouled)
        # print fouled.split(" ")[0]
        if len(fouled.split(" ")[0]) == 1:
            fouled = "0" + fouled

        # print fouled
        datetime_object = datetime.strptime(fouled, '%d %B %Y')
        # print datetime_object

        delta = datetime.now() - datetime_object
        age = delta.days

        for race in races.select("tr"):
            try:
                race_date = datetime.strptime(race.select("td")[0].text, '%d/%m/%y')
                age_at_race = int((race_date - datetime_object).days/365)
                position = race.select("td")[1].text.split("/")[0]

                if re.search("^[0-9]+$", position):
                    normalised_position = int(float(race.select("td")[1].text.split("/")[0]) / float(race.select("td")[1].text.split("/")[1])*10.0)
                else:
                    continue

                type = race.select("td")[3].text
                # print type
                # print "age: ", age_at_race, "position: ", position.split("/")[0]

                if type not in performance_dict.keys():
                    performance_dict[type] = {}

                if  age_at_race not in performance_dict[type].keys():
                    performance_dict[type][age_at_race] = []

                performance_dict[type][age_at_race].append(normalised_position)
            except Exception as ex:
                print "skipping race"
    except Exception as ex:
        print "skipping horse"


dist_9 = freq_dist(performance_dict["FLAT"][9])
dist_10 = freq_dist(performance_dict["FLAT"][10])
dist_11 = freq_dist(performance_dict["FLAT"][11])
dist_12 = freq_dist(performance_dict["FLAT"][12])

plt.subplot(2,1,1)
plt.scatter(dist_9.keys(), dist_9.values())

plt.subplot(2,1,2)
plt.scatter(dist_11.keys(), dist_11.values())
#
# plt.subplot(2,1,3)
# plt.scatter(dist_11.keys(), dist_11.values())
#
# plt.subplot(2,1,4)
# plt.scatter(dist_12.keys(), dist_12.values())
plt.show()
