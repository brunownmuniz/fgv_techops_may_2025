def soma(a, b):
    """Retorna a soma de dois n�meros."""
    return a + b

def subtracao(a, b):
    """Retorna a subtra��o de dois n�meros."""
    return a - b

def multiplicacao(a, b):
"""Retorna a multiplica��o de dois n�meros."""
return a * b

def divisao(a, b):
"""Retorna a divis�o de dois n�meros. Lan�a erro se b for zero."""
if b == 0:
	raise ValueError("Divis�o por zero n�o � permitida.")
return a / b