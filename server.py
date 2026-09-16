
import os
import sys
import json
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket

PORT = 8000

class CyberRiskServer(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS and cache-control headers for development
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def do_GET(self):
        # Health check endpoint
        if self.path == '/api/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            payload = {
                "status": "online",
                "app": "Digital Twin — Cybersecurity Risk Predictor",
                "team": "Morningstar",
                "authors": ["Rushil S", "Nikitha H S"]
            }
            self.wfile.write(json.dumps(payload).encode('utf-8'))
            return
        
        return super().do_GET()

def find_available_port(start_port=8000):
    port = start_port
    while port < 65535:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
            port += 1
    return start_port

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    port = find_available_port(PORT)
    url = f"http://localhost:{port}"

    print("=" * 60)
    print("   MORNINGSTAR CYBERSECURITY — DIGITAL TWIN PREDICTOR")
    print(f"   Researchers: Rushil S & Nikitha H S")
    print("=" * 60)
    print(f"[*] Serving application at: {url}")
    print("[*] Opening your browser...")
    print("[*] Press Ctrl+C to stop the server.")
    print("=" * 60)

    webbrowser.open(url)

    server = HTTPServer(('127.0.0.1', port), CyberRiskServer)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[*] Shutting down Morningstar Cyber Risk Server.")
        server.server_close()

if __name__ == '__main__':
    main()
