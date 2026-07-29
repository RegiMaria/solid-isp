# ISP — Interface Segregation Principle

Projeto didático em Python demonstrando o **Princípio da Segregação de Interface** (o "I" de SOLID), baseado no cenário de um sistema de CRM: cadastro de **Contratos**, **Produtos** e **Usuários**, cada um com necessidades distintas de persistência, log e notificação.

Para a definição completa do princípio, exemplos visuais e comparação com os demais princípios SOLID, veja **[CONCEITOS.md](./CONCEITOS.md)**.

## O cenário

Um sistema de CRM precisa cadastrar diferentes tipos de dados:

- **Contrato** → só precisa ser **salvo**.
- **Produto** → precisa ser **salvo** e **gerar notificação**, mas não precisa de log.
- **Usuário** → precisa ser **salvo**, **gerar log** e **gerar notificação**.

## Estrutura do projeto

```
isp-solid-project/
├── dominio/
│   └── objetos.py          # Contrato, Log, Notificacao (objetos de domínio)
├── violando_isp/
│   └── cadastro.py         # Uma única interface "gorda" -> viola o ISP
├── aplicando_isp/
│   └── cadastro.py         # Três interfaces segregadas -> respeita o ISP
├── tests/
│   ├── test_violando_isp.py
│   └── test_aplicando_isp.py
├── CONCEITOS.md            # Teoria detalhada do ISP
└── README.md
```

## Violando o ISP (`violando_isp/cadastro.py`)

Uma única interface `Cadastro` concentra três responsabilidades:

```python
class Cadastro(ABC):
    @abstractmethod
    def salvar(self, dado) -> None: ...

    @abstractmethod
    def registrar_log(self, log: Log) -> None: ...

    @abstractmethod
    def enviar_notificacao(self, notificacao: Notificacao) -> None: ...
```

`ContratoRepository` só precisa de `salvar`, mas é **obrigado** a implementar `registrar_log` e `enviar_notificacao` — que aqui nem têm lógica real, apenas lançam `NotImplementedError`. Isso é a violação do ISP na prática: a classe depende de métodos que não usa.

## Aplicando o ISP (`aplicando_isp/cadastro.py`)

A interface é segregada em três contratos pequenos e coesos:

```python
class CadastroInterface(ABC):
    @abstractmethod
    def salvar(self, dado) -> None: ...

class LogInterface(ABC):
    @abstractmethod
    def registrar_log(self, log: Log) -> None: ...

class NotificacaoInterface(ABC):
    @abstractmethod
    def enviar_notificacao(self, notificacao: Notificacao) -> None: ...
```

E cada classe implementa **só o que precisa**:

| Classe | Interfaces implementadas |
|---|---|
| `ContratoRepository` | `CadastroInterface` |
| `ProdutoRepository` | `CadastroInterface`, `NotificacaoInterface` |
| `UsuarioRepository` | `CadastroInterface`, `LogInterface`, `NotificacaoInterface` |

Nenhuma classe carrega método que não usa. Baixo acoplamento, alta coesão.

## Rodando os testes

Instale o `pytest` (se ainda não tiver):

```bash
pip install pytest
```

Rode os testes:

```bash
python -m pytest tests/ -v
```

- `test_violando_isp.py` prova que `ContratoRepository` quebra em runtime ao usar um método que só existe por obrigação da interface.
- `test_aplicando_isp.py` prova que, com as interfaces segregadas, cada classe implementa exatamente o que precisa — nada a mais, nada a menos.

## Requisitos

- Python 3.10+

## Licença

Uso livre para fins de estudo.
