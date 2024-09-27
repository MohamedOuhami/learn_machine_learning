import os
import tarfile
from six.moves import urllib

import pandas as pd

# The link to the data
DOWNLOAD_ROOT = "https://github.com/ageron/data/raw/main/housing.tgz"
HOUSING_PATH = "datasets/housing"

def fetch_data():
    # Create the folder for the data
    if not os.path.isdir(HOUSING_PATH):
        os.makedirs(HOUSING_PATH)

    tgz_path = os.path.join(HOUSING_PATH,'housing.tgz')
    
    # Download the file
    urllib.request.urlretrieve(DOWNLOAD_ROOT,tgz_path)

    # Unpack the tar file
    housing_tgz = tarfile.open(tgz_path)

    # Extract the files
    housing_tgz.extractall(HOUSING_PATH)

    # Close the tar files
    housing_tgz.close()

    print("Fetched the data from teh sourc")

fetch_data()
    