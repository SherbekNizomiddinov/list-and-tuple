list_1 = [-10, 21, "SalomDunyo", "ShahzodJo'ra", 43, 5, 31.7, -6, "Assalomu Aleykum", -66] #Bu yerda faqat butun sonlarni qabul qiladi

list_2 = [] #Bo'sh list jildini yaratamiz 
for i in list_1: 
    if isinstance(i, int) and i > 0: 
        list_2.append(i) 
    elif isinstance(i, str):
            list_2.append(i.lower()) #Bunda katta yozuv bilan so'zlarimizni kichkina harfda qilib qo'yadi 

print(list_2) #Va natijani chiqaramiz 
