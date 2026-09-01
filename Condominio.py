import json
from Morador import Morador

class Condominio:
    def __init__(self):
        self.__moradores = []

    def carregar_moradores(self) -> None:
        with open('aptos.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            for x in dados:
                self.__moradores.append(Morador(x['_nome'], x['_apto'], x['_telefone']))

    def adicionar(self, morador_novo: Morador) -> None:
        if self.buscar_apto(morador_novo.apto):
            raise ValueError('Nâo é possivel adicionar morador já existente.')
            
        self.__moradores.append(morador_novo)
        self.gravar_moradores()
    
    def remover(self, apto) -> None:
        morador_excluir = self.buscar_apto(apto)
        if not morador_excluir:
            raise ValueError('Não é possivel excluir morador inexistente.')

        self.__moradores.remove(morador_excluir)
        self.gravar_moradores()

    def gravar_moradores(self):
        with open('aptos.json', 'w', encoding='utf-8') as arquivo:
            moradores_json = []
            for x in self.__moradores:
                moradores_json.append(x.__dict__)

            json.dump(moradores_json, arquivo, indent=2)

    def buscar_apto(self, apto: str) -> Morador | None:
        for morador in self.__moradores:
            if morador.apto == apto:
                return morador

        return None

