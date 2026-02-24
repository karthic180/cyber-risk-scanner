# core/ssl_check.py

import ssl
import socket

def check_ssl(domain):
    """
    Function to check if a domain has a valid SSL certificate.
    
    Returns:
        True if SSL is valid, False if invalid.
    """
    try:
        context = ssl.create_default_context()
        # Try connecting to the domain on port 443 (SSL port)
        with socket.create_connection((domain, 443), timeout=10) as conn:
            with context.wrap_socket(conn, server_hostname=domain) as ssock:
                ssock.getpeercert()  # Get the SSL certificate
                return True  # SSL certificate is valid
    except Exception as e:
        return False  # Return False if there is an issue (invalid certificate, connection issue)