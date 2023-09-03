# -*- encoding: utf-8 -*-
'''
@File    :   Freq_unsuccessful_genotype_breed.py
@Time    :   2023/04/21 14:52:26
@Author  :   Zhang FW 
@Contact :   z1039055126@163.com
@note    :   
'''

import pandas as pd
import numpy as np
from sys import argv
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    data = pd.read_csv(r'merge.vcf.statistic.csv.G75.loc.vcf.recode.vcf.1', sep='\t')
    data1=data.iloc[:,:1]
    breednam=pd.read_csv(r'breed_sample.txt', sep='\t')
    groupb = dict(breednam.groupby('Breed')['Sampleid'].apply(list))

    for key in groupb.keys():
        data1[key] = data[groupb[key]].apply(lambda x : x.value_counts().get('.',0 ),axis=1)
    data_t = data1.iloc[:,1:]
    data2 = data_t.div(data_t.sum(axis=1), axis=0)
    data2.to_csv(r'xia.breed_p.csv', sep='\t',index=0)

if __name__ == "__main__":
   main()
