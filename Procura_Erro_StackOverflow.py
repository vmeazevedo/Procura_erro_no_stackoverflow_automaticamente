import webbrowser
import logging

try:
    # Valida se o usuário digitou um número
    a = int(input("Digite um número qualquer: "))
except BaseException as e:
    # Caso o valor inserido nao for um número irá armazenar a log de erro em 'e'
    logging.error('Error: ' + str(e))
    # Busca o erro apresentado diretamente no site do stackoverflow
    url='https://stackoverflow.com//search?q='
    # Passa a url e a variavel com a string do erro para efetuar a busca
    search_url = url + str(e)
    # Abre a pagina da pesquisa
    webbrowser.open(search_url)
else:
    # Caso o usuario digite corretamente print o texto
    print("Você digitou um número.")




