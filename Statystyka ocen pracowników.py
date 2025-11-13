wyniki = (45, 67, 82, 90, 55, 74, 100, 61)

srednia = sum(wyniki) / len(wyniki)
print(f"Średnia ocen: {srednia:.2f}")

powyzej_sredniej = [x for x in wyniki if x > srednia]
print("Wyniki powyżej średniej:", powyzej_sredniej)

zdali = [x for x in wyniki if x >= 60]
print(f"Liczba osób, które zdały test: {len(zdali)}")

if 100 in wyniki:
    print("Gratulacje dla najlepszego uczestnika!")
