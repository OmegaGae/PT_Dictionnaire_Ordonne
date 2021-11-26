coverage erase
coverage run --omit test_dictionnaire_ordonnee.py -m unittest -v test_dictionnaire_ordonnee 
coverage report -m  
coverage annotate -d ./AnnotationbyCov
coverage html
