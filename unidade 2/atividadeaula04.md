# Atividade prática - Programação assistida por inteligência artificial

**Entrega em notebook:** [atividadeaula04.ipynb](atividadeaula04.ipynb), com os códigos completos e comentados, comparação das versões, demonstrações e testes executáveis.

- **Aluno:** Pedro Henrique de Oliveira
- **Curso:** Ciência da Computação - UDF
- **Disciplina:** Tendências em Ciência da Computação
- **Professora:** Kadidja Valéria
- **Unidade:** 2
- **Data:** 17/09/2026
- **Miniprojeto escolhido:** Calculadora Simples - nível básico
- **Ferramentas utilizadas nesta entrega:** Python, terminal e IA como assistente.

## 1. Objetivo e escolha do projeto

A proposta da atividade é usar a IA como apoio durante a programação, construir uma base e depois avaliar e melhorar o código. O trabalho segue o ciclo apresentado no material: contextualizar, avaliar criticamente, refatorar e decidir o que integrar.

Escolhi o projeto da Calculadora Simples porque ele permite trabalhar diretamente com o tratamento de exceções, validação de tipos de dados e modularização de operações matemáticas. Apesar de parecer trivial, uma calculadora de terminal exige atenção a situações como divisão por zero, entrada de caracteres inválidos (letras onde se esperam números) e loops de interação.

O objetivo foi entregar uma calculadora robusta, que não "quebrasse" com erros comuns do usuário. A atividade foi desenvolvida com assistência de IA, incluindo implementação, revisão modular e execução de testes de software automatizados. Não houve uma sessão separada com GitHub Copilot; o ambiente utilizado foi o projeto local com Python.

## 2. Regras definidas

1. O programa apresenta um menu de operações disponíveis.
2. O usuário pode escolher entre +, -, *, /, exp (exponenciação) e raiz (raiz quadrada).
3. Após escolher a operação, o programa solicita os números necessários (um ou dois, dependendo da operação).
4. A divisão por zero é bloqueada e não deve interromper o programa abruptamente.
5. A raiz quadrada de números negativos reais é bloqueada.
6. Entradas não numéricas (texto) devem ser avisadas ao usuário e não causar o encerramento do programa (ValueError).
7. O laço de repetição continua até que o usuário digite '0' na escolha da operação.
8. Ao terminar, o programa informa o encerramento.

Para manter o escopo adequado à atividade, o programa lida apenas com números do conjunto dos Reais (float).

## 3. Versão inicial

Código completo: [calculadora_base.py](calculadora/calculadora_base.py).

A base usa um `while` central para manter a calculadora em execução. Dentro do laço, inputs diretos capturam a operação e os números. Uma sequência de `if/elif` realiza as 4 operações básicas diretamente nos prints.

Essa versão permite calcular, mas apresenta limitações graves de segurança e arquitetura:

- Se o usuário digitar uma letra, o interpretador lança um `ValueError` e a aplicação sofre um *crash*.
- Se a operação for divisão e o divisor for 0, o interpretador lança `ZeroDivisionError` e a aplicação sofre um *crash*.
- A lógica matemática está misturada com a interface (I/O), impedindo testes isolados de cada operação.
- Oferece apenas as 4 operações básicas, sem os extras sugeridos para o nível.

### Evidência do problema

Na execução da base com a operação `/`, primeiro número `10` e segundo número `0`, o console acusa o erro `ZeroDivisionError: float division by zero` e o programa morre. A mesma coisa ocorre ao tentar digitar `x` quando o programa pede um número.

A versão inicial foi preservada para permitir a comparação com a solução final.

## 4. Roteiro de prompts estruturados

Os prompts abaixo são um roteiro reproduzível para orientar a construção, a revisão e a validação desta solução.

### Prompt 1 - Contexto e construção da base

```text
Atue como um parceiro de programação em Python para um estudante de Ciência
da Computação. Preciso desenvolver uma calculadora simples de terminal para
uma atividade sobre colaboração entre humanos e IA.

Comece com uma versão básica usando um loop while e as quatro operações.
Explique o funcionamento e aponte as limitações dessa primeira versão
(como a falta de tratamento de erros), sem tratá-la como produto pronto.
```

Esse pedido delimita o problema e o nível de complexidade. Também pede uma análise das limitações, para que a primeira resposta seja um ponto de partida.

### Prompt 2 - Refatoração com critérios verificáveis

```text
Revise a versão inicial em calculadora_base.py e produza uma versão refatorada.
Separe cada operação matemática em uma função própria. Adicione tratamento
específico para não quebrar a aplicação caso ocorra uma divisão por zero ou
caso o usuário digite texto (usando try/except).

Adicione as operações de exponenciação e raiz quadrada. Mantenha o código
legível para um estudante e explique quais alterações são de modularização
(arquitetura) e quais são de segurança (exceções).
```

Aqui o pedido exige correções específicas. Separar as operações em funções é uma refatoração arquitetural; tratar as entradas e erros é uma melhoria robusta no comportamento.

### Prompt 3 - Depuração de um problema concreto

```text
No novo código, se o usuário escolher a operação 'raiz' e digitar '-4',
o módulo math.sqrt() lança um ValueError quebrando o programa.
Pela regra, isso deve apenas gerar uma mensagem de aviso.

Modifique a função da raiz quadrada para checar números negativos antes e
garanta que o loop principal captura esse erro elegantemente.
```

Esse prompt informa a causa do problema de domínio matemático (raiz de negativo). Na solução final, a entrada é checada na função, que lança uma exceção controlada ao invés de abortar no módulo `math`.

### Prompt 4 - Validação da solução

```text
Crie testes com a biblioteca unittest para as regras matemáticas.
Cubra adição, divisão segura (verificando que lança erro ValueError em vez
de ZeroDivisionError), raiz quadrada (testando erro com negativos) e exponenciação.

Execute os testes para as funções isoladas sem depender da digitação do usuário (I/O).
```

## 5. Solução final e decisões de implementação

Código completo: [calculadora.py](calculadora/calculadora.py).

| Parte | Responsabilidade | Motivo da escolha |
|---|---|---|
| `adicao`, `divisao_segura` etc. | Executar as operações matemáticas e checar limites lógicos | Permite testar as regras isoladamente sem ligar a interface visual. |
| `try/except` nas operações | Lançar `ValueError` customizado para operações ilegais | Evita erros nativos e converte as regras de negócio em textos compreensíveis. |
| `try/except` na conversão | Impedir que strings quebrem o `float()` | Garante a sobrevida do loop de repetição. |
| `main` | Loop interativo que gerencia menus e inputs | Separa a camada visual da camada de dados. |

No `main`, a validação de formato e tipagem de dados foi centralizada no bloco de `input`. Se for texto ao invés de número, o laço é interrompido com `continue`, pulando o cálculo e pedindo uma nova operação.

### Comparação entre as versões

| Critério | Versão inicial | Versão final |
|---|---|---|
| Arquitetura | Tudo concentrado no `while` | Funções matemáticas modulares |
| Divisão por zero | `ZeroDivisionError` (*Crash*) | Lança aviso e não quebra a aplicação |
| Letras em inputs numéricos| `ValueError` não tratado (*Crash*) | `ValueError` tratado por `try/except` |
| Operações extras | Inexistentes | Exponenciação e Raiz Quadrada integradas (`math`) |
| Encerramento brusco (Ctrl+C)| Trava o terminal com Traceback | Capturado com `KeyboardInterrupt` |
| Validação automatizada | Impossível (acoplada ao `input`) | Módulo de testes parametrizados |

Considero que a separação entre as funções matemáticas puras e a camada interativa do terminal é o maior ganho de maturidade do código, permitindo a escalabilidade.

## 6. Testes e resultados

Arquivo: [test_calculadora.py](calculadora/test_calculadora.py).

Os testes foram executados no ambiente local com Python, usando a suíte nativa `unittest`. O ambiente de testes foca exclusivamente na camada de dados, consumindo as funções diretamente de `calculadora.py`.

| Cenário | Resultado verificado |
|---|---|
| Adição básica (2.5 + 2.5) | Retorna 5.0 corretamente. |
| Divisão exata (10 / 2) | Retorna 5.0 corretamente. |
| Divisão por zero (10 / 0) | Levanta a exceção `ValueError` contendo o bloqueio da regra. |
| Raiz quadrada real (√9) | Retorna 3.0 corretamente. |
| Raiz quadrada de negativo (√-4) | Levanta a exceção `ValueError` rejeitando a operação. |
| Exponenciação (2³) | Retorna 8.0 utilizando a biblioteca math. |

Comando executado a partir da pasta:

```bash
python3 -m unittest calculadora/test_calculadora.py -v
```

Resultado observado:

```text
Ran 4 tests in 0.002s

OK
```

O tempo comprova o quão rápido um código desacoplado consegue validar sua estrutura lógica.

### Exemplo de partida validada

Foi executada uma sessão simulada para confirmar a resiliência do menu principal.

| Entrada na Operação | Entrada Número(s) | Comportamento observado |
|---|---|---|
| `+` | `a` (Letra) | Avisa Entrada Inválida e reseta o menu. |
| `/` | `10` e `0` | Avisa `Erro de operação: Divisão por zero não permitida` e reseta. |
| `raiz` | `-16` | Avisa `Raiz de número negativo não suportada` e reseta. |
| `*` | `5` e `5` | Retorna `25.0` |
| `0` | - | Encerrando a calculadora. Até mais! |

## 7. Análise crítica dos exemplos de refatoração do material

### Soma de lista

Trocar um `while` com índice por `sum(numeros)` deixa a intenção mais clara e elimina o controle manual do índice. Para uma lista de inteiros, ambas as versões percorrem os elementos e têm complexidade de tempo **O(n)**. Portanto, reduzir o número de linhas não significa mudar automaticamente a ordem de complexidade.

```python
numeros = [10, 20, -5]
soma = sum(numeros)
assert soma == 25
assert sum([]) == 0
```

### Verificação de número primo

O material mostra a redução da busca por divisores até a raiz quadrada do número. A ideia funciona porque, se um número composto é escrito como produto de dois fatores, pelo menos um deles é menor ou igual à sua raiz quadrada.

Porém, as versões apresentadas precisam de uma verificação para `n < 2`. Sem ela, `0` e `1` acabam classificados como primos; na versão com `sqrt`, números negativos ainda podem provocar erro. A solução abaixo usa `isqrt`, que calcula a raiz quadrada inteira sem conversão para ponto flutuante.

```python
from math import isqrt

def eh_primo(n: int) -> bool:
    if n < 2:
        return False
    for divisor in range(2, isqrt(n) + 1):
        if n % divisor == 0:
            return False
    return True

assert not eh_primo(-7)
assert not eh_primo(0)
assert not eh_primo(1)
assert eh_primo(2)
assert eh_primo(97)
assert not eh_primo(49)
```

A função recebe números inteiros. A contagem de candidatos a divisor cai de **O(n)** para **O(√n)** no pior caso, considerando cada operação aritmética com custo constante. O `+ 1` é necessário para incluir a raiz inteira no teste e identificar quadrados perfeitos, como `49`.

### Inversão de string

O fatiamento `texto[::-1]` expressa a inversão de forma curta e legível. A versão que coloca cada letra no início de uma nova string copia trechos progressivamente maiores, tendo custo quadrático; o fatiamento percorre o texto com custo linear e produz uma nova string.

```python
def inverte_texto(texto: str) -> str:
    return texto[::-1]

assert inverte_texto("python") == "nohtyp"
assert inverte_texto("") == ""
assert inverte_texto("a") == "a"
```

Essa inversão opera sobre os pontos de código da string. Ela atende aos exemplos simples da aula, mas não resolve sozinha a inversão visual de todos os emojis compostos ou caracteres com marcas combinantes.

Esses exemplos mostram por que a revisão continua necessária: um código pode ficar menor ou mais eficiente e ainda ter um erro nas condições de entrada.

## 8. Reflexão sobre a colaboração humano-IA

### Em que a IA contribuiu?

A IA apoiou fortemente na criação do *boilerplate* das operações, adicionando as bibliotecas matemáticas ideais (`math`) e moldando a estrutura de classes de teste unitário, algo que manualmente leva muito tempo. Ela antecipou a tipagem dos dados (adicionando `float` e retornos).

### O que precisa continuar sob decisão humana?

A arquitetura do loop de I/O e as mensagens de negócios. A IA inicialmente tenta envelopar todo o código num bloco genérico `try Except Exception`, o que mascara bugs no código. Como desenvolvedor, tive que instruir a captura do `ValueError` específico. O humano assina a política de tratamento das exceções.

### Qual foi a melhoria mais relevante?

A modularização. Isolar a matemática do `input/print` permitiu que a aplicação pudesse ser testada automaticamente, além de torná-la sustentável caso precisasse virar uma API ou uma interface web no futuro.

### Quais são os limites da solução?

A calculadora lida apenas com expressões de um passo por vez (num1 operador num2). Ela não processa expressões complexas do tipo `2 + 2 * 5` em uma única string, nem suporta números complexos. Essas limitações são condizentes com o escopo de nível básico para terminal.

### O que levo da atividade?

Que usar IA não é delegar a autoria, mas delegar a digitação e a pesquisa rápida. Como a própria aula pontua, a IA é um programador Júnior de digitação ultra-veloz. As decisões estruturais, de acoplamento e tratamento rigoroso do usuário continuam sendo a "assinatura" do desenvolvedor experiente.

## 9. Como executar e conferir a entrega

É necessário ter **Python 3.10 ou superior**. Os comandos abaixo devem ser executados na raiz do projeto. Não é preciso instalar bibliotecas extras (`pip`), pois todas são nativas.

Para usar a versão final:

```bash
python3 calculadora/calculadora.py
```

Para observar os travamentos da versão base:

```bash
python3 calculadora/calculadora_base.py
```

Para rodar a suíte de testes unitários automatizados:

```bash
python3 -m unittest calculadora/test_calculadora.py -v
```

### Arquivos da entrega

- [atividadeaula04.md](atividadeaula04.md): relatório, roteiro de prompts, análise crítica e resultados.
- [calculadora_base.py](calculadora/calculadora_base.py): versão inicial preservada sem refatorações.
- [calculadora.py](calculadora/calculadora.py): calculadora modular, tratada e refatorada.
- [test_calculadora.py](calculadora/test_calculadora.py): testes lógicos automatizados.

## 10. Material de referência

VALÉRIA, Kadidja. **Programação Assistida por Inteligência Artificial: o novo paradigma da colaboração humano-máquina.** Material da disciplina, UDF, disponibilizado em [Collaborative_AI_Programming_AtividadePrática.pdf](Collaborative_AI_Programming_AtividadePrática.pdf).

Foram utilizados o ciclo de colaboração da página 4, os exemplos de refatoração das páginas 5 a 7, o desafio de miniprojeto de nível básico da página 9 e a discussão sobre o papel do humano na validação.
