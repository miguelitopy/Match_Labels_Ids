import os
import shutil
from datetime import datetime

# Nome do arquivo original
arquivo_original1 = "results_queue_ids.txt"
arquivo_original2 = "history_set_ids.txt"
# Nome da pasta de destino
pasta_destino = "History_Match"

# Criar a pasta se não existir
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# Obter a data atual no formato YYYY-MM-DD
data_atual = datetime.now().strftime("%Y-%m-%d")

# Criar o novo nome do arquivo 1 com a data no final
nome_base, extensao = os.path.splitext(arquivo_original1)
novo_nome = f"{nome_base}_{data_atual}{extensao}"

# Criar o novo nome do arquivo 2 com a data no final
nome_base_2, extensao_2 = os.path.splitext(arquivo_original2)
novo_nome_2 = f"{nome_base_2}_{data_atual}{extensao_2}"


# Caminho completo do novo arquivo
caminho_novo = os.path.join(pasta_destino, novo_nome)

# Caminho completo do novo arquivo
caminho_novo_2 = os.path.join(pasta_destino, novo_nome_2)

# Mover o arquivo renomeado para a pasta History
if os.path.exists(arquivo_original1):
    shutil.move(arquivo_original1, caminho_novo)
    print(f"Arquivo movido para: {caminho_novo}")
else:
    print(f"Arquivo '{arquivo_original1}' não encontrado.")

# Mover o arquivo renomeado para a pasta History
if os.path.exists(arquivo_original2):
    shutil.move(arquivo_original2, caminho_novo_2)
    print(f"Arquivo movido para: {caminho_novo_2}")
else:
    print(f"Arquivo '{arquivo_original2}' não encontrado.")


