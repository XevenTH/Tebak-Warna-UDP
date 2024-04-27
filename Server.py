import socket
import threading
import time
import random

from Warna import Warna as w

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 12345)
server_socket.bind(server_address)

def handle_game(client_socket, client_address, WArray):
        client_socket.sendto(b"Selamat datang di server!", client_address)

        warna = random.choice(WArray)
        
        client_socket.sendto(b"Game Dimulai, Warna akan diacak dan diberikan dalam 10 detik kedepan!!", client_address)
        for count in range(1, 12):
            pesan = ""
            if count == 11:
                pesan = "STOP"
            else:
                pesan = f"{count}"

            client_socket.sendto(pesan.encode(), client_address)
            time.sleep(1)

        client_socket.sendto(str(warna.GetWarna()).encode(), client_address)
        client_socket.sendto(b"Anda Mempunyai Waktu 5 Detik Untuk Menjawab", client_address)

        try:
            client_socket.settimeout(5)  # Set timeout menjadi 5 detik
            while True:
                client_data, _ = client_socket.recvfrom(4096)
                if client_data:
                    break
            
            jawaban = client_data.decode()
            if jawaban == "TIMEOUT":
                client_socket.sendto(str(warna.GetPointAnswer(0)).encode(), client_address)
            else:
                client_socket.sendto(str(warna.GetPointAnswer(jawaban)).encode(), client_address)
        except socket.timeout:
            print("Waktu habis tanpa jawaban dari klien.")

def accept_connections(maxConnection, array_warna):
    clients = []
    while True:
        try:
            client_data, client_address = server_socket.recvfrom(1024)
            print(f"Koneksi dari {client_address}")

            client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            clients.append((client_socket, client_address))

            if len(clients) >= maxConnection:
                print(f"Koneksi Sebanyak {maxConnection} Telah terhubung")
                print("Segera memulai Permainan....")
                threads = []
                for client_socket, client_address in clients:
                    client_thread = threading.Thread(target=handle_game, args=(client_socket, client_address, array_warna))
                    client_thread.start()
                    threads.append(client_thread)

                for thread in threads:
                    thread.join()  # Menunggu hingga semua thread selesai
                    
                break
        except ConnectionResetError:
            print(f"Koneksi dengan {client_address} telah ditutup oleh klien sebelumnya.")
        except KeyboardInterrupt:
            print("Server dimatikan.")

try:
    maxConnection = int(input("Masukan Maximal Koneksi: "))

    kuning = w("Yellow", "Kuning")
    ungu = w("Purple", "Ungu")
    hijau = w("Green", "Hijau")
    merah = w("Red", "Merah")
    biru = w("Blue", "Biru")

    array_warna = [kuning, ungu, hijau, merah, biru]

    print("Server siap menerima koneksi...")
    accept_connections(maxConnection, array_warna)
finally:
    # Setelah semua thread selesai, baru socket server ditutup
    server_socket.close()
