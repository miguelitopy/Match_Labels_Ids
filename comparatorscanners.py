import os

class Comparator:
    def __init__(self, input_file, output_file):
        self.input_file = input_file #Arquivo que guarda
        self.output_file = output_file #Arquivo que guarda o resultado
        self.flag = 0

    def compare_labels(self, final_label):
        print(f"valor atual da flag {self.flag}")
        """
        Lê a primeira etiqueta do arquivo inicial, compara com o final_label e salva o resultado.
        """
        # Verifica se o arquivo inicial existe
        if not os.path.exists(self.input_file):
            self.flag = 0
            raise FileNotFoundError(f"Arquivo {self.input_file} não encontrado.")

        # Lê a primeira linha do arquivo inicial
        with open(self.input_file, 'r') as file:
            lines = file.readlines()
        
        if not lines:
            print("Nenhuma etiqueta para comparar. Arquivo vazio.")
            self.flag=0
            return "OK"
        
        initial_label = lines[0].strip()

        # Compara as etiquetas
        status = "OK" if initial_label == final_label else "NG"

        if status=='NG' and self.flag == 0 :
           return "OK"

        if status=='OK' and self.flag == 0 :
           self.flag = 1

        if self.flag == 1 :

            # Salva o resultado no arquivo de saída
            with open(self.output_file, 'a') as file:
                result = f"{initial_label},{final_label},{status}"
                file.write(result + "\n")

            # Remove a etiqueta usada do arquivo inicial
            with open(self.input_file, 'w') as file:
                file.writelines(lines[1:])

            # Exibe o resultado no console
            print(f"Resultado: {initial_label},{final_label},{status}")

        return status



