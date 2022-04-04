from locale import currency
import sys
import re

f = open(sys.argv[1], 'r').read()

currencies = re.findall(r'[$|₹|£]\d+\.?\d*\b', f)
print('Currencies ($ or ₹ or £) in the given file are')
print(currencies)
print('------------------------------------------------------------')

dates = re.findall(r'\b\d{2}\/\d{2}\/\d{2}\b', f) + re.findall(r'\b\d{2}\/\d{2}\/\d{4}\b', f)
print('Dates with format (dd/mm/yyyy or dd/mm/yy or mm/dd/yyyy or mm/dd/yy) in the given file are')
print(dates)
print('------------------------------------------------------------')

cardinalities = re.findall(r'\bfirst\b|\bsecond\b|\bthrid\b|\bzeroth\b|\bfourth\b|\bfifth\b|\bsixth\b|\bseventh\b|\beigth\b|\bnineth\b|\btenth\b|\beleventh\b|\btwelveth\b|\bthirteenth\b|\bfourteenth\b|\bfifteenth\b|\bsixteenth\b|\bseventeenth\b|\beighteenth\b|\bnineteenth\b', f)
orders = re.findall(r'\b1st|2nd|3rd|[04-9]th|1[1-9]th\b', f)
print('Cardinalities and Orders in the given file are')
print(cardinalities)
print(orders)
print('------------------------------------------------------------')

words = re.findall(r'\b[aeiouAEIOU][a-zA-Z]{3}\b', f)
print('Four letter words starting with vowels in the given file are')
print(words)