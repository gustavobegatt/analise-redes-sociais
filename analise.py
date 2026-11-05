"""
====================================================================
Projeto: A influência das redes sociais na opinião política da sociedade
Objetivo: Investigar e mensurar a influência das redes sociais na opinião 
política e no comportamento dos cidadãos através de dados do Google Forms.
====================================================================
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dados.csv')

# Mapeamento dos nomes antigos para os novos nomes curtos
new_column_names = {
    'Carimbo de data/hora': 'Data/Hora',
    'Endereço de e-mail': 'Usuário',
    '\nQual rede social você mais utiliza para se informar ou consumir conteúdos sobre política no seu dia a dia? ': 'Rede Social',
    '\nEm média, quanto tempo por dia você passa consumindo conteúdos políticos ou debates sociais em plataformas digitais? ': 'Tempo Conteúdo Político',
    '\nEm uma escala de 1 a 5, quanto você acredita que os algoritmos de recomendação e postagens de influenciadores afetam a sua própria opinião sobre temas políticos? ': 'Influência Algoritmo',
    '\nVocê já mudou de opinião sobre um candidato, partido ou pauta política específica por causa de um conteúdo (vídeo, texto ou infográfico) que viu nas redes sociais? ': 'Mudou Opinião',
    '\nNa sua avaliação, quais são os fatores que tornam as redes sociais confiáveis ou prejudiciais para o debate político? ': 'Fatores Confiabilidade'
}

# Renomear as colunas do DataFrame
df = df.rename(columns=new_column_names)

# Exibir informações estruturais básicas
print("--- Primeiras Linhas ---")
print(df.head())

print("\n--- Informações do Dataset ---")
df.info()

print("\n--- Descrição Estatística ---")
print(df.describe())

# Verificar valores nulos e tratar
print("\n--- Valores Nulos por Coluna ---")
print(df.isnull().sum())

# Tratamento da coluna 'Rede Social' substituindo nulos
df['Rede Social'] = df['Rede Social'].fillna('Não informado')

# Média de influência do algoritmo agrupada por rede social
print("\n--- Média de Influência do Algoritmo por Rede Social ---")
print(df.groupby("Rede Social")["Influência Algoritmo"].mean())


# --------------------------------------------------------------------
# 2. Visualizações Gráficas
# --------------------------------------------------------------------

# Gráfico 1: Rede Social Mais Utilizada (Gráfico de Pizza)
social_media_counts = df['Rede Social'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(social_media_counts, labels=social_media_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Rede Social Mais Utilizada pelos Usuários')
plt.axis('equal')
plt.show()


# Gráfico 2: Influência Média do Algoritmo por Rede Social (Gráfico de Barras)
algorithm_influence_by_social_media = df.groupby("Rede Social")["Influência Algoritmo"].mean()

plt.figure(figsize=(10, 6))
algorithm_influence_by_social_media.plot(kind='bar')
plt.title('Influência Média do Algoritmo por Rede Social')
plt.xlabel('Rede Social')
plt.ylabel('Média de Influência do Algoritmo (1-5)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# Gráfico 3: Tempo de Consumo de Conteúdo Político (Gráfico de Linha)
time_consumption_counts = df['Tempo Conteúdo Político'].value_counts()

custom_order = [
    'Menos de 30 minutos.',
    '30 minutos a 1 hora.',
    '1 Hora.',
    '2 Horas.',
    'Mais de 3 horas.'
]

time_consumption_ordered = time_consumption_counts.reindex(custom_order, fill_value=0)

plt.figure(figsize=(10, 6))
time_consumption_ordered.plot(kind='line', marker='o')
plt.title('Número de Usuários por Tempo de Consumo de Conteúdo Político')
plt.xlabel('Tempo de Consumo Diário')
plt.ylabel('Número de Usuários')
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


"""
====================================================================
3. Conclusão da Análise:
====================================================================
A análise dos dados permitiu responder diretamente à pergunta central da 
pesquisa sobre o peso das plataformas digitais na política. Contrariando 
a ideia de um impacto absoluto, os resultados revelam que as redes sociais 
não exercem uma influência tão profunda na opinião política dos respondentes: 
a média de percepção da influência algorítmica ficou em torno de 2.94 
(numa escala de 1 a 5), indicando um efeito moderado. 

Embora plataformas como Instagram e TikTok estejam intensamente presentes 
no quotidiano, os dados demonstram que a maioria dos utilizadores não tem 
as suas convicções drasticamente alteradas por esse meio. Assim, conclui-se 
que as redes atuam muito mais como canais de circulação de notícias do 
que como fatores decisivos de mudança de opinião.
====================================================================
"""
