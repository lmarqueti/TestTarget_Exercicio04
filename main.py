'''
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
Escreva um programa na linguagem que desejar onde calcule o percentual de representação
que cada estado teve dentro do valor total mensal da distribuidora.
'''


faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total = sum(faturamento.values())

percentual = {}
for estado, valor in faturamento.items():
    percentual[estado] = (valor / total) * 100

for estado, valor in percentual.items():
    print(f'{estado}: {valor:.2f}%')