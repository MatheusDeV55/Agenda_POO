
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
        try:
            with open(arquivo, 'w', encoding='utf-8') as f:
                json.dump([g.to_dict() for g in self.grupos], f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Erro ao salvar arquivo: {e}")

    def carregar(self, arquivo):
        if not os.path.exists(arquivo) or os.stat(arquivo).st_size == 0:
            self.grupos = []
            return
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                self.grupos = [Grupo.from_dict(g) for g in dados]
        except (json.JSONDecodeError, KeyError, IOError) as e:
            print(f"Erro ao carregar o arquivo: {e}")
            self.grupos = []
        except Exception as e:
            print(f"Erro inesperado: {e}")
            self.grupos = []
