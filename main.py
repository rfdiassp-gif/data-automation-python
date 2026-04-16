import csv

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    values = [int(row['value']) for row in reader]

average = sum(values) / len(values)

print(f"Average value: {average}")