# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:40:54 2020

@author: paudel
"""


from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pandas as pd
from scipy.signal import savgol_filter
import numpy as np
import os

output_folder = 'Experiment_1-description/python_results/Traces'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#### the first item in the tuple will be the name that goes into the graph legend
data_paths = {
    "example1":"Figures/Figure_5/raw_data/200715_Fluc_FoldandUnfold/05_PATH_D111020_T2254.dat",
    "example2":"Figures/Figure_5/raw_data/200715_Fluc_FoldandUnfold/92_PATH_D111020_T2254.dat",
    "example3":"Figures/Figure_5/raw_data/200715_Fluc_FoldandUnfold/80_PATH_D111020_T2254.dat"
}

exposure = 0.5  ### exposure in seconds

def load_data(filename):
    trace_df = pd.DataFrame(np.loadtxt(filename))
    trace_df.columns = ["frames", "donor", "acceptor", "FRET", "idealized FRET"]
    trace_df["Time"] = trace_df["frames"]/(1/exposure)
    trace_df["smoothed_FRET"] = savgol_filter(trace_df["FRET"], 5, 2)
    return trace_df

compiled_df = []
for data_name, data_path in data_paths.items():
    imported_data = load_data(data_path)
    imported_data["treatment_name"] = data_name
    compiled_df.append(imported_data)
compiled_df = pd.concat(compiled_df)   #### .rename(columns = {1:"test", 3:"test2"}) ## can rename individually if needed

#FRET-time plot
def plot_FRET(treatment):
    plt.rcParams['svg.fonttype'] = 'none'
    sns.set(style = "darkgrid")
    plot2 = plt.figure(figsize = (5, 2))
    plt.xlim(0, 200, 10)
    plt.ylim(0, 1.1, 0.2)
    sns.lineplot(x = treatment["Time"], y = treatment["smoothed_FRET"], color = 'black')
    sns.lineplot(x = treatment["Time"], y = treatment["idealized FRET"], color = 'darkorange')
    plt.xlabel("Time (s)")
    plt.ylabel("FRET")
    plt.show()
    return plot2


for data_name, data_path in data_paths.items():
    treatment = compiled_df[compiled_df["treatment_name"] == data_name]
    mol_ident = data_path.split('/')[-1]
    plot_FRET(treatment).savefig(f'{output_folder}/{data_name}_Trace_{mol_ident}.svg', dpi = 600)

