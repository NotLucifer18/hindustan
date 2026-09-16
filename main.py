#!/usr/bin/env python3
"""
Digital Twin — Cybersecurity Risk Predictor
Black & Red Cyber Command Center Entrypoint (main.py)
Organization: Morningstar Cyber Labs
Lead Researchers: Rushil S & Nikitha H S
"""

import os
import sys
import json
import webbrowser
import socket
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Ensure UTF-8 output encoding on Windows consoles
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PORT = 8000

class MorningstarHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Prevent aggressive browser caching during active development
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def do_GET(self):
        # Health & Telemetry API
        if self.path == '/api/health':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            payload = {
                "status": "ONLINE",
                "system": "Digital Twin — Cybersecurity Risk Predictor",
                "team": "Morningstar Cyber Labs",
                "researchers": ["Rushil S", "Nikitha H S"],
                "architecture": "Client-Side Zero-Backend Command Center"
            }
            self.wfile.write(json.dumps(payload, indent=2).encode('utf-8'))
            return
        
        # Default index handler
        if self.path == '/' or self.path == '':
            self.path = '/index.html'

        return super().do_GET()

def find_open_port(preferred_port=8000):
    port = preferred_port
    while port < 65535:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
            port += 1
    return preferred_port

def print_banner(url):
    print("=" * 66)
    print("            MORNINGSTAR CYBERSECURITY DEFENSE LABS")
    print("          Digital Twin Threat Predictor & Simulator")
    print("=" * 66)
    print(f" Research Team:  Rushil S & Nikitha H S")
    print(f" Organization:   Morningstar Cyber Labs")
    print(f" Interface:      Black & Red Multi-Page Cyber Command Center")
    print(f" Local Address:  {url}")
    print(f" Health API:     {url}/api/health")
    print("=" * 66)
    print(" [+] Launching default browser...")
    print(" [!] Press Ctrl+C in this terminal to shut down the server.\n")

def main():
    # Ensure current directory is the script root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    port = find_open_port(PORT)
    url = f"http://localhost:{port}"

    print_banner(url)

    # Open the browser to the web app
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"Notice: Could not automatically launch browser ({e}). Please navigate manually to {url}")

    server = HTTPServer(('127.0.0.1', port), MorningstarHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Shutting down Morningstar Cyber Command Server...")
        server.server_close()
        print("[+] Server safely stopped.\n")

if __name__ == '__main__':
    main()
