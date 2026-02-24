from core.risk import calculate_risk

def test_calculate_risk():
    assert calculate_risk("http://paypa1.com") == "High"
    assert calculate_risk("http://google.com") == "Low"