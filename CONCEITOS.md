# ISP - Interface Segregation Principle (Princípio da Segregação de Interface)

O **I** de SOLID.

## Definição

> Clientes não devem ser forçados a depender de métodos que não usam.

Aqui, **"clientes"** são as classes que implementam uma interface. Quando uma classe implementa uma interface, ela é **obrigada** a implementar todos os métodos definidos nessa interface — mesmo que alguns desses métodos não façam sentido nenhum para o comportamento real daquela classe.

## O problema: interfaces "gordas" (fat interfaces)

Quando uma única interface concentra métodos de responsabilidades diferentes, toda classe que precisar de **apenas uma parte** desses métodos é forçada a implementar os outros também — geralmente com implementações vazias, `pass`, ou lançando erros como `NotImplementedError`.

Isso gera:

- **Acoplamento desnecessário**: a classe passa a depender de comportamentos que não usa.
- **Código frágil**: métodos "forçados" sem lógica real são um convite a bugs — se alguém chamar esse método achando que ele funciona, o programa quebra.
- **Baixa coesão**: a classe deixa de representar bem uma única responsabilidade.

## A solução: segregar interfaces

Em vez de uma interface única com N métodos, criamos **várias interfaces pequenas e coesas**, cada uma representando uma única responsabilidade. As classes então implementam **somente as interfaces que fazem sentido** para o seu comportamento real.

```
Interface única (viola o ISP)          Interfaces segregadas (respeita o ISP)
┌─────────────────────┐                ┌────────────────┐
│ Cadastro             │                │ CadastroInterface│
│  - salvar()           │               │  - salvar()      │
│  - registrar_log()     │              └────────────────┘
│  - enviar_notificacao() │             ┌────────────────┐
└─────────────────────┘                │ LogInterface     │
                                        │  - registrar_log()│
                                        └────────────────┘
                                        ┌────────────────┐
                                        │ NotificacaoInterface│
                                        │  - enviar_notificacao()│
                                        └────────────────┘
```

## Palavra de ordem

**Baixo acoplamento + alta coesão.**

- Baixo acoplamento: cada classe depende só do que realmente precisa.
- Alta coesão: cada interface representa uma única responsabilidade bem definida.

## ISP em Python

Diferente de linguagens como PHP, Java ou C#, Python não tem uma palavra-chave `interface`. O jeito idiomático de representar uma interface em Python é através de **classes abstratas** (`abc.ABC` + `@abstractmethod`), ou, em casos mais flexíveis, através de **Protocols** (`typing.Protocol`, tipagem estrutural).

Neste projeto usamos `ABC`, por deixar o contrato mais explícito e didático — igual a uma `interface` de outras linguagens.

## Relação com os outros princípios SOLID

- O ISP é uma consequência natural de se levar a sério o **SRP** (Single Responsibility Principle) também no nível das interfaces: uma interface deve ter um único motivo para mudar.
- O ISP também favorece o **LSP** (Liskov Substitution Principle): interfaces pequenas e coesas tornam mais fácil garantir que qualquer implementação pode substituir a interface sem surpresas, porque não existem métodos "extras" sendo forçados artificialmente.

## Resumindo

| Antes (violando ISP) | Depois (aplicando ISP) |
|---|---|
| Uma interface grande com métodos de múltiplas responsabilidades | Várias interfaces pequenas, uma por responsabilidade |
| Classes implementam métodos que nunca usam | Classes implementam só o que realmente usam |
| Alto acoplamento, baixa coesão | Baixo acoplamento, alta coesão |
| Erros em tempo de execução por métodos "vazios"/forçados | Nenhum método forçado; contratos claros e específicos |
