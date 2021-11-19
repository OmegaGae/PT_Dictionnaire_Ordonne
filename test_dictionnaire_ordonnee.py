#!/usr/bin/env python3
# -*- coding:utf-8 -*
import unittest
from TP_dict_ordonnee_v2 import structuredDictionary
from parameterized import parameterized, parameterized_class



class TestStructuredDictionaryInitCase12(unittest.TestCase):

    #init case 1: just an instancification without any arg in input
    def test_init_case1(self):
        dictionary_1 = structuredDictionary()
        self.assertEqual(type(dictionary_0),structureDictionary)
        self.assertEqual(type(dictionary_0.key),list)
        self.assertEqual(type(dictionary_0.value),list)
        self.assertEqual(len(dictionary_0.key),0)
        self.assertEqual(len(dictionary_0.value),0)
        
    #init case 2: instantion with input type dict()
       
    def test_init_case2(self):
        dictionary_0 = {"jil":0,"emely":8,"pierre":3,
        "pomme":10,"richie":11,"pierrot":"vanessa"}

        dictionary_2 = structuredDictionary(dictionary_0)
        self.assertEqual(type(dictionary_2),structureDictionary)
        for key in dictionary_0:
            self.assertIn(key,dictionary_2.key)
            self.assertIn(dictionary[key],dictionary_2.value)
        
        with self.assertRaises(TypeError):
            dictionary_error = []
            dictionary_type_error = structuredDictionary(dictionary_error)
    
#init case 3: instantion with input as (parameter1=23,parameter4=67)
@parameterized_class(("parameter1","parameter2","parameter3","all_keys","all_values")[

    (jil=0,emely=8,pierre=3,[0,8,3],["jil","emely","pierre"]),
    (pomme=10,richie=11,pierrot=9,[10,11,9],["pomme","richie","pierrot"])
        ])
class TestStructuredDictionaryInitCase3(unittest.TestCase):

    def test_init_case3(self):
        dictionary_3 = structuredDictionary(self.parameter1,self.parameter2,self.parameter3)
        self.assertEqual(type(dictionary_3),structureDictionary)
        self.assertEqual(self.all_keys,dictionary_3.key)
        self.assertIn(self.all_values,dictionary_3.value)
        

@parameterized_class(("key1","key2","key3","key_no_exist","value1","value2","value3","expected_keys","expected_values")[

    ("jil","emely","pierre","nothing",0,8,3,["jil","emely","pierre"],[0,8,3]),
    ("pomme","richie","pierrot","nothing2",10,11,9,["pomme","richie","pierrot"],[10,11,9],)
        ])
class TestStructuredDictionaryContainer(unittest.TestCase):
    
    empty_dictionary = structuredDictionary()
    get_key = []
    get_value = []

    def test_setitem(self):
        empty_dictionary[self.key1] = self.value1
        empty_dictionary[self.key2] = self.value2
        empty_dictionary[self.key3] = self.value3
        self.assertEqual(empty_dictionary.value,self.expected_values)
        
       
    def test_getitem(self):
        value1 = empty_dictionary[self.key1]
        value2 = empty_dictionary[self.key2]
        value3 = empty_dictionary[self.key3]
        self.assertEqual([value1,value2,value3],self.expected_values)

        with self.assertRaises(AssertionError):
            empty_dictionary[self.key_no_exist]

   def test_key_and_value(self):
        
        get_key = empty_dictionary.key
        get_value = empty_dictionary.value
        
        self.assertEqual(get_key,self.expected_keys)
        self.assertEqual(get_value,self.expected_values)
   
   def test_delitem(self):

        del empty_dictionary[self.key2]
        self.assertNotIn(self.key2,empty_dictionary.key)
        self.assertNotIn(self.value2,empty_dictionary.value)
        
        with self.assertRaises(AssertionError):
            empty_dictionary[self.key_no_exist]


@parameterized_class([
    {"key":"emely","expected":True},
    {"key":"nothing","expected":False},
    {"key":"pierre","expected":True}
])
class TestStructuredDictionaryContains(unittest.TestCase):
    
    dictionary_contains = structuredDictionary(jil=0,emely=8,pierre=3)
    
    def test_contains(self):
        self.assertEqual(self.key in dictionary_contains,self.expected)
 


@parameterized_class(("dictionary1","dictionary2","expected_length","expected_add","expected_sorted")[

    ({"jil":0,"emely":8,"pierre":9},{"julien":6,"elene":8,"patrick":18},3,
        {"jil":0,"emely":8,"pierre":9,"julien":6,"elene":8,"patrick":18},{"emely":8,"jil":0,"pierre":9}),
    ({"jil":0,"emely":8},{"franck":0,"emo":4,"pierre":9},2,{"jil":0,"emely":8,"franck":0,"emo":4,"pierre":9},{"emely":8,"jil":0}),
    ({"jil":0,"emely":8,"pierre":9,"pat":44,"vero":34},{"jack":89,"emelyne":23,"paul":97},5,
        {"jil":0,"emely":8,"pierre":9,"pat":44,"vero":34,"jack":89,"emelyne":23,"paul":97},{"emely":8,"jil":0,"pat":44,"pierre":9,"vero":34})
])
class TestStructuredDictionary(unittest.TestCase):
    
    def test_length(self):
        self.assertEqual(len(StructuredDictionary(self.dictionary1)),self.expected_length)

    def test_add(self):
        structured_dictionary1= StructuredDictionary(self.dictionary1)
        structured_dictionary2= StructuredDictionary(self.dictionary2)
        self.assertEqual(structured_dictionary1 + structured_dictionary2,self.expected_add)


   


@parameterized_class(("key1","key2","key3","key_no_exist","value1","value2","value3","expected_keys","expected_values")[

    ("jil","emely","pierre","nothing",0,8,3,["jil","emely","pierre"],[0,8,3])
    ("pomme","richie","pierrot","nothing2",10,11,9,["pomme","richie","pierrot"],[10,11,9],)
        ])
class TestStructuredDictionary(unittest.TestCase):














