#Guess 2/3 of the average

#importing libaries
import matplotlib.pyplot as plt
import numpy as np

#defining constants
a = 1/2
r = 2/3

#X-th order
def x_order(x):
    return a*(r**x)

#from Zeroth to X-order
def x_sum(x):
    val = 0
    lst = []
    for i in range(x+1):
        val += x_order(i)
    return val*r/(x+1)

##########################################################################################################################################################################################################

#alternate x_sum using fold

def fold(op, f, n):
    if n == 0:
        return f(0)
    return op(f(n), fold(op, f, n-1))

def x_sum_fold(n):
    return fold(lambda x,y: x+y, lambda x: a*(r**x), n)*r/(n+1)

#test
#print(x_sum_fold(3))

##########################################################################################################################################################################################################

#add probability to list
def lst(x):
    lst = []
    for i in range(x+1):
        lst.append(x_sum(i))
    return lst

#print probability
def prob(x):
    for i in range(x+1):
        print(str(i) + "-sum: " + str(x_sum(i)))

#test
#print(x_sum(3))
#print(lst(10))
#print(prob(10))

#plotting graph


###
        
#defining variables
n = 10 #last order to consider

###

#defining function        
x = [i for i in range(n+1)]
y = lst(n)

#plotting the points
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
    marker='o', markerfacecolor='blue', markersize=12)

#setting x and y axis range
plt.ylim(0,1)
plt.xlim(0,n)

#naming the x and y axis
plt.xlabel('X-order')
plt.ylabel('Probability')

#naming the graph
plt.title('Graph of Probability vs X-order')

##########################################################################################################################################################################################################

#extension: assuming skewed normal distribution instead of even spread

#import library
from scipy.stats import skewnorm 

def new_x_sum(n,m,k): #n is last order to consider; m is some factor of y-peak
    x1 = [i for i in range(n+1)]      
    y1 = skewnorm.pdf(x1, 0, k, m)
    plt.plot(x1, y1, "r--")
    val = 0
    divisor = 0
    for i in range(n+1):
        val += x_order(i)*y1[i]
        divisor += y1[i]
        print(i,"- order: Guess -",x_order(i),"; Probability -", y1[i])
    return val*r/divisor

#Test
print("You should guess:", new_x_sum(10,1.4,1))
plt.show()

##########################################################################################################################################################################################################

#fitting m and k

##for m in range(10,25):
##    for k in range(10,25):
##        if abs(new_x_sum(10,m/10,k/10)-0.21)<=0.01:
##            print(m,k,new_x_sum(10,m/10,k/10))

