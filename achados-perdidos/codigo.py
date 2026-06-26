class Usuario:
    def __init__(self, id: int, nome: str, telefone: str, email: str, data_cadastro: str):
        self._id = id
        self._nome = nome
        self._telefone = telefone
        self._email = email
        self._data_cadastro = data_cadastro
    def get_id(self) -> int:
        return self._id
    def get_nome(self) -> str:
        return self._nome
    def get_telefone(self) -> str:
        return self._telefone
    def get_email(self) -> str:
        return self._email
    def atualizar_dados(self, nome, telefone, email) -> None:
        self._nome = nome
        self._telefone = telefone
        self._email = email

class Categoria:
    def __init__(self, nome: str):
        self._nome = nome
    def get_nome(self) -> str:
        return self._nome
    def __str__(self) -> str:
        return f"ID de categoria: {self._id}\nNome da categoria: {self._nome}"
    
class StatusItem:
    def __init__(self, nome: str, descricao: str):
        self._nome = nome
        self._descricao = descricao
    def get_nome(self) -> str:
        return self._nome
    def get_descricao(self) -> str:
        return self._descricao
    def __str__(self) -> str:
        return f"ID de status: {self._id}\nNome do status: {self._nome}\nDescrição do status: {self._descricao}"  
      
class Item:
    def __init__(self, id: int, nome: str, descricao: str, categoria: Categoria, cor: str, status: StatusItem):
        self._id = id
        self._nome = nome
        self._descricao = descricao
        self._categoria: Categoria = categoria
        self._cor = cor
        self._status: StatusItem = status
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
    def get_status(self) -> StatusItem:
        return self._status
    def exibir_detalhes(self) -> str:
        return f"===Dados do item===\nID: {self._id}\nNome: {self._nome}\nDescrição: {self._descricao}\nCategoria: {self._categoria}\nCor: {self._cor}\nStatus: {self._status}"
    
class Administrador(Usuario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, data_cadastro: str, nivel_acesso: str):
        super().__init__(id, nome, telefone, email, data_cadastro)
        self._nivel_acesso: str = nivel_acesso
    def aprovar_devolucao(self, sol) -> None:
        pass
    def rejeitar_devolucao(self, sol) -> None:
        pass
    def remover_registro(self, it: Item) -> None:
        pass

class ItemEncontrado(Item):
    def __init__(self, id: int, nome: str, descricao: str, categoria: Categoria, cor: str, status: StatusItem, 
                 local_encontro: str, data_encontro: str, observacoes: str):
        super().__init__(id, nome, descricao, categoria, cor, status)
        self._local_encontro: str = local_encontro
        self._data_encontro: str = data_encontro
        self._observacoes: str = observacoes

    def registrar_encontro(self) -> None:
        pass

    def exibir_detalhes(self) -> str:
        detalhes_base = super().exibir_detalhes()
        detalhes_especificos = f"\nLocal Encontrado: {self._local_encontro}\nData do Encontro: {self._data_encontro}\nObservações: {self._observacoes}"
        return detalhes_base + detalhes_especificos
    
class StatusCorrespondencia:

    def __init__(self, id: int, nome: str, descricao: str):
        self._id = id
        self._nome = nome
        self._descricao = descricao

    def get_id(self) -> int:
        return self._id

    def get_nome(self) -> str:
        return self._nome

    def get_descricao(self) -> str:
        return self._descricao

    def __str__(self) -> str:
        return (
            f"ID: {self._id}\n"
            f"Nome: {self._nome}\n"
            f"Descrição: {self._descricao}"
        )
  
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
    
class StatusSolicitacao:
    def __init__(self, id: int, nome: str, descricao: str):
        self._id = id
        self._nome = nome
        self._descricao = descricao
    def get_id(self) -> int:
        return self._id
    def get_nome(self) -> str:
        return self._nome
    def get_descricao(self) -> str:
        return self._descricao
    def __str__(self) -> str:
        return (
            f"ID: {self._id}\n"
            f"Nome: {self._nome}\n"
            f"Descrição: {self._descricao}"
        )

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
    
class SistemaAchadosPerdidos:

    def _init_(self):
        self._usuarios = []
        self._items_encontrados = []
        self._correspondencias = []
        self._solicitacoes = []
        self._notificacoes = []

    def cadastrar_usuario(self, usuario):
        self._usuarios.append(usuario)      

    def cadastrar_item(self, it):
        if isinstance(it, ItemEncontrado):
            self._item_encontrados.append(it)

    def buscar_correspondencias(self):
        return self._correspondencias 

    def emitir_relatorio(self, tipo):
        return Relatorio(tipo)