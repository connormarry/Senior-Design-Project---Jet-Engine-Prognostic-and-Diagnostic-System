import os
import sys
import time
from create_dataset import createDataset
from test_bnlearn import bnLearn_Tests
from test_pgmpy import test_pgmpy
from test_pomegranate import fit_data, replace_index, test_pomegranate

# This file will be used to compare the results of each framework
# This is a rough draft and should be edited.

# This is the number of datasets that should be created
SAMPLE_COUNT = 1

# This is the different levels of noise to test each dataset with
NOISE_LEVELS = [
    {
    "name": "LOW",
    "epsilon": 0.1,
    "epsilonRain": 0.01,
    "epsilonSprinkler": 0.01,
    "binsRain": 10,
    "binsWet": 10
    },
    {
    "name": "MID",
    "epsilon": 0.4,
    "epsilonRain": 0.08,
    "epsilonSprinkler": 0.035,
    "binsRain": 6,
    "binsWet": 6
    },
    {
    "name": "HIGH",
    "epsilon": 0.8,
    "epsilonRain": 0.4,
    "epsilonSprinkler": 0.06,
    "binsRain": 6,
    "binsWet": 6
}]

###################
### Please Note ###
###################
# The total number of datasets generated will be equal to SAMPLE_COUNT * len(NOISE_LEVELS)
# So ensure that you are only testing a reasonable number or else the program will take a long time to run
###################

# Create folders to store datasets and tests
#seed = 224592
time_integer = int(time.time())
current_time = str(time_integer)
os.mkdir(f"Test-{current_time}")
os.mkdir(f"Test-{current_time}/datasets")
os.mkdir(f"Test-{current_time}/results")
os.mkdir(f"Test-{current_time}/results/bnlearn")
os.mkdir(f"Test-{current_time}/results/pgmpy")
os.mkdir(f"Test-{current_time}/results/pomegranate")

# Debugging Text
print("Starting test at time:", current_time)

# Create the datasets to test
for i in range(SAMPLE_COUNT):
    for noise in NOISE_LEVELS:
        name = noise["name"]
        print(f"Creating dataset {i} with noise level {name}...")
        createDataset(f"{i}-{name}", f"Test-{current_time}/datasets", 1000, noise, time_integer)

def PeformTests(testFunction, solver = ""):
    for i in range(SAMPLE_COUNT):
        for noise in NOISE_LEVELS:
            name = noise["name"]
            testFunction(f"Test-{current_time}/datasets/dataset{i}-{name}.csv", f"{i}-{name}") 

# Test BNLearn
def PerformTestBNLearn(filePath, fileId):
    # Redirect stdout to a file
    with open(f"Test-{current_time}/results/bnlearn/{fileId}_Test_Results.txt", 'w') as f:
        sys.stdout = f
        bnLearn_Tests(filePath)

# Test Pomegranate
def PerformTestPomegranate(filePath, fileId):
    # Redirect stdout to a file
    with open(f"Test-{current_time}/results/pomegranate/{fileId}_Test_Results.txt", 'w') as sys.stdout:
        test_pomegranate(filePath)
        
# Test Pgmpy
def PerformTestPgmpy(filePath, fileId):
    # Redirect stdout to a file
    with open(f"Test-{current_time}/results/pgmpy/{fileId}_Test_Results.txt", 'w', encoding="utf-8") as f:
        sys.stdout = f
        test_pgmpy(filePath)

if __name__ == "__main__":
    PeformTests(PerformTestBNLearn, "bnlearn")
    PeformTests(PerformTestPomegranate, "pomegranate")
    PeformTests(PerformTestPgmpy, "pgmpy")
