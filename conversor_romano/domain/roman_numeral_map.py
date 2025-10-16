# Camada de Domínio (Entidade/Regra)

"""
Camada de Domínio.

Contém as regras de negócio mais puras e essenciais.
Neste caso, o mapa de conversão de inteiros para algarismos romanos.
Esta tupla é a "entidade" principal do nosso sistema.
A ordem (do maior para o menor) é crucial para o algoritmo de conversão.
"""

# Tupla de tuplas representando o valor e o símbolo romano correspondente.
# Inclui os casos de subtração (como 900, 400, 90, 40, 9, 4) para simplificar a lógica.
ROMAN_NUMERAL_MAP = (
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
    (1, 'I')
)