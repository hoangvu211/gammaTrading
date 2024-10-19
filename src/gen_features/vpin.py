# Volume Synchronized Probability of Informed Trading
# https://github.com/yt-feng/VPIN

__author__ = 'FENG Yutong'
__credits__='FANG Boyue'

'''The file is intended for VPIN calculation'''


import pandas
from math import *
import math
import numpy as np

def std(list):
    element = 0
    for item in list:
        element = element + float((item**2)/( len(list)))
    return math.sqrt(element)

def phi(x):
    #'Cumulative distribution function for the standard normal distribution'
    return (1.0 + erf(x / sqrt(2.0))) / 2.0

def calx(v_i,delta_p_i,sigma):
    x = v_i * phi(delta_p_i/sigma)
    return x

def main():
    global df
    df = pandas.read_table("data.txt").dropna()

if __name__ == '__main__':
    main()