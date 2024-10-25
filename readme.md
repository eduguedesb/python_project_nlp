Este projeto é um analisador de sentimentos desenvolvido em Python, utilizando a biblioteca TextBlob para processar textos e determinar sua polaridade. Ele classifica o texto como positivo, negativo ou neutro, com base na análise de sentimentos.

Funcionalidades

Análise de Sentimento: O programa classifica textos fornecidos como positivos, negativos ou neutros, dependendo da polaridade.
Polaridade: A polaridade varia de -1 (totalmente negativo) até 1 (totalmente positivo), com 0 representando um sentimento neutro.

Como Funciona

O usuário insere um texto.
O programa processa o texto usando TextBlob para determinar a polaridade.
O resultado é exibido no terminal, mostrando a classificação do sentimento (Positivo, Negativo ou Neutro) e o valor da polaridade.

Obs.: Inicialize o banco de dados do TextBlob para análise de texto (somente na primeira execução): python -m textblob.download_corpora
