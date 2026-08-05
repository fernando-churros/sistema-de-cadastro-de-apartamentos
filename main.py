import json

def main():
    while True:
        option = menu()
        match option:
            case 1:
                is_cadastred = cadastrar_apto(input('Apto: '), input('Nome: '), input('Tel: '))
                if is_cadastred:
                    print('Morador cadastrado.')
                else:
                    print('Morador já cadastrado.')
            case 2:
                is_exist_apto = buscar_apto(input('Apto: '))
                if is_exist_apto:
                    print(is_exist_apto)
                else:
                    print('Morador não encontrado.')
            case 3:
                is_exclude = excluir_apto(input('Apto: '))
                
                if is_exclude:
                    print('Morador excluido.')
                else:
                    print('Morador não encontrado.')
            case 4:
                print('Programa encerrado.')
                break

def buscar_apto(search_apto):
    with open("aptos.json", "r", encoding="utf-8") as arquivo:
        aptos = json.load(arquivo)

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

    with open("aptos.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    is_exist = buscar_apto(apto)
    
    if not is_exist:
        dados.append(morador)
        with open("aptos.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo)
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
        with open('aptos.json', 'r') as arquivo:
            dados = json.load(arquivo)
    
        dados.remove(deleted_apto)
    
        with open('aptos.json', 'w') as arquivo:
            json.dump(dados, arquivo)

        return True
    else:
        return False


if __name__ == '__main__':
    main()
