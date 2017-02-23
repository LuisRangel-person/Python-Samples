#Luis Rangel(luisrngl5@gmail.com or LuisRangel@my.unt.edu)
#CSCE 4430
#Project Part 4:Python II
#importing the libaries, that was a pain in the butt to install
import urllib
import sys
import string
import collections
from bs4 import BeautifulSoup

#Read in the html provided by the first command line arg
r = urllib.urlopen(sys.argv[1]).read()
soup = BeautifulSoup(r, "html.parser")

#Read in the stopwords file, provided by the second command line arg
f = open(sys.argv[2])
stopwords = f.readlines()#Read in lines and insert into list
stopwords = [x.rstrip() for x in stopwords]#Post processing

#pre processing the HTML text for the programs purposes
text = soup.get_text()#Getting rid of all tags
exclude = set(string.punctuation)#Removing punctuation
text = ''.join(ch for ch in text if ch not in exclude)
text = text.lower()#Making the text string all lowercase, this is what I understood "as regardless of casing"
textwords = text.split()
#removing stop words
resultwords  = [word for word in textwords if word not in stopwords]
result = ' '.join(resultwords)
#Counting words
counts = collections.Counter(resultwords)
#Printing the resultword
for i in range (10):
    print "#", i + 1 , '\t', counts.most_common(10)[i][0], "=", counts.most_common(10)[i][1]
f.close()#Closing the file
