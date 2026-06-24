class ObjetoPerdido(Objeto):
    def _init_(self, id: int, nome: str, descricao: str, categoria: Categoria, cor: str, status: StatusObjeto, 
                 local_perda: str, data_perda: str, observacoes: str):
        super()._init_(id, nome, descricao, categoria, cor, status)
        self._local_perda: str = local_perda
        self._data_perda: str = data_perda
        self._observacoes: str = observacoes

    def registrar_perda(self) -> None:
        pass

    def exibir_detalhes(self) -> str:
        detalhes_base = super().exibir_detalhes()
        detalhes_especificos = f"\nLocal da Perda: {self._local_perda}\nData da Perda: {self._data_perda}\nObservações: {self._observacoes}"
        return detalhes_base + detalhes_especificos
