from status_correspondencia import StatusCorrespondencia

class Correspondencia:

    def __init__(self, id: int, porcentagem_compatibilidade: float, data_analise: str, status: StatusCorrespondencia):
        self._id = id
        self._porcentagem_compatibilidade = porcentagem_compatibilidade
        self._data_analise = data_analise
        self._status = status

    def calcular_compatibilidade(self) -> float:
        return self._porcentagem_compatibilidade

    def alterar_status(self, status: StatusCorrespondencia) -> None:
        self._status = status

    def get_status(self) -> StatusCorrespondencia:
        return self._status

    def exibir_detalhes(self) -> str:
        return (f"=== Correspondência ===\n"f"ID: {self._id}\n"f"Compatibilidade: {self._porcentagem_compatibilidade}%\n"f"Data da análise: {self._data_analise}\n"f"Status: {self._status}")