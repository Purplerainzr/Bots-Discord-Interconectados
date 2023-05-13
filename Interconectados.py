import discord
import asyncio

intents = discord.Intents().all() # Habilita todos os eventos (intents) disponíveis para os bots.

# Define uma lista de tokens para os bots do Discord. Adicione quantos tokens quiser.
TOKENS = ['token1', 'token2', 'token3']

clients = [] # Inicializa uma lista vazia para armazenar os clientes/bots.

# Cria um cliente/bot para cada token e adiciona na lista de clients.
for token in TOKENS:
    client = discord.Client(intents=intents)
    clients.append(client)

# Define o evento on_ready() para ser executado assim que os bots estiverem conectados.
async def on_ready():
    for client in clients:
        print(f'{client.user} está conectado ao Discord!')

# Inicia cada bot com o respectivo token usando o asyncio.ensure_future().
# O asyncio é uma biblioteca para programação assíncrona em Python.
for i in range(len(TOKENS)):
    asyncio.ensure_future(clients[i].start(TOKENS[i]))

# Obtém o loop de eventos padrão do asyncio e o executa indefinidamente com loop.run_forever().
loop = asyncio.get_event_loop()
loop.run_forever()
