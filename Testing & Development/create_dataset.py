import numpy as np
import matplotlib.pyplot as plt

np.random.seed(224592)
x = np.random.rand(5000)
a = 1.0
b = 0.5
xn = a * np.random.randn(5000) + b

plt.figure()
plt.hist(x)
plt.title('uniform pdf')

plt.figure()
plt.hist(xn)
plt.title('normal pdf')

plt.figure()
plt.hist(np.sin(5 * x))
plt.title('how a nonlinear function changes a uniform pdf')

F = lambda x: 2.0 * x * x + x + 1.0
G = lambda x: np.sin(5 * x)

xl = np.linspace(0, 1, 200) #make an array of 2000 entries, linear from 0 to 1

#------------------------------------------------------------------
#trying to test F(x1) + epsilon * random number
epsilon = 0.1               #testing with epsilon 0.1
np.random.seed(224592)      #resets random seed

#for each x1, we draw 20 random numbers and add to y
y = np.zeros(len(xl) * 20)      #creates an array of 0s -- size = 2000 * 20 (20 enried for each x1 entry)
xin = np.zeros(len(xl) * 20)    #same as y

# print(xl)
# print(y)
# print(xin)
for ix in range(len(xl)):               #loops 2000 times
    xin[ix*20:(ix*20)+20] = xl[ix]      #assigns the correct block of 20 to the value in x1
    #print(xin[ix*20:(ix*20)+20] )
    for ir in range(20):                #loops 20 times 
        y[ix*20+ir] = F(xl[ix]) + epsilon * np.random.randn(1)
        #print(np.random.randn(1))
print(y)
print(xin)

plt.plot(xin, y, '.')
plt.title('error in independent variable that is independent of its value')
#plt.show()

#----------------------------------------------------
y = np.zeros(len(xl) * 20)          #initializes xin to have 2000 * 20 entried 
xin = np.zeros(len(xl) * 20)

for ix in range(len(xl)):
    xin[ix*20:(ix*20)+20] = xl[ix]
    for ir in range(20):
        y[ix*20+ir] = F(xl[ix]) + epsilon * G(xl[ix]) * np.random.randn(1)

plt.figure()
plt.plot(xin, y, '.')
plt.title('error in the model with a missing term and unknown parameter')
#plt.show()

#----------------------------------------------

y = np.zeros(len(xl) * 20)
xin = np.zeros(len(xl) * 20)

for ix in range(len(xl)):
    xin[(ix * 20):(ix * 20 + 20)] = xl[ix]
    for ir in range(20):
        y[(ix * 20 + ir)] = F(xl[ix]) + epsilon * G(xl[ix] + epsilon * np.random.randn(1)) * np.random.randn(1)

plt.figure()
plt.plot(xin, y, '.')
plt.title('error in the model with a missing term and unknown parameter and uncertainty in the independent variable')

plt.figure()
plt.plot(xin, y, '.')
plt.title('error in the model with a missing term and unknown parameter')