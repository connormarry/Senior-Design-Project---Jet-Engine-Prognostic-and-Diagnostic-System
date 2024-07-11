# Imports
import numpy as np
import matplotlib.pyplot as plt
from random import randint
from createPlots import rainPlots, sprinklerPlots, wetPlots, slipperyPlots, falldownPlots
import csv
import warnings  
warnings.filterwarnings('ignore')

np.random.seed(224592) # Generate random seed to ensure reproducibility.

# These are the relationships we are looking for
edges = [
     ("Season", "Rain"),
     ("Season", "Sprinkler"),
     ("Rain", "Wet"),
     ("Sprinkler", "Wet"),
     ("Wet", "Slippery"), 
     ("Slippery", "Fall")
]

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

# Create functions for the different nodes
rainFunc = lambda s: 2.0 * s + s + 1.0
sprinklerFunc = lambda s: (s**2 + 2.5) * 0.5
wetFunc = lambda r, sp: np.cos(2 * r) + 1.5 * sp
slipperyFunc = lambda w: np.sin(5 * w)
fallFunc = lambda sl: (1.2 * sl * sl) + (0.5 * sl)

numSamples = 100 # Number of samples to generate
epsilon = 0.1 # The amount of noise to add to the data

# Create function to bin data
# - If data is greater than half of the maximum value, set to 1
# - Otherwise, set to 0
def binaryBinData(data, numBins = 2):
    big = max(data)
    start = big / numBins
    ranges = []
    binnedData = []

    for i in range(numBins):
        ranges.append(start)
        start += start
    
    # print(ranges)
        
    for i in range(len(data)):
        for j in range(numBins):
            if data[i] <= ranges[j]:
                binnedData.append(int(j))
                break
    return binnedData

#====================================================================================
# Create the season values
sVals = np.zeros(numSamples) # Create an array of zeros to store the season values
seasonInd = 0 # Initialize the season index
for i in range(len(sVals)):
    if (i+1) % (numSamples // 4) == 0:
        seasonInd += 1
    temp = seasonInd + np.random.randint(0, 2)

    if temp >= 4:
        temp = 0

    sVals[i] = temp

# Debugging Code
#print("Season Values: ")
# print(sVals[0:25])
# print(sVals[26:50])
# print(sVals[50:75])
# print(sVals[75:100])
# print(np.count_nonzero(sVals == 0))
# print(np.count_nonzero(sVals == 1))
# print(np.count_nonzero(sVals == 2))
# print(np.count_nonzero(sVals == 3))

#====================================================================================
# Create the rain values

rVals = np.zeros(numSamples) # Create an array of zeros to store the rain values
rValsBeforeRandom = np.zeros(numSamples)  #array of zeros for rain values before random

for i in range(len(rVals)):
    rValsBeforeRandom[i] = rainFunc(sVals[i])
    temp = rainFunc(sVals[i]) + epsilon * np.random.randn(1)
    rVals[i] = temp

binnedRain = binaryBinData(rVals)   #bins rain values, default is 2 bins

rainPlots(sVals, rValsBeforeRandom, rVals, binnedRain)      #generate rain plots

# Debugging Code
#print("Rain Values: ")
# print(rVals[0:25])
# print(rVals[26:50])
# print(rVals[50:75])
# print(rVals[75:100])

#====================================================================================
# Create the sprinkler values

spVals = np.zeros(numSamples) # Create an array of zeros to store the sprinkler values
spValsBeforeRandom = np.zeros(numSamples) #Creates array of zeros for sprinkler values before random

for i in range(len(spVals)):
    spValsBeforeRandom[i] = sprinklerFunc(sVals[i])
    temp = sprinklerFunc(sVals[i]) + epsilon * np.random.randn(1)
    spVals[i] = temp

binnedSprinkler = binaryBinData(spVals)     

sprinklerPlots(sprinklerFunc, sVals, spVals, binnedSprinkler)       #generate sprinkler plots

# Debugging Code
#print("Sprinkler Values: ")
# print(spVals[0:25])
# print(spVals[26:50])
# print(spVals[50:75])
# print(spVals[75:100])

#====================================================================================
# Create the wet values

wVals = np.zeros(numSamples) # Create an array of zeros to store the wet values
for i in range(len(wVals)):
    temp = wetFunc(rVals[i], spVals[i]) + epsilon * np.random.randn(1)
    wVals[i] = temp

binnedWet = binaryBinData(wVals)

wetPlots(wetFunc, rVals, spVals, wVals, binnedWet) #generates the wet plots

# Debugging Code
# print("Wet Values: ")
# print(wVals[0:25])
# print(wVals[26:50])
# print(wVals[50:75])
# print(wVals[75:100])

#====================================================================================
# Create the slippery values

slVals = np.zeros(numSamples) # Create an array of zeros to store the slippery values
for i in range(len(slVals)):
    temp = slipperyFunc(wVals[i]) + epsilon * np.random.randn(1)
    slVals[i] = temp
binnedSlip = binaryBinData(slVals)

slipperyPlots(slipperyFunc, wVals, slVals, binnedSlip)  #generates the slippery plots
# Debugging Code
# print("Slippery Values: ")
# print(slVals[0:25])
# print(slVals[26:50])
# print(slVals[50:75])
# print(slVals[75:100])

#====================================================================================
#create the Fall values

fVals = np.zeros(numSamples)
for i in range(len(fVals)):
    temp = fallFunc(slVals[i]) + epsilon * np.random.randn(1)
    fVals[i] = temp

binnedFall = binaryBinData(fVals)

falldownPlots(fallFunc, slVals, fVals, binnedFall)      #generates the fall down plots

# Debugging Code
# print("Fall Down Values: ")
# print(fVals[0:25])
# print(fVals[26:50])
# print(fVals[50:75])
# print(fVals[75:100])

#====================================================================================
# Write dataset to CSV file

with open('updatedDataset.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Season', 'Rain', 'Sprinkler', 'Wet', 'Slippery', 'Fall_Down'])
    for i in range(numSamples):
        writer.writerow([sVals[i], binnedRain[i], binnedSprinkler[i], binnedWet[i], binnedSlip[i], binnedFall[i]])
