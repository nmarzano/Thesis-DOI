# smFRET analysis and plotting for N. Marzano Thesis:

This code was written to analyse single-molecule FRET (smFRET) data generated as part of the thesis entitled 'The development of single-molecule approaches for the study of molecular chaperones' written by Nicholas Marzano. Generally, the code enables raw data to be imported and used to construct histogram distributions, transition density plots (TDPs) and to analyze the kinetics orginating from a Hidden Markov Models (HMM) fitting of the data using the vbFRET MATLAB program. Furthermore, analyzed data can be plottted and presented using custom written code.

**Prerequisites**:
Two kinds of data are required for this analysis. 
(1) The raw and idealized FRET data for individual molecules following HMM analysis using vbFRET. Data for individual molecules is exported from vbFRET and stored within a folder.
(2) Raw TDP data, including the initial FRET state (prior to a transition) and the final FRET state (FRET state after the transition) and the corresponding number of frames that the molecule was in the initial FRET state prior to the transition to the final FRET state. This data is required for each molecule with data for all molecules concatenated. 

**Workflow**:
To reproduce analyses presented in the manuscript, it is recommended to use the following order: Numbered items in order (0 - 3) and within each numbered analysis scripts to follow the lettered order (A- Z). This will ensure any source data is generated as needed.

0-import_data (imports data into VsCode environment from computer directory).
1A-plot-histogram (imports data from vscode environment, removes major outliers and plots histograms. Also can plot ridgeline plots using code at bottom of script).
1B-plot_traces (used to plot any individual molecule of interest).
2A-initial_cleanup_TDP (cleans TDP data and removes outliers, finds the proportion of molecules from each treatment that goes below a defined threshold).
2B-plot_TDP (plots TDP plots).
2C-dwell_time_analysis (cleans all TDP data, removes outliers, removes the first residence time for each molecule, calculates transition frequency of specific classes, plots violin plot of fret state prior to transition below defined threshold).
2D-pot_transition_frequency (plots transition frequency graphs).
2E-plot_violin_plots (calculates basic statistics, plots violin plots in a variety of ways).
3-summary_plot (plots summary heatmaps, which includes information on the proportion of time below a threshold, residence times and transition probabilities).