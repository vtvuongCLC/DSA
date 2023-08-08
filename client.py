import socket

HOST = "127.0.0.1"
PORT = 65432

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
print("Connecting to server with port " + str(PORT))
client.connect(server_address)

try:
    while True:
        msg = input("Client: ")
        client.sendall(bytes(msg, "utf8"))
        data = client.recv(1024)
        print(data.decode("utf8"))
        if(data == bytes("stop", "utf8")): break
except KeyboardInterrupt:
    client.close()
finally:
    client.close()