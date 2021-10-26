'''
    This is the third part of this project, which we cluster the data, to divide states in to two type
    The first step is read the data from csv file, and then normalise them. since different data have different
characteristic, here we use different method for different factors.
    The second step is the clustering (both k-means and hierarchical clustering)
    Finally we plot the result of the hierarchical clustering (when threshold of euclidean distance is 2,
two clustering algorithm have the same result).
'''
# part one: read data, and normalise them
import numpy as np
import math
raw_data = np.loadtxt(open("cluster_new_data_only.csv", "rb"), delimiter = ",", skiprows = 0)
normalized_data=raw_data
# we normalize the data row by row, the first row is the income
normalized_data[0]=(raw_data[0]-min(raw_data[0]))/(max(raw_data[0])-min(raw_data[0]))
# the second row is the PM2.5
normalized_data[1]=(raw_data[1]-min(raw_data[1]))/(max(raw_data[1])-min(raw_data[1]))
# the third row is the total population, this will be normalized after log func
population=raw_data[2]
for i in range(len(population)):
    population[i]=math.log(float(population[i]))
normalized_data[2]=(population-min(population))/(max(population)-min(population))
# the forth row is the unemployment
normalized_data[3]=(raw_data[3]-min(raw_data[3]))/(max(raw_data[3])-min(raw_data[3]))
# the fifth row is the population density
normalized_data[4]=(raw_data[4]-min(raw_data[4]))/(max(raw_data[4])-min(raw_data[4]))
# the sixth row is the GVA, this will be normalized after log func
gva=raw_data[5]
for i in range(len(gva)):
    gva[i]=math.log(float(gva[i]))
normalized_data[5]=(gva-min(gva))/(max(gva)-min(gva))
# the seventh row is the labour
labour=raw_data[6]
for i in range(len(labour)):
    labour[i]=math.log(float(labour[i]))
normalized_data[6]=(labour-min(labour))/(max(labour)-min(labour))
# the eighth row is the hospital recurrent
recurrent=raw_data[7]
for i in range(len(recurrent)):
    recurrent[i]=math.log(float(recurrent[i]))
normalized_data[7]=(recurrent-min(recurrent))/(max(recurrent)-min(recurrent))

# second step, clustering, and display
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist
input_label=['NSW','VIC','QLD','SA','WA','TAS','NT','ACT']
inputs = np.array([normalized_data[:,0],normalized_data[:,1],normalized_data[:,2],normalized_data[:,3],normalized_data[:,4],normalized_data[:,5],normalized_data[:,6],normalized_data[:,7]])
d = pdist(inputs, 'euclidean')
hc2 = linkage(d, 'complete')
dendrogram(hc2, labels=input_label)
plt.title('Result of Hierarchical Clustering')
plt.show()

from sklearn.cluster import KMeans

clusters = KMeans(n_clusters=2).fit(inputs)
print(clusters.cluster_centers_)
print("the states label are:")
print(input_label)
print("and the result of k-means is:")
print(clusters.labels_)