# Relatório de Atividade: Programação Assistida por IA

**Projeto:** Calculadora Simples (Nível Básico)
**Aluno:** Pedro Henrique de Oliveira
**Curso:** Ciência da Computação - UDF
**Disciplina:** Tendências em Ciência da Computação
**Professora:** Kadidja Valéria
**Data:** 17 de Setembro de 2026
**Arquivos auxiliares:** `atividadeaula04.ipynb`, `calculadora.py`, `calculadora_base.py`, `test_calculadora.py`

---

## 1. Contextualização e Escolha do Tema

Para esta prática de colaboração Humano-Máquina, optei por desenvolver a **Calculadora Simples**. Embora pareça um projeto inicial, a construção de uma calculadora de terminal é um excelente laboratório para lidar com exceções clássicas de software: a conversão de tipos (strings para floats) e as restrições de domínio matemático (como a impossibilidade da divisão por zero ou raízes de números negativos nos reais).

O objetivo principal não foi apenas entregar o código funcionando, mas demonstrar o ciclo de refatoração, onde saímos de um código imperativo frágil (base) para uma arquitetura modular e protegida por testes. A Inteligência Artificial atuou como minha parceira de *Pair Programming*, acelerando a escrita e sugerindo melhorias.

## 2. Escopo do Desenvolvimento

O sistema foi delimitado para atender aos seguintes critérios:
* **Interatividade:** Um loop contínuo que oferece opções até o usuário decidir sair.
* **Operações suportadas:** Soma, Subtração, Multiplicação, Divisão, Exponenciação e Raiz Quadrada.
* **Segurança da Aplicação:** O programa jamais deve fechar inesperadamente (*crash*) devido a erros de digitação (ex: digitar "dez" em vez de "10") ou falhas lógicas (divisão por zero).
* **Desacoplamento:** A lógica de cálculo não deve estar misturada com os comandos de `print` e `input`.

## 3. Análise da Primeira Versão (O Ponto de Partida)

A primeira iteração do código, preservada no arquivo `calculadora_base.py`, representa a abordagem tradicional e não otimizada. Nela, o loop `while` abriga diretamente as requisições de input e os cálculos sequenciais via `if/elif`.

**Principais Defeitos Identificados:**
1. **Acoplamento total:** É impossível testar a soma sem ter que simular o teclado, pois tudo ocorre dentro do mesmo bloco interativo.
2. **Vulnerabilidade a erros:**
   * Se a operação escolhida for `/` e o segundo número for `0`, o interpretador do Python levanta `ZeroDivisionError` e interrompe a execução sumariamente.
   * A ausência de tratamento em `float(input())` significa que qualquer letra digitada aciona um `ValueError` fatal, expulsando o usuário da aplicação.

## 4. O Diálogo com a IA (Engenharia de Prompts)

A evolução do código se deu através de uma comunicação estruturada com a IA. Abaixo, o resumo das diretrizes enviadas:

* **Passo 1 (Criação do cenário base):** 
  *"Escreva o código de uma calculadora básica em Python rodando em um loop while. Faça algo bem direto, focado apenas em fazer as 4 operações básicas funcionarem com inputs numéricos. Não precisa de tratamentos de erro por enquanto."*
* **Passo 2 (A Refatoração e a Defesa):**
  *"Atue como um Engenheiro de Software revisando este código. Precisamos refatorar essa calculadora: extraia cada operação para funções separadas (modularização). Além disso, blinde o código: crie tratamentos para que divisões por zero ou digitação de textos (ValueError) exibam mensagens amigáveis em vez de quebrar o programa. Adicione raiz quadrada e exponenciação."*
* **Passo 3 (Garantia de Qualidade):**
  *"Agora, abstraia a interface. Escreva uma suíte de testes usando a biblioteca 'unittest' para bater contra as funções matemáticas que criamos. Quero testes que provem que nossa função levanta um ValueError apropriado quando tentamos dividir por zero ou extrair raiz de número negativo."*

## 5. A Solução Refatorada

A nova versão (`calculadora.py`) implementa o padrão de divisão de responsabilidades:

* **Módulo Matemático:** Funções independentes (ex: `divisao_segura()`) que processam dados. Caso detectem uma anomalia (como denominador `0`), elas *levantam* (`raise`) uma exceção customizada, delegando o problema para quem chamou a função.
* **Módulo de Interface (`main`):** Responsável por exibir menus, capturar as strings e convertê-las. Aqui residem os blocos `try/except` que envelopam a experiência do usuário. Se um número for inválido, o comando `continue` apenas reinicia o laço interativo com suavidade.

## 6. Validação por Testes Automatizados

Em vez de testar as operações manualmente no terminal (o que gasta tempo e é propenso a falhas), a IA me ajudou a construir `test_calculadora.py`. 

**O que foi testado:**
* **Cálculos Básicos:** Assertivas de igualdade (ex: 2.5 + 2.5 = 5.0).
* **Regras de Negócio (Exceções):** Utilizei o `assertRaises` para garantir que `divisao_segura(10, 0)` dispara especificamente um `ValueError`. O mesmo foi aplicado à raiz de `-4`.

Executar o comando `python3 -m unittest` processa todas as regras em uma fração de segundo, validando que a fundação matemática está intacta.

## 7. Reflexões sobre os Exemplos de Refatoração da Aula

O PDF da disciplina trouxe exemplos valiosos que reforçam a necessidade da supervisão humana sobre o código "curto":

* **Soma de Lista:** 
  Substituir a iteração manual de um `while` por `sum(numeros)` não altera a ordem de complexidade temporal, que continua sendo $O(n)$. O verdadeiro benefício aqui é a clareza e a expressividade do código (estilo declarativo versus imperativo), reduzindo a carga cognitiva de quem lê.
* **Algoritmo de Número Primo:** 
  A ideia de limitar a busca por divisores até a raiz quadrada do número é brilhante para performance (reduzindo para $O(\sqrt{n})$). No entanto, sem a malícia do desenvolvedor para tratar os *edge cases* (casos extremos como números 0, 1 ou negativos), a otimização matemática entregue pela máquina classifica dados inválidos incorretamente.
* **Inversão de String:** 
  A abordagem em *Pythonic slicing* (`texto[::-1]`) é fantástica comparada à alocação repetitiva de strings em um loop de concatenação. Contudo, assim como nos casos anteriores, o programador precisa saber se está lidando com emojis compostos ou caracteres especiais que podem ser quebrados visualmente por uma simples inversão de bytes.

## 8. O Paradigma Dev+IA: Considerações Finais

O processo de criação da Calculadora validou o novo paradigma: a programação não é mais solitária. 

A Inteligência Artificial atua como um parceiro extremamente ágil na sintaxe, poupando minutos de digitação de configurações de bibliotecas (como o `math` e o `unittest`). A máquina oferece opções e velocidade.

Entretanto, o papel crítico de "Tech Lead" recai totalmente sobre o humano. A IA tentou usar tratamentos de erros genéricos (`except Exception as e:`), o que é considerado uma má prática, pois camufla bugs reais. Fui eu quem defini a arquitetura desacoplada e limitei a captura ao `ValueError`.

A IA escreve a rotina, mas a responsabilidade sobre a coerência, as regras matemáticas adotadas e a arquitetura do projeto continua sendo intransferível.

---

## 9. Instruções para Execução

**Requisito:** Python 3.10+

* **Para iniciar a versão interativa refatorada:**
  `python3 calculadora/calculadora.py`
* **Para experimentar os defeitos da primeira versão:**
  `python3 calculadora/calculadora_base.py`
* **Para rodar a bateria de validação automática:**
  `python3 -m unittest calculadora/test_calculadora.py -v`
