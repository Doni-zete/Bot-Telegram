import telebot


API_KEY = "6614407546:AAGRd5g6zI_ovCDBEojjGvkLXmEJmxB73ms"

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=["escolha_1"])
def escolha_1(mensagem):
    print(mensagem)
    texto = """
    
Pressione sobre a opção que deseja e iremos mostrar a imagem 
do produto selecionado!

/Sorvete_Morango
/Sorvete_Amendoim
/Sorvete_com_Acai
/Sorvete_Acai
/Sorvete_com_Morango
/Sorvete_Chocolate
/Sorvete_pedaco_Morango
/Sorvete_Morango_com_Acai

/Voltar
    """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["Sorvete_Morango"])
def Sorvete_Morango(mensagem):
    bot.send_photo(mensagem.chat.id, photo=open(
        'https://github.com/Doni-zete/Bot-Telegram/blob/main/assets/copo-sorvete1.png', 'rb'))


@bot.message_handler(commands=["Sorvete_Amendoim"])
def Sorvete_Amendoim(mensagem):
    bot.send_photo(mensagem.chat.id, photo=open(
        'https://github.com/Doni-zete/Bot-Telegram/blob/main/assets/copo-sorvete2.png', 'rb'))


@bot.message_handler(commands=["Sorvete_com_Acai"])
def Sorvete_com_Acai(mensagem):
    bot.send_photo(mensagem.chat.id, photo=open(
        'https://github.com/Doni-zete/Bot-Telegram/blob/main/assets/copo-sorvete3.png', 'rb'))


@bot.message_handler(commands=["Sorvete_Acai"])
def Sorvete_Acai(mensagem):
    bot.send_photo(mensagem.chat.id, photo=open(
        'https://github.com/Doni-zete/Bot-Telegram/blob/main/assets/copo-sorvete4.png', 'rb'))


@bot.message_handler(commands=["Sorvete_com_Morango"])
def Sorvete_com_Morango(mensagem):
    bot.send_photo(mensagem.chat.id, photo=open(
        'https://github.com/Doni-zete/Bot-Telegram/blob/main/assets/copo-sorvete5.png', 'rb'))


@bot.message_handler(commands=["Sorvete_Chocolate"])
def Sorvete_Chocolate(mensagem):
    bot.send_photo(mensagem.chat.id, photo=open(
        'https://github.com/Doni-zete/Bot-Telegram/blob/main/assets/copo-sorvete6.png', 'rb'))


@bot.message_handler(commands=["Sorvete_pedaco_Morango"])
def Sorvete_pedaco_Morango(mensagem):
    bot.send_photo(mensagem.chat.id, photo=open(
        'https://github.com/Doni-zete/Bot-Telegram/blob/main/assets/copo-sorvete7.png', 'rb'))


@bot.message_handler(commands=["Sorvete_Morango_com_Acai"])
def Sorvete_Morango_com_Acai(mensagem):
    bot.send_photo(mensagem.chat.id, photo=open(
        'https://github.com/Doni-zete/Bot-Telegram/blob/main/assets/copo-sorvete8.png', 'rb'))


@bot.message_handler(commands=["Voltar"])
def Voltar(mensagem):
    texto = """
    
Escolha uma opção pressionando em cima para continuar

/escolha_1 - Conhecer os sabores deliciosos disponíveis hoje.
/escolha_2 - Informações sobre tamanhos das porções e preços.
/escolha_3 - Promoções e descontos.
/escolha_4 - Pontos de venda e horários de funcionamento.
/escolha_5 - Falar com um atendente.


Na Sorveteria Donilícia, estamos aqui para adoçar seus momentos. 
Agradecemos por escolher nossos sorvetes de alta qualidade e estamos
ansiosos para atender você!"""
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["escolha_2"])
def escolha_2(mensagem):
    texto = """

Abaixo estão as opções disponíveis, juntamente com seus respectivos preços:

PEQUENO: 
Uma porção perfeita para saborear um sabor de cada vez ou para aqueles que 
preferem uma dose sutil de doçura. 

Preço: [R$ 4,99]💵.
Copo: 150 ml

MÉDIO: 
Ideal para os amantes de sorvete que desejam um pouco mais de indulgência. 
Aprecie uma combinação de sabores ou mergulhe em seu favorito. 

Preço: [R$ 6,99]💵.
Copo: 250 ml

GRANDE: 
Uma escolha indulgente para quem quer uma porção generosa de felicidade gelada. 
Experimente uma festa de sabores ou concentre-se no seu predileto. 

Preço: [R$ 10,99]💵.
Copo: 350 ml


Nossos sorvetes são feitos com ingredientes de alta qualidade e amor, 
garantindo que cada colherada seja uma explosão de sabor. 

Venha nos visitar e descubra a combinação perfeita de tamanho e sabor 
para satisfazer o seu paladar.

Ou ligue para nós, e descubra a combinação perfeita de tamanho
e sabor para satisfazer o seu paladar. 

Também é possível fazer seu pedido pelo Telegram! 

Estamos ansiosos para tornar seus momentos ainda mais doces!
🥰🤤

/Voltar

/Falar_com_atendente
    """
    bot.reply_to(mensagem, texto)


@bot.message_handler(commands=["escolha_3"])
def escolha_3(mensagem):
    texto = """
    
🍨🍨🍨🍨🍨🍨🍨🍨🍨
Combo Degustação:
Compre um tamanho Pequeno e Médio e ganhe um desconto de 10% no total.

Dia do Sorvete Duplo:
Aos sábados, compre um tamanho Grande 
e ganhe um tamanho Pequeno de sorvete grátis.

Pague por Volume:
Compre dois tamanhos Pequenos pelo preço de um Médio.

Mix & Match:
Compre um tamanho Médio e adicione um sabor extra do tamanho Pequeno
por metade do preço.

Desconto de Quantidade:
Compre três tamanhos Médios e ganhe 20% de desconto na compra.

Tamanho Família:
Compre um tamanho Grande e dois tamanhos Médios com 15% de desconto no total.

/Voltar

/Falar_com_atendente
"""
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["escolha_4"])
def escolha_4(mensagem):
    texto = """
🕛Segunda a Sexta-feira: 12:00 - 22:00 

🕚Sábado e Domingo: 11:00 - 23:00 

🏭Central: 
Endereço: Rua dos Sabores, 123
Bairro: Delícias da Cidade
Cidade: Delicilândia
CEP: 12345-678

🏚️Filial Encanto Gelado:
Endereço: Avenida das Delícias, 456
Bairro: Frescor da Vila
Cidade: Geladosville
CEP: 98765-432

🏚️Filial Sabor Celestial:
Endereço: Praça dos Sorvetes, 789
Bairro: Céu das Sobremesas
Cidade: Delicilândia
CEP: 54321-876

🏚️Filial Refrescância Total:
Endereço: Travessa dos Gelados, 101
Bairro: Frescor do Lago
Cidade: Delicilândia
CEP: 23456-789

/Voltar

/Falar_com_atendente
   """
    bot.send_message(mensagem.chat.id, texto)


@bot.message_handler(commands=["escolha_5"])
def escolha_5(mensagem):
    bot.send_message(mensagem.chat.id, """
                     
Entre em contato com atendente: 
👦@doniliciasorvetes
ou mande um e-mail para: 
✉️doniliciasorvetes@email.com

/Votar

""")
    
    
@bot.message_handler(commands=["Falar_com_atendente"])
def Falar_com_atendente(mensagem):
    bot.send_message(mensagem.chat.id, """
                     
Entre em contato com atendente: 
👦@doniliciasorvetes
ou mande um e-mail para: 
✉️doniliciasorvetes@email.com

/Votar
""")


def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def reponder(mensagem):
    texto = """Bem-vindo à Sorveteria Donilícia! 🍦
Donilícia Sorvetes: Tornando Momentos em Doçura

Escolha uma opção pressionando em cima para continuar


/escolha_1 - Conhecer os sabores deliciosos disponíveis hoje.
/escolha_2 - Informações sobre tamanhos das porções e preços.
/escolha_3 - Promoções e descontos.
/escolha_4 - Pontos de venda e horários de funcionamento.
/escolha_5 - Falar com um atendente.

🍨🍧🍨🍧🍨🍧🍨🍧🍨🍧🍨🍧🍨🍧🍨🍧
Na Sorveteria Donilícia, estamos aqui para adoçar seus momentos. 
Agradecemos por escolher nossos sorvetes de alta qualidade e estamos
ansiosos para atender você!
🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰🥰
"""
    bot.reply_to(mensagem, texto)


bot.polling()
