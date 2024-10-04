from bs4 import BeautifulSoup
from horse import Horse
from jockey import Jockey

race_file = file("./horse_racing_data/2018-03-24/32red-casino-handicap")
html_doc = race_file.read()

soup = BeautifulSoup(html_doc, 'html.parser')
runners = soup.find_all('section', attrs={"class", "hr-racing-runner-wrapper"})

for runner in runners:
    position = runner.find_all('span', attrs={'class', 'ordinal'})[0].text
    horse_span = runner.find_all('span', attrs={'class', 'hr-racing-runner-horse-name'})[0]
    jockey_span = runner.find_all('span', attrs={'class', 'hr-racing-runner-form-jockey-name'})[0]
    horse = Horse(horse_span.text, horse_span.a)
    jockey = Jockey(jockey_span.text, 0, jockey_span.a)
    print position, '\t', horse.link, '\t', jockey.link
