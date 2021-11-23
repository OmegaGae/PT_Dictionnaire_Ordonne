coverage erase
coverage run -m unittest -v test_dictionnaire_ordonnee
coverage report -m
coverage annotate -d ./AnnotationbyCov
coverage html
