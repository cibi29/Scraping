#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mtranslate import translate
from string import ascii_lowercase

# a - list of files containing source data that is to be translated. 
# b - list of files to store the translated versions of these respective files. 

a = []
b = []

for k in ascii_lowercase:
	a.append("xb" + k)

for i in range(len(a)):
	b.append("tr_"+a[i])

def main():
	for j in range(len(a)):
		with open(("corpora/b/"+a[j]),"r") as the_file:
			a_list = the_file.read().splitlines()
			i = 0
			while i < len(a_list):
				destination = open(("/users/cibi.pragadeesh/MT_models/europarl_english_hindi/translated_files/" + b[j]),"a+")
				to_translate = a_list[i]
				while ((len(to_translate) < 2000) and (i<(len(a_list)-1))):
					if len(to_translate + " " + a_list[i+1]) < 2000:
						to_translate = to_translate + " " + a_list[i+1]
						i = i + 1
					else:
						break
				destination.write(translate(to_translate,"hi").encode('utf-8')+" ")
				destination.close()
				i = i + 1

if __name__ == '__main__':
	main()
