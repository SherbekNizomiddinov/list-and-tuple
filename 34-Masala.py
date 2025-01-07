one_tuple = 12, 34.2, "Velosiped", True, False, 2, 3, 5, False, False, False #Bu yerda tuplga elementlarni kiritb olamiz
max = 0 #maxni 0ga tenglab olamiz

for element in set (one_tuple):
    if max< one_tuple.count(element):
        max = one_tuple.count(element) #Eng ko'p takrorlangan elementni aniqlab olamiz 
        max_value = element

print("Eng ko'p takrorlangan element: {}, {} marta takrorlandi".format(max_value, max)) #Natijada eng ko'p takrorlangan element "False" bo'ladi 