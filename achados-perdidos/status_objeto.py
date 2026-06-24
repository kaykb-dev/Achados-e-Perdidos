class StatusObjeto:
    def _init_(self, id: int, nome: str, descricao: str):
        self._id = id
        self._nome = nome
        self._descricao = descricao
    def get_id(self) -> int:
        return self._id
    def get_nome(self) -> str:
        return self._nome
    def get_descricao(self) -> str:
        return self._descricao
    def _str_(self) -> str:
        return f"ID de status: {self._id}\nNome do status: {self._nome}\nDescrição do status: {self._descricao}"
    