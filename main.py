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
                    print(f'Morador {apto} cadastrado.')
                else:
                    print(f'Morador do {apto} já cadastrado.')
            case 2:
                apto_search = remover_spaces(input('Apto: ')) 
                _, apto_exist = buscar_apto(apto_search)
                if apto_exist:
                    imprimir_dados(apto_exist)
                else:
                    print(f'Morador {apto_search} não encontrado.')
            case 3:
                is_exclude, apto_exclude = excluir_apto(remover_spaces(input('Apto: ')))
                
                if is_exclude:
                    print(f'Morador do {apto_exclude} excluido.')
                else:
                    print(f'Morador {apto_exclude} não encontrado.')
            case 4:
                dados = carregar_dados()
                if dados:
                    listar_aptos(dados)
                else:
                    print('Nenhum morador cadastrado.')
            case 5:
                print('Programa encerrado.')
                break

def buscar_apto(search_apto):
    aptos = carregar_dados()

    for apto in aptos:
        if apto.get('apto') == search_apto:
            return aptos, apto
    return aptos, False

def cadastrar_apto(apto, nome, tel):
    dados, apto_exist = buscar_apto(apto)

    if not apto_exist:
        morador = {
                'apto': apto,
                'nome': nome,
                'tel': tel
        }

        dados.append(morador)
        salvar_dados(dados)

        return True
    return False

def menu():
    while True:
        try:
            print('-' * 30)
            option = int(input('1 - Cadastrar\n2 - Buscar\n3 - Excluir\n4 - Listar Aptos\n5 - Sair\n:'))
            print('-' * 30)

            if 1 <= option <= 5:
                return option
            else:
                print('Opção Inválida')

        except ValueError:
            print('Opção inválida.')

def excluir_apto(apto_search):
    dados, apto = buscar_apto(apto_search)

    if apto:
        dados.remove(apto)
        salvar_dados(dados)
    
        return True, apto_search

    return False, apto_search

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

def listar_aptos(dados):
    aptos_list = []
    for x in dados:
        aptos_list.append(x.get('apto'))
    aptos_list.sort()

    for i, x in enumerate(aptos_list):
        print(x, end=' ')

        if i == len(aptos_list) - 1:
            print()
        elif (i + 1) % 5 == 0:
            print()

if __name__ == '__main__':
    criar_json()
    main()
