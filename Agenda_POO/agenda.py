
import json
import os
from grupo import Grupo

class Agenda:
    def __init__(self):
        self.grupos = []

    def adicionar_grupo(self, nome):
        self.grupos.append(Grupo(nome))

    def buscar_grupo(self, nome):
        for g in self.grupos:
            if g.nome == nome:
                return g
        return None

    def salvar(self, arquivo):
        with open(arquivo, 'w') as f:
            json.dump([g.to_dict() for g in self.grupos], f, indent=4)

    def carregar(self, arquivo):
        if not os.path.exists(arquivo) or os.stat(arquivo).st_size == 0:
            self.grupos = []
            return
        with open(arquivo, 'r') as f:
            dados = json.load(f)
            self.grupos = [Grupo.from_dict(g) for g in dados]
            