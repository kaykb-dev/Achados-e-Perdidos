class SolicitacaoDevolucao:

    def __init__(self, id: int, data_solicitacao: str, justificativa: str, status: StatusSolicitacao, data_resolucao: str = ""):
        self._id = id
        self._data_solicitacao = data_solicitacao
        self._justificativa = justificativa
        self._status = status
        self._data_resolucao = data_resolucao

    def aprovar(self, admin) -> None:
        pass

    def rejeitar(self, admin, motivo: str) -> None:
        pass

    def cancelar(self, usuario) -> None:
        pass

    def exibir_detalhes(self) -> str:
        return (
            f"=== Solicitação de Devolução ===\n"
            f"ID: {self._id}\n"
            f"Data da Solicitação: {self._data_solicitacao}\n"
            f"Justificativa: {self._justificativa}\n"
            f"Status: {self._status}\n"
            f"Data de Resolução: {self._data_resolucao}"
        )
    