# Projeto Levenshtein com PocketPy

## Descrição
Este projeto implementa o algoritmo de distância de Levenshtein em C com integração ao interpretador Python através da biblioteca PocketPy. O projeto permite calcular a similaridade entre strings tanto em código C nativo quanto através de scripts Python embarcados.

## Funcionalidades
**Cálculo de Distância de Levenshtein**: Implementação eficiente do algoritmo para medir a diferença entre duas strings

**Integração Python**: Execução de scripts Python embarcados através do PocketPy

**Interface C/Python**: Comunicação bidirecional entre código C e Python

**Exemplos Práticos**: Scripts demonstrando o uso das funcionalidades 

## Pré-requisitos
- Compilador GCC ou Clang
- Make
- Sistema operacional compatível (Linux, macOS, Windows com MinGW)

## Estruturas dos Arquivos
**main.c**
- Ponto de entrada do programa
- Inicialização do PocketPy
- Inicialização e execução do arquivo script.py
- Exporta a função distance() para Python
- Integração entre código C e Python

**levenstein.c/.h**
- Implementação do algoritmo de distãncia de Levenshtein (MIT License)
- Duas funções principais:
  - levenstein()
  - levenstein_n()
- Algoritmo otimizado com uso eficiente de memória
- Interface para integração com Python

**pocketpy.c/.h**
- Biblioteca para embarcamento do interpretador Python
- Interface C para execução de código Python
- Gerenciamento de memória e objetos Python

**Makefile**
O Makefile inclui os seguintes targets:
- **make** ou **make all**: Compila o projeto completo
- **make main**: Compila apenas o executável principal
- **make run**: Compila e executa o programa
- **make clean**: Remove todos os arquivos objeto e executável


## Release versionado para download.
link: https://github.com/Jean-Massumi/LP_UEM
