# -*- coding: utf-8 -*-
from string import digits
import biovec
import pandas as pd
import os
import re
import argparse
import time
from smart_open import open

def getArgs():
    parser = argparse.ArgumentParser('python')
    parser.add_argument('-inputfile', required=True)
    return parser.parse_args()

def extracFeatures(inputfile):
    pv = biovec.models.load_protvec('swissprot-reviewed-protvec.model')
    with open(inputfile, 'r') as file:
        data = file.read()
        num = data.count('>hsa:')
        for i in range(1, num + 1):
            keystr = data.split('>hsa:')[i]
            digit = re.findall('\d+', keystr)
            remove_digits = str.maketrans('', '', digits)
            res = keystr.translate(remove_digits)
            temp = res.replace("\n", "")
            temp1 = temp.lstrip()
            pv1 = pv.to_vecs(temp1)
            new_series = pd.DataFrame(pv1)
            new_series.to_csv('temp.csv', index=None)
            dst = "hsa:" + str(digit[0]) + "_" + str(digit[1]) + ".csv"
            os.rename('temp.csv', dst)


if __name__ == "__main__":
    args = getArgs()
    features = extracFeatures(args.inputfile)
    start = time.time()
    end = time.time()

    print('time elapsed:' + str(end - start))
