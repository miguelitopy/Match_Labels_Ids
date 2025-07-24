import socket
from time import sleep
import serial
import os

ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,
    parity=serial.PARITY_ODD,
    stopbits=serial.PARITY_ODD,
    bytesize=serial.SEVENBITS
)

HOST_SCANNER = "192.168.0.61"
PORT_SCANNER = 9004
FILE_PATH = "history_set_ids.txt"
ERROR_LOG = "error_log.txt"

try:
    socket_scanner = socket.create_connection((HOST_SCANNER, PORT_SCANNER), timeout=50)
    print("Scanner 1 conectado!")
except socket.error as e:
    with open(ERROR_LOG, 'a') as error_file:
        error_file.write(f"Erro na conexão com o Scanner 1: {e}\n")
    print(f"Erro na conexão com o Scanner 1: {e}")

while True:
    response = ""
    while not response:
        try:
            response = socket_scanner.recv(1024).decode('utf-8').strip()
        except:
            print("Timeout na leitura")
            sleep(2)
    try:
        if response:
            response = response[2:]
            if "ERROR" in response:
                print("Scanner 1 não leu a etiqueta anterior, faça a leitura manualmente no posto.")
                response = ser.readline().decode().strip().replace("/", "").replace("r", "").replace("n", "")
                print(f"Leitura manual realizada: {response}")
                
            with open(FILE_PATH, 'a') as file:
                file.write(response + "\n")
                print(f"Salvo: {response}")
            sleep(0.5)
    except Exception as e:
        with open(ERROR_LOG, 'a') as error_file:
            error_file.write(f"Erro de leitura no Scanner 1. Aguardando leitura manual: {e}\n")
        print(f"Erro de leitura no Scanner 1: {e}")
