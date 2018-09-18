#import all the necessary modules
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
%matplotlib inline

plt.style.use('ggplot')

######generating training data#############
np.random.seed(42) #this will generate same values even after rerunning the script
#function that will take number of data points to generate 
#and number of data features every data point has
def generate_data(num_samples, num_features=2):
    #data matrix 
    data_size = (num_samples, num_features)
    data = np.random.randint(0, 100, size=data_size)
    #label matrix
    labels_size = (num_samples, 1)
    label = np.random.randint(0, 2, size=labels_size)
    return data.astype(np.float32), label
    
#testing the generate_data function
train_data, labels = generate_data(10, 2)

#plotting the training set
def plot_data(all_blue, all_red):
    #plot all the blue points
    plt.scatter(all_blue[:,0], all_blue[:,1], c='b', marker='s', s=180)
    #plot all the red points
    plt.scatter(all_red[:,0], all_red[:,1], c='r', marker='^', s=180)
    #annonate the plot with labels
    plt.xlabel('x coordinate')
    plt.ylabel('y coordinate')  

#splitting all the data points into blue and red sets
#ravel flattens the array
#blue data points are those rows of train_data whose corresponding label is 0
blue_set = train_data[labels.ravel() == 0]
#red data points are those rows of train_data whose corresponding label is 1
red_set = train_data[labels.ravel() == 1]

plot_data(blue_set, red_set)



