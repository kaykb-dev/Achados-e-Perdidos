class Categoria:
    def _init_(self, id: int, nome: str):
        self._id = id
        self._nome = nome
    def get_id(self) -> int:
        return self._id
    def get_nome(self) -> str:
        return self._nome
    def _str_(self) -> str:
        return f"ID de categoria: {self._id}\nNome da categoria: {self._nome}"