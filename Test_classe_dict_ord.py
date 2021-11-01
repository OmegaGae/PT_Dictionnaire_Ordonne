#python 3.10.0
#-*-coding:Latin-1 -*

import TP_dictionnaire_ordonnee as dic_ord

dict1={"jil":0,"emely":8,"pierre":8}
dict2= dic_ord.DictionnaireOrdonne()
dict3= dic_ord.DictionnaireOrdonne(dict1)
dict4= dic_ord.DictionnaireOrdonne(carotte = 26, haricot = 48)

print(dict2)
print(dict3)
print(dict4)

#dict2["chanpion"]=6
#dict2[23]="eeczc"
#print(dict2)
