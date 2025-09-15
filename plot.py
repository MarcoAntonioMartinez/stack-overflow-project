# importing the required libraries
import matplotlib.pyplot as plt
import numpy as np

#create figure and axis
fig, ax = plt.subplots( nrows=1, ncols=1)

# define data values
x = np.array([1, 2, 3, 4])  # X-axis points
y = x*2  # Y-axis points

ax.plot(x, y)  # Plot the chart
fig.savefig('./assets/plot.png')
plt.close(fig)
#plt.show()  # display



#need a way to read json file and count the tag types for certain languages, sort same language ones together
    #in own data structure


