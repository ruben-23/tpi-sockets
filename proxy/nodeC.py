import socket
import time

def nodC():
    nodB_ip = '127.0.0.1'
    nodB_port_tcp = 5002

    # Așteptare de 5 secunde înainte de a trimite cererea
    time.sleep(5)

    # Trimiterea solicitării TCP către NodB
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((nodB_ip, nodB_port_tcp))
        s.sendall("Trimite mesaje".encode())
        print("NodC a trimis solicitarea către NodB.")

        # Primirea celor 3 mesaje de la NodB
        for _ in range(3):
            data = s.recv(1024).decode()
            print(f"NodC a primit: {data}")

if __name__ == "__main__":
    nodC()

