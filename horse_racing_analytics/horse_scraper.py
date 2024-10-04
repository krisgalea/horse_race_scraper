from bs4 import BeautifulSoup
from horse import Horse
from meeting import Meeting
from runner import Runner

with open("./horse_racing_data/horses/252916", 'r') as doc:
    html_doc = doc.read()
    soup = BeautifulSoup(html_doc, "html.parser")
    values = soup.find_all(attrs={"class": "horse-profile-summary-value"})
    name = soup.find_all(attrs={"class": "horse-profile-heading1"})[0].text
    dob = values[0].span.text
    trainer = values[1].text
    sex = values[2].text
    sire = values[3].text
    dam = values[4].text
    owner = values[5].text

    print name, dob, trainer, sex, sire, dam, owner
    horse = Horse(name, dob, trainer, sex, sire, dam, owner)

    result_table = soup.find_all(attrs={"class": "horse-profile-results-table"})[0].tbody
    results = result_table.find_all('tr')
    for result in results:
        # print result
        cells = result.find_all('td')

        #24/03/18	1/10	100	FLAT	Doncaster, 6f 2y, Soft, C1	4/1
        print(cells[4].text)
        meeting_location = cells[4].text.split(',')[0]
        meeting_distance = cells[4].text.split(',')[1]
        meeting_going = cells[4].text.split(',')[2]
        try:
            meeting_surface = cells[4].text.split(',')[3]
        except Exception as ex:
            print "moving on ..."

        meeting_date = cells[0].text
        meeting_type = cells[3].text

        runner_odds = cells[5].text
        runner_finish = cells[1].text

        #MORE DATA REQUIRED: SURFACE, MEETING DETAILS: HANDICAP

        meeting = Meeting(meeting_location, meeting_date, meeting_type, meeting_going, meeting_surface, meeting_distance)
        runner = Runner(horse=horse, meeting=meeting,
                        odds=runner_odds, finish_position=runner_finish)
