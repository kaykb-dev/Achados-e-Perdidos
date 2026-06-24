
class ObjetoEncontrado(Objeto):
    def _init_(self, id: int, nome: str, descricao: str, categoria: Categoria, cor: str, status: StatusObjeto, 
                 local_encontro: str, data_encontro: str, observacoes: str):
        super()._init_(id, nome, descricao, categoria, cor, status)
        self._local_encontro: str = local_encontro
        self._data_encontro: str = data_encontro
        self._observacoes: str = observacoes

    def registrar_encontro(self) -> None:
        pass

    def exibir_detalhes(self) -> str:
        detalhes_base = super().exibir_detalhes()
        detalhes_especificos = f"\nLocal Encontrado: {self._local_encontro}\nData do Encontro: {self._data_encontro}\nObservações: {self._observacoes}"
        return detalhes_base + detalhes_especificos