import socket

def nod_3():
    # Configurarea adresei și porturilor pentru comunicarea cu Nodul 2 și Nodul 1
    host_nod_2 = '127.0.0.1'
    port_nod_2 = 5002  # Portul de ascultare al Nodului 3 (de la Nodul 2)
    host_nod_1 = '127.0.0.1'
    port_nod_1 = 5000  # Portul Nodului 1 (pentru trimiterea mesajului înapoi)

    # Ascultare pentru mesajul de la Nodul 2
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', port_nod_2))
        s.listen()
        print("Nodul 3 așteaptă mesaj de la Nodul 2...")
        conn, addr = s.accept()
        with conn:
            mesaj = conn.recv(1024).decode()
            print(f"Nodul 3 a primit mesajul: {mesaj}")

    # Trimiterea mesajului înapoi la Nodul 1
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host_nod_1, port_nod_1))
        s.sendall(mesaj.encode())

if __name__ == "__main__":
    nod_3()

