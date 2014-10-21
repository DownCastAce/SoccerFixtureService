from arsenalExtractor import *

def testTeamName():
	arsenal = ArsenalExtractor()
	assert arsenal.teamName() == "Arsenal"
