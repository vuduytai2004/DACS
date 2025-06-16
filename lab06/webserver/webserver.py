import socket

def handle_request(client_socket, request_data):
    if "GET /admin" in request_data:
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nWelcome to the admin page!"
    else:
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nHello, this is a simple web server!"
    
    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()
    import socket
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8080))  # Fixed: Added parentheses for tuple
    server_socket.listen(5)

    print("Server listening on port 8080...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")  # Fixed: Added f-string
        request_data = client_socket.recv(1024).decode('utf-8')  # Fixed: Changed 'rev' to 'recv'
        handle_request(client_socket, request_data)

if __name__ == '__main__':
    main()