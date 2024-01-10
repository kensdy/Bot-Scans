import discord
from discord import app_commands
import random
import requests
from bs4 import BeautifulSoup
import json

# Função para carregar obras de um arquivo JSON
def load_obras_from_json(file_name):
    try:
        with open(file_name, 'r') as file:
            obras = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        obras = []
    return obras

# Função para salvar obras em um arquivo JSON
def save_obras_to_json(file_name, obras):
    with open(file_name, 'w') as file:
        json.dump(obras, file)

# Classe para o cliente Discord
class Client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        # Verifica se já foi sincronizado
        if not self.synced:
            await tree.sync()  # Sincroniza os comandos globais
            self.synced = True
        print(f"Entramos como {self.user}.")

    # Método estático para raspar informações de mangá a partir de um link
    @staticmethod
    def scrape_manga_info(link):
        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')

        description_element = soup.find('meta', attrs={'name': 'description'})
        description = description_element['content'] if description_element else None

        image_element = soup.find('meta', attrs={'property': 'og:image:secure_url'})
        image_url = image_element['content'] if image_element else None

        return description, image_url

# Nomes dos arquivos para armazenar obras
obras_genero_file = 'obras_genero.json'

# Carrega obras de arquivos JSON
obras_genero = load_obras_from_json(obras_genero_file)

# Cria instância do cliente e árvore de comandos
aclient = Client()
tree = app_commands.CommandTree(aclient)

# Comando para recomendar uma obra de um Gênero especifico
@tree.command(name='genero', description='Recomenda obra de determinado Gênero')
async def slash_genero(interaction: discord.Interaction):
    obras_genero_file = 'obras_genero.json'
    obras_genero = load_obras_from_json(obras_genero_file)

    obra = random.choice(obras_genero)
    titulo = obra["titulo"]
    link = obra["link"]

    description, image_url = aclient.scrape_manga_info(link)

    embed = discord.Embed(title=titulo, description=f"[Link]({link})\n\n{description}", color=0x000000) #Coloque a cor que preferir
    if image_url:
        embed.set_image(url=image_url)

    embed.set_author(name="Recomendação de mangá Gênero")

    await interaction.response.send_message(embed=embed, ephemeral=False)

    save_obras_to_json(obras_genero_file, obras_genero)

# Inicia o cliente Discord
aclient.run('Key')
