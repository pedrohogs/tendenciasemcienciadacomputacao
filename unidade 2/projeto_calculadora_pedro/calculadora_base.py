"""Versão inicial da calculadora, preservada para comparação com calculadora.py.

Como executar:
    python3 calculadora/calculadora_base.py

Limitações desta base:
    1. Não trata divisão por zero (causa ZeroDivisionError).
    2. Não trata entradas inválidas (letras no lugar de números causam ValueError).
    3. Tudo está concentrado em uma única função.
    4. Apenas as 4 operações básicas.
"""

def calcular_base():
    print("Calculadora Simples - Versão Base")
    while True:
        op = input("Operação (+, -, *, /) ou '0' para sair: ")
        if op == '0':
            print("Saindo...")
            break
            
        if op in ['+', '-', '*', '/']:
            # Limitação: Se digitar texto, o programa quebra (ValueError)
            num1 = float(input("Primeiro número: "))
            num2 = float(input("Segundo número: "))

            if op == '+':
                print(f"Resultado: {num1 + num2}")
            elif op == '-':
                print(f"Resultado: {num1 - num2}")
            elif op == '*':
                print(f"Resultado: {num1 * num2}")
            elif op == '/':
                # Limitação: Se num2 for 0, o programa quebra (ZeroDivisionError)
                print(f"Resultado: {num1 / num2}")
        else:
            print("Operação inválida.")

if __name__ == "__main__":
    calcular_base()
