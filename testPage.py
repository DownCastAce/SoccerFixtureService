from bs4 import BeautifulSoup

def testPageGet():
	f = open("tests/first-team", "r")
	content = f.read()
	assert content != None

def testBS():
	f = open("tests/first-team", "r")
	content = f.read()
	print content[:10]
	soup = BeautifulSoup(content)
	assert soup != None
	for elem in soup.find_all(class_='versus'):
		print elem

def testNextTeam():
	f = open("tests/first-team", "r")
	content = f.read()
	soup = BeautifulSoup(content)
	assert soup != None
	for elem in soup.find_all(class_='fixture-info'):
		print elem

def testNextTeamInfo():
	f = open("tests/first-team", "r")
	content = f.read()
	soup = BeautifulSoup(content)
	assert soup != None
	for elem in soup.find_all(class_='fixture-info'):
		print elem

if __name__ == "__main__":
	testPageGet()
#	testBS()
#	testNextTeam()
	testNextTeamInfo()
