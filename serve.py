import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.csv': 'text/csv',
})

print(f"Starting server at http://localhost:{PORT}")
print("Open your browser and go to http://localhost:8000")
print("Press Ctrl+C to stop the server")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever() 