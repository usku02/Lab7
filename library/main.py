# import csv
# with open('customer.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)     # each line as dict
#     for row in csv_reader:
#         print(row)

from time import  strftime
from time import localtime
print(strftime('%Y-%m-%d', localtime()))