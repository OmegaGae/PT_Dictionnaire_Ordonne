#!/usr/bin/env python3
# -*- coding:utf-8 -*
import unittest
import json
from TP_dict_ordonnee_v2 import StructuredDictionary
from parameterized import parameterized, parameterized_class



class TestStructuredDictionaryInitCase12(unittest.TestCase):

    #init case 1: just an instancification without any arg in input
    def test_init_case1(self):
        dictionary_1 = StructuredDictionary()
        self.assertEqual(type(dictionary_1),StructuredDictionary)
        self.assertEqual(type(dictionary_1.key),list)
        self.assertEqual(type(dictionary_1.value),list)
        self.assertEqual(len(dictionary_1.key),0)
        self.assertEqual(len(dictionary_1.value),0)
        
    #init case 2: instantion with input type dict()
       
    def test_init_case2(self):
        dictionary_0 = {"jil":0,"emely":8,"pierre":3,
        "pomme":10,"richie":11,"pierrot":"vanessa"}

        dictionary_2 = StructuredDictionary(dictionary_0)
        self.assertEqual(type(dictionary_2),StructuredDictionary)
        for key in dictionary_0:
            self.assertIn(key,dictionary_2.key)
            self.assertIn(dictionary_0[key],dictionary_2.value)
        
        with self.assertRaises(TypeError):
            dictionary_error = []
            dictionary_type_error = StructuredDictionary(dictionary_error)
    
#init case 3: instantion with input as (parameter1=23,parameter4=67)
@parameterized_class(("expected_values","expected_keys"),[

    ([0,8,3],["jil","emely","pierre"]),
        ])
class TestStructuredDictionaryInitCase3(unittest.TestCase):

    def test_init_case3(self):
        dictionary_3 = StructuredDictionary(jil=0,emely=8,pierre=3)
        self.assertEqual(type(dictionary_3),StructuredDictionary)
        self.assertEqual(dictionary_3.key,self.expected_keys)
        self.assertEqual(dictionary_3.value,self.expected_values)
        

@parameterized_class(("dictionary","dictionary_deleted","key1","key2","key3","key_exist","key_no_exist","value1","value2","value3","expected_keys","expected_values","expected_values_setitem"),[

    ({"jil":0,"emely":8,"pierre":3},{"jil":0,"emely":8,"pierre":3},"jil","emely","pierre","emely","nothing",0,8,3,["jil","emely","pierre"],[0,8,3],[0,3,3]),
    ({"pomme":10,"richie":11,"pierrot":9},{"pomme":10,"richie":11,"pierrot":9},"pomme","richie","pierrot","richie","nothing2",10,11,9,["pomme","richie","pierrot"],[10,11,9],[10,9,9]),
        ])
class TestStructuredDictionaryContainer(unittest.TestCase):
    
    
    def test_setitem(self):
        empty_dictionary = StructuredDictionary()
        empty_dictionary[self.key1] = self.value1
        empty_dictionary[self.key2] = self.value2
        empty_dictionary[self.key3] = self.value3
        empty_dictionary[self.key_exist] = self.value3

        self.assertEqual(empty_dictionary.value,self.expected_values_setitem)
        
       
    def test_getitem(self):
        getitem_dictionary = StructuredDictionary(self.dictionary)
        value1 = getitem_dictionary[self.key1]
        value2 = getitem_dictionary[self.key2]
        value3 = getitem_dictionary[self.key3]
        self.assertEqual([value1,value2,value3],self.expected_values)

        with self.assertRaises(AssertionError):
            getitem_dictionary[self.key_no_exist]

    def test_key_and_value(self):
       
        key_value_dictionary = StructuredDictionary(self.dictionary)    
        
        self.assertEqual(key_value_dictionary.keys(),self.expected_keys)
        self.assertEqual(key_value_dictionary.values(),self.expected_values)
   
    def test_delitem(self):

        delitem_dictionary = StructuredDictionary(self.dictionary_deleted)

        del delitem_dictionary[self.key2]
        self.assertNotIn(self.key2,delitem_dictionary.key)
        self.assertNotIn(self.value2,delitem_dictionary.value)
        
        with self.assertRaises(ValueError):
            del delitem_dictionary[self.key_no_exist]
        


@parameterized_class([
    {"key":"emely","expected":True},
    {"key":"nothing","expected":False},
    {"key":"pierre","expected":True}
])
class TestStructuredDictionaryContains(unittest.TestCase):
    
       
    def test_contains(self):
        dictionary_contains = StructuredDictionary(jil=0,emely=8,pierre=3)
        self.assertEqual(self.key in dictionary_contains,self.expected)
 


@parameterized_class(("dictionary1","dictionary2","fake_dictionary","expected_length","expected_add","expected_sort","expected_sort_reverse"),[

    ({"jil":0,"emely":8,"pierre":9},{"julien":6,"elene":8,"patrick":18},["{","emely",":",0,"}"],3,{"jil":0,"emely":8,"pierre":9,"julien":6,"elene":8,"patrick":18},{"emely":8,"jil":0,"pierre":9},{"pierre":9,"jil":0,"emely":8}),
    ({"jil":0,"emely":8},{"franck":0,"emo":4,"pierre":9},"\"emely\":0",2,{"jil":0,"emely":8,"franck":0,"emo":4,"pierre":9},{"emely":8,"jil":0},{"jil":0,"emely":8}),
    ({"jil":0,"emely":8,"pierre":9,"pat":44,"vero":34},{"jack":89,"emelyne":23,"paul":97},1011091011081215848,5,{"jil":0,"emely":8,"pierre":9,"pat":44,"vero":34,"jack":89,"emelyne":23,"paul":97},{"emely":8,"jil":0,"pat":44,"pierre":9,"vero":34},{"vero":34,"pierre":9,"pat":44,"jil":0,"emely":8}),
])
class TestStructuredDictionary(unittest.TestCase):
    
    def test_length(self):
        self.assertEqual(len(StructuredDictionary(self.dictionary1)),self.expected_length)

    def test_add(self):
        
        structured_dictionary1 =  StructuredDictionary(self.dictionary1) + StructuredDictionary(self.dictionary2)
        self.assertEqual(json.loads(str(structured_dictionary1)),self.expected_add)
        
        with self.assertRaises(TypeError):
            structured_dictionary_error = StructuredDictionary(self.dictionary1)
            structured_dictionary_error = structured_dictionary_error + self.fake_dictionary
        

    def test_sort(self):
        self.assertEqual(json.loads(str(StructuredDictionary(self.dictionary1).sort())),self.expected_sort)
        self.assertEqual(json.loads(str(StructuredDictionary(self.dictionary1).sort(reverse=True))),self.expected_sort_reverse)


   
@parameterized_class(("dictionary","expected_representation"),[

    ({"jil":0,"emely":8,"pierre":9},"{\"jil\":0,\"emely\":8,\"pierre\":9}"),
    ({"jil":0,"emely":8},"{\"jil\":0,\"emely\":8}"),
    ({"jil":0,"emely":8,"pierre":9,"pat":44,"vero":34},"{\"jil\":0,\"emely\":8,\"pierre\":9,\"pat\":44,\"vero\":34}"),
])
class TestStructuredDictionaryRepresentation(unittest.TestCase):

    def test_representation(self):
        
        dictionary_representation = StructuredDictionary(self.dictionary)
        self.assertEqual(dictionary_representation.__str__(),self.expected_representation)



@parameterized_class(("dictionary","expected_keys","expected_values"),[

    ({"jil":0,"emely":8,"pierre":9},["jil","emely","pierre"],[0,8,9]),
    ({"jil":0,"emely":8},["jil","emely"],[0,8]),
    ({"jil":0,"emely":8,"pierre":9,"pat":44,"vero":34},["jil","emely","pierre","pat","vero"],[0,8,9,44,34]),
])
class TestStructuredDictionaryGenerator(unittest.TestCase):

    def test_generator(self):
        
        dictionary_generator = StructuredDictionary(self.dictionary)
        for cle in dictionary_generator:
            self.assertIn(cle,self.expected_keys)
            self.assertIn(dictionary_generator[cle],self.expected_values)

    def test_items(self):
       
        dictionary_generator = StructuredDictionary(self.dictionary)
        for cle,valeur in dictionary_generator.items():
            self.assertIn(cle,self.expected_keys)
            self.assertIn(valeur,self.expected_values)


        



























