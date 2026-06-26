class SistemaAchadosPerdidos:

    def _init_(self):
        self._usuarios = []
        self._objetos_perdidos = []
        self._objetos_encontrados = []
        self._correspondencias = []
        self._solicitacoes = []
        self._notificacoes = []

    def cadastrar_usuario(self, usuario):
        self._usuarios.append(usuario)      

    from objeto_perdido import ObjetoPerdido
    from objeto_encontrado import ObjetoEncontrado

    def cadastrar_objeto(self, obj):

        if isinstance(obj, ObjetoPerdido):
            self._objetos_perdidos.append(obj)

        elif isinstance(obj, ObjetoEncontrado):
            self._objetos_encontrados.append(obj)

    def buscar_correspondencias(self):
        return self._correspondencias 

    from relatorio import Relatorio

    def emitir_relatorio(self, tipo):
        return Relatorio(tipo)