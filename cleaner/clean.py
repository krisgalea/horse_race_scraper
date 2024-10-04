from bs4 import BeautifulSoup


with open("race-1-claiming", "r") as html_file:
    html = html_file.read()
    soup = BeautifulSoup(html, "html.parser")
    runners = soup.findAll("section", class_="hr-racing-runner-wrapper")
    print runners[0].text
