def sprawdz_pelnoletnosc():
    rok_urodzenia = int(input("Podaj rok urodzenia: "))
    obecny_rok = 2025

    wiek = obecny_rok - rok_urodzenia

    if wiek >= 18:
        print(f"Masz {wiek} lat — jesteś pełnoletni.")
    else:
        print(f"Masz {wiek} lat — jesteś niepełnoletni.")
