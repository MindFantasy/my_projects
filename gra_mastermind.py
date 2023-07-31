import random
import time
password = ""

print("Gra mastermind")
print("""Zasady gry:
 - Gra jest przeznaczona dla jednej lub dwóch osób,
 - Gdy w grę gra jedna osoba hasło generowane jest automatycznie
 - Gdy w grę grają dwie osoby, to jedna z nich ustala hasło, a druga je zgaduje
 - Hasło składa się z czterech liczb od 1 do 6,
 - Osoba zgadująca ma 10 prób na odadnięcie hasła, po każdej ostaje odpowiedź w postaci 4 symboli:
    \"o\" - właściwa cyfra na właściwym miejscu
    \"*\" - właściwa cyfra na niewłaściwym miejscu
    \".\" - pudło
- Symbole są posortowane w kolejnośći \"o\" -> \"*\" -> \".\" """)

print()

liczba_graczy = int(input("Ile graczy będzie grało?: "))
if liczba_graczy == 1:
    for i in range (4):
        password_number = random.randint(1,6)
        password += str(password_number)

elif liczba_graczy == 2:
    password = input("Hasło pierwszego gracza: ")
    if not ((password.isdigit()) and int(password) >= 1111 and int(password) <= 6666):
        raise ValueError("Hasło nie jest zgodne z zasadami gry, proszę nie oszukiwać!")
else:
    raise ValueError("Niewłaściwa liczba graczy, tak nie da się grać!")

password_list = list(password)
countdown = 0
output_unsorted = []
output = []
rozwiazanie = False
start = time.time()

for i in range (10):

    countdown +=1
    password_player = input("Zgadnij hasło: ")
    password_player_list = list(password_player)
    if (password_player.isdigit()) and int(password_player) >= 1111 and int(password_player) <= 6666:

        # Właściwa cyfra na właściwym miejscu
        for i in range(4):
            if password_player == password:
                print("Poprawnie zgadnięto hasło")
                rozwiazanie = True
                break
            # Właściwa cyfra na właściwym miejscu
            elif password_player[i] == password[i]:
                output_unsorted.append("o")
                password_list.remove(password[i])
                password_player_list.remove(password_player[i])

        for i in range(4):
            # właściwa cyfra na niewłaściwym miejscu
            for j in range (len(password)):
                if  (password_player[j] == password[i]) and (password[i] in password_list) and (password_player[j] in password_player_list)  :
                    output_unsorted.append("*")
                    password_list.remove(password[i])
                    password_player_list.remove(password_player[j])
                    break
        # Jeżeli hasło zostanie odgadnięte
        if rozwiazanie:
                break
        # sortowanie symboli
        for i in output_unsorted:
            if i == "o":
                output.insert(0, i)
            else:
                output.append(i)

        while len(output)< 4:
            output.append(".")

        for i in range(4):
            print(output[i], end = " ")
            if i == 1:
                print()

        output_unsorted.clear()
        output.clear()
        password_list.clear()
        password_list = list(password)
        password_player_list.clear()
    else:
        print("Hasło powinno zawierać jedynie cztery cyfry od 1 do 6")
    print("\n")


if countdown == 10:
    print("Hasło nie zostało odgadnięte!")
    print(f"Hasło brzmiało:{password}")

end = time.time()
print(f"Time {end - start:.0f} seconds")


