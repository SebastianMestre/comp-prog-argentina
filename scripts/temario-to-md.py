#!/usr/bin/env python3

import csv
import sys
import argparse
from collections import defaultdict

REPO_URL = "https://github.com/SebastianMestre/comp-prog-argentina"

p = argparse.ArgumentParser()
p.add_argument("input", type=argparse.FileType("r"), default=sys.stdin)
args = p.parse_args()

temario = defaultdict(lambda: defaultdict(list))
for row in csv.DictReader(args.input, delimiter='\t'):
	cat = row['Categoria']
	subcat = row['Subcategoria']
	tema = row['Tema']

	temario[cat][subcat].append(tema)
	
print("""
# Temario

Lista de temas para IOI/ICPC

> Existen otros temarios. Por ejemplo:
>
> - <https://youkn0wwho.academy/topic-list>

""")

for cat in temario:
	print('')
	print('##', cat)
	print('')

	for subcat in temario[cat]:

		if subcat != '':
			print('')
			print('###', subcat)
			print('')

		for tema in temario[cat][subcat]:
			print('-', tema)

