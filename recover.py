import os
import shutil

# Define o caminho do disco a ser varrido
path = "C:\\"

# Faz a varredura do disco
for root, dirs, files in os.walk(path):
    for file in files:
        # Verifica se o arquivo foi apagado
        if file.endswith("~"):
            # Recupera o arquivo
            source = os.path.join(root, file)
            destination = os.path.join("C:\\recovered_files", file)
            shutil.move(source, destination)
