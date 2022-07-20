import socket
import json


HOST = '127.0.0.1'              # Endereco IP do Servidor
PORT = 3333            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print 'Concetado por', cliente
    while True:
        msg = con.recv(1024)
        if not msg: break
        msg = json.loads(msg)
        print cliente, msg
        
        response = json.dumps({"message": "mensagem recebida!"})
        con.send(response)
    print 'Finalizando conexao do cliente', cliente
    con.close()