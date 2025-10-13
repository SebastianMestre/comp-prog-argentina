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

print(f"""
# Temario

Lista de temas para IOI/ICPC

> Existen otros temarios. Por ejemplo:
>
> - [Temario oficial de IOI]( https://ioinformatics.org/page/syllabus/12 )
> - <https://youkn0wwho.academy/topic-list>
>
> Podes contribuir a este temario sugiriendo cambios en <{REPO_URL}/blob/trunk/raw/temario.tsv>

""")

for cat in temario:

	print('')
	print("<details>")
	print(f" <summary>{cat}</summary>")

	for subcat in temario[cat]:

		if subcat != "":
			print(f"<h3>{subcat}</h3>")

		print(" <ul>")
		for tema in temario[cat][subcat]:
			print(f"  <li>{tema}</li>")
		print(" </ul>")

	print("</details>")

