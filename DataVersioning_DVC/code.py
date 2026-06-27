import pandas as pd
import os

data = {
    'Name' : ['Subham', 'Nikesh', 'Jitul', 'Subhra', 'Denkhw', 'Barun'],
    'age' : [19, 19, 21, 20, 20, 22],
    'City' : ['Rowta', 'Thelamara', 'Basugaon', 'Basugaon', 'Bongaigaon', 'Tezpur']
}

df = pd.DataFrame(data)

dir = 'DataVersioning_DVC/data'

os.makedirs(dir, exist_ok=True)

filepath = os.path.join(dir, 'sample_data.csv')

df.to_csv(filepath, index=False)


print(df)
print(f"File saved successfully to {filepath}")