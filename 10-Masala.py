one_list = [10,23,43,21] #Bunda biz listga elementlarni kiritb olamiz 

list_tuple = tuple(one_list) #Va bunda list tuplga birinchi yaratgan listimizni kiritb qo'yamiz 

two_list = list(list_tuple) #Bu yerda ikkinchi listga list tuplni kiritib olamiz 

two_list[3] = 7 #Endi esa biz 3-indeksimizni qiymatini 7ga o'zgartramiz

print(two_list) #Va natijani chiqaramiz