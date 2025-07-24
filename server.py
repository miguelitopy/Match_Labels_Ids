from flask import Flask, render_template, jsonify
from threading import Thread
import os
from comparatorscanners import Comparator

# ================= ROTAS DO FRONTEND ==================

# Caminho absoluto para templates e arquivos estáticos
template_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Frontend', 'templates')
static_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Frontend', 'static')

FILE_PATH = "history_set_ids.txt"
RESULT_FILE = "results_queue_ids.txt"

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Caminho de Rotas Flask
@app.route('/')
def index():
    return render_template('index.html')

def get_last_line(file_path):
    """Lê a última linha de um arquivo."""
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
            return lines[-1].strip() if lines else "Sem leitura"
    return "Arquivo não encontrado"

@app.route("/leituras", methods=["GET"])
def get_leituras():
    """Retorna as últimas leituras dos scanners."""
    scanner1 = get_last_line(FILE_PATH)
    scanner2 = get_last_line(RESULT_FILE)
    return jsonify({"scanner1": scanner1, "scanner2": scanner2})

# Retorna o último status de comparação OK/NG
@app.route('/api/get-comparison-results')
def get_comparison_results():
    try:
        with open("results_queue_ids.txt", "r") as file:
            lines = file.readlines()
            if lines:
                last_result = lines[-1].strip().split(',')
                return jsonify({"status": last_result[-1]})
    except Exception as e:
        print(f"Erro ao ler o arquivo de resultados: {e}")
    return jsonify({"status": "Error"})


# Retorna todas as etiquetas processadas
@app.route('/api/getall')
def get_all_results():
    try:
        with open("results_queue_ids.txt", "r") as file:
            lines = file.readlines()
            results = [line.strip().split(',') for line in lines if line.strip()]
            results.reverse()
            return jsonify({"results": results})
    except Exception as e:
        print(f"Erro ao ler o arquivo de resultados: {e}")
    return jsonify({"results": []})

# Rota para apagar histórico
@app.route('/api/clear-history', methods=['POST'])
def clear_history():
    try:
        # Lista de arquivos para limpar
        files_to_clear = ["results_queue_ids.txt", "history_set_ids.txt"]

        for file in files_to_clear:
            open(file, 'w').close()  # Abre o arquivo no modo de escrita para esvaziá-lo

            return jsonify({"status": "success", "message": "Histórico apagado com sucesso!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
    
@app.route('/api/get-error')
def get_error():
    try:
        with open("Erro_log_txt","r") as file:
            errors = file.readlines()
            if errors:
                return jsonify({"error": errors[-1].strip()})  # Retorna o último erro registrado
    except FileNotFoundError:
        return jsonify({"error": "Nenhum erro encontrado"})
    return jsonify({"error": ""})  # Caso não haja erros registrados


# ================= EXECUÇÃO ==================

if __name__ == '__main__':
    app.run(debug=True, port=5000)


   #MUDANÇA PARA INSERIR POPUP

# from flask import Flask, render_template, jsonify
# import os

# # Configuração de caminhos
# template_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Frontend', 'templates')
# static_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Frontend', 'static')

# app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# # Página principal
# @app.route('/')
# def index():
#     return render_template('index.html')

# # Retorna o último status (OK/NG)
# @app.route('/api/get-comparison-results')
# def get_comparison_results():
#     try:
#         with open("results_queue_ids.txt", "r") as file:
#             lines = file.readlines()
#             if lines:
#                 return jsonify({"status": lines[-1].strip().split(',')[-1]})
#     except Exception as e:
#         return jsonify({"status": "Error"})

# # Retorna todas as etiquetas processadas
# @app.route('/api/getall')
# def get_all_results():
#     try:
#         with open("results_queue_ids.txt", "r") as file:
#             results = [line.strip().split(',') for line in file if line.strip()]
#             return jsonify({"results": results[::-1]})
#     except Exception as e:
#         return jsonify({"results": []})

# # Apaga os históricos de leitura
# @app.route('/api/clear-history', methods=['POST'])
# def clear_history():
#     try:
#         for file in ["results_queue_ids.txt", "history_set_ids.txt"]:
#             open(file, 'w').close()
#         return jsonify({"status": "success", "message": "Histórico apagado!"})
#     except Exception as e:
#         return jsonify({"status": "error", "message": str(e)})

# # Rota para obter o último erro de leitura
# @app.route('/api/get-last-error')
# def get_last_error():
#     try:
#         with open("error_log.txt", "r") as file:
#             errors = file.readlines()
#             if errors:
#                 return jsonify({"error": errors[-1].strip()})
#     except:
#         return jsonify({"error": ""})  # Nenhum erro encontrado
#     return jsonify({"error": ""})

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)

