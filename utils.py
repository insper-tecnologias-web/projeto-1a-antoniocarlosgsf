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
    

def adicionar_anotacao(nova_anotacao, caminho_arquivo='data/notes.json'):
    try:
        # Tenta abrir e carregar o conteúdo atual do arquivo
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            anotacoes = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        # Se o arquivo não existir ou estiver vazio/corrompido, inicia uma lista vazia
        anotacoes = []
    
    # Adiciona a nova anotação
    anotacoes.append(nova_anotacao)
    
    # Escreve a lista atualizada de volta no arquivo
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(anotacoes, arquivo, ensure_ascii=False, indent=4)

def build_response(body='', code=200, reason='OK', headers=''):
    """
    Constrói uma resposta HTTP.
    :param body: O corpo da resposta HTTP.
    :param code: O código de status da resposta (padrão: 200).
    :param reason: O motivo do código de status (padrão: 'OK').
    :param headers: Cabeçalhos adicionais da resposta (padrão: '').
    :return: A resposta HTTP formatada corretamente.
    """
    response_line = f"HTTP/1.1 {code} {reason}"
    
    # # Garantindo que headers seja uma string válida
    if headers:
        response_line += '\n'
    
    
    
    # Linha em branco separando cabeçalho e corpo
    return f"{response_line}{headers}\n\n{body}".encode()

# b'HTTP/1.1 404 Not Found\n\n'
# b'HTTP/1.1 404 Not Found\n\n\n'