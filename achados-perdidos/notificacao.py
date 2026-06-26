class Notificacao:

    def _init_(self, id, mensagem, data_envio, tipo):
        self._id = id
        self._mensagem = mensagem
        self._data_envio = data_envio
        self._tipo = tipo
        self._lida = False

    def marcar_como_lida(self):
        self._lida = True

    def enviar(self, destinatario):
        print(f"Notificação enviada para {destinatario.get_nome()}.")