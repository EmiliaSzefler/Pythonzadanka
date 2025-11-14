def planer_podrozy():
    km = float(input("Ile kilometrów chcesz przejechać? "))
    spalanie = float(input("Średnie spalanie auta (l/100 km): "))
    cena_paliwa = float(input("Cena paliwa za litr: "))
    pasazerowie = input("Podaj liczbę pasażerów (lub zostaw puste): ")

    zuzycie_paliwa = (km / 100) * spalanie
    koszt = zuzycie_paliwa * cena_paliwa

    print(f"\nZużyjesz około {zuzycie_paliwa:.2f} litrów paliwa.")
    print(f"Koszt podróży: {koszt:.2f} zł")

    if pasazerowie.strip():
        pasazerowie = int(pasazerowie)
        print(f"Koszt na osobę: {koszt / pasazerowie:.2f} zł")

    if km > 500:
        print("Długa trasa – zaplanuj przerwy na odpoczynek!")
