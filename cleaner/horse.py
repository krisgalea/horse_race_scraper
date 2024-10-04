import datetime


class Horse:

    def __init__(self, id, name, gender, sire, year_of_birth, dam):
        self.id = id
        self.name = name
        self.gender = gender
        self.sire = sire
        self.year_of_birth = year_of_birth
        self.dam = dam

    def calculate_age(self):
        now = datetime.datetime.now()
        return now.year - self.year_of_birth
