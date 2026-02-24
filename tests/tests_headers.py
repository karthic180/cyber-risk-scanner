from core.headers import get_headers

def test_headers_returns_dict():
    result = get_headers("example.com")
    assert isinstance(result, dict)