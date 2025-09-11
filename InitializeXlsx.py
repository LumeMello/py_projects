import pandas as pd
from datetime import datetime

now = datetime.now()

dt = pd.DataFrame(
    {
        "Day/Time": [
            now
        ]
    }

)
print(dt)
output_file_path = 'Entradas.xlsx'
dt.to_excel(output_file_path, index=False)
