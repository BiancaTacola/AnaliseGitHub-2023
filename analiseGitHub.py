import requests
from collections import Counter
import matplotlib.pyplot as plt

# Nome de usuário do GitHub
username = 'BiancaTacola'

# Obtém a lista de repositórios do usuário
url = f'https://api.github.com/users/{username}/repos'
response = requests.get(url)

# Verifica se a resposta da API foi bem-sucedida
if response.status_code != 200:
    print(f"Erro ao obter repositórios. Código de status: {response.status_code}")
    exit()

repos = response.json()

# Coleta informações sobre as linguagens usadas nos repositórios criados em 2023
languages_used = Counter()

for repo in repos:
    created_at = repo['created_at']

    if created_at.startswith('2023'):
        languages_url = f"{repo['languages_url']}"
        repo_languages = requests.get(languages_url).json()

        for language in repo_languages.keys():
            languages_used[language] += 1

# Gera o gráfico de barras
labels, counts = zip(*languages_used.items())

# Lista de meses de 2023
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

plt.bar(labels, counts)
plt.xlabel('Linguagem')
plt.ylabel('Quantidade de Projetos')
plt.title(f'Linguagens Usadas em Repositórios Criados em 2023 ({username})')
plt.xticks(rotation=45, ha='right')

# Adiciona o número de projetos dentro das barras
for i, count in enumerate(counts):
    plt.text(i, count, str(count), ha='center', va='bottom')

# Ajusta o eixo Y para representar os meses
plt.yticks(range(1, len(meses) + 1), meses)

plt.tight_layout()

# Caminho completo para o arquivo de imagem
caminho_arquivo = 'C:\\Bianca\\Bianca\\Alura\\Python_1\\grafico_repositorios.png'

# Salva o gráfico como um arquivo de imagem
plt.savefig(caminho_arquivo)

# Exibe a mensagem indicando que o arquivo foi salvo com sucesso
print(f'O gráfico foi salvo em: {caminho_arquivo}')

# Exibe o gráfico
plt.show()

