import json, os

def main():
    while True:
        option = menu()
        match option:
            case 1:
                apto = remover_spaces(input('Apto: '))
                nome = remover_spaces(input('Nome: '), 'nome')
                tel = remover_spaces(input('Tel: '))

                is_valid_apto = validar_dados(apto, 'apto')
                is_valid_nome = validar_dados(nome, 'nome')
                is_valid_tel = validar_dados(tel, 'tel')

                if not is_valid_apto or not is_valid_nome or not is_valid_tel:
                    print('Dados inválidos.')
                    continue

                is_cadastred = cadastrar_apto(apto, nome, tel)
                if is_cadastred:
                    print('Morador cadastrado.')
                else:
                    print('Morador já cadastrado.')
            case 2:
                is_exist_apto = buscar_apto(remover_spaces(input('Apto: ')))
                if is_exist_apto:
                    imprimir_dados(is_exist_apto)
                else:
                    print('Morador não encontrado.')
            case 3:
                is_exclude = excluir_apto(remover_spaces(input('Apto: ')))
                
                if is_exclude:
                    print('Morador excluido.')
                else:
                    print('Morador não encontrado.')
            case 4:
                print('Programa encerrado.')
                break

def buscar_apto(search_apto):
    aptos = carregar_dados()

    for apto in aptos:
        if apto.get('apto') == search_apto:
            return apto
    return False

def cadastrar_apto(apto, nome, tel):
    morador = {
            'apto': apto,
            'nome': nome,
            'tel': tel
        
    }
    
    is_exist = buscar_apto(apto)
    if not is_exist:
        dados = carregar_dados()
        dados.append(morador)
        salvar_dados(dados)

        return True
    else:
        return False 

def menu():
    while True:
        try:
            print('-' * 30)
            option = int(input('1 - Cadastrar\n2 - Buscar\n3 - Excluir\n4 - Sair\n:'))
            print('-' * 30)

            if 1 <= option <= 4:
                return option

        except ValueError:
            print('Opção inválida.')

def excluir_apto(apto):
    deleted_apto = buscar_apto(apto)

    if deleted_apto:
        dados = carregar_dados()
    
        dados.remove(deleted_apto)
    
        salvar_dados(dados)

        return True
    else:
        return False

def carregar_dados():
    with open('aptos.json', 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)

def salvar_dados(dados):
    with open('aptos.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4)

def criar_json():
    if not os.path.exists('aptos.json'):
        salvar_dados([])

def remover_spaces(el, tag='nospace'):
    el = el.strip()
    el = el.split(' ')
    str_list = []
    for x in el:
        if x != '':
            str_list.append(x)
    
    match tag:
        case 'nome':
            return ' '.join(str_list) 
        case 'nospace':
            return ''.join(str_list)

def validar_dados(el, dado_type):
    primeiro_andar = 1
    ultimo_andar = 6
    qtd_quartos = 10

    match dado_type:
        case 'nome':
            return el.replace(' ', '').isalpha()
        case 'apto':
            if el.isnumeric() and len(el) == 3:
                andar = int(el[0])
                quarto = int(el[1:])
                if primeiro_andar <= andar <= ultimo_andar and 1 <= quarto <= qtd_quartos:
                    return True
        case 'tel':
            if el.isnumeric() and len(el) == 11:
                return True
    return False

def formatar_dado(el, dado_type):
    match dado_type:
        case 'nome':
            return el.title()
        case 'tel':
            return f'({el[:2]}) {el[2]} {el[3:7]}-{el[7:]}'
        case _:
            return el

def imprimir_dados(el):
    for x, y in el.items():
        print(f'{x.upper()}: {formatar_dado(y, x)}')

if __name__ == '__main__':
    criar_json()
    main()
