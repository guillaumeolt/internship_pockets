# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:39:10 2020

@author: Guillaume
"""
import os
import pandas as pd
import numpy as np
from math import *
import random
import time
#kmeans
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster.kmeans import kmeans, kmeans_visualizer
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
from pyclustering.utils.metric import type_metric, distance_metric, euclidean_distance
from pyclustering.cluster.elbow import elbow
#
path_data_ph="../data/dt_72clean-50.csv"
dt = pd.read_csv(path_data_ph, sep=',', index_col = 0)
#dt.index.values
names_dt = dt.index.values
#dt = dt.values.tolist()
#regession listique values
Intercept = 6.61543
hydrophobic_kyte = -0.52657#vec1[56]-vec2[56]
p_aromatic_residues = -0.26214#vec1[69]-vec2[69]
p_charged_residues = -0.42272#vec1[6]-vec2[6]
p_negative_residues = 0.33210#vec1[23]-vec2[23]
p_positive_residues = 0.59123#vec1[10]-vec2[10]
charge = -0.73920#vec1[24]-vec2[24]
p_Nlys_atom = -0.26117#vec1[15]-vec2[15]
p_Ocoo_atom = -0.16479#vec1[67]-vec2[67]
p_small_residues = -0.16480#vec1[7]-vec2[7]
p_C_atom = 0.19381#vec1[64]-vec2[64]
p_nitrogen_atom = -0.36986#vec1[9]-vec2[9]
RADIUS_HULL = -3.33198#vec1[31]-vec2[31]
SURFACE_HULL = -3.57145#vec1[73]-vec2[73] 
DIAMETER_HULL = 1.10726#vec1[49]-vec2[49]
VOLUME_HULL = 2.46588#vec1[28]-vec2[28]
RADIUS_CYLINDER = 1.07161#vec1[3]-vec2[3]
C_RESIDUES = -0.65951#vec1[63]-vec2[63]
PSI = -0.18916#vec1[58]-vec2[58]
PCI = 0.16018#vec1[12]-vec2[12]
INERTIA_2 = -0.32137#vec1[18]-vec2[18]
INERTIA_3 = -0.15445#vec1[70]-vec2[70]
A = -0.16218#vec1[32]-vec2[32]
C = -0.34735#vec1[34]-vec2[34]
D = -0.15076#vec1[36]-vec2[36]
G = -0.43486#vec1[37]-vec2[37]
F = -0.18449#vec1[38]-vec2[38]
I = -0.30728#vec1[39]-vec2[39]
H = -0.27257#vec1[40]-vec2[40]
K = -0.27611#vec1[41]-vec2[41]
M = -0.27610#vec1[42]-vec2[42]
L = -0.34013#vec1[43]-vec2[43]
Q = -0.11223#vec1[45]-vec2[45]
P = -0.11730#vec1[46]-vec2[46]
S = -0.30554#vec1[47]-vec2[47]
R = -0.22685#vec1[48]-vec2[48]
T = -0.30320#vec1[50]-vec2[50]
W = -0.15142#vec1[51]-vec2[51]
Y = -0.11486#vec1[53]-vec2[53]

def descriptors_similarity(vec1, vec2):
    sim = Intercept + \
    hydrophobic_kyte * sqrt((vec1[56]-vec2[56])**2) + \
    p_aromatic_residues * sqrt((vec1[69]-vec2[69])**2) + \
    p_charged_residues * sqrt((vec1[6]-vec2[6])**2) + \
    p_negative_residues *sqrt((vec1[23]-vec2[23])**2) + \
    p_positive_residues *sqrt((vec1[10]-vec2[10])**2) + \
    charge *sqrt((vec1[24]-vec2[24])**2) + \
    p_Nlys_atom *sqrt((vec1[15]-vec2[15])**2) + \
    p_Ocoo_atom *sqrt((vec1[67]-vec2[67])**2) + \
    p_small_residues *sqrt((vec1[7]-vec2[7])**2) + \
    p_C_atom *sqrt((vec1[64]-vec2[64])**2) + \
    p_nitrogen_atom *sqrt((vec1[9]-vec2[9])**2) + \
    RADIUS_HULL *sqrt((vec1[31]-vec2[31])**2) + \
    SURFACE_HULL *sqrt((vec1[73]-vec2[73])**2) + \
    DIAMETER_HULL *sqrt((vec1[49]-vec2[49])**2) + \
    VOLUME_HULL *sqrt((vec1[28]-vec2[28])**2) + \
    RADIUS_CYLINDER *sqrt((vec1[3]-vec2[3])**2) + \
    C_RESIDUES *sqrt((vec1[63]-vec2[63])**2) + \
    PSI *sqrt((vec1[58]-vec2[58])**2) + \
    PCI *sqrt((vec1[12]-vec2[12])**2) + \
    INERTIA_2 *sqrt((vec1[18]-vec2[18])**2) + \
    INERTIA_3 *sqrt((vec1[70]-vec2[70])**2) + \
    A *sqrt((vec1[32]-vec2[32])**2) + \
    C *sqrt((vec1[34]-vec2[34])**2) + \
    D *sqrt((vec1[36]-vec2[36])**2) + \
    G *sqrt((vec1[37]-vec2[37])**2) + \
    F *sqrt((vec1[38]-vec2[38])**2) + \
    I *sqrt((vec1[39]-vec2[39])**2) + \
    H *sqrt((vec1[40]-vec2[40])**2) + \
    K *sqrt((vec1[41]-vec2[41])**2) + \
    M *sqrt((vec1[42]-vec2[42])**2) + \
    L *sqrt((vec1[43]-vec2[43])**2) + \
    Q *sqrt((vec1[45]-vec2[45])**2) + \
    P *sqrt((vec1[46]-vec2[46])**2) + \
    S *sqrt((vec1[47]-vec2[47])**2) + \
    R *sqrt((vec1[48]-vec2[48])**2) + \
    T *sqrt((vec1[50]-vec2[50])**2) + \
    W *sqrt((vec1[51]-vec2[51])**2) + \
    Y *sqrt((vec1[53]-vec2[53])**2)
    return 1-exp(sim)/(1+exp(sim))

#tranform data to list
names_dt = dt.index.values
dt = dt.values.tolist()
#


print(descriptors_similarity(dt[0],dt[1]))
Seeds = [5,10,20,30,40,50,60,70,80,90,100,200,300,400,500,600,700,800,900,1000]
for Nseeds in Seeds:
    print("----"+str(Nseeds)+"----")
    #
    initial_medoids = [random.randint(0,len(names_dt)) for i in range(Nseeds)]
    #
    metric = distance_metric(type_metric.USER_DEFINED, func= descriptors_similarity)
    #
    #initial_medoids = kmedoids_plusplus_initializer(dt, 8).initialize()
    # Create instance of K-Means algorithm with prepared centers.
    kmedoids_instance = kmedoids(dt, initial_medoids, metric=metric, itermax = 10)
    # Run cluster analysis and obtain results.
    
    start = time.time()
    print("hello")
    kmedoids_instance.process()
    end = time.time()
    print(end - start)
    #
    clusters = kmedoids_instance.get_clusters()
    final_medoids = kmedoids_instance.get_medoids()
    #final_centers = kmedoids_instance.get_centers()
    # run cluster analysis and obtain results
    #
    #names_dt[clusters[0]]
    #
    #for i in range(len(clusters)):
    #    print(len(clusters[i]))
        
    #SSE (Sum Square Error != Iintra)
    SSE = np.zeros(len(clusters))
    for i in range(len(clusters)):
        for j in range(len(clusters[i])):
            SSE[i] = SSE[i] + descriptors_similarity(dt[clusters[i][j]],dt[final_medoids[i]])**2
    #Betweens
    #BTW = TSS - sum(SSE)
    
    ## WRITE Inertie : TOT, INTRA, INTER
    #
    file_SSE = open("../results/kmedoids_results_reglog/kmedoids_reglog_SSE_seeds"+str(Nseeds)+".txt","w")
    file_SSE.write("cluster,SSE\n")
    for i in range(len(SSE)):
        file_SSE.write("{},{}\n".format(i,SSE[i]))
    
    file_SSE.close()
    #write clusters
    file_clusters = open("../results/kmedoids_results_reglog/kmedoids_reglog_seeds"+str(Nseeds)+"_clusters.txt","w")
    for i in range(len(clusters)):
        for j in range(len(clusters[i])):
            file_clusters.write("{},{}\n".format(names_dt[clusters[i]][j],i))
    
    file_clusters.close()
    #write medoids
    file_medoids = open("../results/kmedoids_results_reglog/kmedoids_reglog_seeds"+str(Nseeds)+"_medoids.txt","w")
    
    for i in range(len(clusters)):
        file_medoids.write("{},{}\n".format(i,final_medoids[i])) #attention commence à 0
    
    file_medoids.close()
    ###
#average medoid
initial_medoids_1 = [random.randint(0,len(names_dt)) for i in range(1)]
kmedoids_instance_1 = kmedoids(dt, initial_medoids_1, metric=metric, itermax=10)
kmedoids_instance_1.process()
final_medoids_1 = kmedoids_instance_1.get_medoids()
dt_medoid = dt[final_medoids_1[0]]
#TSS
TSS = 0
for i in range(len(dt)):
    TSS = TSS + descriptors_similarity(dt[i], dt_medoid)**2
#
file_TSS = open("../results/kmedoids_results_reglog/kmedoids_reglog_TSS.txt","w")
file_TSS.write("{}\n".format(TSS))
file_TSS.close
#

def descriptors_similarity_bis(vec1, vec2):
    if len(vec1) != 75:
        print("hey")
        return 1
    vec = np.sqrt((vec1 - vec2)**2)
    sim = Intercept + \
    hydrophobic_kyte * vec[56] + \
    p_aromatic_residues * vec[69]+ \
    p_charged_residues * vec[6] + \
    p_negative_residues * vec[23] + \
    p_positive_residues * vec[10] + \
    charge * vec[24] + \
    p_Nlys_atom * vec[15] + \
    p_Ocoo_atom * vec[67] + \
    p_small_residues * vec[7] + \
    p_C_atom * vec[64] + \
    p_nitrogen_atom * vec[9] + \
    RADIUS_HULL * vec[31] + \
    SURFACE_HULL * vec[73] + \
    DIAMETER_HULL * vec[49] + \
    VOLUME_HULL * vec[28] + \
    RADIUS_CYLINDER * vec[3] + \
    C_RESIDUES * vec[63] + \
    PSI * vec[58] + \
    PCI * vec[12] + \
    INERTIA_2 * vec[18] + \
    INERTIA_3 * vec[70] + \
    A * vec[32] + \
    C * vec[34] + \
    D * vec[36] + \
    G * vec[37] + \
    F * vec[38] + \
    I * vec[39] + \
    H * vec[40] + \
    K * vec[41] + \
    M * vec[42] + \
    L * vec[43] + \
    Q * vec[45] + \
    P * vec[46] + \
    S * vec[47] + \
    R * vec[48] + \
    T * vec[50] + \
    W * vec[51] + \
    Y * vec[53]
    return 1-exp(sim)/(1+exp(sim))


####### KMEANS ##########
names_dt = dt.index.values
###
metric = distance_metric(type_metric.USER_DEFINED, func= descriptors_similarity_bis)
initial_medoids = kmeans_plusplus_initializer(dt, 2).initialize()
kmeans_instance = kmeans(dt, initial_medoids, metric=metric)
# Run cluster analysis and obtain results.
start = time.time()
print("hello")
kmeans_instance.process()
end = time.time()
print(end - start)
#
clusters = kmeans_instance.get_clusters()
final_centers = kmeans_instance.get_centers()


names_dt[clusters[i]][j]

