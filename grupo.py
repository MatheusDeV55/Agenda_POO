
from contato import Contato

class Grupo:
    def __init__(self, nome):
        self.nome = nome
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)
    
    def remover_contato(self, contato_id):
        self.contatos = [c for c in self.contatos if c.id != contato_id]

    def listar_contatos(self):
        return self.contatos

    def to_dict(self):
        return {
            "nome": self.nome,
            "contatos": [c.to_dict() for c in self.contatos]
        }

    @staticmethod
    def from_dict(dados):
        grupo = Grupo(dados["nome"])
        for c in dados["contatos"]:
#            grupo.adicionar_contato(Contato.from_dict(c))
            contato = Contato.from_dict(c)
            if contato:
                grupo.adicionar_contato(contato)
        return grupo
    