import discord
import json
import random

# Загружаем секреты
with open('secrets.json') as f:
    secrets = json.load(f)

TOKEN = secrets['DISCORD_TOKEN']
CHANNEL_ID = secrets['WELCOME_CHANNEL_ID']

# Список интересных фактов
facts = [
    "У нашего солнца есть спина, которая вращается быстрее его ядра!",
    "Достижение Млечного Пути — это одна из самых больших красот в нашей Вселенной.",
    "Земля никогда не останавливается, она постоянно движется!",
    "Мозг человека примерно на 75% состоит из воды.",
    "Пчёлы могут распознавать человеческие лица."
]

# Создаем клиент
intents = discord.Intents.default()
intents.members = True  # Необходимо для отслеживания новых участников
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Бот подключен как {client.user}')

@client.event
async def on_member_join(member):
    # Получаем канал по ID
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        fact = random.choice(facts)
        message = (
            f"Привет, {member.mention}!\n"
            f"Интересный факт: {fact}"
        )
        await channel.send(message)

# Запуск бота
client.run(TOKEN)
