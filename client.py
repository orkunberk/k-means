# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 23:07:21 2021

@author: orkun.yuzbasioglu
"""

from KMeans import KMeans, generate_data

# Training data generation
sample_count_per_class = 200 # number of data samples for each cluster
training_data = generate_data(sample_count_per_class) # generate data using a function

# Create kMeans clustering object
k_means = KMeans(cluster_count=5, max_iteration=7)

# Perform kMeans clustering training, i.e, find and plot cluster centers
k_means.fit(training_data)