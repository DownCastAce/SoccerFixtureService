import fixture

def test_default_values():
    test_fixture = fixture.Fixture()
    assert test_fixture.date == None
    assert test_fixture.home_team == None
    assert test_fixture.away_team == None
    assert test_fixture.competition == None
    assert test_fixture.location == None
    
