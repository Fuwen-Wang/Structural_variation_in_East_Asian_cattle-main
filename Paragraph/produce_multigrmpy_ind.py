#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   produce_multigrmpy_ind.py
@Time    :   2022/01/14 21:05:40
@Author  :   Xiaoting Xia
@Contact :   xiaxiaoting1991@163.com
@Note    :   A script used to generate the single-sample script in the population-scale genotyping when running the Paragraph software. Script usage: python produce_multigrmpy_ind.py. The input file (list1_4.txt) consists of four columns: Sample BAM_PATH Depth 150.
'''
def main():
    num_list = [x.strip().split() for x in open(r'list1_4.txt').readlines()]
    for unit in num_list:
        sample = unit[0]
        depth = int(float(unit[2]))*20
        with open(sample+'.sh','w') as f:
            f.write('''#!/bin/sh
export ref=/PATH/MG.all.fa
export vcf=/PATH/02_NEW_SET_ALL.Finally.vcf
export Manifest=/PATH
        ''')
            f.write('''
multigrmpy.py -i $vcf -m $Manifest/%s.Manifest1 -r $ref --threads 20 -o %s -M %s
        '''%(sample,sample,depth))

if __name__ == "__main__":
    main()
    



