#leitura de dados
nivel = int(input("Digite o nivel de seu personagem: "))
ataque = int(input("Digite o poder de ataque de seu personagem: "))
defesa = int(input("Digite o poder de defesa de seu personagem: "))
ouro = int(input("Digite o quanto de ouro seu personagem possui: "))

#escolha da missao
missao = "0"
maiorouro = ouro

missao1 = ouro
if ataque >= 30 and defesa >= 10:
    missao1 += 25
    
    if missao1 > maiorouro:
        missao = "1"
        maiorouro  = missao1

missao2 = ouro
if missao2 >= 30 and defesa >= 30:
    missao2 += 10

    if missao2 > maiorouro:
        missao = "2"
        maiorouro = missao2

missao3 = ouro
if nivel >= 3 and ataque < defesa and missao3 >= 50:
    missao3 += 50

    if missao3 > maiorouro:
        missao3 = "3"
        maiorouro = missao3

missao4 = ouro
if nivel >= 3:
    if ataque >= 20 and defesa >= 30:
        missao4 += 40
    elif missao4 >= 20:
        missao4 += 20

    if missao4 > maiorouro:
        missao = "4"
        maiorouro = missao4

missao5 = ouro
if nivel >= 5 and ataque >= 40 and defesa >= 50 and missao5 >= 50:
    missao5 += 80

    if missao5 > maiorouro:
        missao = "5"
        maiorouro = missao5

missao6 = ouro
if nivel >= 5 and defesa >= 50:
    missao6 += 30
    if ataque >= 50:
        missao6 += 30

    if missao6 > maiorouro:
        missao = "6"
        maiorouro = missao6

print("Missão escolhida: ", missao)
print("Moedas de ouro: ", maiorouro)