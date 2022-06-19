import pandas as pd

filename = r'C:\Users\OWNER\Documents\카카오톡 받은 파일\자연에서 자연스럽게 정답 이벤트 .xlsx'

df = pd.read_excel(filename, engine='openpyxl')

print(df)
df['이름']