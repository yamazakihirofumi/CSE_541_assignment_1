import kagglehub
import pandas as pd
import numpy as np


# Download latest version
path = kagglehub.dataset_download("crawford/20-newsgroups")

print("Path to dataset files:", path)


