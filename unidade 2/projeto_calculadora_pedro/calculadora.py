"""Versão final da calculadora, refatorada com apoio de IA.

Como executar:
    python3 calculadora/calculadora.py

O que foi refatorado:
    - Funções matemáticas separadas e modulares.
    - IA sugeriu adição de funções extras (raiz quadrada e exponenciação).
    - Tratamento de exceções (ValueError para letras, ZeroDivisionError para divisão).
"""
import math

def adicao(a: float, b: float) -> float:
    return a + b

def subtracao(a: float, b: float) -> float:
    return a - b

def multiplicacao(a: float, b: float) -> float:
    return a * b

def divisao_segura(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Erro: Divisão por zero não permitida.")
    return a / b

def raiz_quadrada(a: float) -> float:
    if a < 0:
        raise ValueError("Erro: Raiz de número negativo no conjunto dos reais.")
    return math.sqrt(a)

def exponenciacao(base: float, expoente: float) -> float:
    return math.pow(base, expoente)

def main():
    print("\n=== Calculadora Inteligente ===")
    print("Opções: +, -, *, /, raiz, exp | '0' para sair")
    
    while True:
        op = input("\nSua operação: ").strip().lower()
        if op == '0':
            print("Encerrando a calculadora. Até mais!")
            break
            
        if op in ['+', '-', '*', '/', 'exp']:
            try:
                num1 = float(input("Primeiro número: "))
                num2 = float(input("Segundo número: "))
            except ValueError:
                print("Entrada inválida! Digite apenas números.")
                continue
                
            try:
                if op == '+': print(f"Resultado: {adicao(num1, num2)}")
                elif op == '-': print(f"Resultado: {subtracao(num1, num2)}")
                elif op == '*': print(f"Resultado: {multiplicacao(num1, num2)}")
                elif op == '/': print(f"Resultado: {divisao_segura(num1, num2)}")
                elif op == 'exp': print(f"Resultado: {exponenciacao(num1, num2)}")
            except ValueError as e:
                print(e)
                
        elif op == 'raiz':
            try:
                num = float(input("Número: "))
                print(f"Resultado: {raiz_quadrada(num)}")
            except ValueError as e:
                print(f"Entrada inválida ou erro: {e}")
        else:
            print("Operação não reconhecida. Tente novamente.")

if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nOperação interrompida pelo usuário.")
