import pandas as pd

df = pd.read_excel('Klabin - EF.xlsx', sheet_name='BD', header=[3])


# df = df[df['Quant.'].notnull()]
for c in range(1, 8):
    df = df.drop(df.columns[[c+16]], axis=1, errors='ignore')
    df = df.drop(df.columns[[c + 16]], axis=1, errors='ignore')
for c in range(1, 15):
    df = df.drop(df.columns[[23]], axis=1, errors='ignore')

# TRASNPOR COLUNAS
df1 = pd.melt(df, id_vars=['Unnamed: 0', 'GRD', 'Isométrico', 'Folha', 'revisão', 'Linha', 'Item', 'Cód Material', 'Descrição Material', 'material', 'DN', 'unid.', 'Quant.', 'Peso', 'p/unid.', 'PEND.'])

# RENOMEAR DADOS
df1['variable'] = df1['variable'].map({'prev.':'spool 1','prev..1':'spool 2','prev..2': 'spool 3', 'prev..3': 'spool 4', 'prev..4': 'spool 5', 'prev..5': 'spool 6', 'prev..6': 'spool 7'}, na_action=None)

df1 = df1[df1['value'].notnull()]



df1.to_excel('Alterado.xlsx')


