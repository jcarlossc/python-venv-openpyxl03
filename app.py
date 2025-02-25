# Importa módulos Openpyxl, Openpyxl.style e Openpyxl.Chart
from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.chart import BarChart, Reference

# Criar nova planilha
planilha = Workbook()
planilha_ativa = planilha.active
planilha_ativa.title = "Relatório"

# Adicionar cabeçalhos
planilha_ativa.append(["Produto", "Quantidade"])

# Adiciona produtos ao array produtos
produtos = [("Notebook", 50), 
            ("Mouse", 200), 
            ("Teclado", 150),
            ("Processador", 50),
            ("Monitor", 100)]

# Adiciona os produtos à planilha ativa
for produto, vendas in produtos:
    planilha_ativa.append([produto, vendas])

# Aplicar negrito ao cabeçalho
for cell in planilha_ativa["1:1"]:
    cell.font = Font(bold=True)

# Criar um gráfico de barras
chart = BarChart()
chart.title = "Quantidade de Produtos"
chart.x_axis.title = "Produtos"
chart.y_axis.title = "Quantidade"

# Definir os dados para o gráfico (valores numéricos)
data = Reference(planilha_ativa, min_col=2, min_row=2, max_row=len(produtos) + 1)
# Definir os rótulos do eixo X (nomes dos produtos)
categories = Reference(planilha_ativa, min_col=1, min_row=2, max_row=len(produtos) + 1)

# Adicionar dados e categorias ao gráfico
chart.add_data(data, titles_from_data=False)
chart.set_categories(categories)

# Inserir o gráfico na planilha (Célula "D1")
planilha_ativa.add_chart(chart, "D1")

# Salvar arquivo
planilha.save("planilhas/relatorio.xlsx")
print("Relatório criado com sucesso!")