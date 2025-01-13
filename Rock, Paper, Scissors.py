import random

playerName = input("Masukkan Nama Kamu : ")
print(f"Selamat datang {playerName} di permainan Rock, Paper, Scissors! 🎮")

def rpseasymode ():
    choices = ["Batu", "Gunting", "Kertas"]
    nyawa_kamu = 100
    nyawa_bot = 100
    babak_permainan = 0

    while nyawa_kamu > 0 and nyawa_bot > 0:
        babak_permainan += 1
        botChoices = random.choice(choices)
        playerChoices = input("Masukkan Pilihan kamu : ")
        print(f"======================== Babak ke : {babak_permainan} =======================")
        print(f"{playerName} memilih : {playerChoices}")
        print(f"Bot memilih : {botChoices}")
        print("=============================================================")

        if botChoices == playerChoices : 
            print("Waduh, Hasilnya seri nih bro!")
        elif (botChoices == "Batu" and playerChoices == "Gunting" ) or (botChoices == "Kertas" and playerChoices == "Batu") or (botChoices == "Gunting" and playerChoices == "Kertas") : 
            print("Yah, Kamu kalah... Semangat ya! [Nyawa kamu berkurang 20 💖]"),
            nyawa_kamu -= 20
        else : 
            print("Yey, Kamu menang... Gas teruss! [Nyawa bot berkurang 20 💖]"),
            nyawa_bot -= 20
        

        print(f"Sisa nyawa kamu : {nyawa_kamu} 💖, Sisa nyawa bot : {nyawa_bot} 💖")
    
    if nyawa_kamu > 0:
        print(f"Selamat king, lu menang permainan ini! 👑 | Jumlah Putaran: {babak_permainan}")
    else:
        print(f"Yah, kok kamu kalah 😓? Yuk coba lagi! | Jumlah Putaran: {babak_permainan}")

def rpshardmode ():
    choices = ["Batu", "Gunting", "Kertas"]
    nyawa_kamu = 60
    nyawa_bot = 100
    babak_permainan = 0

    while nyawa_kamu > 0 and nyawa_bot > 0:
        babak_permainan += 1
        botChoices = random.choice(choices)
        playerChoices = input("Masukkan Pilihan kamu : ")
        print(f"======================== Babak ke : {babak_permainan} =======================")
        print(f"{playerName} memilih : {playerChoices}")
        print(f"Bot memilih : {botChoices}")
        print("=============================================================")

        if botChoices == playerChoices : 
            print("Waduh, Hasilnya seri nih bro!")
        elif (botChoices == "Batu" and playerChoices == "Gunting" ) or (botChoices == "Kertas" and playerChoices == "Batu") or (botChoices == "Gunting" and playerChoices == "Kertas") : 
            print("Yah, Kamu kalah... Semangat ya! [Nyawa kamu berkurang 20 💖]"),
            nyawa_kamu -= 20
        else : 
            print("Yey, Kamu menang... Gas teruss! [Nyawa bot berkurang 20 💖]"),
            nyawa_bot -= 20
        

        print(f"Sisa nyawa kamu : {nyawa_kamu} 💖, Sisa nyawa bot : {nyawa_bot} 💖")
    
    if nyawa_kamu > 0:
        print(f"Selamat king, lu menang permainan ini! 👑 | Jumlah Putaran: {babak_permainan}")
    else:
        print(f"Yah, kok kamu kalah 😓? Yuk coba lagi! | Jumlah Putaran: {babak_permainan}")

def rpsimpmode ():
    choices = ["Batu", "Gunting", "Kertas"]
    nyawa_kamu = 1
    nyawa_bot = 100
    babak_permainan = 0

    while nyawa_kamu > 0 and nyawa_bot > 0:
        babak_permainan += 1
        botChoices = random.choice(choices)
        playerChoices = input("Masukkan Pilihan kamu : ")
        print(f"======================== Babak ke : {babak_permainan} =======================")
        print(f"{playerName} memilih : {playerChoices}")
        print(f"Bot memilih : {botChoices}")
        print("=============================================================")

        if botChoices == playerChoices : 
            print("Waduh, Hasilnya seri nih bro!")
        elif (botChoices == "Batu" and playerChoices == "Gunting" ) or (botChoices == "Kertas" and playerChoices == "Batu") or (botChoices == "Gunting" and playerChoices == "Kertas") : 
            print("Yah, Kamu kalah... Semangat ya! [Nyawa kamu berkurang 1 💖]"),
            nyawa_kamu -= 1
        else : 
            print("Yey, Kamu menang... Gas teruss! [Nyawa bot berkurang 20 💖]"),
            nyawa_bot -= 20
        

        print(f"Sisa nyawa kamu : {nyawa_kamu} 💖, Sisa nyawa bot : {nyawa_bot} 💖")
    
    if nyawa_kamu > 0:
        print(f"Buset, hoki betul lu bro, congrats yak! | Jumlah Putaran: {babak_permainan}")
    else:
        print(f"Yah, kok kamu kalah 😓? Yuk coba lagi! | Jumlah Putaran: {babak_permainan}")

def modepermainan ():
    print("Pilih Mode Permainan (Ketik Angka 1 ~ 3): ")
    print("1. Easy Mode 🍀")
    print("Easy Mode -> Nyawa kamu dan bot 100, setiap kalah nyawa berkurang 20")
    print("2. Hard Mode ⚔️")
    print("Hard Mode -> Nyawa kamu 60 dan bot 100, setiap kalah nyawa berkurang 20")
    print("3. Impossible Mode ☠️")
    print("Impossible Mode -> Nyawa kamu 1 dan bot 100, setiap kalah nyawa berkurang 20... wait what? 😂 (Jangan sampai kalah 1x pun)")
    mode = int(input("Masukkan Pilihan Mode : "))
    if mode == 1:
        print("=============================================================")
        print("Kamu memilih Easy Mode 🍀")
        print("=============================================================")
        rpseasymode()
    elif mode == 2:
        print("=============================================================")
        print("Kamu memilih Hard Mode ⚔️")
        print("=============================================================")
        rpshardmode()
    elif mode == 3:
        print("=============================================================")
        print("Kamu memilih Impossible Mode ☠️")
        print("=============================================================")
        rpsimpmode()
    else:
        print("=============================================================")
        print("❌ Pilihan tidak tersedia, silahkan pilih mode yang tersedia! ❌")
        print("=============================================================")
        modepermainan()

modepermainan()