# Bot-Scans
Um bot do Discord que recomenda obras de um scan, podendo ser personalizado de acordo com os critérios estabelecidos pela equipe.

# Bot-Scans

Bot Scans Discord

## Descrição

Este bot Discord fornece recomendações de obras de mangá com base em gêneros específicos. Ele utiliza web scraping para obter informações detalhadas sobre as obras a partir de links fornecidos.

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/kensdy/Bot-Scans.git
```

2. Instale as dependências usando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Configuração

1. No arquivo `main.py`, substitua `'Key'` em `aclient.run('Key')` pela chave do seu bot Discord.

2. Certifique-se de que todos os arquivos necessários estão presentes e nas localizações corretas:

   - `obras_genero.json` para armazenar informações sobre obras por gênero.

## Utilização

1. Execute o bot usando o comando:

```bash
python main.py
```

2. Após iniciar, o bot estará pronto para uso.

## Comandos

### `/genero`

- Descrição: Recomenda uma obra de um gênero específico.
- Uso: `/genero`
- Resposta: O bot envia uma recomendação de uma obra do gênero escolhido, incluindo título, link e informações adicionais.

## Notas

- Certifique-se de que o bot tenha as permissões adequadas no servidor Discord.
- Este bot usa web scraping para obter informações sobre mangás. Certifique-se de que esta prática está em conformidade com os Termos de Serviço do site que está sendo rasgado.
- Os arquivos JSON são utilizados para armazenar e carregar informações sobre as obras.

**Aviso:** Este bot é fornecido "como está" e pode exigir ajustes para funcionar de acordo com as mudanças nos sites de onde as informações são obtidas. Utilize-o com responsabilidade e em conformidade com os termos de serviço dos sites envolvidos.
