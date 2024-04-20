from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class WebRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        
        # Establecer la cookie si el parámetro 'register_click' está en la URL
        query = urlparse(self.path).query
        params = parse_qs(query)
        if 'register_click' in params:
            book_title = params['register_click'][0]
            self.send_header("Set-Cookie", f"register_click={book_title}; Path=/")
        
        self.end_headers()
        
        # Escribir el contenido HTML de la respuesta
        self.wfile.write("""
            <!DOCTYPE html>
            <html lang="es-mx">
            <head>
                <meta charset="UTF-8">
                <title>La Biblioteca</title>
            </head>
            <body>
                <h1>La Biblioteca</h1>
                <p><a href="?register_click=C# avanzado">C# avanzado</a></p>
                <p><a href="?register_click=El nuevo sistema operativo MS-DOS">El nuevo sistema operativo MS-DOS</a></p>
            </body>
            </html>
        """.encode("utf-8"))

if __name__ == "__main__":
    print("Server starting...")
    server = HTTPServer(("0.0.0.0", 8000), WebRequestHandler)
    server.serve_forever()

