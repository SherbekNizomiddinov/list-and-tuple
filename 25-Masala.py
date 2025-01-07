one_list = [
         (1, 2, 3)
         (4, 5, 6)
         (7, 8, 9)
         (9, 8, 5)
         (4, 3, 2)]

all_tuples = []

for tuples in one_list:
    
    all_tuples.append([element for element in set(tuples)])


all_elements = [element for lists in all_tuples for element in lists]


for i in set(all_elements):
    if all_elements.count(i) == len(one_list):
        print(i)

