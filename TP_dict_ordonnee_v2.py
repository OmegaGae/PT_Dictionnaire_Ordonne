#python 3.10.0
import json #petite triche car import json non vu dans le cours sera utile pour str -> dict()

class DictionnaireOrdonne :

    
    def __init__(self, dictionnaire = dict(),**parametresN_dict):
        """Initialisation de objet conteneurs de trois maniere differentes: dict(), dict("p":2,"d":3), dict(dict1)\
            creation de deux listes contenant respectivement la cle et la valeur correspondant de l'objet conteneur"""
        
        self._liste_cle=list() # attribut privé
        self._liste_valeur=list() #attribut privé
        self.position=-1
        

        if (type(dictionnaire)  is not dict) and (type(dictionnaire) is not DictionnaireOrdonne):
            raise TypeError("Cecin'est pas un dictionnaire, veuillez entrer un dictionnaire soit d" \
                "type dict, ou DictionnaireOrdonne")
        else:
            for cle in dictionnaire:
                self._liste_cle.append(cle)
                self._liste_valeur.append(dictionnaire[cle])
        
            for clep,valuep in parametresN_dict.items():
                self._liste_cle.append(clep)
                self._liste_valeur.append(valuep)
        
        

    def __repr__(self):
        """Representation des dictionnaires sur le terminal"""
        self._string_dict="{" #attr privé
        _nbr_cle= len(self._liste_cle) #attr privé

        for i, elem in enumerate(self._liste_cle):

            if i < _nbr_cle-1:
                self._string_dict= self._string_dict +"\""+ str(elem)+"\""+ ":" + str(self._liste_valeur[i]) + ","
            else:
                self._string_dict= self._string_dict +"\"" + str(elem) + "\"" + ":" + str(self._liste_valeur[i])

        
        self._string_dict = "".join(self._string_dict) +"}"+"\n"

        return "{}".format(self._string_dict)

    def __str__(self):
        """méthode appelée lorsque qu'un objet est appelée dans print(), elle va appeler __repr__"""
        return repr(self)

    def __getitem__(self,index):
        """méthode appelée lorsqu'on fait objet[index]\
            elle va rediriger vers self._dict_conteneur"""
        try :
            _found_ind=False #attr local pas d acces et attr privé
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
        
        self._liste_cle.append(index)
        self._liste_valeur.append(valeur)
        
                
    def __delitem__(self, index):
        """descrution d'un élément de l'objet conteneur"""
        _found_ind=False #attr local pas d'acces et  privé
        try:
            for i,cle in enumerate(self._liste_cle):
                if cle == index:
                    _found_ind=True
                    del self._liste_cle[i]
                    del self._liste_valeur[i]
            assert(_found_ind)
        except AssertionError as ass:
            "Exception:{} occured, this key does not exit in this dictionnary, so impossible to delete".format(ass)
            
    def __len__(self):
        """methode permettant d'obtenir la longueur du conteneur"""
        return len(self._liste_cle)
    
    def __contains__ (self,objt_c):
        """Méthode renvoyant un booléenne si l'objet cherché est contenu dans l'objet conteneur"""
        _bool_con=False #attr privé
        for i in self._liste_cle:
            if i == objt_c:
                _bool_con=True

        return _bool_con
    
    def __iter__ (self):
        """méthode permettant de créer un objet qui va pouvoir parcourir\
            l'objet conteneur """
        return self
    
    def __next__(self):
        """méthode qui va permettre a l'objet itérateur de passer d'un \
            élément à l'autre dans l'objet conteneur"""
        
        if self.position == len (self._liste_cle)-1:
            raise StopIteration 
        self.position+=1

        return self._liste_cle[self.position]
        

         
    
    def __add__ (self, objt_ajouter =dict()):
        """Additionner des objets conteneurs entre eux: d1= d1 + d2"""
        _objt_ajouter_dict=json.loads(str(objt_ajouter))  #petite triche car import json non vu dans le cours
        if (type(_objt_ajouter_dict)  is not dict) and (type(_objt_ajouter_dict) is not DictionnaireOrdonne):
            raise TypeError("Cecin'est pas un dictionnaire, veuillez entrer un dictionnaire soit d" \
                "type dict, ou DictionnaireOrdonne")
        else:
            
            for cle in dict(_objt_ajouter_dict):
                self._liste_cle.append(cle)
                self._liste_valeur.append(_objt_ajouter_dict[cle])
            
        return repr(self)
    
    

        

        
        

        








        

        