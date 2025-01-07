one_tuple = 12, "Sherbek", "Asadbek", 45, 67, "Shahzodbek", "Olimjon", True, False #Bu yerda listga o'zgaruvchi kirgizib olamiz 
i = 0 #0-chi qadam bilan boshlashni aytib qo'yamiz

one_list = [] #Va bo'sh list yaratib olamiz 

while i < 3: #Whileni elemntgacha yurishini berib qo'yamiz 
    one_list.append(one_tuple[i]) 
    i+=1


while i:
    one_list.append(one_tuple[len(one_tuple) - i]) 
    i-=1
print(one_list)


print(one_list[::-1]) #Bunda biz elementlarni teskarisga chiqaramiz 