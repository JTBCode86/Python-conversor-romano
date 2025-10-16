#Camada de Apresentação (entry point)
"""
Camada de Apresentação (Frameworks & Drivers).

Ponto de entrada da aplicação. Responsável pela interação direta com o usuário.
Neste caso, é uma interface de linha de comando (CLI).
"""
import os
from interfaces.roman_numeral_controller import RomanNumeralController

def main():
    """
    Função principal que executa o loop da aplicação.
    """
    
    #limpa a tela
    os.system('cls')

    # Cria uma instância do nosso controller
    controller = RomanNumeralController()
    
    print("--- Conversor de Inteiros para Algarismos Romanos ---")
    print("Digite um número entre 1 e 3999 para converter.")
    
    while True:
        user_input = input("Digite um número (ou 'sair' para terminar): ")
        
        if user_input.lower() == 'sair':
            print("Até logo!")
            break
            
        # A camada de apresentação apenas passa a entrada para o controller
        # e imprime a resposta formatada que ele retorna.
        result = controller.convert_number(user_input)
        print(result)
        print("-" * 20)

if __name__ == "__main__":
    main()