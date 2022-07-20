import socket
import thread
import json

HOST = '127.0.0.1'              # Endereco IP do Servidor
PORT = 3333            # Porta que o Servidor esta

def conectado(con, cliente):
    print 'Conectado por', cliente

    while True:
        msg = con.recv(1024)
        if not msg: break
        msg = json.loads(msg)
        print cliente, msg
        
        response = json.dumps({"message": "mensagem recebida!"})
        con.send(response)

    print 'Finalizando conexao do cliente', cliente
    con.close()
    thread.exit()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    thread.start_new_thread(conectado, tuple([con, cliente]))

tcp.close()