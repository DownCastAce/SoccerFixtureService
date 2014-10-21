from extractionFactory import *

def testCreateExtractorForUnknownTeam():
        factory = ExtractionFactory()
        assert factory.createExtractor("foo") == None

def testCreateExtractorForArsenal():
        factory = ExtractionFactory()
        arsenal = factory.createExtractor("Arsenal") 
	assert arsenal != None
	assert arsenal.teamName() == "Arsenal"
