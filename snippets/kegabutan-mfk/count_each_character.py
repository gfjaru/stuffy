import csv

karakter = {}

with open("kata_dasar_kbbi.csv") as kbbi_dasar:
  data = csv.reader(kbbi_dasar, delimiter=',')
  for row in data:
    for i in row[0]:
      if i in karakter:
        karakter[i] += 1
      else:
        karakter[i] = 1

print(karakter)
