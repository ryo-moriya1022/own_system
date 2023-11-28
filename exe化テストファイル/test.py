import csv

# CSVファイルの読み込み
with open('./test.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# CSVファイルへの書き込み
with open('./test.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['John', '30', 'New York'])
