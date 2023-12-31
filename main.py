import pandas as pd
import os
save_path = os.path.join(os.getcwd(), '1.csv')

# Create a sample DataFrame
data = {'Column1': [1, 2, 3, 4], 'Column2': ['A', 'B', 'C', 'D']}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv(save_path, index=False)
