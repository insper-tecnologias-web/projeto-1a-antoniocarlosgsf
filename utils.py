from pathlib import Path
import json

def extract_route(request: str) -> str:
    # Divide a string da requisição em linhas
    lines = request.split("\n")
    
    # A primeira linha contém o método HTTP e a rota
    first_line = lines[0]
    
    # Divide a primeira linha por espaços e obtém a rota
    parts = first_line.split()
    if len(parts) > 1:
        route = parts[1]
        
        # Remove o primeiro caractere '/' se existir
        return route.lstrip('/')
    
    return ""  # Retorna string vazia caso a estrutura da requisição seja inválida


def read_file(file_path: Path) -> bytes:
    # Verifica se o arquivo existe antes de tentar abrir
    if not file_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    
    with file_path.open("rb") as file:
        return file.read()
    

def load_data(filename: str):
    # Define o caminho do arquivo na pasta 'data'
    file_path = Path("data") / filename
    
    # Lê e carrega o conteúdo JSON como um objeto Python
    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)
    

def load_template(filename: str) -> str:
    # Define o caminho do arquivo na pasta 'templates'
    file_path = Path("templates") / filename
    
    # Lê e retorna o conteúdo do arquivo como string
    with file_path.open("r", encoding="utf-8") as file:
        return file.read()