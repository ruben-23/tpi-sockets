import socket

def nod_2():
    # Configurarea adresei și porturilor pentru comunicarea cu Nodul 1 și Nodul 3
    host_nod_1 = '127.0.0.1'
    port_nod_1 = 5001  # Portul de ascultare al Nodului 2 (de la Nodul 1)
    host_nod_3 = '127.0.0.1'
    port_nod_3 = 5002  # Portul Nodului 3
    
    # Ascultare pentru mesajul de la Nodul 1
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', port_nod_1))
        s.listen()
        print("Nodul 2 așteaptă mesaj de la Nodul 1...")
        conn, addr = s.accept()
        with conn:
            mesaj = conn.recv(1024).decode()
            print(f"Nodul 2 a primit mesajul: {mesaj}")

    # Trimiterea mesajului mai departe către Nodul 3
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host_nod_3, port_nod_3))
        s.sendall(mesaj.encode())

if __name__ == "__main__":
    nod_2()

