import socket
import sys
import select
import threading

# Membuat soket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)

sock.sendto(b"ConnectionCode", server_address)

def get_input():
    global jawaban
    jawaban = input("Jawaban: ")

def handle_timeout():
    print("Waktu habis, mengirim TIMEOUT ke server")
    sock.sendto("TIMEOUT".encode(), server_address)


try:
    data, _ = sock.recvfrom(4096)
    print('Menerima balasan dari server:', data.decode())

    data, _ = sock.recvfrom(4096)
    print(data.decode())
    
    while True:
        data, _ = sock.recvfrom(4096)
        if data.decode() == "STOP":
            break
        else:
            print(data.decode())

    data, _ = sock.recvfrom(4096)
    print(f"Warna sekarang adalah: {data.decode()}")

    data, _ = sock.recvfrom(4096)
    print(data.decode())

    input_thread = threading.Thread(target=get_input)

    timeout = 5

    input_thread.start()

    input_thread.join(timeout)

    if input_thread.is_alive():
        handle_timeout()
    else:
        sock.sendto(jawaban.encode(), server_address)

    print("Mengecek Hasil...")

    while True:
        data, _ = sock.recvfrom(4096)
        if(data):
            break
    
    if int(data.decode()) == 100:
        print(f"Selamat Anda mendapatkan {int(data.decode())} poin!")
    else:
        print(f"Sayang sekali, Anda salah. Poin yang Anda dapatkan: {int(data.decode())}")

    sys.exit()

except Exception as e:
    print("Terjadi kesalahan:", e)

finally:
    sock.close()
