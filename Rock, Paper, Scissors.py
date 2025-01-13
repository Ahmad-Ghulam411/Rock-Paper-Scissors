import random

def playgame ():
    choices = ["Batu", "Gunting", "Kertas"]
    nyawa_kamu = 3
    nyawa_bot = 3
    babak_permainan = 0

    while nyawa_kamu > 0 and nyawa_bot > 0:
        babak_permainan += 1
        botChoices = random.choice(choices)
        playerChoices = input("Masukkan Pilihan anda : ")
        print("Babak ke : ", babak_permainan) 
        print("Kamu memilih : ", playerChoices)
        print("Bot memilih : ", botChoices)

        if botChoices == playerChoices : 
            print("Hasilnya seri!")
        elif (botChoices == "Batu" and playerChoices == "Gunting" ) or (botChoices == "Kertas" and playerChoices == "Batu") or (botChoices == "Gunting" and playerChoices == "Kertas") : 
            print("Kamu kalah!"),
            nyawa_kamu -= 1
        else : 
            print("Kamu menang"),
            nyawa_bot -= 1
        

        print(f"Sisa nyawa kamu : {nyawa_kamu}, Sisa nyawa bot : {nyawa_bot}")
    
    if nyawa_kamu > 0:
        print(f"Selamat king, lu menang permainan ini! 👑 | Jumlah Putaran: {babak_permainan}")
    else:
        print(f"Yah, kok kamu kalah 😓? Yuk coba lagi! | Jumlah Putaran: {babak_permainan}")

    
playgame()
