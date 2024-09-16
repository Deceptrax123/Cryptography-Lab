import socket
import ssl

hostname = 'localhost'
port = 8443

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('SSL-Socket/ssl/certificate.pem',
                        'SSL-Socket/ssl/key.pem')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind((hostname, port))
    sock.listen(5)

    while True:
        conn, addr = sock.accept()
        with context.wrap_socket(conn, server_side=True) as ssock:
            data = ssock.recv(1024)
            print(data.decode())
            ssock.sendall(b"HTTP/1.1 200 OK\r\n\r\nHello from the server!")
