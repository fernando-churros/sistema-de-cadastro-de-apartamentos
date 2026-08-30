class Morador:
    def __init__(self, nome: str, apto: str, telefone: str):
        self.nome = nome
        self.apto = apto
        self.telefone = telefone
    
    @property
    def nome(self) -> str:
        return self._nome
    @nome.setter
    def nome(self, valor):
        self._nome = self.remover_espacos(valor, 'nome')
    
    @property
    def apto(self):
        return self._apto
    @apto.setter
    def apto(self, valor):
        self._apto = int(self.remover_espacos(valor, 'nospaces'))

    @property
    def telefone(self):
        return self._telefone
    @telefone.setter
    def telefone(self, valor):
        self._telefone = int(self.remover_espacos(valor, 'nospaces'))

    def remover_espacos(self, item, tipo):
        match tipo:
            case 'nospaces':
                x = []
                for n in item.split():
                    if n != '':
                        x.append(n)
                return ''.join(x)
            case 'nome':
                x = []
                for n in item.split():
                    if n != '':
                        x.append(n)
                return ' '.join(x)


