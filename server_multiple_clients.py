import socket
import select

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Allow port reuse so you don't get errors if you restart the server quickly
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    
    # Set the server socket to non-blocking mode
    server_socket.setblocking(False)

    # Maintain a list of sockets we want to monitor for incoming data
    # Initially, this is just the server socket listening for new connections
    sockets_list = [server_socket]

    print(f"Listening on {HOST}:{PORT}")

    while True:
        # select() blocks until at least one socket in sockets_list is ready to be read
        read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

        for notified_socket in read_sockets:
            # If the ready socket is the server_socket, it means we have a new incoming connection
            if notified_socket == server_socket:
                conn, addr = server_socket.accept()
                conn.setblocking(False)
                sockets_list.append(conn)
                print(f"Connected by {addr}")

            # Otherwise, it's an existing client socket sending data
            else:
                try:
                    data = notified_socket.recv(1024)
                    
                    if data:
                        # Echo the data back to the client
                        notified_socket.sendall(data)
                    else:
                        # An empty byte string means the client gracefully closed the connection
                        print(f"Connection closed by {notified_socket.getpeername()}")
                        sockets_list.remove(notified_socket)
                        notified_socket.close()
                        
                except ConnectionResetError:
                    # Handle unexpected client disconnects (e.g., closing the terminal)
                    print("Client disconnected abruptly.")
                    sockets_list.remove(notified_socket)
                    notified_socket.close()

        # Clean up any sockets that threw an error
        for notified_socket in exception_sockets:
            sockets_list.remove(notified_socket)
            notified_socket.close()