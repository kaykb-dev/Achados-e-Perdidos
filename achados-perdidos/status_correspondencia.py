class StatusCorrespondencia:

    def __init__(self, id: int, nome: str, descricao: str):
        self._id = id
        self._nome = nome
        self._descricao = descricao

    def get_id(self) -> int:
        return self._id

    def get_nome(self) -> str:
        return self._nome

    def get_descricao(self) -> str:
        return self._descricao

    def __str__(self) -> str:
        return (
            f"ID: {self._id}\n"
            f"Nome: {self._nome}\n"
            f"Descrição: {self._descricao}"
        )