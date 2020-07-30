def test_localhost_is_up(selenium):
    selenium.get('http://localhost:8000')
    assert 'Django' in selenium.title
