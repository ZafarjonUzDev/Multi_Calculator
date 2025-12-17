# Class yaratish
class Calculator:

    # Konstruktor yaratish
    def __init__(self):
        pass

    # To'rtburchak yuzasini hisoblash metodi
    def tortburchak_S(self, a, b):

        self.s = a*b # To'rtburchak yuzasini hisoblash | Formulasi: S=a*b
        return f"<<< To'rtburchakning yuzasi: {self.s} sm.kv ga teng >>>\n" # natija

    # To'rtburchak peremetrini hisoblash metodi
    def tortburchak_P(self, a, b):
        self.p = 2*(a+b) # To'rtburchak peremetrini hisoblash | Formulasi: P=2(a+b)
        return f"To'rtburchakning peremetri: {self.p} sm ga teng\n" # Natija

    # Uchburchak yuzasini hisoblash metodi
    def uchburchak_S(self, a, b, c):
        # Geron formulasidan foydalanamiz
        p = (a+b+c)/2 # yairm peremetr
        self.s = (p*(p-a)*(p-b)*(p-c)) ** (1/2) # yuzani hisoblash | Formulasi: √p*(p-a)*(p-b)*(p-c)
        return f"Uchburchak yuzasi: {self.s:.2f} sm.kv ga teng\n" # natija

    # Uchburchak peremetrini hisoblash metodi
    def uchburchak_P(self, a, b, c):

        self.p = a+b+c # Uchburchak peremetrini hisoblash | P=a+b+c
        return f"Uchburchak peremetri: {self.p:.2f} sm ga teng\n" # natija

    # Doira yuzasini hisoblash metodi
    def doira_S(self, r):

        self.s = 3.14 * (r ** 2) # Doira yuzasini hisoblash (π=3.14) | Formulasi: π*r^2 (r - radius)
        return f"Doiraning yuzasi: {self.s:.2f} sm.kv ga teng\n" # natija

    # Doira uzunligini hisoblash metodi
    def doira_L(self, r):

        self.l = 2 * 3.14 * r # Doira uzunligini hisoblash (π=3.14) | Formulasi: 2*π*r (r - radius)
        return f"Doiranig uzunligi: {self.l:.2f} sm ga teng\n" # natija

    # Tana Massa Indeksi(TMI) ni hisoblash metodi
    def TMI(self, h, kg):
        # h - bo'yi; kg - vazni
        h1 = h/100 # Santimetr(cm) ni metrga o'tkazish
        self.tmi = kg/(h1**2) # TMI ni hisoblash | Formulasi: kg/(h^2)

        # TMI natijasiga ko'ra darajani belgilash jarayoni
        if self.tmi <= 18.5:
            daraja = "Darajangiz: Ozg'inlik"
        elif 18.6 <=  self.tmi <= 29.9:
            daraja = "Darajangiz: Normal vazn"
        elif 30 <= self.tmi <= 34.9:
            daraja = "Darajangiz: Semizlik (1-daraja)"
        elif 35 <= self.tmi <= 39.9:
            daraja = "Darajangiz: Semizlik (2-daraja)"
        else:
            daraja = "Darajangiz: Og'ir semizlik"

        return f"Tana Massa Indeksingiz(TMI): {self.tmi:.1f}  |{daraja}"


# Dasturni ishga tushirish
while True:

    # Menyularni chiqarish
    print("""|--------------------------------------------------|
|    Multi_Calculator dasturiga xush kelibsiz!     |
|--------------------------------------------------|""")
    print("| 1. Geometrik shakllar bilan ishlash              |")
    print("| 2. Sog'liqni saqlash                             |")
    print("| 0. Dasturdan chiqish                             |")
    print("|--------------------------------------------------|")
    amal = input(f">>> Amalni tanlang: ") # Amalni tanlash/so'rash
    print("|--------------------------------------------------|\n")

    # Xatolikni tutish
    try: amal = int(amal)
    except ValueError:
        print("{{{ Kerakli amalning raqamini kiriting! }}}\n")

    # Geometrik shakillar bo'limiga o'tish
    if amal == 1:

        # Davomiylikni ta'minlash uchun while loop
        while True:
            # Geometrik shakllar menyusini chiqarish
            print(">>> GEOMETRIK SHAKLLAR <<< bo'limi:\n")
            print("1. To'tburchak ning yuzasini hisoblash")
            print("2. To'tburchak ning peremetrini hisoblash")
            print("3. Uchburchak ning yuzasini hisoblash")
            print("4. Uchburchak ning peremetrini hisoblash")
            print("5. Doira yuzasini hisoblash")
            print("6. Doira uzunligini hisoblash")
            print("0. Orqaga qaytish uchun\n")

            # Geometrik shakllar menyusidan kerakli amalni tanlash/so'rash
            amal_g = input("Hisoblash amalni tanlang: ")

            # Xato buyruq kiritilganda xatolikni tutish
            try: amal_g = int(amal_g)
            except ValueError:
                print("{{{ Hisoblash amali raqamini kiriting! }}}\n")
                continue

            # Calculator klassidan obyekt yaratish
            hisoblash = Calculator()

            # Tanlovga asosan hisoblashni boshlash
            if amal_g == 1:
                print("1. To'tburchak ning yuzasini hisoblash:") # Qanaqa amal bajarilayotganini ko'rsatish

                # Qiymatlarni olish
                a = input("To'rtburchakning eni(cm): ")
                b = input("To'rtburchakning bo'yi(cm): ")

                # Xato ma'lumot kiritilganda xatolikni tutish
                try:
                    a = float(a)
                    b = float(b)
                except ValueError:
                    print("{{{ Faqat butun son kiriting! }}}")
                    continue

                # Natijani chiqarish
                print(hisoblash.tortburchak_S(a, b))

            # Tanlovga asosan hisoblashni boshlash
            elif amal_g == 2:
                print("2. To'tburchak ning peremetrini hisoblash:") # Qanaqa amal bajarilayotganini ko'rsatish

                # Qiymatlarni olish
                a = input("To'rtburchakning eni(cm): ")
                b = input("To'rtburchakning bo'yi(cm): ")

                # Xato ma'lumot kiritilganda xatolikni tutish
                try:
                    a = float(a)
                    b = float(b)
                except ValueError:
                    print("{{{ Faqat butun son kiriting! }}}")
                    continue
                print(hisoblash.tortburchak_P(a, b))

            # Tanlovga asosan hisoblashni boshlash
            elif amal_g == 3:
                print("3. Uchburchak ning yuzasini hisoblash:") # Qanaqa amal bajarilayotganini ko'rsatish

                # Qiymatlarni olish
                a = input("1-tomon ni kiriting(cm): ")
                b = input("2-tomon ni kiriting(cm): ")
                c = input("3-tomon ni kiriting(cm): ")

                # Xato ma'lumot kiritilganda xatolikni tutish
                try:
                    a = float(a)
                    b = float(b)
                    c = float(c)
                except ValueError:
                    print("{{{ Faqat butun son kiriting! }}}")
                    continue
                print(hisoblash.uchburchak_S(a, b, c))

            # Tanlovga asosan hisoblashni boshlash
            elif amal_g == 4:
                print("4. Uchburchak ning yuzasini hisoblash:") # Qanaqa amal bajarilayotganini ko'rsatish

                # Qiymatlarni olish
                a = input("1-tomon ni kiriting(cm): ")
                b = input("2-tomon ni kiriting(cm): ")
                c = input("3-tomon ni kiriting(cm): ")

                # Xato ma'lumot kiritilganda xatolikni tutish
                try:
                    a = float(a)
                    b = float(b)
                    c = float(c)
                except ValueError:
                    print("{{{ Faqat butun son kiriting! }}}")
                    continue
                print(hisoblash.uchburchak_S(a, b, c))

            # Tanlovga asosan hisoblashni boshlash
            elif amal_g == 5:
                print("5. Doira yuzasini hisoblash") # Qanaqa amal bajarilayotganini ko'rsatish

                # Qiymatni olish
                r = input("Radius ni kiriting(cm): ")

                # Xato ma'lumot kiritilganda xatolikni tutish
                try:
                    r = float(r)
                except ValueError:
                    print("{{{ Faqat butun son kiriting! }}}")
                    continue
                print(hisoblash.doira_S(r))

            # Tanlovga asosan hisoblashni boshlash
            elif amal_g == 6:
                print("6. Doira uzunligini hisoblash") # Qanaqa amal bajarilayotganini ko'rsatish

                # Qiymatni olish
                r = input("Radius ni kiriting(cm): ")

                # Xato ma'lumot kiritilganda xatolikni tutish
                try:
                    r = float(r)
                except ValueError:
                    print("{{{ Faqat butun son kiriting! }}}")
                    continue
                print(hisoblash.doira_L(r))

            # Orqaga qaytish
            elif amal_g == 0:
                break

            # Mavjud bo'lmagan buyruqni kiritilganda ogohlantirish
            else:
                print("Faqat amal raqamini kiriting!!!")

    # Buyruqqa asosan Sog'liqni saqlash bo'limiga o'tish
    elif amal == 2:

        # Dastur davomiyligini ta'minlash uchun while loop
        while True:

            # Menyularni ekranga chiqarish
            print(">>> SOG'LIQNI SAQLASH <<< bo'limi:\n")
            print("1. Tana Massa Indeksi(TMI) ni hisoblash")
            print("0. Orqaga qaytish uchun\n")

            # Buyruqni qabul qilish
            amal_s = input("Hisoblash amalni tanlang: ")

            # Noto'g'ri buyruq kiritilganda xatolikni tutish
            try:
                amal_s = int(amal_s)
            except ValueError:
                print("{{{ Hisoblash amali raqamini kiriting! }}}\n")
                continue

            # Calculator klassidan obyekt yaratish
            hisoblash = Calculator()

            # Tanlovga asosan hisoblashni boshlash
            if amal_s == 1:
                print("1. Tana Massa Indeksi(TMI) ni hisoblash")
                h = input("Bo'yi(cm): ")
                kg = input("Vazni(kg): ")

                # Xato ma'lumot kiritilganda xatolikni tutish
                try:
                    h = float(h)
                    kg = float(kg)
                except ValueError:
                    print("{{{ Faqat butun son kiriting! }}}")
                    continue

                # Natijani chiqarish
                print(hisoblash.TMI(h, kg))

            # Oraqaga qaytish
            elif amal_s == 0:
                break

            # Mavjud bo'lmagan buyruqni kiritilganda ogohlantirish
            else:
                print("}}} Faqat amal raqamini kiriting !!! {{{\n")

    elif amal == 0:
        break
    # Mavjud bo'lmagan buyruqni kiritilganda ogohlantirish
    else:
        print("}}} Faqat amal raqamini kiriting !!! {{{\n")