from Morador import Morador
from Condominio import Condominio

def main():
    condominio = Condominio()
    condominio.carregar_moradores()

    while True:
        try:
            option = int(input('1 - Cadastrar 2 - Remover 3 - Buscar 5 - Sair\n: ')) 

            match option:
                case 1:
                    nome = str(input('Nome: '))
                    apto = str(input('Apto: '))
                    telefone = str(input('telefone: '))

                    condominio.adicionar(Morador(nome, apto, telefone))
                    print('Morador cadastrado com sucesso!')
                case 2:
                    apto = str(input('Apto: '))
                    condominio.remover(apto)
                    print('Morador excluido com sucesso!')
                case 3:
                    apto = str(input('Apto: '))

                    morador = condominio.buscar_apto(apto)
                    if not morador:
                        print('Morador não encontrado')
                    else:
                        print('-' * 30)
                        print(morador)
                        print('-' * 30)

                case 5:
                    print('\nSaindo...\n')
                    break

        except (ValueError, TypeError) as erro:
            print(erro)

if __name__ == '__main__':
    main()

