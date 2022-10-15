import requests
import pandas as pd

URL = 'https://servicodados.ibge.gov.br/api/v3/agregados'
response = requests.get(URL)

json_data = response.json()


df = pd.json_normalize(json_data, 'agregados')
df = pd.DataFrame.from_dict(json_data[0])
df.to_excel('dados_agregados.xlsx', index=False)