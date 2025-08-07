import urllib.request
import socket

class InternetChecker:
    @staticmethod
    def is_connected():
        """Check internet connectivity with timeout"""
        try:
            urllib.request.urlopen('https://www.google.com', timeout=2)
            return True
        except (urllib.request.URLError, socket.timeout):
            return False