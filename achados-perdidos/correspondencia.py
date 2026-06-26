from status_correspondencia import StatusCorrespondencia
class Correspondencia:

        self._id = id
        self._porcentagem_compatibilidade = porcentagem_compatibilidade
        self._data_analise = data_analise
        self._status = status

    def calcular_compatibilidade(self) -> float:
        return self._porcentagem_compatibilidade

        self._status = status

    def exibir_detalhes(self) -> str:
