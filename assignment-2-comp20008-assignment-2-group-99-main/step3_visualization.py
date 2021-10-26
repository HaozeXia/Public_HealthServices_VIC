#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#the assumption of the regresssion is that the independent varaibles are independent.
#First need to check this one by one.We have 7 variables in total,GVA,income,labour,life pm2.5,population, umpoly.
#start with scatter plots between independent variables.


# In[29]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt


# In[30]:


import pandas as pd
GVA=pd.read_csv('A2data/GVA.csv').drop('Unnamed: 0', axis=1).set_index('YEAR')
Income=pd.read_csv('A2data/income.csv').drop('Unnamed: 0', axis=1).set_index('YEAR').iloc[4:18]
Labour=pd.read_csv('A2data/labour.csv').drop('Unnamed: 0', axis=1).set_index('YEAR').iloc[3:17]
LifeExp=pd.read_csv('A2data/Life expectancy.csv').drop('Unnamed: 0', axis=1).set_index('YEAR').iloc[3:17]
Air=pd.read_csv('A2data/air.csv').drop('Unnamed: 0', axis=1).set_index('YEAR').iloc[2:16]
Population=pd.read_csv('A2data/population.csv').drop('Unnamed: 0', axis=1).set_index('YEAR').iloc[3:17]
Unemployment=pd.read_csv('A2data/Unemployment.csv').drop('Unnamed: 0', axis=1).set_index('YEAR').iloc[3:17]
Recurrent=pd.read_csv('A2data/recurrent.csv').drop('Unnamed: 0', axis=1).set_index('YEAR').iloc[:14]


# In[ ]:





# In[ ]:





# In[31]:


#Now try to do the regression for NSW first.
NSW=pd.DataFrame({"GVA":GVA["NSW"],"Income":Income["NSW"],"Labor":Labour["NSW"],"LifeExp":LifeExp["NSW"],"Air":Air["NSW"],"Population":Population["NSW"],
"Unemployment":Unemployment["NSW"],"Recurrent":Recurrent["NSW"]})

VIC=pd.DataFrame({"GVA":GVA["VIC"],"Income":Income["VIC"],"Labor":Labour["VIC"],"LifeExp":LifeExp["VIC"],"Air":Air["VIC"],"Population":Population["VIC"],
"Unemployment":Unemployment["VIC"],"Recurrent":Recurrent["VIC"]})

QLD=pd.DataFrame({"GVA":GVA["QLD"],"Income":Income["QLD"],"Labor":Labour["QLD"],"LifeExp":LifeExp["QLD"],"Air":Air["NSW"],"Population":Population["QLD"],
"Unemployment":Unemployment["QLD"],"Recurrent":Recurrent["QLD"]})


QLD=pd.DataFrame({"GVA":GVA["QLD"],"Income":Income["QLD"],"Labor":Labour["QLD"],"LifeExp":LifeExp["QLD"],"Air":Air["NSW"],"Population":Population["QLD"],
"Unemployment":Unemployment["QLD"],"Recurrent":Recurrent["QLD"]})


SA=pd.DataFrame({"GVA":GVA["SA"],"Income":Income["SA"],"Labor":Labour["SA"],"LifeExp":LifeExp["SA"],"Air":Air["SA"],"Population":Population["SA"],
"Unemployment":Unemployment["SA"],"Recurrent":Recurrent["SA"]})


WA=pd.DataFrame({"GVA":GVA["WA"],"Income":Income["WA"],"Labor":Labour["WA"],"LifeExp":LifeExp["WA"],"Air":Air["WA"],"Population":Population["WA"],
"Unemployment":Unemployment["WA"],"Recurrent":Recurrent["WA"]})


TAS=pd.DataFrame({"GVA":GVA["TAS"],"Income":Income["TAS"],"Labor":Labour["TAS"],"LifeExp":LifeExp["TAS"],"Air":Air["TAS"],"Population":Population["TAS"],
"Unemployment":Unemployment["TAS"],"Recurrent":Recurrent["TAS"]})


NT=pd.DataFrame({"GVA":GVA["NT"],"Income":Income["NT"],"Labor":Labour["NT"],"LifeExp":LifeExp["NT"],"Air":Air["NT"],"Population":Population["NT"],
"Unemployment":Unemployment["NT"],"Recurrent":Recurrent["NT"]})

ACT=pd.DataFrame({"GVA":GVA["ACT"],"Income":Income["ACT"],"Labor":Labour["ACT"],"LifeExp":LifeExp["ACT"],"Air":Air["ACT"],"Population":Population["ACT"],
"Unemployment":Unemployment["ACT"],"Recurrent":Recurrent["ACT"]})


# In[33]:


import seaborn as sns
g1= sns.PairGrid(NSW)
g1.map(sns.scatterplot)
plt.savefig("NSW.png")


# In[34]:


g2=sns.PairGrid(VIC)
g2.map(sns.scatterplot)
plt.savefig("VIC.png")


# In[35]:


g3=sns.PairGrid(QLD)
g3.map(sns.scatterplot)
plt.savefig("QLD.png")


# In[36]:


g4=sns.PairGrid(SA)
g4.map(sns.scatterplot)
plt.savefig("SA.png")


# In[37]:


g5=sns.PairGrid(WA)
g5.map(sns.scatterplot)
plt.savefig("WA.png")


# In[38]:


g6=sns.PairGrid(TAS)
g6.map(sns.scatterplot)
plt.savefig("TAS.png")


# In[39]:


g7=sns.PairGrid(NT)
g7.map(sns.scatterplot)
plt.savefig("NT.png")


# In[40]:


g8=sns.PairGrid(ACT)
g8.map(sns.scatterplot)
plt.savefig("ACT.png")


# In[ ]:


#When we first get the data, we want to build multiple regression models for each area （NSW，VIC，QLD，SA，WA，TAS，NT，ACT）
#separately.
#However, the assumption for the multiple regression models is the independent variables are not highly correlated
#to each other. We plot the scatter plot for all pairs of independent variables for each area. It is obvious that 
#some independent variables are correlated to others For example, it seems like there exists a linear relationship 
#between labor and the population.
#Let us check it by computing the person coefficient.


# In[40]:


AreaList=["NSW","VIC","QLD","SA","WA","TAS","NT","ACT"]
for area in AreaList:
    current_labour=Labour[area].values
    current_population=Population[area].values
    print(area,np.corrcoef(current_labour,current_population)[0,1])


# In[ ]:


#The Pearson coefficients between population and labor in all areas are extremely high. Therefore, it is fair to conclude that these 
#two variables are not independent. Besides population and labor, it seems like there also exists a linear relationship between 
#labor and income. Therefore the assumption of multiple regression is not satisfied in this situation.
#There are  two methods to fix this problem:
#1. List all the combinations of independent variables and select the combinations that satisfy the independent assumption. Then create
#models based on all combinations and choose the one that gives the smallest total sum of squares.
#2. Using forward selection to avoid using dependent variables.

#However, the calculation requirements of the first method are extremely large. And for the second method, python does not have 
#packages to do the forward selections Automatically.
#Besides this, even we can build multiple regression models based on approximate independent variables, there is still one more 
#problem: Comparing with the sample size, the number of features is quite large. This may lead to imprecise parameter estimation.
#In order to solve all these problems, we decide to use the principal component analysis. It can avoid inappropriate independent 
#variables selection and reduce the dimension at the same time.


# In[ ]:


#Now let us do some visualization about the result.


# In[12]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
from numpy import arange

change = ['-10%','-5%','-1%','0','+1%','+5%',"+10%"]

Influence_cause_by_GVA= [0.08,2.49,2.56,2.49,2.50,2.49,2.49]
GVA_0change=[2.49,2.49,2.49,2.49,2.49,2.49,2.49]

Influence_cause_by_unemployment=[2.49,2.49,2.77,2.48,2.52,2.5,1.34]
unemployment_0change=[2.48,2.48,2.48,2.48,2.48,2.48,2.48]

Influence_cause_by_recurrent=[2.48,2.48,2.48,2.47,2.49,2.51,2.49]
recurrent_0change=[2.47,2.47,2.47,2.47,2.47,2.47,2.47]

Influence_cause_by_income=[2.48,2.48,2.51,2.46,2.49,2.49,4.25]
income_0change=[2.46,2.46,2.46,2.46,2.46,2.46,2.46]

Influence_cause_by_labour=[2.48,2.47,2.49,2.47,2.48,2.49,11.7]
labour_0change=[2.47,2.47,2.47,2.47,2.47,2.47,2.47]

Influence_cause_by_LifeExp=[2.49,2.48,2.46,2.48,2.45,2.49,13]
LifeExp_0change=[2.48,2.48,2.48,2.48,2.48,2.48,2.48]

Influence_cause_by_environment=[2.49,2.48,2.35,2.48,2.41,2.49,2.46]
environment_0change=[2.48,2.48,2.48,2.48,2.48,2.48,2.48]

Influence_cause_by_density=[2.49,2.48,2.22,2.49,2.51,2.48,2.47]
density_0change=[2.49,2.49,2.49,2.49,2.49,2.49,2.49]

Influence_cause_by_population=[2.49,2.49,2.5,2.49,2.5,2.48,2.48]
population_0change=[2.49,2.49,2.49,2.49,2.49,2.49,2.49]


# In[50]:


plt.bar(arange(len(Influence_cause_by_GVA)),Influence_cause_by_GVA,color="c")#draw graph
plt.xticks(arange(len(change)),change, rotation=30) #label the x terms
plt.plot(change,GVA_0change, "k", marker='.', ms=10, label="Y value without change GVA")
plt.legend()
plt.title('Influence cause by GVA')
plt.xlabel('GVA')
plt.ylabel('Y values')
plt.savefig("GVA.png")
plt.show()


# In[51]:


plt.bar(arange(len(Influence_cause_by_unemployment)),Influence_cause_by_unemployment,color="c")
plt.xticks(arange(len(change)),change, rotation=30) #label the x terms
plt.plot(change,unemployment_0change, "k", marker='.', ms=10, label="Y value without change unemloyment situation")
plt.legend()
plt.title('Influence cause by unemployment situation')
plt.xlabel('Unemployment')
plt.ylabel('Y values')
plt.savefig("unemployment.png")
plt.show()


# In[52]:


plt.bar(arange(len(Influence_cause_by_recurrent)),Influence_cause_by_recurrent,color="c")
plt.xticks(arange(len(change)),change, rotation=30) #label the x terms
plt.plot(change,recurrent_0change, "k", marker='.', ms=10, label="Y value without change recurrent")
plt.legend()
plt.title('Influence cause by recurrent')
plt.xlabel('Unemployment')
plt.ylabel('Y values')
plt.savefig("recurrent.png")
plt.show()


# In[53]:


plt.bar(arange(len(Influence_cause_by_income)),Influence_cause_by_income,color="c")
plt.xticks(arange(len(change)),change, rotation=30) #label the x terms
plt.plot(change,income_0change, "k", marker='.', ms=10, label="Y value without change income")
plt.legend()
plt.title('Influence cause by income')
plt.xlabel('Income')
plt.ylabel('Y values')
plt.savefig("income.png")
plt.show()


# In[54]:


plt.bar(arange(len(Influence_cause_by_labour)),Influence_cause_by_labour,color="c")
plt.xticks(arange(len(change)),change, rotation=30) #label the x terms
plt.plot(change,labour_0change, "k", marker='.', ms=10, label="Y value without change labour")
plt.legend()
plt.title('Influence cause by labour')
plt.xlabel('Labour')
plt.ylabel('Y values')
plt.savefig("labour.png")
plt.show()


# In[55]:


plt.bar(arange(len(Influence_cause_by_LifeExp)),Influence_cause_by_LifeExp,color="c")
plt.xticks(arange(len(change)),change, rotation=30) #label the x terms
plt.plot(change,LifeExp_0change, "k", marker='.', ms=10, label="Y value without change LifeExp")
plt.legend()
plt.title('Influence cause by LifeExp')
plt.xlabel('LifeExp')
plt.ylabel('Y values')
plt.savefig("LifeExp.png")
plt.show()


# In[56]:


plt.bar(arange(len(Influence_cause_by_environment)),Influence_cause_by_environment,color="c")
plt.xticks(arange(len(change)),change, rotation=30) #label the x terms
plt.plot(change,environment_0change, "k", marker='.', ms=10, label="Y value without change environment")
plt.legend()
plt.title('Influence cause by environment')
plt.xlabel('Environment')
plt.ylabel('Y values')
plt.savefig("Environment.png")
plt.show()


# In[57]:


plt.bar(arange(len(Influence_cause_by_density)),Influence_cause_by_density,color="c")
plt.xticks(arange(len(change)),change, rotation=30) #label the x terms
plt.plot(change,density_0change, "k", marker='.', ms=10, label="Y value without change density")
plt.legend()
plt.title('Influence cause by density')
plt.xlabel('Density')
plt.ylabel('Y values')
plt.savefig("density.png")
plt.show()


# In[58]:


plt.bar(arange(len(Influence_cause_by_population)),Influence_cause_by_population,color="c")
plt.xticks(arange(len(change)),change, rotation=30) #label the x terms
plt.plot(change,population_0change, "k", marker='.', ms=10, label="Y value without change population")
plt.legend()
plt.title('Influence cause by population')
plt.xlabel('Population')
plt.ylabel('Y values')
plt.savefig("population.png")
plt.show()

