#Código feito por Pedro Gustavo

arquivo = input("Digite o nome do arquivo para ser analizado (OBS: Sem o .txt no final): ").strip().lower()
palavra = input("\nAgora digite a palavra que você deseja contar: ").strip().lower()
print()

#tentando ler o arquivo
try:
    with open(arquivo + ".txt".lower(), "r") as file:
        leitura = file.read().lower()
        cont = leitura.count(palavra)

        #Checagem para saber se existe a palavra
        if(cont > 0):
            print(f"A palavra '{palavra}' apareceu {cont} vezes.")
        else:
            print(f"A palavra '{palavra}' não foi encontrada no texto.")

except FileNotFoundError:
    print("O arquivo não foi encontrado.")

except Exception as e:
    print("Ocorreu um erro: ", e)

input("Pressione qualquer tecla para sair...")
