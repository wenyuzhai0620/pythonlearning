import seaborn as sns
%matplotlib inline
iris = sns.load_dataset('iris')

sns.pairplot(iris)
#########grid#############
g = sns.PairGrid(iris)
#just a empty grid
g.map(plt.scatter)
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)

tips = sns.load_dataset('tips')
g = sns.FacetGrid(data=tips, col='time', row='smoker')
g.map(sns.distplot, 'total_bill')
g.map(plt.scatter, 'total_bill', 'tip')

#########Regression Plot#############

sns.lmplot(x='total_bill', y='tip', data = tips, hue= 'sex',markers = ['o','v'],
          scatter_kws={'s':100})
sns.lmplot(x='total_bill', y = 'tip', data = tips, col='day', hue = 'sex'. aspect = 0.6, size=8)

#######style and color##########
plt.figure(figsize=(12,3))
sns.set_style('ticks') #background, darkgrid/whitegrid
sns.set_context('poster', font_scale = 3) #set context of figure, notebook
sns.countplot(x='sex',data = tips)
sns.despine(left = True, bottom = tips)


