import socket

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 443]

def scan_ports(domain):
    results = {}
    for port in COMMON_PORTS:
        sock = socket.socket()
        sock.settimeout(1)
        result = sock.connect_ex((domain, port))
        sock.close()
        results[port] = (result == 0)
    return results