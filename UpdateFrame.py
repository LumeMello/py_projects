import pandas as pd
from datetime import datetime

file_path = "Entradas.xlsx"

df = pd.read_excel(file_path)

new_now = datetime.now()
print(df)

new_dt = pd.DataFrame(
    {
        "Day/Time": [
            new_now
        ]
    }
)

output_file_path = 'Entradas.xlsx'
pd.concat([df,new_dt], ignore_index=True).to_excel(output_file_path, index=False)
