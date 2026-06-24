class Usuario:
    def _init_(self, id: int, nome: str, telefone: str, email: str, data_cadastro: str):
        self._id = id
        self._nome = nome
        self._telefone = telefone
        self._email = email
        self._data_cadastro = data_cadastro
    def get_id(self) -> int:
        return self._id
    def get_nome(self) -> str:
        return self._nome
    def get_telefone(self) -> str:
        return self._telefone
    def get_email(self) -> str:
        return self._email
    def atualizar_dados(self, nome, telefone, email) -> None:
        pass