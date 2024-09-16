import socket
import ssl

hostname = 'www.python.org'
port = 443

context = ssl.create_default_context()

with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        ssock.sendall(b"GET / HTTP/1.1\r\nHost: www.python.org\r\n\r\n")
        data = ssock.recv(1024)
        print(data.decode())
