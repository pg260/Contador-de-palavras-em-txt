#Código feito por Pedro Gustavo

arquivo = input("Digite o nome do arquivo para ser analizado (OBS: Sem o .txt no final): ").strip().lower()
print()

cont = 0

#tentando ler o arquivo
try:
    with open(arquivo + ".txt".lower(), "r") as file:
        leitura = file.read().lower()
        texto = leitura.split()

        for palavra in texto:
            for letras in palavra:
                if(letras.isalpha()):
                    cont += 1
                    break

        #Checagem para saber se existe a palavra
        if(cont > 0):
            print(f"Apareceram {cont} palavras no texto.")
        else:
            print(f"Nenhuma palavra foi encontrada no texto.")

except FileNotFoundError:
    print("O arquivo não foi encontrado.")

except Exception as e:
    print("Ocorreu um erro: ", e)

input("Pressione qualquer tecla para sair...")
