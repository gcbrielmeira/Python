import pandas as pd
import matplotlib.pyplot as plt

# Criar os dados para o nosso dataframe 

dados = {
    " nome": [ "arthur", "maria", "matheus", "carlos", "bruna"],
    "idade": [28, 22, 18, 35, 20],
    "Cidade": ["Cotia", " Carapikuiba", "Osasco", "Cotia"]
}

df = pd.DataFrame(dados)
# Exibir o DataFrame
print(df)

# salvar Dataframe no CSV
df.to_csv("pandas_dados.csv", index=False)

df_csv = pd.read_csv("pandas_dados.csv")

df_filtrado = df[df["idade"] > 25 ]
print(df_filtrado) # Todas as pessoas com menos de 25 anos não aparecem

df_ordenado = df. sort_values(by="idade", ascending=False)
print(df_ordenado) # Do maior para o menor ( Decrescente )

# Exibir estatisticas
print(df.describe())

media_cidade = df.groupby("cidade"["idade"].mean())
print(media_cidade)

df.plot(kind="bar", x= "nome", y = "idade", color="blue")
#plt.title("idade das pessoas")
#plt.xlabel("nome")
#plt.ylabel("idade")
#plt.show()

df.boxplot(column="Idade", by="Cidade", grid=False)
plt.title("distribuição de idades por cidade")
plt.xlabel("Cidade")  
plt.ylabel("idade")

plt.show() 
 