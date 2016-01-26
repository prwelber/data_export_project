import csv
import sys

csv.field_size_limit(sys.maxsize)

with open('master_no_issues.csv', newline='') as f:
  reader = csv.reader(f)
  for row in reader:
      print(row[6])
