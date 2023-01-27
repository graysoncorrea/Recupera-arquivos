import os
import shutil
import tqdm

# Define o caminho do disco a ser varrido
path = "C:\\"

# Faz a varredura do disco
for root, dirs, files in tqdm.tqdm(os.walk(path)):
    for file in files:
        # Verifica se o arquivo foi apagado
        if file.endswith("~"):
            if file.endswith((".jpg", ".jpeg", ".png",".3gp", ".bmp", ".mp4", ".avi", ".mkv", ".wmv", ".flv", ".mov")):
                # Recupera o arquivo
                source = os.path.join(root, file)
                destination = os.path.join("D:\\recovered_files", file)
                shutil.move(source, destination)
