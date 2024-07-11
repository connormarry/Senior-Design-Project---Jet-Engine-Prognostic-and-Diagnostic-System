import matplotlib 
from matplotlib import pyplot as plt 
from matplotlib.backends.backend_pdf import PdfPages 
from mpl_toolkits import mplot3d
import numpy as np

def rainPlots(sVals, rValsBeforeRandom, rVals, binnedRain, allPlots):
    #plot the function before and after randomness is added 
    fig0 = plt.figure()
    plt.plot(sVals, rValsBeforeRandom)
    plt.scatter(sVals, rVals, color="red") 
    plt.title("Original Rain Function + Randomness Graphed") 

    fig5 = plt.figure()
    #plt.plot(sVals, rValsBeforeRandom)
    plt.scatter(sVals, binnedRain, color="red") 
    plt.title("Original Rain Function + Randomness Graphed -- BINNED") 

    # filename = 'Rain_Plots.pdf'
    figures = [fig0, fig5]
    allPlots += figures

def sprinklerPlots(f, sVals, spVals, binnedSprinkler, allPlots):
    x = np.linspace(-10, 10, 1000)
    y = f(x)

    #plot the function before and after randomness is added 
    f1 = plt.figure()
    plt.plot(x, y)
    plt.scatter(sVals, spVals, color="red")
    plt.title("Sprinkler with and without Randomness")
    plt.xlim(-0.5, 0.95)
    plt.ylim(0.8, 1.65)
    
    #zoomed in graph for season = 0
    f2 = plt.figure()
    plt.plot(x, y)
    plt.scatter(sVals, spVals, color="red")
    plt.title("Zoomed In Graph at 0") 
    plt.xlim(-0.05, 0.15)
    plt.ylim(1.1, 1.5)

    #Creates a graph for the binned values 
    f6 = plt.figure()
    plt.plot(x, y)
    plt.scatter(sVals, binnedSprinkler, color="red")
    plt.title("Sprinkler with and without Randomness - BINNED")
    plt.xlim(-0.05, 0.15)
    plt.ylim(-5, 7.5)
    
    figures = [f1, f2, f6]
    allPlots += figures

def wetPlots(f, rVals, spVals, wVals, binnedWet, allPlots):
    x = np.linspace(-10, 10, 1000)
    y = np.linspace(-10, 10, 1000)
    x, y = np.meshgrid(x, y)
    z = f(x, y)

    wetFig = plt.figure(figsize=(10, 8))
    ax = plt.axes(projection='3d')
    ax.plot_wireframe(x, y, z, color ='green')
    ax.set_title('Original Wet Function')

    newX, newY = np.meshgrid(rVals, spVals)

    #plots the original function with the randomness scattered 
    wetFig2 = plt.figure(figsize=(10, 8))
    ax2 = plt.axes(projection='3d')
    ax2.plot_wireframe(x, y, z, color ='green')
    ax2.scatter(rVals, spVals, wVals, color="red")
    ax2.set_title('Original Wet Function + Randomness')

    #Plots the binned values for the wet function
    wetFig3 = plt.figure(figsize=(10, 8))
    ax2 = plt.axes(projection='3d')
    ax2.plot_wireframe(x, y, z, color ='green')
    ax2.scatter(rVals, spVals, binnedWet, color="blue")
    ax2.set_title('Original Wet Function + Randomness -- BINNED')

    figures = [wetFig, wetFig2, wetFig3]
    allPlots += figures

def slipperyPlots(f, wVals, slVals, binnedSlip, allPlots):
    x = np.linspace(0, 10, 1000)
    y = f(x)

    #plot the function before and after randomness is added 
    slip1 = plt.figure()
    plt.plot(x, y)
    plt.scatter(wVals, slVals, color="red")
    plt.title("Slippery with and without Randomness")

    #plots the binned values
    slip2 = plt.figure()
    #plt.plot(x, y)
    plt.scatter(wVals, binnedSlip, color="red")
    plt.title("Slippery with and without Randomness - BINNED VALUES")

    figures = [slip1, slip2]
    allPlots += figures

def falldownPlots(f, slVals, fVals, binnedFall, allPlots):
    x = np.linspace(-10, 10, 1000)
    y = f(x)

    #plot the function before and after randomness is added 
    fall1 = plt.figure()
    plt.plot(x, y)
    plt.scatter(slVals, fVals, color="red")
    plt.title("Fall Down with and without Randomness")

    #zoomed in graph
    fall2 = plt.figure()
    plt.plot(x, y)
    plt.scatter(slVals, fVals, color="red")
    plt.title("Fall Down with and without Randomness - ZOOMED")
    plt.xlim(-2, 2)
    plt.ylim(-1, 3)

    #binned graph
    fall3 = plt.figure()
    #plt.plot(x, y)
    plt.scatter(slVals, binnedFall, color="red")
    plt.title("Fall Down with and without Randomness - BINNED")
    plt.xlim(-2.5, 2.5)
    plt.ylim(-0.5, 4.5)

    figures = [fall1, fall2, fall3]
    allPlots += figures
