# -*- encoding: utf-8 -*-
'''
@File    :   deal4caluvcfmissing.py
@Time    :   2023/04/20 11:51:25
@Author  :   Zhang FW 
@Contact :   z1039055126@163.com
@note    :   
'''

import pandas as pd
import numpy as np
from sys import argv

script, input_f, output_f = argv 

def main():
   data = pd.read_csv(input_f, sep='\t')
   data1 = data.iloc[:,:2]
   haps = data.iloc[:,4:]
   data1['haps.'] = haps.apply(lambda x : x.value_counts().get('.',0 ),axis=1)
   data1['haps0'] = haps.apply(lambda x : x.value_counts().get('0/0',0 ),axis=1)
   data1['haps1'] = haps.apply(lambda x : x.value_counts().get('0/1',0 ),axis=1)
   data1['haps2'] = haps.apply(lambda x : x.value_counts().get('1/1',0 ),axis=1)
   data1.to_csv(output_f, sep='\t', index=0)




if __name__ == "__main__":
   main()
