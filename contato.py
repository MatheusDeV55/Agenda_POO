
class Contato:
    contador_id = 1

    def __init__(self, nome, telefone, email, categoria):
        self.id = Contato.contador_id
        Contato.contador_id += 1
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.categoria = categoria

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "telefone": self.telefone,
            "email": self.email,
            "categoria": self.categoria
        }

    @staticmethod
    def from_dict(dados):
        contato = Contato(
            dados["nome"],
            dados["telefone"],
            dados["email"],
            dados["categoria"]
        )
        contato.id = dados["id"]
        if dados["id"] >= Contato.contador_id:
            Contato.contador_id = dados["id"] + 1
        return contato
    