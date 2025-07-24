import socket
from time import sleep
from comparatorscanners import Comparator

HOST_CLP = "192.168.0.51"
PORT_CLP = 2004
HOST_SCANNER = "192.168.0.59"
PORT_SCANNER = 9004
FILE_PATH = "history_set_ids.txt"
RESULT_FILE = "results_queue_ids.txt"
ERROR_LOG = "error_log.txt"

comparator = Comparator(FILE_PATH, RESULT_FILE)

try:
    socket_scanner = socket.create_connection((HOST_SCANNER, PORT_SCANNER), timeout=50)
    print("Scanner 2 conectado!")
except socket.error as e:
    with open(ERROR_LOG, 'a') as error_file:
        error_file.write(f"Erro na conexão com o Scanner 2: {e}\n")
    print(f"Erro na conexão com o Scanner 2: {e}")

atual = ""
while True:
    response = ""
    while not response:
        try:
            response = socket_scanner.recv(1024).decode('utf-8').strip()
        except:
            print("Timeout na leitura")
    try:
        response = response[2:]
        if response and response != atual:
            atual = response
            print(f"Etiqueta final lida: {response}")
            status = comparator.compare_labels(response)
            mensagem = b'%MX2764' if status == "OK" else b'%MX2765'
            try:
                socket_clp = socket.create_connection((HOST_CLP, PORT_CLP), timeout=50)
                socket_clp.send(mensagem)
                socket_clp.close()
            except socket.error as e:
                with open(ERROR_LOG, 'a') as error_file:
                    error_file.write(f"Erro ao enviar para CLP: {e}\n")
                print(f"Erro ao enviar para CLP: {e}")
    except Exception as e:
        with open(ERROR_LOG, 'a') as error_file:
            error_file.write(f"Erro na leitura do Scanner 2: {e}\n")
        print(f"Erro na leitura do Scanner 2: {e}")