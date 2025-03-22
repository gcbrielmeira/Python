import requests # responsavel por enviar a requisição
from bs4 import BeautifulSoup # responsavel por tratar a requisição

# class - > feed-post-link

# url do site 
url = "https://g1.globo.com/"

headers = {
    " Use-Agent": " Mozilla/5.0 ( Windows NT 10.0; Win64; x64) Applewebkit/537.36" # (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
}

# Fazendo requisição HTTP
resposta = requests.get(url)  

# verificando se deu tudo certp
if resposta.status_code == 200:
    # codigo 200 - > sucesso
    print("requisição feita com sucesso.")
    print(resposta.text) # retorno
    # preenchendo nossa sopa
    soup = BeautifulSoup(resposta.text, " html.parser")
    # encontrando as noticias 
    noticias = soup.find_all("a", class_="feed-post-link")

    print( " Ultimas noticias do G1")
    for index, noticias in enumerate(noticias):
        print(f"{index + 1}. {noticias.text.strip()} - {noticias[' href ']}")


