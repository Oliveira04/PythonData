from IPython.display import display
import pandas as pd
#Passo 1: Importar base de dados
   #-> Usar pandas ( Trabalhar com Base de Dados)
  # -> plotly (trabalhar com graficos dinamicos)
table = pd.read_csv("cancelamentos.csv")
display(table)
#Passo 2: Vizualizar a base de dados
   #-> entender quais informações tem disponivel
   #-> procurar os problemas
   #-> colunas inuteis
   #-> informações vazias 
table = table.drop(columns= "CustomerID", axis=1)
display(table)
#Passo 3: Corrigir os erros da base de dados
   #-> valores vazios - excluir as linhas que têm valores vazios
   #->Jogar fora informações vazia -> Nan - Not a number - Info vazia 
display(table.info())
# valores vazios - excluir as linhas que têm valores vazios
table = table.dropna()
display(table.info())
#Passo 4: Análise dos cancelamentos
  # ->quantas pessoas cancelaram e quantas não cancelaram
display(table["cancelou"].value_counts())
# em percentual
display(table["cancelou"].value_counts(normalize= True))
display(table["cancelou"].value_counts(normalize= True).map("{:.1%}".format))

#Analise duração de contrato
display(table["duracao_contrato"].value_counts())
display(table["duracao_contrato"].value_counts(normalize= True).map("{:.1%}".format))
#analisando contrato mensal
display(table.groupby("duracao_contrato").mean(numeric_only = True))
#A media de cancelamento mensal é 1, ou seja quase todos os contratos foram cancelados
table = table[table["duracao_contrato"]!= "Monthly"]
display(table)
display(table["cancelou"].value_counts(normalize= True))
display(table["cancelou"].value_counts(normalize= True).map("{:.1%}".format))

#Analisando assinaturas
display(table["assinatura"].value_counts(normalize= True))
display(table.groupby("assinatura").mean(numeric_only = True))
#Passo 5: Análise da causa dos cancelamentos(como as colunas impactam no cancelamento?)

import plotly.express as px

# criar o grafico
for coluna in table.columns:
    grafic = px.histogram(table, x = coluna, color = "cancelou", width=600)
     # exibir o grafico
    grafic.show()
      # *Causas do cancelamento
    # Todos os cliente cancelaram no contrato mensal
    #  ! Descontos nos contratos Anual
    # Cancelamento do cliente com mais de 20 dias de atraso
   #   ! Criar um sistema de cobrança com 10 dias de atraso
    # Todos os clientes que ligaram mais de 4x pro call center, cancelaram
    #  ! Criar um sistema de alerta para clientes que ligaram mais de 2x


table = table[table["ligacoes_callcenter"]<5]
table = table[table["dias_atraso"]<=20]
display(table)
display(table["cancelou"].value_counts())
display(table["cancelou"].value_counts(normalize= True).map("{:.1}".format))