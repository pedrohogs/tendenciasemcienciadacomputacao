# Atividade prática - Programação assistida por inteligência artificial

**Entrega em notebook:** `atividadeaula04.ipynb`, contendo o relatório, código comentado e testes.

- **Curso:** Ciência da Computação
- **Disciplina:** Tendências em Ciência da Computação
- **Professora:** Kadidja Valéria
- **Miniprojeto escolhido:** Calculadora Simples - nível básico

## 1. Objetivo e escolha do projeto
O objetivo é construir a lógica central da calculadora e utilizar a IA para sugerir funções matemáticas extras e implementar tratamentos de erro, como a divisão por zero. O trabalho acompanha o ciclo de colaboração humano-máquina.

## 2. Regras definidas
1. O programa recebe dois números e uma operação.
2. A IA sugeriu as operações de exponenciação e raiz quadrada.
3. Não é permitida a divisão por zero.
4. Entradas não numéricas (letras) não devem quebrar a aplicação (uso de try/except).

## 3. Versão inicial
A versão inicial (`calculadora_base.py`) possui uma estrutura procedural simples usando if/elif e input direto. Suas limitações principais são a quebra abrupta caso o usuário digite uma letra (ValueError) ou tente dividir por zero (ZeroDivisionError).

## 4. Roteiro de prompts estruturados
- **Prompt 1:** "Atue como um dev Python Sênior. Crie a base de uma calculadora de terminal usando loop while."
- **Prompt 2 (Refatoração):** "Melhore o código separando as operações em funções. Implemente tratamento de divisão por zero e adicione exponenciação."
- **Prompt 3 (Debugging):** "Ao digitar uma letra, o sistema quebra. Como posso refatorar o loop com blocos try/except para validar a entrada?"

## 5. Solução final e decisões de implementação
O código foi refatorado para o padrão Dev+IA. O humano assumiu as decisões de arquitetura e validação do fluxo, enquanto a IA acelerou a sintaxe e sugeriu a lógica segura. 

## 6. Testes e resultados
Os testes (localizados em `test_calculadora.py`) utilizam a biblioteca `unittest` nativa do Python. Eles garantem que as exceções (`ValueError`) são levantadas corretamente ao tentar dividir por zero ou extrair raiz de negativo.

## 7. Reflexão sobre a colaboração humano-IA
A IA atuou perfeitamente como um "piloto" focado na sintaxe e tratamento de exceções, enquanto eu, como "navegador", orquestrei a estrutura e as regras de negócio. 

## 8. Material de referência
- VALÉRIA, Kadidja. **Programação Assistida por Inteligência Artificial**. 
- VALÉRIA, Kadidja. **Programação por Pares com IA**.
