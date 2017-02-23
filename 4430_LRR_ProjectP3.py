#Luis Rangel(luisrngl5@gmail.com or LuisRangel@my.unt.edu)
#CSCE 4430
#Project Part 3:Python I
#importing the libaries, that was a pain in the butt to install
import urllib
from bs4 import BeautifulSoup
#Read in the file
r = urllib.urlopen('http://www.technewsworld.com/').read()
soup = BeautifulSoup(r, "html.parser")
#Getting the top 10 stories by the title
letters = soup.find_all("div", class_="title")
dates = soup.find_all("div", class_="date")
prefix = "http://www.technewsworld.com"
#for loop in order to make things easier
print "This is the Top Hits from this Website!!!"
for i in range(0,10):
    #Printing the websites
    print "#" , i + 1 ,"-", letters[i].get_text(), "\t\t\t|Date:", dates[i].get_text()
    print prefix, letters[i].a["href"]
