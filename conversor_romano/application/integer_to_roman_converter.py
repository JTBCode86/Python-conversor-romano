# Camada de Aplicação (Use Case)
"""
Camada de Aplicação (Use Case).

Responsável por orquestrar a lógica de negócio para um caso de uso específico.
Este caso de uso converte um número inteiro para seu correspondente em algarismo romano.
Ele depende da camada de Domínio para obter as regras de conversão.
"""
from domain.roman_numeral_map import ROMAN_NUMERAL_MAP

class IntegerToRomanConverterUseCase:
    """
    Executa a conversão de um número inteiro para algarismos romanos.
    """
    def execute(self, number: int) -> str:
        """
        Aplica o algoritmo de conversão.

        Args:
            number (int): O número inteiro a ser convertido.

        Returns:
            str: A representação do número em algarismos romanos.
        """
        if not isinstance(number, int):
            raise TypeError("O valor de entrada deve ser um número inteiro.")
            
        roman_numeral = []
        num = number

        # Itera sobre o mapa de conversão (do maior para o menor)
        for value, symbol in ROMAN_NUMERAL_MAP:
            # Enquanto o número for maior ou igual ao valor do mapa,
            # anexa o símbolo e subtrai o valor.
            while num >= value:
                roman_numeral.append(symbol)
                num -= value
        
        return "".join(roman_numeral)