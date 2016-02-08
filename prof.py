#!usr/bin/env
from BeautifulSoup import BeautifulSoup
import requests

# TODO: Create file support to save all of this in a file.
# Current usage: python prof.py > cs_professrs.txt

def main():
    dept = "computer-science" 
    BASE_URL= "https://www.rit.edu/gccis/people" 
    html = requests.get(BASE_URL.format(dept)).text
    soup = BeautifulSoup(html)
    for staff in soup.findAll('div', 'staff-info'):
        print staff.find("div", {"class":"staff-name"}).find('a').contents[0]
        anchor_email = filter(lambda x : 'mailto' in x['href'], staff.findAll("a"))
        print map(lambda y : str(y.contents[0]) if len(y) > 0  else None, anchor_email)[0]
        # Print new line to make it look better in the file
        print ""


if __name__ == '__main__':
    main()
