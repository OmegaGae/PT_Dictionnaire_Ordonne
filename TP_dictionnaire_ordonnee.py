#python 3.10.0

class DictionnaireOrdonne :

    
    def __init__(self, dictionnaire=dict(),**parametresN_dict):
        
        self._liste_cle_d=list()
        self._liste_valeur_d=list()

        self._liste_cle_p=list()
        self._liste_valeur_p=list()

        self._dict_conteneur={}
        self.position=0

        if (type(dictionnaire)  is not dict) and (type(dictionnaire) is not DictionnaireOrdonne):
            raise TypeError("Cecin'est pas un dictionnaire, veuillez entrer un dictionnaire soit d" \
                "type dict, ou DictionnaireOrdonne")
        
        for cle,value in dictionnaire.items():
            self._liste_cle_d.append(cle)
            self._liste_valeur_d.append(value)
      
        for clep,valuep in parametresN_dict.items():
            self._liste_cle_p.append(clep)
            self._liste_valeur_p.append(valuep)
        
        

    def __repr__(self):
        """Representation des dictionnaires"""
        
        if self.position == 0:
            if len(self._liste_cle_d) == 0 and len (self._liste_cle_p)==0:
                return "{}".format("{}")

            elif len(self._liste_cle_d) >0:
                i=0
                self.dict_copy={}

                for c in self._liste_cle_d:
                    self.dict_copy[c]=self._liste_valeur_d[i]
                    i+=1
                
                return "{}".format(self.dict_copy)

            elif len (self._liste_cle_p) >0:
                p=0
                self.dict_p={}

                for c in self._liste_cle_p:
                    self.dict_p[c]=self._liste_valeur_p[p]
                    p+=1
                
                return "{}".format(self.dict_p)

            else:
                return "{}".format("{}") #a revoir
        elif self.position == 1:
            return "{}".format(self._dict_conteneur[self.index])


    def __str__(self):
        
        return repr(self)

    def __getitem__(self,index):
        """méthode appelée lorsqu'on fait objet[index]\
            elle va rediriger vers self._dict_conteneur"""
        
        self.position=1
        self.index=index
        
        return repr(self)

    def __setitem__(self,index,valeur):
        """méthode appelée lorsqu'on veut stocker une valeur dans un dict special\
            cad: objet[index]=valeur"""
        self._dict_conteneur[index] = valeur

    def __delattr__(self, index):
        """descrution d'un élément de l'objet conteneur"""
        del self._dict_conteneur[index]


        
