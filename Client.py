import socket

# Membuat soket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)

sock.sendto(b"ConnectionCode", server_address)

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

    jawaban = input("Jawaban: ")

    sock.sendto(jawaban.encode(), server_address)

    print("Mengecek Hasil...")
    sock.settimeout(6)

    data, _ = sock.recvfrom(4096)
    if int(data.decode()) == 100:
        print(f"Selamat Anda mendapatkan {int(data.decode())} poin!")
    else:
        print(f"Sayang sekali, Anda salah. Poin yang Anda dapatkan: {int(data.decode())}")

except Exception as e:
    print("Terjadi kesalahan:", e)

finally:
    sock.close()
