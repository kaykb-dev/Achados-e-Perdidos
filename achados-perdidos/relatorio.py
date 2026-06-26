class Relatorio:

    def __init__(self, id: int, tipo: str, data_emissao: str, conteudo: str):
        self._id = id
        self._tipo = tipo
        self._data_emissao = data_emissao
        self._conteudo = conteudo

    def get_id(self) -> int:
        return self._id

    def get_tipo(self) -> str:
        return self._tipo

    def get_data_emissao(self) -> str:
        return self._data_emissao

    def get_conteudo(self) -> str:
        return self._conteudo

    def exibir_relatorio(self) -> str:
        return (
            f"=== Relatório ===\n"
            f"ID: {self._id}\n"
            f"Tipo: {self._tipo}\n"
            f"Data de emissão: {self._data_emissao}\n"
            f"Conteúdo:\n{self._conteudo}"
        )