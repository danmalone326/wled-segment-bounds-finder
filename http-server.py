from http.server import HTTPServer, BaseHTTPRequestHandler
import sys
import os
import socket

#########################################
### THIS IS A VERY SIMPLE HTTP SERVER
### SERVING ONLY THE ONE FILE
### THIS IS NOT SECURE AND SHOULD NOT
### BE MADE OPEN TO THE PUBLIC INTERNET
#########################################

FILE_NAME = "segment-bounds-finder.html"

def index_path(path):
    """Returns the path to the index file."""
    return os.path.join(os.getcwd(), path)

class SingleFileRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handles GET requests and serves the specified file."""
        try:
            with open(index_path(FILE_NAME), "rb") as f: 
                content = f.read()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, "File Not Found")

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    server = HTTPServer(('', port), SingleFileRequestHandler)
    ip = get_ip()
    print(f"Connect to this server using: http://{ip}:{port}/")
    print("<Ctrl-C> to stop.")
    server.serve_forever()

if __name__ == "__main__":
    main()