# tests/test_ssl.py

from core.ssl_check import check_ssl  # Ensure this is the correct import for check_ssl

def test_ssl_invalid_domain():
    # Assuming check_ssl returns a boolean (True if valid, False if invalid)
    result = check_ssl("invalid-domain-xyz-test.com")
    
    # Assert that the result is False, because it's an invalid domain
    assert result is False  # Since the domain is invalid