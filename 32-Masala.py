one_tuple = 12, 34.2, "Velosiped", True, False, 5, 7, 3, False #Bunda biz tuple uchun elementlar berib chiqamiz

for element in set (one_tuple): #Bunda biz har bir elementni chiqarb olamiz
    print("Bu element {}, {} marta qatnashgan".format(element, one_tuple.count(element))) #Va natijada elementlar necha marta qatnashganligini yozib chiqaramiz