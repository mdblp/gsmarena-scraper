import pandas as pd
from os.path import exists 

def getColumns(filename):
    columns = []
    with open(filename) as file:
        for line in file:
            cur = line.rstrip().split(';')
            columns.extend(cur)
    return columns


columnsFile = 'columns.txt'
columns = getColumns(columnsFile)
print(columns)

brands = ['apple', 'lg', 'motorola', 'google', 'samsung', 'sony']
for brand in brands:
    phone = 'Exports/' + brand + '-phones-export.csv'
    if exists(phone):
        print("Processing %s" % brand)
        # phone_reordered = os.path.splitext(phone)[0] + '.csv'
        phone_reordered = 'Exports/' + brand + '-phones-reordered.csv'
        df = pd.read_csv(phone, delimiter=";")
        df_reduced = df[df.columns.intersection(columns)]

        df_reorder = df_reduced[columns]
        df_reorder.sort_values(by=['Name'], ascending=False)
        df_reorder.to_csv(phone_reordered, sep=";")
    else:
        print("%s does not exist" % brand)

# df_reorder.to_csv('/path/to/sample_reorder.csv', index=False)


