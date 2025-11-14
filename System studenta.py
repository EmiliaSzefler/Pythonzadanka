def student_info():
    imie = input("Imię: ")
    nazwisko = input("Nazwisko: ")
    rok = int(input("Rok studiów: "))
    kierunek = input("Kierunek: ")
    
    oceny_input = input("Podaj listę ocen oddzielonych spacją: ")
    oceny = [float(o) for o in oceny_input.split()]

    student = {
        "imie": imie,
        "nazwisko": nazwisko,
        "rok": rok,
        "kierunek": kierunek,
        "oceny": oceny,
        "srednia": sum(oceny) / len(oceny)
    }

    print("\n--- Kalkulator prostokąta ---")
    a = float(input("Podaj długość boku A: "))
    b = float(input("Podaj długość boku B: "))

    pole = a * b
    obwod = 2 * (a + b)

    student["pole_prostokata"] = pole
    student["obwod_prostokata"] = obwod

    return student
