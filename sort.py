import csv
import glob

path = 'data/*.csv'
processed_rows = []

for filename in glob.glob(path):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['product'].strip().lower() == 'pink morsel':
                quantity = int(row['quantity'])
                price = float(row['price'].replace('$', '').replace(',', ''))
                sales = quantity * price

                processed_rows.append({
                    'sales': f'${sales:.2f}',
                    'date': row['date'],
                    'region': row['region']
                })

header = ['sales', 'date', 'region']

with open('formatted_output.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(processed_rows)
