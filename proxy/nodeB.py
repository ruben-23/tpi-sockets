import socket

def nodB():
    nodB_ip = '127.0.0.1'
    nodB_port_udp = 5001  # Portul UDP pentru primirea mesajelor de la NodA
    nodB_port_tcp = 5002  # Portul TCP pentru primirea cererii de la NodC

    mesaje_primite = []

    # Pasul 1: Primirea mesajelor de la NodA prin UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_sock:
        udp_sock.bind((nodB_ip, nodB_port_udp))
        print("NodB așteaptă mesaje de la NodA...")
        for _ in range(3):
            data, addr = udp_sock.recvfrom(1024)
            mesaj = data.decode()
            mesaje_primite.append(mesaj)
            print(f"NodB a primit: {mesaj} de la {addr}")

    # Pasul 2: Așteptarea cererii de la NodC prin TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_sock:
        tcp_sock.bind((nodB_ip, nodB_port_tcp))
        tcp_sock.listen(1)
        print("NodB așteaptă solicitare TCP de la NodC...")

        conn, addr = tcp_sock.accept()
        with conn:
            print(f"NodB a fost contactat de NodC: {addr}")
            data = conn.recv(1024).decode()
            if data == "Trimite mesaje":
                print("NodB trimite mesajele către NodC...")
                for mesaj in mesaje_primite:
                    conn.sendall(mesaj.encode())
                    print(f"NodB a trimis: {mesaj}")

if __name__ == "__main__":
    nodB()

