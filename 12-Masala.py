import random #Bu yerda random sonlarni chiqaruvchi kutbxona yaratb olamiz 

one_list = [] #Va bo'sh listni ham yaratib olamiz

for i in range(10): #Va forda elementlarni 10 marta aylantrish uchun takrorlab qo'yamiz 
    one_list.append(random.randint(10, 50)) #Bu yerda 10dan 50gacha bo'lgan random sonlarni takrorlaymiz 

print(one_list) #Va bu yerda birinchi listni chiqaramiz

one_list.append(999) #Va bunda listni ohirgi elementini 999ga o'zgatramiz

one_list.pop(0) #Va o'sha o'zgargan qiymatni chiqaramiz 

print("New result") #Natijada yangi qiymatni chiqaradi 

print(one_list) #Bunda esa birinchi listni natijasi chiqadi 