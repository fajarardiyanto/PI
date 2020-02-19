import csv

with open('./data_csv/laporan.csv', 'r') as csv_file:
     csv_reader = csv.DictReader(csv_file)

     for line in csv_reader:
         print(line)