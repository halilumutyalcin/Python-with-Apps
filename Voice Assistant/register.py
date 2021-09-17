import webbrowser
import time

def go():
    url = "https://www.google.com/maps/place"
    time.sleep(10)
    webbrowser.get().open(url)
go()