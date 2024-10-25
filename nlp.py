from textblob import TextBlob

# Função para analisar a polaridade de um texto
def analisar_sentimento(texto):
    # Cria um objeto TextBlob
    blob = TextBlob(texto)
    
    # Obtém a polaridade do texto
    polaridade = blob.sentiment.polarity
    
    # Define a categoria do sentimento baseado na polaridade
    if polaridade > 0:
        sentimento = "Positivo"
    elif polaridade < 0:
        sentimento = "Negativo"
    else:
        sentimento = "Neutro"
    
    return sentimento, polaridade

# Função principal
def main():
    print("Analisador de Sentimentos - Digite um texto para análise.")
    
    # Lê o texto de entrada do usuário
    texto = input("Digite um texto: ")
    
    # Análise do sentimento
    sentimento, polaridade = analisar_sentimento(texto)
    
    # Exibe o resultado
    print(f"Sentimento: {sentimento}")
    print(f"Polaridade: {polaridade:.2f}")

if __name__ == "__main__":
    main()
