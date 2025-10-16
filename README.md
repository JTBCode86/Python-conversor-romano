# Python-conversor-romano
Este repositório contém um codigo python que segue os padrões de POO e Clean arqtecture. Seu objetivo é receber um algarismo natural e convertelo para números romanos.

# Estrutura do projeto
conversor_romano/
├── main.py     # Camada de Apresentação (entry point)
│
├── application/
│   ├── __init__.py
│   └── integer_to_roman_converter.py  # Camada de Aplicação (Use Case)
│
├── domain/
│   ├── __init__.py
│   └── roman_numeral_map.py  # Camada de Domínio (Entidade/Regra)
│
└── interfaces/
    ├── __init__.py
    └── roman_numeral_controller.py  # Camada de Interface (Controller)
