# python 3.10.0
# -*-coding:Latin-1 -*

import TP_dict_ordonnee_v2 as dic_ord

dict1 = {"jil": 0, "emely": 8, "pierre": 8}
dict2 = dic_ord.structuredDictionary()
dict3 = dic_ord.structuredDictionary(dict1)
dict4 = dic_ord.structuredDictionary(carotte=26, haricot=48, noix=27)

print(dict2)
print(dict3)
print(dict4)

dict2["pomme"] = 6
dict2["melon"] = 5
dict2["poire"] = 10
dict2["voiture"] = 1000

print(dict2)

del dict2["voiture"]
print(dict2)


print(len(dict2))

T_F = "melonr" in dict2
print(T_F)

for cle in dict4:
    print(cle)


dict2 = dict2 + dict4
print(dict2)

dict2.sort()
print(dict2)

dict2.sort(reverse=True)
print(dict2)


print(dict2.keys())  

print(dict2.values())  

for nom, qtt in dict2.items():
    print("{0} ({1})".format(nom, qtt))
