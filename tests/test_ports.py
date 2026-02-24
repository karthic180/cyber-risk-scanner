from core.ports import scan_ports

def test_scan_ports_structure(monkeypatch):
    def fake_connect_ex(self, addr):
        return 0  # simulate open port

    monkeypatch.setattr("socket.socket.connect_ex", fake_connect_ex)

    result = scan_ports("example.com")

    assert isinstance(result, dict)
    for port, status in result.items():
        assert status is True