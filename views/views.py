from utils import load_data, load_template, adicionar_anotacao, build_response
from urllib.parse import unquote_plus

def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        
        if len(partes) > 1:
            corpo = partes[1]
            params = {}
            
            # Preenchendo o dicionário params com os valores do corpo da requisição
            for chave_valor in corpo.split('&'):
                chave, valor = chave_valor.split('=')  # Divide em chave e valor
                params[chave] = unquote_plus(valor)  # Decodifica caracteres especiais
        adicionar_anotacao(params)
        
        # Retorna resposta com redirecionamento
        return build_response(code=303, reason='See Other', headers='Location: /')

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]
    notes = '\n'.join(notes_li)

    return build_response(body=load_template('index.html').format(notes=notes))