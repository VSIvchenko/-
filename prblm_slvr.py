"""
@author: Виталий Ивченко (БФЗ-203)
"""

#Прога должна брать название файла и убирать все лишнее

name = 'st1.txt'#имя вашего файла или путь, если солвер не в папке с файлом

f = name
file = open(f, 'r', encoding='utf-8')

uq = list(file.readlines())
for i in range(len(uq)-1, -1, -1):
    #print(uq[i])
    if uq[i][0] == '=' or uq[i][0] == '>' or uq[i][0] == '<':
        uq.remove(uq[i])
    
file.close()

file = open(f, 'w', encoding='utf-8')
file.writelines(uq)
file.close()


# #    if uniq[i][0] == '<' or uniq[i][0] == '>' or uniq[i][0] == '=':
#     if i[0] == '<' or i[0] == '>' or i[0] == '=':
#         uniq.remove(i)


# for i in uq:
#     print(uq)

#print(uq[1])


# import sys
# import fileinput

# with fileinput.FileInput(inplace=True, backup='.bak', mode='rb') as file:
#     seen = set()
#     for line in file:
#         if line not in seen: # first time
#             seen.add(line)
#             sys.stdout.buffer.write(line) # redirected to the file

