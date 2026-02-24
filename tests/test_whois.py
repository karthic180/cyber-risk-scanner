from core.whois_lookup import get_whois

def test_whois_returns_dict():
    result = get_whois("example.com")
    assert isinstance(result, dict)