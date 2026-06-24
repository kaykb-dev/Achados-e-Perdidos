class Administrador(Usuario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, data_cadastro: str, nivel_acesso: str):
        super()._init_(id, nome, telefone, email, data_cadastro)
        self._nivel_acesso: str = nivel_acesso

    def aprovar_devolucao(self, sol) -> None:
        pass

    def rejeitar_devolucao(self, sol) -> None:
        pass

    def remover_registro(self, obj: Objeto) -> None:
        pass

    def gerar_relatorio(self):
        pass