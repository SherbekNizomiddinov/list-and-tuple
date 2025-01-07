import random #Bu yerda biz random son chiqaradigan kutbxona chaqrb olamiz 

one_list = [] #Va bu yerga bo'sh list yaratib olamiz

for i in range(10): #Va bu yerda forga 10 marta aylanishini chaqrb qo'yamiz 
    one_list.append(random.randint(10, 50)) #Va bu yerda 10dan 50gacha bo'lgan random sonlarni chiqarishini so'raymiz

print(one_list) #Va natijani chiqaramiz !!!