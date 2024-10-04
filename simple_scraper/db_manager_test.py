from db_manager import DbManager
from track import Track

if __name__ == "__main__":
    print "hi there!"
    manager = DbManager()

    track = Track(1,"test", "turf", 2.5)
    manager.addItem(track)
