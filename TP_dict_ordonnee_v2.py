# python 3.10.0
import json  
import typing

class DictionnaireOrdonne:
    """Classe permmettant de gérer l'utilisation des objets conteneurs"""

    def __init__(self, dictionary:typing.Optional[dict]=dict(), **parameters):
        """Initialisation de objet conteneurs de trois maniere differentes: dict(), dict("p":2,"d":3), dict(dict1)\
            creation de deux listes contenant respectivement la cle et la valeur correspondant de l'objet conteneur"""

        self.key = list()  
        self.value = list()
        self.position = -1  # attr de position pour la méthode __next__
        self.item = False

        if (type(dictionary) is not dict) and (
            type(dictionary) is not DictionnaireOrdonne
        ):
            raise TypeError(
                "Cecin'est pas un dictionnaire, veuillez entrer un dictionnaire soit d"
                "type dict, ou DictionnaireOrdonne"
            )
        else:
            for cle in dictionary:
                self.key.append(cle)
                self.value.append(dictionary[cle])

            for clep, valuep in parameters.items():
                self.key.append(clep)
                self.value.append(valuep)

    def __repr__(self):
        """Representation des dictionnaires sur le terminal"""
        dictionary_str = "{"  
        nbr_cle = len(self.key) 

        for i, elem in enumerate(self.key):

            if i < nbr_cle - 1:
                dictionary_str = (
                    dictionary_str
                    + '"'
                    + str(elem)
                    + '"'
                    + ":"
                    + str(self.value[i])
                    + ","
                )
            else:
                dictionary_str = (
                    dictionary_str
                    + '"'
                    + str(elem)
                    + '"'
                    + ":"
                    + str(self.value[i])
                )

        dictionary_str = "".join(dictionary_str) + "}" + "\n"

        return "{}".format(dictionary_str)

    def __str__(self):
        """méthode appelée lorsque qu'un objet est appelée dans print(), elle va appeler __repr__"""
        return repr(self)

    def __getitem__(self, index):
        """méthode appelée lorsqu'on fait objet[index]\
            elle va rediriger vers self._dict_conteneur"""
        try:
            index_found = False  
            for i, cle in enumerate(self.key):
                if cle == index:
                    index_found = True
                    return "{}".format(self.value[i])
            assert index_found
        except AssertionError as ass:
            "Exception:{} occured, this key does not exit in this dictionnary".format(
                ass
            )

    def __setitem__(self, index, valeur):
        """méthode appelée lorsqu'on veut stocker une valeur dans un dict special\
            cad: objet[index]=valeur"""

        for i, cle in enumerate(self.key):
            if cle == index:
                self.value[i] = valeur

        self.key.append(index)
        self.value.append(valeur)

    def __delitem__(self, index):
        """descrution d'un élément de l'objet conteneur"""
        index_found = False  
        try:
            for i, cle in enumerate(self.key):
                if cle == index:
                    index_found = True
                    del self.key[i]
                    del self.value[i]
            assert index_found
        except AssertionError as a:
            "Exception:{} occured, this key does not exit in this dictionnary, so impossible to delete".format(
                a
            )

    def __len__(self):
        """methode permettant d'obtenir la longueur du conteneur"""
        return len(self.key)

    def __contains__(self, object_container):
        """Méthode renvoyant un booléenne si l'objet cherché est contenu dans l'objet conteneur"""
        container = False  
        for i in self.key:
            if i == object_container:
                container = True

        return container

    def __iter__(self):
        """méthode permettant de créer un objet qui va pouvoir parcourir\
            l'objet conteneur """
        return self

    def __next__(self):
        """méthode qui va permettre a l'objet itérateur de passer d'un \
            élément à l'autre dans l'objet conteneur"""
        if self.item == False:
            if self.position == len(self.key) - 1:
                raise StopIteration
            self.position += 1

            return self.key[self.position]
        else:
            if self.position == len(self.key) - 1:
                raise StopIteration
            self.position += 1

            return self.key[self.position], self.value[self.position]

    def __add__(self, object_added:dict()):
        """Additionner des objets conteneurs entre eux: d1= d1 + d2"""
        object_added_type_dict = json.loads(
            str(object_added)
        )  
        if (type(object_added_type_dict) is not dict) and (
            type(object_added_type_dict) is not DictionnaireOrdonne
        ):
            raise TypeError(
                "Cecin'est pas un dictionnaire, veuillez entrer un dictionnaire soit d"
                "type dict, ou DictionnaireOrdonne"
            )
        else:

            for cle in dict(object_added_type_dict):
                self.key.append(cle)
                self.value.append(object_added_type_dict[cle])

        return self

    def sort(self, reverse=False):
        """Fonction permettant de trier le dictionnaireOrdonnee: aissance de la classe"""
        if reverse == False:

            sorted_a = []
            sorted_b = []
            sorted_cle = []
            sorted_value = self.key
              

            sorted_cle = sorted(self.key)

            for elem1 in self.key:
                sorted_b.append(elem1)

            for elem2 in sorted_cle:
                sorted_a.append(elem2)

            for i3, elem3 in enumerate(sorted_b):

                for i4, elem4 in enumerate(sorted_a):

                    if elem3 == elem4:
                        sorted_value[i4] = self.value[i3]
                    else:
                        pass

            self.key = sorted_cle
            self.value = sorted_value

            return self

        elif reverse == True:

            sorted_a = []
            sorted_b = []
            sorted_cle = []
            sorted_value = self.key

            sorted_cle = sorted(self.key, reverse=True)

            for elem1 in self.key:
                sorted_b.append(elem1)

            for elem2 in sorted_cle:
                sorted_a.append(elem2)

            for i3, elem3 in enumerate(sorted_b):

                for i4, elem4 in enumerate(sorted_a):

                    if elem3 == elem4:
                        sorted_value[i4] = self.value[i3]
                    else:
                        pass

            self.key = sorted_cle
            self.value = sorted_value

            return self

    def keys(self):
        """Méthode renvoyant une liste des clés de l'objet conteneur appelant"""
        return self.key

    def values(self):
        """Méthode renvoyant une liste des valeurs de l'objet conteneur appelant"""
        return self.value

    def items(self):
        """Méthode permettant de renvoyer un tuple contenant la clé et la valeur\
            de l'objet conteneur appelant"""
        self.item = True
        return iter(self)
