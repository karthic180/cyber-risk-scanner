# Make sure the import path is correct
from core.url_analysis import is_phishing

def test_is_phishing():
    # Test case to check phishing detection
    assert is_phishing("http://paypa1.com") == True
    assert is_phishing("http://google.com") == False