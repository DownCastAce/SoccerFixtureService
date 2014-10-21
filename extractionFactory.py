from arsenalExtractor import *

class ExtractionFactory:
    def createExtractor(self, team):
	if team == "Arsenal":
		return ArsenalExtractor()
             
