import socket

def nod_1():
    # Configurarea adresei și portului pentru Nodul 1
    host_nod_2 = '127.0.0.1'  # IP-ul Nodului 2
    port_nod_2 = 5001  # Portul Nodului 2
    
    # Configurarea adresei și portului pentru ascultarea de la Nodul 3
    port_nod_1 = 5000  # Portul Nodului 1 (pentru așteptare de la Nodul 3)

    # Citire mesaj de la utilizator
    mesaj = input("Introduceți un mesaj: ")

    # Trimiterea mesajului către Nodul 2
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host_nod_2, port_nod_2))
        s.sendall(mesaj.encode())

    # Ascultare pentru a primi mesajul de la Nodul 3
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', port_nod_1))
        s.listen()
        print("Nod 1 așteaptă mesaj de la Nodul 3...")
        conn, addr = s.accept()
        with conn:
            mesaj_final = conn.recv(1024).decode()
            print(f"Nodul 1 a primit mesajul de la Nodul 3: {mesaj_final}")

if __name__ == "__main__":
    nod_1()

