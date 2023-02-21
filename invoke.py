import os
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from io import StringIO

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        output = self.execute_shell_script()
        
        self.wfile.write(output.encode('utf-8'))

    def execute_shell_script(self):
        script = './script.sh'
        output = StringIO()

        try:
            subprocess.check_call(script, stdout=output, stderr=output, shell=True)
        except subprocess.CalledProcessError as e:
            output.write(f"Error executing script: {e}\n")

        return output.getvalue()

def main():
    port = int(os.getenv('PORT', '8080'))

    with HTTPServer(('', port), Handler) as httpd:
        print(f"Starting server on port {port}")
        httpd.serve_forever()

if __name__ == '__main__':
    main()
