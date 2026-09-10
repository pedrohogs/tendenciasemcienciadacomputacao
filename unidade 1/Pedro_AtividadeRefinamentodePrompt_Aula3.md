# Atividade - Refinamento de Prompts

## Identificação

- **Nome:** Pedro Henrique de Oliveira Gomes
- **Turma:** Ciência da Computação
- **Data:** 10/09/2026
- **Ferramenta de IA utilizada:** ChatGPT

---

## Problema escolhido

### Contexto

Estou começando a estudar programação em Python e ainda tenho algumas dificuldades para entender como o programa toma decisões. Um assunto que ainda gera dúvida para mim é o uso do `if` e do `else`.

### Problema

Entender como funcionam as estruturas condicionais `if` e `else` em Python e conseguir identificar quando usar cada uma.

### Objetivo

Usar a Inteligência Artificial para aprender o conceito de estruturas condicionais e observar como a resposta muda quando o prompt vai sendo melhorado.

---

## Prompt 1 - Versão inicial

### Prompt

```text
Explique if e else em Python.
```

### Resultado

O `if` e o `else` são estruturas condicionais utilizadas em Python para executar diferentes blocos de código dependendo de uma condição.

Exemplo:

```python
idade = 18

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

Nesse exemplo, o programa verifica se a idade é maior ou igual a 18. Se a condição for verdadeira, mostra "Maior de idade". Caso contrário, mostra "Menor de idade".

### Primeira impressão

A resposta explicou o básico e mostrou um exemplo que dá para entender.

Mesmo assim, achei que ficou muito resumida. Ela não explicou muito bem o que significa uma condição, nem explicou cada parte do código.

Também senti falta de outro exemplo para entender melhor quando usar `if` e quando usar `else`.

---

## Prompt 2 - Primeiro refinamento

### Alterações realizadas

- **Papel:** Pedi para a IA atuar como professor de programação.
- **Contexto:** Informei que estou começando a aprender Python.
- **Objetivo:** Entender como funcionam as decisões dentro de um programa.
- **Público:** Estudante iniciante de Ciência da Computação.
- **Formato:** Explicação dividida em tópicos e com exemplos.
- **Restrições:** Utilizar linguagem simples.
- **Critérios:** A resposta deve ser fácil de entender para alguém que está começando.

### Prompt

```text
Atue como um professor de programação.

Sou estudante iniciante de Ciência da Computação e estou começando a aprender Python.

Explique de forma simples o que são if e else.

Mostre:
1. para que eles servem;
2. o que é uma condição;
3. como funciona a estrutura do if;
4. um exemplo simples usando idade;
5. outro exemplo usando uma nota de aluno.

Explique cada parte do código e evite palavras muito técnicas.

O objetivo é que eu consiga entender como um programa escolhe entre duas possibilidades.
```

### Resultado

O `if` e o `else` são usados quando queremos que o programa tome uma decisão.

### O que é uma condição?

Uma condição é uma comparação que pode ser verdadeira ou falsa.

Por exemplo:

```python
idade >= 18
```

Essa condição pergunta se a idade é maior ou igual a 18.

### Estrutura básica

```python
if condicao:
    comando
else:
    outro_comando
```

O `if` significa que o programa vai verificar uma condição.

Se a condição for verdadeira, o código que está dentro do `if` será executado.

Se for falsa, o código dentro do `else` será executado.

### Exemplo usando idade

```python
idade = 20

if idade >= 18:
    print("Pode entrar")
else:
    print("Não pode entrar")
```

Como a idade é 20, a condição `idade >= 18` é verdadeira.

Por isso, o programa mostra:

```text
Pode entrar
```

### Exemplo usando nota

```python
nota = 6

if nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")
```

Nesse caso, a nota é 6.

Como 6 não é maior ou igual a 7, a condição é falsa e o programa executa o `else`.

A saída será:

```text
Reprovado
```

Resumindo, o `if` verifica uma condição e o `else` define o que acontece quando essa condição não é verdadeira.

---

## Comparação entre Prompt 1 e Prompt 2

| Critério | Prompt 1 | Prompt 2 |
|---|---:|---:|
| Clareza | 3 | 5 |
| Precisão | 4 | 5 |
| Relevância | 3 | 5 |
| Organização | 3 | 5 |
| Adequação ao público | 3 | 5 |
| Atendimento ao objetivo | 3 | 5 |
| Utilidade prática | 3 | 5 |
| **Total** | **22** | **35** |

### Análise da comparação

O Prompt 2 gerou uma resposta mais completa e mais fácil de acompanhar.

No primeiro prompt, a explicação foi correta, mas a IA não sabia qual era o meu nível de conhecimento.

Depois que eu informei que era iniciante e pedi exemplos específicos, a resposta passou a explicar melhor o significado de cada parte.

A explicação do que é uma condição também ajudou bastante.

---

## Etapa antes do segundo refinamento

### 1. O que estava inadequado na primeira resposta?

A primeira resposta era muito curta e não explicava os detalhes do código.

### 2. O que melhorou após o primeiro refinamento?

A resposta passou a explicar o conceito de condição, apresentou dois exemplos e ficou mais adequada para quem está começando.

### 3. O que ainda pode ser melhorado?

Ainda pode ser explicado o `elif`, porque ele aparece bastante quando existem mais de duas possibilidades.

Também seria interessante mostrar um erro comum de iniciante.

### 4. Qual nova informação será adicionada?

Vou pedir uma explicação do `elif`, um exemplo com três possibilidades e um exercício no final.

### 5. Qual informação poderá ser retirada?

Não é necessário adicionar muitos exemplos. Um exemplo com três condições já pode complementar os anteriores.

### 6. Por que essas alterações podem melhorar o resultado?

Porque o `elif` ajuda a entender que um programa pode ter mais de duas decisões, e o exercício pode servir para testar se eu realmente entendi.

---

## Prompt 3 - Segundo refinamento

### Hipótese de melhoria

Acredito que a resposta ficará melhor porque, além de explicar `if` e `else`, também vai mostrar o `elif`, que é usado quando temos mais de duas opções.

### Prompt

```text
Atue como um professor de programação para estudantes iniciantes.

CONTEXTO:
Sou estudante de Ciência da Computação e estou começando a aprender Python. Já conheço variáveis e print, mas ainda tenho dificuldade com condições.

OBJETIVO:
Quero entender como um programa toma decisões usando if, elif e else.

TAREFA:
Explique:
1. o que é uma condição;
2. para que serve o if;
3. para que serve o elif;
4. para que serve o else;
5. um exemplo com três possibilidades;
6. um erro comum de iniciante.

FORMATO:
Organize a resposta com subtítulos e pequenos exemplos de código.

RESTRIÇÕES:
- utilize linguagem simples;
- não use conceitos avançados;
- explique os símbolos de comparação utilizados;
- não faça exemplos muito grandes.

CRITÉRIO DE QUALIDADE:
No final, eu devo conseguir explicar com minhas palavras a diferença entre if, elif e else.

Finalize com um exercício simples e não apresente a resposta.
```

### Resultado

## O que é uma condição?

Uma condição é uma comparação que pode resultar em verdadeiro ou falso.

Por exemplo:

```python
idade >= 18
```

O símbolo `>=` significa "maior ou igual".

Então o programa está perguntando:

"A idade é maior ou igual a 18?"

## Para que serve o `if`?

O `if` é usado para testar a primeira condição.

Exemplo:

```python
idade = 20

if idade >= 18:
    print("Maior de idade")
```

Se a condição for verdadeira, o comando será executado.

## Para que serve o `elif`?

O `elif` pode ser usado quando temos outra condição para verificar.

Ele fica entre o `if` e o `else`.

Exemplo:

```python
nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")
```

Primeiro o programa verifica se a nota é maior ou igual a 9. Como não é, ele testa a próxima condição.

Como 7 é maior ou igual a 7, a saída será:

```text
Aprovado
```

## Para que serve o `else`?

O `else` é executado quando nenhuma das condições anteriores foi verdadeira.

No exemplo anterior, se a nota fosse 5, o resultado seria:

```text
Reprovado
```

## Símbolos comuns de comparação

| Símbolo | Significado |
|---|---|
| `>` | maior que |
| `<` | menor que |
| `>=` | maior ou igual |
| `<=` | menor ou igual |
| `==` | igual |
| `!=` | diferente |

Um detalhe importante é que `==` serve para comparar dois valores.

## Erro comum de iniciante

Um erro comum é usar apenas um sinal de igual quando queremos comparar.

Errado:

```python
if idade = 18:
    print("Tem 18 anos")
```

Correto:

```python
if idade == 18:
    print("Tem 18 anos")
```

O sinal `=` normalmente é usado para colocar um valor em uma variável.

Já `==` é usado para comparar valores.

## Resumindo

O `if` testa a primeira condição.

O `elif` testa outras condições, caso a anterior seja falsa.

O `else` é utilizado quando nenhuma das condições anteriores é verdadeira.

## Exercício

Crie uma variável chamada `temperatura`.

Faça um programa que mostre:

- "Está quente" se a temperatura for maior que 30;
- "Está agradável" se for maior ou igual a 20;
- "Está frio" nos outros casos.

Tente resolver usando `if`, `elif` e `else`.

---

## Comparação final

| Critério | Prompt 1 | Prompt 2 | Prompt 3 |
|---|---:|---:|---:|
| Clareza | 3 | 5 | 5 |
| Precisão | 4 | 5 | 5 |
| Relevância | 3 | 5 | 5 |
| Organização | 3 | 5 | 5 |
| Adequação ao público | 3 | 5 | 5 |
| Atendimento ao objetivo | 3 | 5 | 5 |
| Utilidade prática | 3 | 5 | 5 |
| **Total** | **22** | **35** | **35** |

### Análise das melhorias

O Prompt 3 trouxe uma resposta mais completa porque explicou uma situação com mais de duas possibilidades.

A explicação do `elif` e dos símbolos de comparação tornou a resposta mais útil para estudar.

Também achei importante mostrar o erro entre `=` e `==`, porque é uma coisa que pode confundir quem está começando.

Mesmo com a mesma nota do Prompt 2, considero que o Prompt 3 ficou melhor para aprender o conteúdo.

---

## Qual modificação teve maior impacto no resultado?

A modificação que mais teve impacto foi explicar o contexto e informar que a resposta deveria ser voltada para um aluno iniciante.

No prompt inicial, a IA deu apenas uma explicação básica.

Quando eu especifiquei o que queria aprender e pedi exemplos, a resposta ficou mais organizada e fácil de entender.

---

## Validação crítica

Para verificar a resposta, analisei os exemplos de código e observei se as condições realmente produziam as saídas indicadas.

Também conferi se os sinais de comparação estavam sendo utilizados de forma coerente nos exemplos.

As explicações pareceram compatíveis com os conteúdos básicos de Python que estou estudando.

Mesmo assim, entendi que uma resposta da IA não deve ser considerada correta apenas porque parece bem escrita.

Em uma situação mais importante, seria necessário comparar também com o material da disciplina ou com a documentação oficial da linguagem.

### Checklist de validação

- [x] Os conceitos apresentados fazem sentido.
- [x] Os exemplos são compatíveis com as explicações.
- [x] As condições dos exemplos produzem os resultados apresentados.
- [x] A resposta atende ao problema escolhido.
- [x] Não encontrei referências ou informações aparentemente inventadas.
- [x] Consigo explicar a diferença entre `if`, `elif` e `else`.
- [x] A resposta ainda deve ser validada antes de ser usada como fonte definitiva.

---

# Reflexão individual

## 1. Qual foi a principal diferença entre o prompt inicial e o prompt refinado?

A principal diferença foi que o prompt refinado informou melhor o que eu queria aprender.

No primeiro eu apenas pedi uma explicação. Nos outros eu coloquei meu nível de conhecimento, o objetivo e os exemplos que gostaria de receber.

## 2. Quais elementos tiveram maior impacto no resultado?

Acredito que o contexto, o público e o formato tiveram maior impacto.

Quando a IA soube que a resposta era para um iniciante, a explicação ficou mais detalhada.

## 3. Um prompt mais longo necessariamente produz uma resposta melhor? Justifique.

Não. Um prompt pode ser muito longo e ainda assim ser confuso.

O mais importante é que as informações sejam úteis e ajudem a explicar claramente o objetivo.

## 4. O que acontece quando o objetivo solicitado à IA não está claramente definido?

A IA pode interpretar o pedido de uma maneira diferente da esperada e entregar uma resposta muito genérica ou fora do nível de conhecimento do usuário.

## 5. Quais informações você considera indispensáveis para elaborar um bom prompt?

Acho importante informar o objetivo, o contexto, quem vai utilizar a resposta, o formato desejado e alguma limitação, quando for necessário.

## 6. Como o refinamento de prompts pode ser útil para um profissional de Ciência da Computação?

Pode ajudar a obter explicações melhores sobre código, analisar erros, estudar novas tecnologias, produzir documentação, criar exemplos e até organizar ideias para projetos.

## 7. Que riscos podem surgir quando confiamos em uma resposta da IA sem avaliar sua qualidade?

Podemos aprender uma informação errada, utilizar código com problema ou confiar em dados que não existem.

A IA pode escrever de maneira convincente mesmo quando está errada.

## 8. Houve alguma situação em que o Prompt 3 ficou pior que o Prompt 2? Se sim, explique.

Não ficou pior, mas ele ficou mais detalhado.

Dependendo da dúvida, talvez não fosse necessário colocar tantas instruções. Para uma pergunta muito simples, um prompt menor poderia ser suficiente.

## 9. Existe um ponto em que adicionar mais instruções começa a prejudicar a resposta?

Sim. Se colocarmos regras demais, o prompt pode ficar difícil de entender ou limitar demais a resposta da IA.

## 10. O que você faria para verificar se a resposta tecnicamente está correta?

Eu testaria os códigos apresentados e compararia as informações com os materiais utilizados nas aulas.

Se fosse necessário, também consultaria a documentação oficial do Python.

---

# Take Away

> **Um bom prompt não é simplesmente um prompt longo. Ele precisa informar com clareza o que a pessoa deseja obter e fornecer contexto suficiente para a IA entender a tarefa.**

A atividade mostrou que melhorar um prompt pode mudar bastante a qualidade da resposta.

Também percebi que é importante analisar o resultado e não confiar automaticamente em tudo que a IA apresenta.

---

# Cinco recomendações práticas

1. Escreva claramente qual é o objetivo da pergunta.
2. Informe o contexto necessário para a IA entender a situação.
3. Diga qual é o nível de conhecimento do público.
4. Especifique como você gostaria que a resposta fosse organizada.
5. Confira as informações importantes antes de utilizá-las.

---

# Desafio final

Antes de alterar um prompt que não funcionou, eu faria estas perguntas:

1. O que eu pedi estava realmente claro?
2. A IA tinha contexto suficiente para responder?
3. Eu expliquei qual era o meu nível de conhecimento?
4. O problema está na resposta ou eu esperava um formato diferente?
5. As informações apresentadas podem ser verificadas?

### Pergunta final

O problema pode estar no prompt, na resposta da IA, nas informações utilizadas ou até na maneira que o usuário interpretou o resultado.

Por isso, é importante analisar cada uma dessas possibilidades antes de simplesmente concluir que a IA respondeu errado.

---

## Conclusão

Com essa atividade eu percebi que pequenas alterações em um prompt podem deixar uma resposta muito mais útil.

No primeiro prompt, a resposta foi simples e genérica.

Depois que foram adicionadas informações sobre contexto, objetivo, público e formato, a explicação ficou mais adequada para quem está começando a aprender programação.

Também entendi que usar Inteligência Artificial não significa aceitar tudo que ela responde. É necessário analisar, testar e verificar as informações antes de utilizá-las.
