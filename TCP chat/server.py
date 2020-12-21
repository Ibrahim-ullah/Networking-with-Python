import threading
import socket

host = '127.0.0.1' #localhost
port = 55555

#this will make the port 55555 of the localhost to listen
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()


clients = []
nicknames = []

#broadcasting. this function sends message to all the clients connecting to the server.
def broadcast(message):
    for client in clients:
        client.send(message)


'''this handle function will be created for every client connection.There will be single thread for every client. When a
user lefts it will create a broadcast message to everyone. This function handles the message received by
previous function which need to be sent to everyone '''
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            nicknames.remove(nickname)
            break
         


def receive():
    while True:
        client, address = server.accept() #accept client all the time
        print(f"Connected with {str(address)}") # whenever a client is connected, we show his address
        client.send('NICK'.encode('ascii')) #it asks the client for its nickname 
        nickname = client.recv(1024).decode('ascii') #it decondes the nickname provided by the user
        nicknames.append(nickname) 
        clients.append(client)


        print(f"Nickname of the the client is {nickname}")
        broadcast(f'{nickname} joined the chat'.encode('ascii'))
        client.send('Connected to ther server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()