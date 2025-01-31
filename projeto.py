#Dados sobre o sono de 62 mamíferos 

#As conclusões desses dados trabalhados estão presentes no artigo "Sleep in Mammals: Ecological and Constitutional Correlates" by Allison, T. and Cicchetti, D. (1976), Science, November 12, vol. 194, pp. 732-734. 
#Para as conclusões, os autores do artigo citado utilizaram variáveis como: 'species of animal', 'body weight in kg', 'brain weight in g', 'slow wave ("nondreaming") sleep (hrs/day) 'paradoxical ("dreaming") sleep (hrs/day)', 'total sleep (hrs/day) (sum of slow wave and paradoxical sleep)', 'maximum life span (years)', 'gestation time (days) ', 'predation index (1-5) 1 = minimum (least likely to be preyed upon) 5 = maximum (most likely to be preyed upon) ', 'sleep exposure index (1-5) 1 = least exposed (e.g. animal sleeps in a well-protected den) 5 = most exposed' e 'overall danger index (1-5) (based on the above two indices and other information) 1 = least danger (from other animals) 5 '.


#Importações utilizadas:
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
#from sklearn.model_selection import train_test_split
#from sklearn.metrics import r2_score
#from sklearn.feature_selection import SelectKBest, chi2
#from sklearn.feature_selection import chi2
#from sklearn.datasets import load_digits
#from sklearn.feature_selection import f_classif




#Upload do csv:
dtsleep =  pd.read_csv(r'C:\Users\Usuario\Downloads\sleepdata.csv')
                       
#Visualização das 5 primeiras linhas no dataset:
dtsleep.head()
        
#Uso da função describe() para observar: Min, Max, Mean...
dtsleep.describe()

#Utilizaão do "dtpes" para observar os tipos(int, float, str):
dtsleep.dtypes

#Soma do total de valores nulos para verificar a existência desses
dtsleep.isnull().sum()


#Verificação dos valores duplicados e exclusão desses valores
duplicadas_colunas = dtsleep.duplicated()
print(duplicadas_colunas)

dtsleep.drop_duplicates(inplace=True)


#Busca por valores ausentes ou  com "?" para transformá-los em "np.nan"

dtsleep.replace('?', np.nan, inplace=True)

#Preenchimento dos valores NaN com 0
dtsleep['max_life_span'] = dtsleep['max_life_span'].fillna(0)
dtsleep['gestation_time'] = dtsleep['gestation_time'].fillna(0)
dtsleep['total_sleep'] = dtsleep['total_sleep'].fillna(0)

#Transformação da coluna 'total_sleep' para float e posteriormente int
dtsleep['total_sleep'] = dtsleep['total_sleep'].astype(float)
dtsleep['total_sleep'] = dtsleep['total_sleep'].astype(int)


# Divisão das variáveis em X e y
X = dtsleep.drop('total_sleep', axis=1)
y = dtsleep['total_sleep']

# Separação em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Seleção de características usando f_classif 
select_k_best = SelectKBest(score_func=f_classif, k=3)
X_train_k_best = select_k_best.fit_transform(X_train, y_train)

# Exbição das características selecionadas
selected_features = X_train.columns[select_k_best.get_support()]
print("Selected features:", selected_features)

#Observação das correlações

print(dtsleep.corr())

#Exposição das correlações por meio do hatmap
corrmat = dtsleep.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(20,20))
g=sns.heatmap(dtsleep[top_corr_features].corr(),annot=True,cmap="RdYlGn")
plt.show()


