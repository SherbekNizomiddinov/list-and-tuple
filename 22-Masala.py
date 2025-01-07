text = "Salom Python Olami"  # Matn ko'rinishidagi o'zgaruvchi, ichida so'zlar bo'shliqlar bilan ajratilgan

one_list = text.split()  #Text ichidagi so'zlarni bo'shliqlar bo'yicha ajratib, ro'yxatga joylaydi

word = ''  # Bo'sh satr o'zgaruvchi, keyinchalik bosh harflarni yig'ish uchun ishlatiladi

for i in one_list:  # 'one_list' dagi har bir so'z ustida aylanadi
    word += i[0]  # Har bir so'zning birinchi harfini olib, 'word' o'zgaruvchisiga qo'shib boradi

print(word)  # Olingan barcha bosh harflarni birlashtirib ekranga chiqaradi