import socket
import time

def nodA():
    nodB_ip = '127.0.0.1'
    nodB_port = 5001

    mesajele = ["Mesaj 1", "Mesaj 2", "Mesaj 3"]

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        for mesaj in mesajele:
            s.sendto(mesaj.encode(), (nodB_ip, nodB_port))
            print(f"NodA a trimis: {mesaj}")
            time.sleep(1)  # Pauză de 1 secundă între mesaje

if __name__ == "__main__":
    nodA()

