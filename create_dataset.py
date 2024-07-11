# Imports
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages 
from mpl_toolkits import mplot3d
from random import randint
from create_plots import rainPlots, sprinklerPlots, wetPlots, slipperyPlots, falldownPlots
import csv
import warnings  
warnings.filterwarnings('ignore')

# Implement create dataset function for programatic dataset generation
def createDataset(id, path, sample_count, noise, seed):

    # Set the seed for reproducibility
    np.random.seed(seed) 

    # Relationships to look for
    edges = [
        ("Season", "Rain"),
        ("Season", "Sprinkler"),
        ("Rain", "Wet"),
        ("Sprinkler", "Wet"),
        ("Wet", "Slippery"), 
        ("Slippery", "Fall")
    ]

    allPlots = []
    #####################
    #### Shortcuts: #####
    #####################
    #  s    = season    #
    #  r    = rain      #
    #  sp   = sprinkler #
    #  w    = wet       #
    #  sl   = slippery  #
    #  f    = fall_down #
    #####################

    # Initialize Plots
    allPlots = []

    # Create functions for the different nodes
    rainFunc = lambda s: 2.0 * s + s + 1.0
    sprinklerFunc = lambda s: (s**2 + 2.5) * 0.5
    wetFunc = lambda r, sp: np.cos(2 * r) + 1.5 * sp
    slipperyFunc = lambda w: np.sin(5 * w)
    fallFunc = lambda sl: (1.2 * sl * sl) + (0.5 * sl)

    numSamples = sample_count # Number of samples to generate
    epsilon = noise["epsilon"] # The amount of noise to add to the data


    # ====================================================================================
    # Create function to bin data
    # Takes in manually defined bins, or a number of bins we want with equal sizes. 
    # ====================================================================================
    def binaryBinData(data, bins = [], numBins = 2):
        binnedData = []

        #In the case that the size of each bin is not specified, but the number of bins wanted is
        if len(bins) == 0:
            
            #defines the range of the bins, what value the smallest bin should start with, and what value the largest bin should end with
            big = max(data)
            small = min(data)

            if small < 0:
                step = (big + abs(small)) / numBins
            else:
                step = (big - small) / numBins
            
            #defining bin ranges based on the number of bins and the step size of the bins
            ranges = []
            for i in range(numBins - 1):
                ranges.append(small + step)
                small += step
            ranges.append(big)
            
            #assigns data points to the bins defined in the ranges
            for i in range(len(data)):
                for j in range(numBins):
                    if data[i] <= ranges[j]:
                        binnedData.append(int(j))
                        break
        else:
            #the case where the bin ranges are predefined and passed into the function
            modBins = bins[1:]
            for i in range(len(data)):
                for j in range(len(modBins)):
                    if data[i] <= modBins[j]:
                        binnedData.append(int(j))
                        break

        return binnedData                           #returns binned values

    # ====================================================================================
    # Second potential binning function
    # ====================================================================================
    def binData(data):
        
        # Create the histogram with automatic binning
        hist, bins = np.histogram(data, bins='auto') 
        
        # map each value in data to it's corresponding bin and get those indicies
        bin_indicies = (np.digitize(data, bins) - 1)
        
        # turn those indicies into binned values
        binned_values = bins[bin_indicies]
        return binned_values

    #====================================================================================
    # Create the season values
    # ====================================================================================
    sVals = np.zeros(numSamples) # Create an array of zeros to store the season values
    seasonInd = 0 # Initialize the season index

    sVals = epsilon * np.random.rand(numSamples)        #generates a random value with the defined seed, multiplies by noise factor, uses uniform function 
    binnedSeason = binaryBinData(sVals, [], 4)          #bins th value into 4 bins representing 4 seasons
    #binnedSeason = binData(sVals)

    #creates histogram of data without specifying number of bins
    h1 = plt.figure()
    plt.hist(sVals, bins=4)
    plt.title("Histogram for Season Values -- UNIFORM DISTRIBUTION")

    #====================================================================================
    # Create the rain values
    # ====================================================================================
    epsilonRain = noise['epsilonRain']
    rVals = np.zeros(numSamples) # Create an array of zeros to store the rain values
    rValsBeforeRandom = np.zeros(numSamples)  #array of zeros for rain values before random

    #goes through parent node (season), puts season through Rain function, adds randomness
    for i in range(len(rVals)):
        rValsBeforeRandom[i] = rainFunc(sVals[i])
        temp = rainFunc(sVals[i]) + epsilonRain * np.random.randn(1)
        rVals[i] = temp

    #creates histogram of data without specifying number of bins
    h2_unSpec = plt.figure()                                                      
    n, binsRain, patches = plt.hist(rVals, bins=noise["binsRain"])                                  
    plt.title("Histogram for Rain Values without Specifying Number of Bins")

    #creates histogram of data, specifying 20 bins
    h2 = plt.figure()
    plt.hist(rVals, bins=20)
    plt.title("Histogram for Rain Values -- Gaussian (20 Bins)")

    #bins the rain values based on the number of bins generated in the histogram
    binnedRain = binaryBinData(rVals, binsRain)   #bins rain values, default is 2 bins
    rainPlots(sVals, rValsBeforeRandom, rVals, binnedRain, allPlots)      #generate rain plots
    #binnedRain = binData(rVals)

    print("Rain Bins:", len(binsRain)-1)           #prints number of bins for node

    #====================================================================================
    # Create the sprinkler values
    # ====================================================================================
    epsilonSprinkler = noise["epsilonSprinkler"]
    spVals = np.zeros(numSamples) # Create an array of zeros to store the sprinkler values
    spValsBeforeRandom = np.zeros(numSamples) #Creates array of zeros for sprinkler values before random

    #goes through parent node (season), puts season through Sprinkler function, adds randomness
    for i in range(len(spVals)):
        spValsBeforeRandom[i] = sprinklerFunc(sVals[i])
        temp = sprinklerFunc(sVals[i]) + epsilonSprinkler * np.random.randn(1)
        spVals[i] = temp

    #creates histogram of data without specifying number of bins
    h3_unSpec = plt.figure()
    n, sprinklerBins, patches = plt.hist(spVals, bins=3)
    plt.title("Histogram for Sprinkler Values without Specifying Number of Bins")

    #bins the sprinkler values based on the number of bins generated in the histogram
    binnedSprinkler = binaryBinData(spVals, sprinklerBins)     
    sprinklerPlots(sprinklerFunc, sVals, spVals, binnedSprinkler, allPlots)       #generate sprinkler plots
    #binnedSprinkler  = binData(spVals)

    print("Sprinkler Bins:", len(sprinklerBins)-1)          #prints number of bins for node

    # ====================================================================================
    # Create the wet values
    # ====================================================================================
    wVals = np.zeros(numSamples) # Create an array of zeros to store the wet values

    #goes through parent nodes (rain, sprinkler), puts nodes through Wet function, adds randomness
    for i in range(len(wVals)):
        temp = wetFunc(rVals[i], spVals[i]) + epsilon * np.random.randn(1)
        wVals[i] = temp

    #creates histogram of data without specifying number of bins
    h4_unSpec = plt.figure()
    n, wetBins, patches = plt.hist(wVals, noise["binsWet"])
    plt.title("Histogram for Wet Values without Specifying Number of Bins")

    #bins the wet values based on the number of bins generated in the histogram
    binnedWet = binaryBinData(wVals, wetBins)
    wetPlots(wetFunc, rVals, spVals, wVals, binnedWet, allPlots) #generates the wet plots
    #binnedWet = binData(wVals)

    print("Wet Bins: ", len(wetBins)-1)    #prints number of bins for node

    # ====================================================================================
    # Create the slippery values
    # ====================================================================================
    slVals = np.zeros(numSamples) # Create an array of zeros to store the slippery values

    #goes through parent node (wet), puts Wet through Slippery function, adds randomness
    for i in range(len(slVals)):
        temp = slipperyFunc(wVals[i]) + epsilon * np.random.randn(1)
        slVals[i] = temp

    #creates histogram of data without specifying number of bins
    h5_unSpec = plt.figure()
    n, slipBins, patches = plt.hist(slVals)
    plt.title("Histogram for Slippery Values without Specifying Number of Bins")

    #bins the slippery values based on the number of bins generated in the histogram
    binnedSlip = binaryBinData(slVals, slipBins)
    slipperyPlots(slipperyFunc, wVals, slVals, binnedSlip, allPlots)  #generates the slippery plots
    #binnedSlip = binData(slVals)

    print("Slippery Bins: ", len(slipBins)-1)       #prints number of bins for node

    # ====================================================================================
    # Create the Fall values
    # ====================================================================================
    fVals = np.zeros(numSamples)        # Create an array of zeros to store the fall down values

    #goes through parent node (slippery), puts slippery through Fall_Down function, adds randomness
    for i in range(len(fVals)):
        temp = fallFunc(slVals[i]) + epsilon * np.random.randn(1)
        fVals[i] = temp

    #creates histogram of data without specifying number of bins
    h6 = plt.figure()
    n, fallBins, patches = plt.hist(fVals)
    plt.title("Histogram for Fall Down Values -- Gaussian")

    #bins the fall_down values based on the number of bins generated in the histogram
    binnedFall = binaryBinData(fVals, fallBins)
    falldownPlots(fallFunc, slVals, fVals, binnedFall, allPlots)      #generates the fall down plots
    #binnedFall = binData(fVals)

    print("Fall Down Bins: ", len(fallBins)-1)      #prints number of bins for node

    #====================================================================================
    # Creates Histograms
    # ====================================================================================
    filename = f"{path}/{id}_Histograms.pdf"
    #filename = "Histograms.pdf"
    figures = [h1, h2_unSpec, h2, h3_unSpec, h4_unSpec, h5_unSpec, h6]

    p7 = PdfPages(filename) 

    for f in figures:
        f.savefig(p7, format='pdf')

    p7.close()

    #====================================================================================
    # Creates Plots with All Nodes
    # ====================================================================================
    filename = f"{path}/{id}_Plots.pdf"
    #filename = "Plots.pdf"

    p8 = PdfPages(filename) 

    for f in allPlots:
        f.savefig(p8, format='pdf')

    p8.close()

    # ====================================================================================
    # Write dataset to CSV file
    # ====================================================================================
    with open(f"{path}/dataset{id}.csv", 'w', newline='') as f:
    #with open("dataset.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Season', 'Rain', 'Sprinkler', 'Wet', 'Slippery', 'Fall_Down'])
        for i in range(numSamples):
            writer.writerow([binnedSeason[i], binnedRain[i], binnedSprinkler[i], binnedWet[i], binnedSlip[i], binnedFall[i]])
            
if __name__ == "__main__":
    noise = {
    "name": "LOW",
    "epsilon": 0.1,
    "epsilonRain": 0.01,
    "epsilonSprinkler": 0.01
    }
    createDataset("", "", 1000, noise, 224592)
    
