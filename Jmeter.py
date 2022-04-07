import requests
from requests.structures import CaseInsensitiveDict
import pandas as pd

url = "https://raw.githubusercontent.com/prathapaparna/Linux-Shell/main/shebang.sh"


# If repo is private - we need to add a token in header:
headers = CaseInsensitiveDict()
headers["Authorization"] = "token TOKEN"

resp = requests.get(url, headers=headers)
'Requests:' in resp.text
print(resp.status_code)

# parser = create_parser('jmeter-result.jtl')

df = pd.read_csv('jmeter-result.jtl')
bool_cols = df.columns[df.dtypes == 'bool']

df[bool_cols] = df[bool_cols].replace({True: 'Yes', False: 'No'})
print(df)

df1 = df['success'].str.contains('Yes')
print('true')


