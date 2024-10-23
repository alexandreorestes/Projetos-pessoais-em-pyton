import requests
from bs4 import BeautifulSoup
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
from wordpress_xmlrpc.exceptions import InvalidCredentialsError

def extract_cifra_info(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        cifra = soup.find('pre')
        titulo = soup.find('title')
        
        if not cifra or not titulo:
            return None, None
        
        titulo_novo = titulo.text.replace(" - Cifra Club", "") + " - Cifra Simplificada"
        return titulo_novo, str(cifra)
    except requests.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        return None, None

def post_to_wordpress(url_wp, username, password, title, content):
    try:
        wp = Client(url_wp, username, password)
        
        post = WordPressPost()
        post.title = title
        post.content = content
        post.post_status = 'publish'
        post.terms_names = {
            'category': ['Cifra', 'World Music']
        }
        
        post_id = wp.call(NewPost(post))
        return f"Post publicado com sucesso! ID: {post_id}"
    except InvalidCredentialsError:
        return "Erro: Credenciais inválidas para o WordPress."
    except Exception as e:
        return f"Erro ao publicar no WordPress: {e}"

def process_url(url, url_wp, username, password):
    titulo, cifra = extract_cifra_info(url)
    
    if not titulo or not cifra:
        print(f"Não foi possível extrair as informações da cifra para a URL: {url}")
        return
    
    print(f"\nExtraindo e publicando: {titulo}")
    
    result = post_to_wordpress(url_wp, username, password, titulo, cifra)
    print(result)

def main():
    url_wp = 'https://worldmusic.mus.br/cifra/xmlrpc.php'
    username = 'xandre2007'
    password = 'Salmos372('

    while True:
        print("\nMenu:")
        print("1. Fornecer um arquivo com URLs")
        print("2. Fornecer uma única URL")
        print("3. Sair")

        choice = input("\nDigite a sua escolha: ")

        if choice == '1':
            file_path = input("Digite o caminho do arquivo contendo as URLs: ")
            try:
                with open(file_path, 'r') as file:
                    urls = file.read().splitlines()
                for url in urls:
                    process_url(url.strip(), url_wp, username, password)
            except FileNotFoundError:
                print(f"Arquivo não encontrado: {file_path}")
            except Exception as e:
                print(f"Erro ao ler o arquivo: {e}")
        elif choice == '2':
            url = input('Digite a URL da cifra: ')
            process_url(url, url_wp, username, password)
        elif choice == '3':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha '1', '2' ou '3'.")

if __name__ == "__main__":
    main()
