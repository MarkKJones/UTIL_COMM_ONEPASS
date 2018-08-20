#!/usr/bin/env python      
import sys                                                             
import os.path                                                     
import subprocess as sp                              
import re                                                             
import pandas as pd                                                  
import csv                                                      
import numpy as np                                       
import matplotlib.pyplot as plt                      


hms_run_list = []
shms_run_list = []
coin_run_list = []

#HMS
f = open('hms_runlist_Aug-18-2018.txt', 'r')
for line in f:
    if('#' in line): continue
    hms_run_list.append(int(line))
f.close()

#SHMS
f = open('shms_runlist_Aug-18-2018.txt', 'r')
for line in f:
    if('#' in line): continue
    shms_run_list.append(int(line))
f.close()

#COIN
f = open('coin_runlist_Aug-18-2018.txt', 'r')
for line in f:
    if('#' in line): continue
    coin_run_list.append(int(line))
f.close()

#print(run_list)
#list of runs to ignore in Buffer Level run list [2173 - 2228] --July 26, 2018
#ignore_run = [2176, 2179,2181,2182,2183,2184,2185,2186,2196,2197,2198,2199,2200,2205,2210,2211,2212, 2217, 2218, 2223, 2224,
#              2229, 2230, 2231, 2232, 2233, 2234, 2235, 2236, 2237, 2238, 2239, 2240, 2241, 2242, 2243, 2244, 2245, 2246, 2247, 2248, 2249,
#              2250, 2251, 2260, 2261, 2262]

os.chdir('../../../')

for run in hms_run_list:
    cmd1 = "./hcana -q \"SCRIPTS/COIN/SCALERS/replay_coin_scalers.C(%d,-1)\""  %run
    os.system(cmd1)

for run in shms_run_list:                           
    cmd2 = "./hcana -q \"SCRIPTS/COIN/SCALERS/replay_coin_scalers.C(%d,-1)\""  %run       
    os.system(cmd2)

for run in coin_run_list:
    cmd3 = "./hcana -q \"SCRIPTS/COIN/SCALERS/replay_coin_scalers.C(%d,-1)\""  %run
    os.system(cmd3)


