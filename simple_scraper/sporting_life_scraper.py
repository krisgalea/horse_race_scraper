from bs4 import BeautifulSoup
from horse import Horse
from race_summary import RaceSummary
from horse import Horse
from jockey import Jockey
from trainer import Trainer
from meeting import Meeting
from race import Race

class SportingLifeScraper(object):

    def __init__(self):
        self.dbManager = DbManager()

    def scrapeMeeting(self):
        #1. Create horse
        #   1.1 Create horse race summary entries
        #2. Create jockey
        #   2.1 Create jockey race summary entries
        #3. Create trainer
        #   3.1 Create trainer race summary entries
        #4. Create Races
        #5. Create Meetings

    def scrapeJockeyHtml(html_doc):

    def scrapeTrainerHtml(html_doc):

    def scrapeRaceHtml(html_doc):

    def scrapeRaceSummary(html_doc):
        race_html = race.select("td")

        race_date = race_html[0].datetime.strptime(race.select("td")[0].text, '%d/%m/%y')
        horse_end_position = race_html[1].text.split("/")[0]
        race_type = race_html[2].text
        #age_at_race = int((race_date - datetime_object).days/365)

        #get a normalised position
        if re.search("^[0-9]+$", horse_end_position):
            normalised_position = int(float(race.select("td")[1].text.split("/")[0]) / float(race.select("td")[1].text.split("/")[1])*10.0)
        else:
            continue

        #meeting name
        meeting_name = race_html[3].select("strong").text

        #race details
        race_details = race_html[3].select("span")
        track_distance = race_details[0].text.replace(",","")
        race_going = race_details[1].text.replace(",","")
        race_class = race_details[2].text.replace(",","")

        return RaceSummary(race_id, race_date, horse_end_position, horse_name, race_type, meeting_name, track_distance, race_going, race_class)


    def scrapeHorseHtml(html_doc):
        parser = BeautifulSoup(html_doc, "html.parser")

        horse_name = parser.find(class_="horse-profile-heading1").text
        horse_card = parser.find(class_="horse-profile-summary-value")

        #horse card
        horse_sex = horse_card[0].text
        horse_sire = horse_card[1].text
        horse_dam = horse_card[2].text
        horse_owner  = horse_card[3].text


        # fouled date extraction : 5th March 2016
        fouled = parser.find(class_="full-date").text
        fouled = re.sub("(rd|st|th|nd)", "", fouled)
        if len(fouled.split(" ")[0]) == 1:
            fouled = "0" + fouled

        #birthday
        birth_date = datetime.strptime(fouled, '%d %B %Y')

        #find age
        delta = datetime.now() - birth_date
        age = delta.days

        #race summaries
        races = doc.find(class_="default-table horse-profile-results-table")
        race_summaries = []

        #DATE	POS	BHA	TYPE	RACE DETAILS	SP
        for race in races.select("tr"):
            try:
                race_summary = scrapeRaceHtml(race)
                race_summaries.push(race_summary)
