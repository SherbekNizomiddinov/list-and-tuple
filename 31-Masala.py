one_tuple = 12, 34.2, "Velosiped", True, False, "Mashina", 7, 76, 65, 32, "Hello Guys", 3234 #Har doimkidek tuplga elementlar qo'shib olamiz 

for i in range(12): #Bu yerda biz 12 o'zgaruvchimiz borligini beramiz
    if i % 2 == 1: #Bu yerda faqat qoldiqli sonlar ishlaydi 
        print(one_tuple[i], end=" ") # end=" " bo'shliq qo'shadi, yangi qatorga o'tilmaydi