import string

def analizuj_tekst(tekst):
    tekst_sformatowany = tekst.strip().lower().replace("python", "PYTHON")

    licznik = {}
    for znak in tekst_sformatowany:
        if znak.isalpha():
            licznik[znak] = licznik.get(znak, 0) + 1

    slowa = tekst_sformatowany.split()
    tekst_odwrocony = " ".join(slow[::-1] for slow in slowa)

    wynik = {
        "tekst_sformatowany": tekst_sformatowany,
        "tekst_odwrocony": tekst_odwrocony,
        "licznik_liter": licznik
    }
    
    print("\n--- WYNIK ANALIZY TEKSTU ---")
    print("Sformatowany tekst:", tekst_sformatowany)
    print("Tekst odwrócony:", tekst_odwrocony)
    print("Licznik liter:", licznik)

    return wynik
