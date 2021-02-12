## This file is just a sample file for reading in datasets, cleaning them up, and combining into one larger dataset

import numpy as np
import pandas as pd
import zipfile

## Steps:
## Read in both Dataset files and local files that are too large to be on github 
data = pd.read_csv(r'Datasets/WellTransferData.csv', dtype='unicode')

zf = zipfile.ZipFile(r'Datasets/wellDOS.zip') 
local = pd.read_csv(zf.open('wellspublic.csv'), dtype='unicode')

api_col = data.columns[0]
local_api_col = local.columns[0]

data[api_col] = data[api_col].str.replace(r'[^0-9]+', '')

## Clean datasets  

## Combine to one dataset 
# how='outer' obtains union of APIs, 'inner' obtains intersection of APIs
merged = local.merge(data, how='outer', left_on=local_api_col, right_on=api_col)

## Export that file localy
merged.to_csv(r'Datasets/mergedDataset.tsv', sep='\t')
