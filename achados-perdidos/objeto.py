class Objeto:
    def _init_(self, id: int, nome: str, descricao: str, categoria: Categoria, cor: str, status: StatusObjeto):
        self._id = id
        self._nome = nome
        self._descricao = descricao
        self._categoria: Categoria = categoria
        self._cor = cor
        self._status: StatusObjeto = status
    def get_id(self) -> int:
        return self._id
    def get_nome(self) -> str:
        return self._nome
    def get_descricao(self) -> str:
        return self._descricao
    def get_categoria(self) -> Categoria:
        return self._categoria
    def get_cor(self) -> str:
        return self._cor
    def get_status(self) -> StatusObjeto:
        return self._status
    def exibir_detalhes(self) -> str:
        return f"===Dados do Objeto===\nID: {self._id}\nNome: {self._nome}\nDescrição: {self._descricao}\nCategoria: {self._categoria}\nCor: {self._cor}\nStatus: {self._status}"