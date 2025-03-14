#Testes do código
from tarefamd4 import extrai_coluna_csv, extrai_linha_txt

print("=== Testando extrai_coluna_csv ===")
valor_venda = extrai_coluna_csv(nome_arquivo='carros.csv', indice_coluna=1, tipo_dado='str')
print("Coluna valor_venda:", valor_venda)

pessoas = extrai_coluna_csv(nome_arquivo='carros.csv', indice_coluna=4, tipo_dado='int')
print("Coluna pessoas:", pessoas)

print("\n=== Testando extrai_linha_txt ===")
linha10 = extrai_linha_txt(nome_arquivo='musica.txt', numero_linha=10)
print("Linha 10:", linha10)