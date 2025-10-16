# Camada de Interface (Controller)
"""
Camada de Interfaces (Adapters).

Responsável por adaptar os dados de entrada/saída entre o mundo exterior
(Frameworks/Drivers) e a camada de aplicação (Use Cases).

O Controller lida com a validação da entrada, chama o caso de uso
e formata a resposta.
"""
from application.integer_to_roman_converter import IntegerToRomanConverterUseCase

class RomanNumeralController:
    """
    Controla o fluxo de conversão, lidando com a entrada do usuário.
    """
    def __init__(self):
        # O Controller depende do Use Case para executar a lógica de negócio.
        # Isso é um exemplo simples de Injeção de Dependência.
        self.converter_use_case = IntegerToRomanConverterUseCase()

    def convert_number(self, input_str: str) -> str:
        """
        Recebe uma string, valida, converte para inteiro, chama o caso de uso
        e retorna uma string formatada como resposta.

        Args:
            input_str (str): A entrada fornecida pelo usuário.

        Returns:
            str: Uma mensagem com o resultado da conversão ou um erro.
        """
        try:
            number = int(input_str)
        except ValueError:
            return "Erro: A entrada deve ser um número inteiro válido."

        # Regra comum: algarismos romanos padrão vão até 3999.
        if not (1 <= number <= 3999):
            return "Erro: O número deve estar no intervalo de 1 a 3999."

        try:
            # Chama o caso de uso para executar a lógica principal
            roman_numeral = self.converter_use_case.execute(number)
            return f"O número {number} em algarismos romanos é: {roman_numeral}"
        except Exception as e:
            # Captura exceções inesperadas do caso de uso
            return f"Ocorreu um erro inesperado: {e}"