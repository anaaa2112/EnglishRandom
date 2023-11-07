import random

studentsNormally = ['Hanaé Bernard Scarpa', 'Milan Bilas', 'Franchesca Fortuna', 'Scarlett Brunel-Thouret', 'Rubeya Bwakira', 'Anaïs Codreanu', 'Linnea Correia', 'Diego Costa', 'Sophie DAigle Edwards', 'Daniel Daraei', 'Ana Paula Desouza', 'Devlynne Dunn', 'Zekiya Ermis-Bolo', 'Isabella Fernando', 'Yaroslava Gorelik', 'Stella Meldrum', 'Piéric Mellina', 'Leïla OConnell', 'Isabel Orrantia', 'Delano Querin', 'Kai Simpson', 'Xavier Shanahan', 'Alija SLAPSYS', 'Naoki St Onge', 'Olivier Tessier', 'Enzo Tozzi Lira', 'Scarlett Trusevych', 'Emily Walchetseder']

#make sure studentsAbsent has the names of the absent students and this should work. It must be written as ['Name 1', 'Name 2', 'Name 3'] or simply ['Name 1'] for one student absent
studentsAbsent = ['']

studentsHere =[x for x in studentsNormally if x not in studentsAbsent]

def make_randomized_groups(studentsHere, number_of_groups):
   
    #Shuffle list of students
    random.shuffle(studentsHere)
   
    #Create groups
    all_groups = []
    for index in range(number_of_groups):
        group = studentsHere[index::number_of_groups]
        all_groups.append(group)
   
    #Format and display groups
    for index, group in enumerate(all_groups):
        print(f"✨Group {index+1}✨: {' / '.join(group)}\n")
       

make_randomized_groups(studentsHere, 11)
#the number after studentsHere is the amount of groups (ex: if there are 22 students in the class an you want groups of two, you would put 11 after studentsHere,)