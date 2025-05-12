**Gerando Grafico:  Gênero**     
import plotly.graph_objects as go     
Gênero = ['Feminino','Masculino','Outro',"Prefiro não informar"]    
Quantidade = [687, 2206, 4, 10]   
cores_marcadores = ["Navy", "IndianRed", "Yellow", "MediumSeaGreen"]   
fig = go.Figure(data = go.Pie(labels = Gênero,   
                             values = Quantidade,   
                              marker_colors = cores_marcadores,))   
fig.update_traces(textposition = "outside", textinfo = "percent+label")   
fig.show()      

**Gerando Grafico:  Faixa de Idade**     
import plotly.graph_objects as go   
Idade = ['17-21','22-24','25-29','30-34', '35-39','40-44', '45-49', '50-54', "55+"]   
Quantidade = [87, 337, 1084, 767, 367, 166, 58, 28, 13]   
cores_marcadores = ["khaki", "MediumSeaGreen", "crimson", "limegreen", "tomato","Aqua", "Navy", "Purple", "Gray"]   
fig = go.Figure(data = go.Pie(labels = Idade,   
                             values = Quantidade,   
                              marker_colors = cores_marcadores,))   
fig.update_traces(textposition = "outside", textinfo = "percent+label")   
fig.show()     

**Gerando Grafico:  Faixa  Salarial**    
import plotly.graph_objects as go     
Salarial = ['-1.000','1.000-2.000','2.001-3.000','3.001-4.000', '4.001-6.000','6.001-8.000', '8.001-12.000', '12.001-16.000', '16.001-20.000', '20.001-25.000', '25.001-30.000', '30.001-40.000', "40.001+"]   
Quantidade = [14, 137, 163, 239, 542, 447, 733, 378, 122, 61, 30, 27, 14]    
cores_marcadores = ["khaki", "MediumSeaGreen", "crimson", "limegreen", "tomato","Aqua", "Navy", "Purple", "Gray", "Lightsalmon", "Green", "Maroon", "Violet"]     
fig = go.Figure(data = go.Pie(labels = Salarial,   
                             values = Quantidade,    
                              marker_colors = cores_marcadores,))   
fig.update_traces(textposition = "outside")   
fig.show()   

**Gerando Grafico:  Nível de Experiência**   
import plotly.graph_objects as go   
Experiência = ['-1','1-2','3-4','4-5', '5-6','7-10', '10+', "Não possui"]  
Quantidade = [282, 897, 788, 293, 229, 212, 198, 8]  
cores_marcadores = ["khaki", "MediumSeaGreen", "crimson", "limegreen", "tomato","Aqua", "Navy", "Purple"]   
fig = go.Figure(data = go.Pie(labels = Experiência,   
                             values = Quantidade,  
                              marker_colors = cores_marcadores,))   
fig.update_traces(textposition = "outside", textinfo = "percent+label")   
fig.show()    
  
**Gerando Grafico:  Ciêntista por Estado**   
import matplotlib.pyplot as plt  
x = ['AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'SC', 'SP', 'SE', 'TO']   
y = [17, 2, 15, 71, 77, 92, 67, 50, 9, 29, 13, 321, 18, 38, 265, 67, 8, 258, 24, 173, 4, 144, 1126, 16, 3]   
eixox = "Estados"   
eixoy = "Quantidade"  
plt.barh(x, y, label='Estados', height=0.6)   
plt.xlabel('Quantidade')   
plt.ylabel('Estados')   
plt.show()     

**Gerando Grafico:  Raça/Etnia/Cor**    
import plotly.graph_objects as go  
Cor = ['Amarela','Branca','Indígena','Outra','Parda','Prefiro não informar',"Preta"]   
Quantidade = [84, 1876, 7, 5, 700, 22, 213]   
cores_marcadores = ["Navy", "Teal", "Yellow", "Chocolate", "Crimson", "limegreen", "MediumPurple"]   
fig = go.Figure(data = go.Pie(labels = Cor,  
                             values = Quantidade,  
                              marker_colors = cores_marcadores,))  
fig.update_traces(textposition = "outside", textinfo = "percent+label")   
fig.show()     
  
**Gerando Grafico:  Ciêntistas por Região**   
import plotly.graph_objects as go   
Região = ['Centro-oeste','Nordeste','Norte','Sudeste',"Sul"]    
Quantidade = [184, 327, 42, 1772, 582]   
cores_marcadores = ["Navy", "IndianRed", "Yellow", "MediumSeaGreen", "Purple"]   
fig = go.Figure(data = go.Pie(labels = Região,   
                             values = Quantidade,   
                              marker_colors = cores_marcadores,))  
fig.update_traces(textposition = "outside", textinfo = "percent+label")   
fig.show()   

**Gerando Grafico:  Nível de Ensino**     
import plotly.graph_objects as go   
Ensino = ['Doutorado ou Phd','Estudante Graduação','Mestrado','Graduação/Bacharelado',"Pós-graduação"]    
Quantidade = [112, 363, 373, 1130, 929]   
cores_marcadores = ["Navy", "IndianRed", "Yellow", "MediumSeaGreen", "Purple"]   
fig = go.Figure(data = go.Pie(labels = Ensino,   
                             values = Quantidade,   
                              marker_colors = cores_marcadores,))   
fig.update_traces(textposition = "outside", textinfo = "percent+label")   
fig.show()     

**Gerando Grafico:  Situação Empresarial**    
import plotly.graph_objects as go   
Situação = ['Empregado (CNPJ)','Empregado (CLT)','Estagiário','Freelancer','Servidor Público','Prefiro não informar',"Empresa de fora do Brasil"]    
Quantidade = [264, 2326, 168, 15, 51, 3, 80]   
cores_marcadores = ["Navy", "Teal", "Yellow", "Chocolate", "Crimson", "limegreen", "MediumPurple"]   
fig = go.Figure(data = go.Pie(labels = Situação,   
                             values = Quantidade,   
                              marker_colors = cores_marcadores,))   
fig.update_traces(textposition = "outside", textinfo = "percent+label")   
fig.show()     

**Gerando Grafico:  Cargo**   
import plotly.graph_objects as go    
Cargo = ['Analista de BI','Analista de Dados','Analista de Inteligência de Mercado','Cientista de Dados', 'Data Product Manager','Administrador de Banco de Dados', 'Engenheiro de Dados/Arquiteto de Dados', 'Engenheiro de Machine Learning',"Estatístico"]     
Quantidade = [489, 874, 37, 665, 79, 19, 651, 72, 21]    
cores_marcadores = ["khaki", "MediumSeaGreen", "Gray","Aqua", "Navy", "Purple", "tomato", "Lightsalmon", "Violet"]    
fig = go.Figure(data = go.Pie(labels = Cargo,    
                             values = Quantidade,    
                              marker_colors = cores_marcadores,))    
fig.update_traces(textposition = "outside", textinfo = "percent+label")    
fig.show()    
  
**Gerando Grafico:  Área de Formação**    
import plotly.graph_objects as go    
Formação = ['Ciências Biológicas','Ciências Sociais','Computação','Economia', 'Estatística','Marketing', 'Outra opção', 'Outras Engenharias', "Química / Física"]    
Quantidade = [58, 46, 1231, 397, 230, 56, 139, 661, 89]    
cores_marcadores = ["khaki", "MediumSeaGreen", "crimson", "limegreen", "tomato","Aqua", "Navy", "Purple", "Gray"]     
fig = go.Figure(data = go.Pie(labels = Formação,    
                             values = Quantidade,    
                              marker_colors = cores_marcadores,))    
fig.update_traces(textposition = "outside", textinfo = "percent+label")    
fig.show()     

