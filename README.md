# Projeto Dados Sleep
Análise de dados sobre os fatores que influenciam o sono de 62 espécies de mamíferos, como o peso do cérebro, o índice de predação, o tempo de gestação, dentre outros

# Fonte dos dados analisados

 Os dados usados nessa análise foram retirados do artigo "Sleep in Mammals: Ecological and Constitutional Correlates" de Allison, T. e Cicchetti, D. (1976), Science, November 12, vol. 194, pp. 732-734, disponíveis em: "https://www.kaggle.com/datasets/mathurinache/sleep-dataset/data". 
 O artigo em questão estuda sobre uma série de variáveis de 62 espécies de animais e o quanto que cada uma dessas características influencia na durabilidade do sono desses animais mamíferos.

# Objetivo do dataset

 O objetivo do projeto é mostrar de forma pragmática a resposta para os seguintes questionamento: "Quais da 10 variáveis estudadas mais influenciam no sono dessas espécies? Essas principais variáveis possuem uma correlação positiva ou negativa com a variável principal('total_sleep" = total de sono) ?".


# Variáveis do "Sleep Data":

species of animal = ESPÉCIE DO ANIMAL
body weight in kg = PESO DO CORPO EM KG
brain weight in g = PESO DO CÉREBRO EM G
slow wave ("nondreaming") sleep (hrs/day) = SONO DE ONDAS LENTAS(SEM SONHAR) (HRS/DIA)
paradoxical ("dreaming") sleep (hrs/day) = SONO PARADOXO(SONHANDO) (HRS/DIA)
total sleep (hrs/day) (sum of slow wave and paradoxical sleep) = SONO TOTAL(HRS/DIA) (SOMA DO SONO DE ONDAS LENTAS E SONO PARADOXO)
maximum life span (years) = VIDA ÚTIL MÁXIMA(ANOS)
gestation time (days) = TEMPO DE GESTAÇÃO(DIAS)
predation index (1-5) 1 = minimum (least likely to be preyed upon) 5 = maximum (most likely to be preyed upon) = INDEX DE PREDAÇÃO (1-5) 1 = MÍNIMO(MESMOS PROVÁVEL DE SER PREDADO) 5 = MÁXIMO(MAIS PROVÁVEL DE SER PREDADO)
sleep exposure index (1-5) 1 = least exposed (e.g. animal sleeps in a well-protected den) 5 = most exposed = ÍNDICE DE EXPOSIÇÃO DE SONO(1-5) 1 = MENOS EXPOSTO( ANIMAIS QUE DORMEM MAIS PROTEGIDOS) 5 = MAIS EXPOSTOS
overall danger index (1-5) (based on the above two indices and other information) 1 = least danger (from other animals) 5 = most danger (from other animals) = ÍNDICE DE PERIGO GERAL(1-5) (BASEADO ACIMA DOS DOIS ÍNDICES E OUTRAS INFORMAÇÕES) 1 = MENOS PERIGO(DE OUTROS ANIMAIS) 5 = MAIS PERIGO(DE OUTROS ANIMAIS)

 
# Bibliotecas Python importadas para análise dos dados:

Pandas: análise e manipulação de dados
Numpy: computação numérica
Matplotlib: criação de gráficos
Seaborn: visualização de dados e estatística
Scikit-learn: aplicação de Machine Learning


# Análise

1) Objetivo: Definir quais da 10 variáveis estudadas possuem uma maior relevância para se obter o total de horas de sono dessas espécies e verificar se essas  principais atribuições possuem uma correlação positiva ou negativa com a variável principal('total_sleep" = total de sono)

2) Limpeza e pré-processamento: para que todos os dados sejam precisos, completos e formatados adequadamente, foram realizos os processos de:
-Panaroma geral dos dados por meio das funções 'dtsleep.head()', 'dtsleep.describe()' e 'dtsleep.dtypes'
-Limpeza dos dados por meio da verificaão de valores nulos('dtsleep.isnull().sum()')
-Observação de valores duplicados e exclusão('dtsleep.drop_duplicates(inplace=True)')
-Substituição de valores "?" por "Nan"(dtsleep.replace('?', np.nan, inplace=True)
-Preenchimento de valores NaN com 0 para que não haja problema nas métricas que não trabalham com NaN((dtsleep['max_life_span'] = dtsleep['max_life_span'].fillna(0))
-Transformação da coluna 'total_sleep' para int para que não houvesse problemas com certas funcionalidades que aceitam apenas valores int(dtsleep['total_sleep'] = dtsleep['total_sleep'].astype(float)) e (dtsleep['total_sleep'] = dtsleep['total_sleep'].astype(int) ))

3) Machine Learning:
- Criação de Treino e Teste:
Serve para treinar o modelo e comprovar se ele realmente funciona
Separa-se em X(X = dtsleep.drop('total_sleep', axis=1)) e Y(y = dtsleep['total_sleep'])
X representa os dados de entrada,ou seja, todos os atributos, exceto o que irá para o "y"('total_sleep)
Y representa os dados de saída, os resultados esperados, ou seja, o "total_sleep" para que posteriormente seja obtida a relação entre as demais variáveis e esse tempo total de sono

- Execução do Treino e Teste:
"X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)"
O "test_size" representa que 20% do modelo foi usado para teste
O "random_state" garante que a mesma randomização seja usada cada vez que você executa o código

- Uso do SelectKBest
select_k_best = SelectKBest(score_func=f_classif, k=3)
Seleciona o quão bem cada recurso se relaciona com a variável alvo, nesse caso é o "total_sleep"
Dessa forma, poderá ser obtido a resposta dos atributos que mais influenciam na quantidade total de horas dormidas pelos 62 mamíferos

- Exibição das características selecionadas
selected_features = X_train.columns[select_k_best.get_support()]
print("Selected features:", selected_features)


4)Conclusão:

Relações entre todos os atributos e a variável alvo('total_sleep')
 ![Image](https://github.com/user-attachments/assets/e4c1ee99-8e0b-4d1f-8aad-686c35f8c004)

 Ao se utilizar o método SelectKBest, obteve-se o resultado de que as variáveis que mais influenciam na quantidade total de horas de sono das 62 espécies são:'Gestation_time' , 'Sleep_exposure_index' e 'Danger_index'.
 Dessa forma, entende-se que o tempo de gestação dos indivíduos, o índice de exposição durante o sono e o índice de perigo são os fatores que mais vão fazer o tempo de sono das espécies serem maiores ou menores.
 Além disso, através do heatmap exibido na imagem acima, percebe-se diferentes correlações. Nesse sentido, os "quadrados" do gráfico que possuem a cor vermelha mais escura representam as correlações mais negativas e os "quadrados" do gráfico que possuem a cor de verde mais escuro, representam as correlações mais positivas.
 Para que fique mais claro, deve-se entender que uma correlação positiva indica duas variáveis que "seguem o mesmo sentido", ou seja, quando uma sobe, a outra sobe; quando uma desce, a outra desce.
 Sendo assim, pode-se inferir que em relação ao 'total_sleep', as variáveis que possuem a maior correlação positiva são: 'body_weight', 'brain_weight' e 'max_life_span'. Então, quanto maior o peso do corpo, o peso do cérebro e a vida útil máxima, também maior será a quantidade de horas de sono.
 Em contrapartida, quanto maior o tempo de gestação, o índice de exposição durante o sono e o índice de perigo, menor será a quantidade de sono desses mamíferos.
 Portanto, os questionamentos apresentados foram respondidos por meio de uma análise de dados que envolve tanto o processo de limpeza e processamento, quanto o uso do Machine Learning para se verificar os atributos que mais influenciam no resultado final: o tempo total de sono dos 62 animais.


   

