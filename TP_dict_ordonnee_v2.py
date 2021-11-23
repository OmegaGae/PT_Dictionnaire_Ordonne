# python 3.10.0
import json
import typing


class StructuredDictionary:
    """This class allows you to manage your own created container object"""

    def __init__(self, dictionary: typing.Optional[dict] = dict(), **parameters)->None:
        """3 ways to create your own container object: dict(), dict("p":2,"d":3), dict(dict1)
        here we create 2 lists which will be respectively the keys and the values"""

        self.key = list()
        self.value = list()
        self.position = -1  # attr de position pour la méthode __next__
        self.item = False

        if (type(dictionary) is not dict) and (
            type(dictionary) is not StructuredDictionary
        ):
            raise TypeError(
                "This is not a dictionary, please enter either"
                "a type dict, ou a type StructuredDictionary dictionary"
            )
        else:
            for cle in dictionary:
                self.key.append(cle)
                self.value.append(dictionary[cle])

            for clep, valuep in parameters.items():
                self.key.append(clep)
                self.value.append(valuep)

    def __repr__(self)->str:
        """Dictionary representation on the terminal"""
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
                    dictionary_str + '"' + str(elem) + '"' + ":" + str(self.value[i])
                )

        dictionary_str = "".join(dictionary_str) + "}"

        return "{}".format(dictionary_str)

    def __str__(self)->repr:
        """This function will be called when using print(), and it will call __repr__"""
        return repr(self)

    def __getitem__(self, index)->str:
        """This method will be called when doing object[index]
        it will go towards self.dict_container"""
        
        index_found = False
        for i, cle in enumerate(self.key):
            if cle == index:
                index_found = True
                return self.value[i]
                
        if not index_found:
            raise ValueError("Exception occured, this key does not exit in this dictionnary, so impossible to get the value")

    def __setitem__(self, index, valeur)->None:
        """You can called this method when you want to store a value in your conatiner object
        as: object[index]=value"""
        index_found = False
        for i, cle in enumerate(self.key):
            if cle == index:
                index_found = True  
                self.value[i] = valeur
        
        if index_found ==False:
            self.key.append(index)
            self.value.append(valeur)

    def __delitem__(self, index)->None:
        """This method will delete the key and value wished inside the container object"""
        index_found = False
       
        for i, cle in enumerate(self.key):
            if cle == index:
                index_found = True
                del self.key[i]
                del self.value[i]
        
        if not index_found:
            raise ValueError("Exception occured, this key does not exit in this dictionnary, so impossible to delete")
        

    def __len__(self)->int:
        """With this method you can get the length of your dictionary"""
        return len(self.key)

    def __contains__(self, object_container)->bool:
        """With this method you can search for a specific key and if it found inside
        the dictionary it will return True if not False"""
        container = False
        for i in self.key:
            if i == object_container:
                container = True

        return container

    def __iter__(self):
        """With this method you have an ietrator which will allow you to go through
        your dictionary"""
        return self

    def __next__(self)->str:
        """This method help iterator method to get step by step (index) the value in your dictionary"""
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

    def __add__(self, object_added: typing.Optional[dict] = dict()):
        """Add method between type StructuredDictionarye d1= d1 + d2"""
        
        if (type(object_added) is not dict) and (
            type(object_added) is not StructuredDictionary
        ):
            raise TypeError(
                "This is not a dictionary, please enter either a type dict, ou a type StructuredDictionary dictionary"
            )
        else:
            object_added_type_dict = json.loads(str(object_added))
            for cle in object_added_type_dict:
                self.key.append(cle)
                self.value.append(object_added_type_dict[cle])

        return self

    def sort(self, reverse=False):
        """Main function: allow your dictionary to be sorted. You can also reverse
        the sort by applying reverse = True"""
        if reverse == False:
            
            sorted_cle = sorted(self.key)
            sorted_value = []

            for key in sorted_cle:
                sorted_value.append(self[key])

            self.key = sorted_cle
            self.value = sorted_value

            return self

        elif reverse == True:

            sorted_cle = sorted(self.key, reverse=True)
            sorted_value_reverse = []

            for key_reverse in sorted_cle:
                sorted_value_reverse.append(self[key_reverse])

            self.key = sorted_cle
            self.value = sorted_value_reverse

            return self

    def keys(self)->list:
        """With this method you can get the keys list"""
        return self.key

    def values(self)->list:
        """With this method you can get the values list"""
        return self.value

    def items(self):
        """This method allows you to get the tuple of key,value of your container object"""
        self.item = True
        return iter(self)
