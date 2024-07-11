import matplotlib 
from matplotlib import pyplot as plt 
from matplotlib.backends.backend_pdf import PdfPages 
from mpl_toolkits import mplot3d
import numpy as np

def rainPlots(sVals, rValsBeforeRandom, rVals, binnedRain):
    #plot the function before and after randomness is added 
    fig0 = plt.figure()
    plt.plot(sVals, rValsBeforeRandom)
    plt.scatter(sVals, rVals, color="red") 
    plt.title("Original Rain Function + Randomness Graphed") 


    fig1 = plt.figure()
    plt.plot(sVals, rValsBeforeRandom)
    plt.scatter(sVals, rVals, color="red")
    plt.title("Zoomed In Graph at 0") 
    plt.xlim(-0.05, 0.2)
    plt.ylim(0.4, 1.5)

    fig2 = plt.figure()
    plt.plot(sVals, rValsBeforeRandom)
    plt.scatter(sVals, rVals, color="red") 
    plt.title("Zoomed In Graph at 1") 
    plt.xlim(0.95, 1.3)
    plt.ylim(3.73, 4.2)

    fig3 = plt.figure()
    plt.plot(sVals, rValsBeforeRandom)
    plt.scatter(sVals, rVals, color="red") 
    plt.title("Zoomed In Graph at 2") 
    plt.xlim(1.95, 2.3)
    plt.ylim(6.7, 7.2)

    fig4 = plt.figure()
    plt.plot(sVals, rValsBeforeRandom)
    plt.scatter(sVals, rVals, color="red") 
    plt.title("Zoomed In Graph at 3") 
    plt.xlim(2.95, 3.3)
    plt.ylim(9.75, 10.2)

    fig5 = plt.figure()
    plt.plot(sVals, rValsBeforeRandom)
    plt.scatter(sVals, binnedRain, color="red") 
    plt.title("Original Rain Function + Randomness Graphed -- BINNED") 

    filename = 'Rain_Plots.pdf'
    figures = [fig0, fig1, fig2, fig3, fig4, fig5]

    p = PdfPages(filename) 
    for f in figures:
        f.savefig(p, format='pdf')

    p.close()

def sprinklerPlots(f, sVals, spVals, binnedSprinkler):
    x = np.linspace(-10, 10, 1000)
    y = f(x)

    #plot the function before and after randomness is added 
    f1 = plt.figure()
    plt.plot(x, y)
    plt.scatter(sVals, spVals, color="red")
    plt.title("Sprinkler with and without Randomness")
    plt.xlim(-0.5, 3.5)
    plt.ylim(0, 7)

    #zooms in graph for season = 0
    f2 = plt.figure()
    plt.plot(x, y)
    plt.scatter(sVals, spVals, color="red")
    plt.title("Zoomed In Graph at 0") 
    plt.xlim(-0.5, 0.95)
    plt.ylim(0, 3)

    #zooms in graph for season = 1
    f3 = plt.figure()
    plt.plot(x, y)
    plt.scatter(sVals, spVals, color="red")
    plt.title("Zoomed In Graph at 1") 
    plt.xlim(0.5, 1.95)
    plt.ylim(0, 3)
    
    #zooms in graph for season = 2
    f4 = plt.figure()
    plt.plot(x, y)
    plt.scatter(sVals, spVals, color="red")    
    plt.title("Zoomed In Graph at 2") 
    plt.xlim(1.5, 2.95)
    plt.ylim(2, 4.5)

    #zooms in graph for season = 3
    f5 = plt.figure()
    plt.plot(x, y)
    plt.scatter(sVals, spVals, color="red")
    plt.title("Zoomed In Graph at 3") 
    plt.xlim(2.5, 3.95)
    plt.ylim(4.5, 7)

    #Creates a graph for the binned values 
    f6 = plt.figure()
    plt.plot(x, y)
    plt.scatter(sVals, binnedSprinkler, color="red")
    plt.title("Sprinkler with and without Randomness - BINNED")
    plt.xlim(-0.5, 3.5)
    plt.ylim(0, 7)
    
    filename = 'Sprinkler_Plots.pdf'
    figures = [f1, f2, f3, f4, f5, f6]

    p2 = PdfPages(filename) 
    for f in figures:
        f.savefig(p2, format='pdf')

    p2.close()

def wetPlots(f, rVals, spVals, wVals, binnedWet):
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

    filename = 'Wet_Plots.pdf'
    figures = [wetFig, wetFig2, wetFig3]

    p5 = PdfPages(filename) 
    for f in figures:
        f.savefig(p5, format='pdf')

    p5.close()

def slipperyPlots(f, wVals, slVals, binnedSlip):
    x = np.linspace(0, 10, 1000)
    y = f(x)

    #plot the function before and after randomness is added 
    slip1 = plt.figure()
    plt.plot(x, y)
    plt.scatter(wVals, slVals, color="red")
    plt.title("Slippery with and without Randomness")

    #plots the binned values
    slip2 = plt.figure()
    plt.plot(x, y)
    plt.scatter(wVals, binnedSlip, color="red")
    plt.title("Slippery with and without Randomness - BINNED VALUES")

    filename = 'Slippery_Plots.pdf'
    figures = [slip1, slip2]

    p3 = PdfPages(filename) 

    for f in figures:
        f.savefig(p3, format='pdf')

    p3.close()


def falldownPlots(f, slVals, fVals, binnedFall):
    x = np.linspace(0, 10, 1000)
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
    plt.xlim(0, 2)
    plt.ylim(-1, 3)

    #binned graph
    fall3 = plt.figure()
    plt.plot(x, y)
    plt.scatter(slVals, binnedFall, color="red")
    plt.title("Fall Down with and without Randomness - BINNED")
    plt.xlim(0, 2)
    plt.ylim(-1, 3)

    filename = 'Fall_Down_Plots.pdf'
    figures = [fall1, fall2, fall3]

    p4 = PdfPages(filename) 

    for f in figures:
        f.savefig(p4, format='pdf')

    p4.close()