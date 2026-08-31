class Morador:
    TAMANHO_TELEFONE = 11
    QTD_APTOS = 10
    ANDARES = 5
    APTO_VALIDO = 3 # Quantidade de digitos para validar se um apto é valido.

    def __init__(self, nome: str, apto: str, telefone: str):
        self.nome = nome
        self.apto = apto
        self.telefone = telefone
    
    @property
    def nome(self) -> str:
        return self._nome
    @nome.setter
    def nome(self, valor):
        nome = self.remover_espacos(valor, 'nome')
        if not nome.replace(' ', '').isalpha():
            raise ValueError('Nome inválido.')
        self._nome = nome

    @property
    def apto(self) -> str:
        return self._apto
    @apto.setter
    def apto(self, valor):
        apto = self.remover_espacos(valor, 'nospaces')
        if not apto.isdigit() or len(apto) != self.APTO_VALIDO:
            raise ValueError('Apto inválido')

        ap = int(apto[1:])
        andar = int(apto[:1])

        if not (1 <= andar <= self.ANDARES and 1 <= ap <= self.QTD_APTOS):
            raise ValueError('Apto ou andar não existe.')

        self._apto = apto

    @property
    def telefone(self) -> str:
        return self._telefone
    @telefone.setter
    def telefone(self, valor):
        telefone = self.remover_espacos(valor, 'nospaces')
        if not telefone.isdigit() or len(telefone) != self.TAMANHO_TELEFONE:
            raise ValueError('Telefone inválido.')
    
        self._telefone = telefone

    @staticmethod
    def remover_espacos(item, tipo) -> str:
        match tipo:
            case 'nospaces':
                return ''.join(item.split())
            case 'nome':
                return ' '.join(item.split())
            case _:
                raise ValueError('Tipo inválido')

    
