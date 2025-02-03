import pandas as pd

url = "https://raw.githubusercontent.com/4GeeksAcademy/decision-tree-project-tutorial/main/diabetes.csv"

df = pd.read_csv(url)

df.to_csv('diabetes_data.csv', index=False)
print("Dataset saved as 'diabetes-data.csv'")