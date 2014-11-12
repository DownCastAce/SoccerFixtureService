from bs4 import BeautifulSoup

def testPageGet():
	f = open("tests/arsenalHardCopy/first-team", "r")
        content = f.read()
	assert content != None

def testBS():
	f = open("tests/arsenalHardCopy/first-team", "r")
	content = f.read()
	print content[:10]
	soup = BeautifulSoup(content)
        assert soup != None
        for elem in soup.find_all(class_='versus'):
		print elem

if __name__ == "__main__":
	testPageGet()
 	testBS()
