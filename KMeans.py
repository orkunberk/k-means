# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 23:08:10 2021

@author: orkun.yuzbasioglu
"""

from random import gauss
import matplotlib.pyplot as plt

def generate_data(sample_count_per_class):
    '''a function to create sample_count_per_class points for each class'''
    mu_x1, sigma_x1 = 0.3, 0.06
    mu_y1, sigma_y1 = 0.7, 0.06

    mu_x2, sigma_x2 = 0.8, 0.15
    mu_y2, sigma_y2 = 0.3, 0.15

    mu_x3, sigma_x3 = 0.2, 0.10
    mu_y3, sigma_y3 = 0.2, 0.10
    
    points_class1 =   [Point(gauss(mu_x1, sigma_x1), gauss(mu_y1, sigma_y1)) for _ in range(0, sample_count_per_class)]
    points_class2 =   [Point(gauss(mu_x2, sigma_x2), gauss(mu_y2, sigma_y2)) for _ in range(0, sample_count_per_class)]
    points_class3 =   [Point(gauss(mu_x3, sigma_x3), gauss(mu_y3, sigma_y3)) for _ in range(0, sample_count_per_class)]
            
    return(points_class1 + points_class2 + points_class3)

class Point():
    
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
        
    def __str__(self):
        return 'X position: {} and Y position: {}'.format(self.x, self.y)
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def distance(self, other):
        distance = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return distance

class KMeans():
    
    def __init__(self, cluster_count, max_iteration):
        self.cluster_count = cluster_count
        self.cluster_centers = []
        self.max_iteration = max_iteration
        self.cluster_assignments = []
    
    def fit(self, training_data):
        
        # initialization of cluster centers
        self.cluster_centers = [Point(gauss(0.4, 0.1), gauss(0.4, 0.1)) for _ in range(0, self.cluster_count)]
        
        #plot initial cluster centers

        # iterations
        for i in range(0, self.max_iteration):
        
            # distance of points to each cluster center
            distances = []
        
            for p in training_data:
                distances.append([p.distance(c) for c in self.cluster_centers])
        
            # cluster assignment
            self.cluster_assignments = []

            for d in distances:
                self.cluster_assignments.append(d.index(min(d))+1)
            
            # plot initial cluster centers and assignments
            if i == 0:
                self.plot_clusters(self.cluster_centers, training_data, self.cluster_assignments, 'iteration 1')        
            
            # updating cluster centers
            self.cluster_centers = []

            for cluster in range(1, self.cluster_count+1):
                
                number_of_points_in_cluster = 0
                cluster_center = Point(0,0)

                for idx, assignment in enumerate(self.cluster_assignments):

                    if(assignment==cluster):

                        number_of_points_in_cluster += 1;
                        cluster_center += training_data[idx]
                        
                new_center = Point(cluster_center.x/number_of_points_in_cluster, cluster_center.y/number_of_points_in_cluster)

                self.cluster_centers.append(new_center)
        
        # plot initial cluster centers and assignments
        self.plot_clusters(self.cluster_centers, training_data, self.cluster_assignments, 'iteration ' + str(self.max_iteration))
    
    @staticmethod
    def plot_clusters(cluster_centers, training_data, training_data_assignment, title):
        
        fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
        
        ax.set_xlim(-0.2, 1.2)
        ax.set_ylim(-0.2, 1.2)
            
        colors = ['darkorange', 'mediumblue', 'green', 'purple', 'crimson', 'magenta', 'gold', 'gray']
        
        for idx, center in enumerate(cluster_centers):
            ax.plot(center.x, center.y, color=colors[idx], marker='o', markersize=12)
            
            for idy, point in enumerate(training_data):
                if training_data_assignment[idy] == idx+1:
                    ax.plot(point.x, point.y, color=colors[idx], marker='o', markersize=2)

        plt.title(title)
        plt.draw()
        # plt.savefig("output.png", bbox_inches='tight', dpi=200)
        plt.show()