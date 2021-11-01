#python 3.10.0

class DictionnaireOrdonne :

    
    def __init__(self, dictionnaire=dict(),**parametresN_dict):
        
        self._liste_cle=list()
        self._liste_valeur=list()
        

        if (type(dictionnaire)  is not dict) and (type(dictionnaire) is not DictionnaireOrdonne):
            raise TypeError("Cecin'est pas un dictionnaire, veuillez entrer un dictionnaire soit d" \
                "type dict, ou DictionnaireOrdonne")
        
        for cle,value in dictionnaire.items():
            self._liste_cle.append(cle)
            self._liste_valeur.append(value)
      
        for clep,valuep in parametresN_dict.items():
            self._liste_cle.append(clep)
            self._liste_valeur.append(valuep)
        
        

    def __repr__(self):
        """Representation des dictionnaires"""
        self._string_dict="{"

        for i, elem in enumerate(self._liste_cle):
            self._string_dict= self._string_dict + elem + ":" + self._liste_valeur[i]

    
        return "{}".format(self._string_dict)

    def __str__(self):
        return repr(self)

    def __getitem__(self,index):
        """méthode appelée lorsqu'on fait objet[index]\
            elle va rediriger vers self._dict_conteneur"""
        try :
            _found_ind=False #attr local pas d acces
            for i,cle in enumerate(self._liste_cle):
                if cle == index :
                    _found_ind=True
                    return "{}".format(self._liste_valeur[i])
            assert(_found_ind)
        except AssertionError as ass:
            "Exception:{} occured, this key does not exit in this dictionnary".format(ass)
            
        
    def __setitem__(self,index,valeur):
        """méthode appelée lorsqu'on veut stocker une valeur dans un dict special\
            cad: objet[index]=valeur"""
            
        for i,cle in enumerate(self._liste_cle):
            if cle == index:
                self._liste_valeur[i]=valeur
            else:
                self._liste_cle.append(index)
                self._liste_valeur.append(valeur)
        
    def __delattr__(self, index):
        """descrution d'un élément de l'objet conteneur"""
        _found_ind=False #attr local pas d'acces
        try:
            for i,cle in enumerate(self._liste_cle):
                if cle == index:
                    _found_ind=True
                    del self._liste_cle[i]
                    del self._liste_valeur[i]
            assert(_found_ind)
        except AssertionError as ass:
            "Exception:{} occured, this key does not exit in this dictionnary, so impossible to delete".format(ass)
            
    def longueurList (self):
        """methode permettant de verifier si la liste des valeurs et des clés ont la même longueur"""
        return len(self._liste_cle) == len(self._liste_valeur)
        

        