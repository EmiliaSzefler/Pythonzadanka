produkty = ("mleko", "chleb", "masło", "ser", "jabłka", "banany", "mąka", "cukier", "ryż", "kawa")

koszyk = []

for i in range(3):
    produkt = input(f"Podaj nazwę produktu #{i+1}: ").lower()

    if produkt in produkty:
        koszyk.append(produkt)
    else:
        print(f"Produkt '{produkt}' jest niedostępny.")

koszyk.sort()
print("\nProdukty w koszyku (alfabetycznie):")
for p in koszyk:
    print("-", p)
