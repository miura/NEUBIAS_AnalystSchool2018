# Bioimage Analysis Workflows

Szeged, Hungary, 2018

Selected workflows for presentation, initially submitted for the school application. 

## Synapse Segmentation and Geometric Measurement

**Ziqiang	Huang**  
[Light Microscopy Facility CRUK Cambridge, UK]( http://www.lightmicroscopy.cruk.cam.ac.uk/new-starter-ziqiang-huang/)

### Collections and Components 

IJ, iLastik, MATLAB

### Workflow Outline

I acquired FIB-SEM image stacks in TIFF format, as my raw image data. The goal is to geometrically analyze the synapses (the object of interests inside the image dataset) contained inside. The workflow involves registration (aligment of 2D images through TrakEM plugin in Fiji), object segmentation (through ilastik), visualization and correction of the segmentation result and 3D geometrical analysis (e.g.: calculate 3D object's Feret diameter for all the segmented synapses; both visualization, processing and analysis were scripted in Matlab).


## Clustering of Single Molecule Localizations

**Hendrik Deschout**  
[Centre for Cellular Imaging, University of Gothenburg, Sweden](http://cf.gu.se/english/Centre_for_Cellular_Imaging)

### Collections and Components 

Matlab, Fiji

### Workflow Outline
A workflow that I would like to share is “identifying protein clusters as observed by single-molecule localization microscopy (SMLM)”. This workflow starts from a time series of SMLM images, and the final result is a list of fluorophore localizations that are each assigned to a certain cluster. The workflow can roughly be decomposed into the following steps: 1) identify in each SMLM image the peaks that correspond to single fluorophores (using e.g. blob detection and intensity thresholding), 2) fit a 2D Gaussian to each identified peak, 3) calculate the corresponding localization uncertainties and select appropriate localizations, 4) apply a clustering algorithm (e.g. Ripley’s K function, DBSCAN, etc.) to the selected localizations, 5) extract the cluster properties, 6) optional: generate a SMLM image. This workflow is partially visualized in figure 1 of the following article: [doi.org/10.1016/j.bpj.2017.09.032](http://dx.doi.org/10.1016/j.bpj.2017.09.032).

## Parameter sweeping for cell shape segmentation


**Tobias	Rasse**  
[ALMF, EMBL, Germany](https://www.embl.de/services/core_facilities/almf/members/)

### Collections and Components 

Python (Jupyter Notebook), Real-time Accurate Cell-shape Extractor (RACE), holoviews, FIJI

### Workflow Outline

I would be most exited to present and discuss a modular workflow for semi-automated analysis of cell shape changes in SPIM time-series. 

Core of the workflow is the Real-time Accurate Cell-shape Extractor (RACE) as previously described by Stegmeier et. al. Dev Cell. 2016 Jan 25;36(2):225-40. [doi: 10.1016/j.devcel.2015.12.028](http://www.cell.com/developmental-cell/fulltext/S1534-5807(15)00837-0?_returnURL=http%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS1534580715008370%3Fshowall%3Dtrue). RACE is computationally very powerful and parameter of the pipeline can be handed over using xml files in a “head-less” mode.

Limitations of the published implementation is the fact that results cannot be matched against a “ground truth” in an automated manner. 

The current workflow implemented a Jupyter Notebook addresses this issue. In detail, approx. 100-2000 of meaningful parameter combinations are synthesized semi-automatically. For these cluster jobs files are generated and deposited on our SPIM Server. 

A second python script executed on our HPC-Cluster monitors the jobs folder and executes all computational demanding tasks on the HPC. Next, it deposits the results on our SPIM server. 

Then the simple Jupyter Notebook (run on my laptop) takes over again and matches results (such as cell number, cell size, cell shape) against a ground truth previously provided by the user. Results are scored and visualized (in graphs) using holoviews (http://holoviews.org/). 

Simple Python scripts are used for basic pre-processing. Multiple slightly differently pre-processed images might be used as input.
Using this pipeline is very easy to identify the ideal processing parameter automatically. 

I am looking forward to presenting my progress on this part of the project.
Importantly, the pipeline can give a catalogue of hypothesis for the true segmentation result as output. The true segmentation might thus be only decided upon tracking the movement of individual cells in a second stage in the workflow. Therefore, the data might be globally optimized. This second part of the workflow will likely not be finished before the meeting, but I would be excited to discuss preliminary results and to jointly test the integration of various existing tools into my work-flow for this purpose.

Everything is set-up that we could test solutions remotely on EMBLs HPC-Cluster or on (rather powerful) Virtual Windows Machines (in case a GUI is required).

## Mitosis detection and Analysis of Features

**Tong Li**  
Centre de Biologie Intégrative, Laboratory of Cellular and Molecular Biology of Control of Proliferation

### Collections and Components 

uManager, Fiji (Trackmate), Conda，cellh5, OpenCV

### Workflow Outline

I have developed a plugin of Micro-Manager and Fiji for single-cell high-content analysis, MAARS (mitosis analysis and recording system, Li et al. 2017, MBoC). Briefly, with MAARS it's possible to perform on-the-fly (or post-) analysis on wide-field microscopy data. It first segments cells with a custom label-free algorithm inspired by the work of Julou et al. (2013) and then extract coordinates of fluorescent spots with Trackmate (Tinevez et al., 2017) to calculate spatial mitosis-focused parameters. e.g. spindle length, spindle angle according to cell major axis etc. Eventually, _in silico_ mitosis synchronization allows us to detect mitotic defects such as chromosome lagging in anaphase.

Currently, we are adding more parameters to MAARS and making MAARS intelligent by using OpenCV. In the future, it is feasible to combine the power of quantitative analysis of MAARS with SIM super-resolution microscopy in order to have an intelligent super-resolution microscopy.

PS : MAARS is now nested on Github (<https://github.com/bnoi/MAARS>). However, since I'm bumping MAARS to version 2.0, the master branch is un-tested and maybe unstable, especially for the on-the-fly analysis.


## 2D FCS

**Jagadish Sankaran**  
[National University of Singapore](http://www.dbs.nus.edu.sg/lab/BFL/current_members.html)

### Collections and Components 

ImageJ

### Workflow Outline

#### Introduction to Imaging FCS

Our lab has pioneered a technique called Imaging FCS which is a multiplexed version of Fluorescence Correlation Spectroscopy (FCS). A time-series stack of fluorescent images is recorded using a fast and sensitive camera in Imaging FCS. Then the autocorrelation functions are calculated and fitted in every pixel of the stack enabling one to display the spatially resolved diffusion coefficients and concentration as a map. By looking at such diffusion coefficient maps, one can then decide whether there are regions of low or high mobility in the biological system being investigated.

#### Imaging FCS plugin

I would like to describe the workflow to analyse Imaging FCS data. This is a plugin developed in JAVA for ImageJ and FIJI. The source code, jar file, trial data set and the manual can be downloaded here.

<http://www.dbs.nus.edu.sg/lab/BFL/imfcs_image_j_plugin.html>

#### Input and Output to the plugin

The input to the program is a time-series image stack (16 bit gray value TIFF) of fluorescent molecules moving in 2D or 3D environments. The molecules could be moving in solutions, tissue culture cell-membranes, zebrafish embryos etc. The output is a map of diffusion coefficients and concentration of molecules obtained after fitting to theoretical models. 

#### Workflow for the plugin

The first step is to read the image stacks. Then the number of pixels in x and y and the number of frames are determined. The image stack is read and displayed to the user. In this program, the autocorrelations are calculated using the sums of products method. A detailed description of the algorithm used to calculate the autocorrelation is described in the next section. The user is then allowed to look at the quality of autocorrelations by clicking on any pixel or selecting a region of interest. The intensity time trace corresponding to each pixel is also shown. If the intensity shows considerable photobleaching, the user can perform a bleach correction operation. Bleaching can be corrected by fitting the data to a polynomial. The user has to provide the degree of the polynomial. In our experience a degree in the range of 4 to 8 is sufficient for bleach correction. The polynomial degree should not be selected too high as otherwise the correction can influence also the fast fluctuations which are investigated and the resulting diffusion coefficients will be biased.
If the user is satisfied, the user then proceeds to calculate the entire set of autocorrelations in the image or in a certain region of interest. Later, upon fitting the data by NLS or GLS, the parameters from the theoretical model are displayed as maps. The entire set of autocorrelations along with its fits are also displayed as graphs. Instead of the entire set of autocorrelations, one can also plot the average correlation along with its fit. The raw data, the fitted data and the fitted parameters can be exported as a Microsoft® Excel file. The user has the option to threshold the fitted parameters and display those only within a chosen range. If need be, the user can visualize the fitted parameters (diffusion coefficient and concentration) as a scatter plot. This enables one to visually identify any correlations between these two fitted parameters. A Bayesian analysis can be performed if need be on every pixel to determine the probability of a particular theoretic model among all the available competing models. Apart from autocorrelation, the programs allows one to evaluate cross-correlation between two pixels as well.

#### Calculation of the autocorrelation function

As stated earlier, the autocorrelations are calculated using the sums of products methods using the formula provided in the publication here. One could also calculate the autocorrelation function by Fourier transforms. A linear calculator computes at all possible lagtimes from k = 1 to k = (n-1) where n is the total number of frames.

The semi-logarithmic correlator architecture (Schaetzel and Peters, 1991, SPIE; Wohland et al, Biophysical Journal, 2001) and is used more frequently since this architecture covers a larger range of lagtimes than the linear correlator using less number of computations. This correlator architecture is based on the multi-tau algorithm described in these two publications here (??). In the most common configuration, the first 16 correlations are at linearly increasing lagtimes with a binwidth of Δτ. The next set of 8 correlations possess linearly spaced lagtimes at intervals of 2Δτ beginning with (15+2)Δτ  and a bin width of 2Δτ . The next set of 8 correlations possess lagtimes at intervals of 4Δτ beginning with (31+4)Δτ and a bin width of 4Δτ. This is repeated for bin widths of 8Δτ, 16Δτ, 32Δτ, 64Δτ and 128Δτ. The last calculated lag time is at (2048-1)Δτ. Substituting Δτ =0.5 ms, a lag time of 1.0235 s can be achieved by just 72 (16+(8-1)×8) correlations. The same lagtime needs 2048 correlations in the linear configuration. The above example was for the configuration of a (16, 8) multi tau correlator but can be directly extended to any (p, q) correlator structure. In a (p, q) correlator, the first p correlations are at linearly increasing lagtimes  where m ranges from 0 to p-1 with a binwidth of Δτ. The next q groups possess p/2 lagtimes with bin width and lagtime intervals which double from group to group. In this way a particular lagtime is always the sum of all the bin widths of  the previous lagtimes.  A (p, q) correlator calculates a correlation function at h = [p+(q-1)×q/2] number of lagtimes.  

#### Other automated data analysis tools provided by the plugin:-

As described above, the program enables one to calculate autocorrelations at every pixel, fit the data and extract diffusion coefficients. Here I would like describe two other operations where autocorrelations are calculated at different pixel sizes by binning and post processing is performed on the extracted diffusion coefficients. These two operations are FCS diffusion law and PSF calibration.

#### FCS diffusion law

##### Principle and Biological application

One can bin the data to vary the pixel size. One can estimate the average time taken to traverse through a pixel by dividing the area of the pixel (A) by the diffusion coefficient (D). In the case of free diffusion, one expects the average transit time to increase linearly with an increase in pixel size. This is referred to as FCS diffusion law. One can estimate deviations from free diffusion by computing the intercept of such a plot. The intercept is zero for free diffusion and non-zero when there is hindered diffusion in domains. This program allows one to calculate the entire FCS diffusion law analysis automatically.

##### FCS diffusion law-Work flow

The workflow for the aforementioned FCS diffusion law is to calculate the autocorrelations at different bin sizes, fit them, and extract the diffusion coefficients. After this, the ratio of the area of the pixel to the diffusion coefficient (A/D) is evaluated for a variety of bin sizes and then the A/D is plotted against the bin size. Later these data points are fitted to a straight line. The slope and intercept are displayed to the user.

#### PSF Calibration

##### Principle

The PSF calibration tool enables one to determine the point spread function (PSF) of the optical system from the Imaging FCS time-series stack based on the fact that the diffusion coefficient is a material property and is independent of the binning size of the pixel used for data analysis. In case the chosen PSF is higher than the PSF of the system, the diffusion coefficient will decrease with an increase in bin size and vice-versa.

##### Workflow

The work flow for PSF calibration is as follows. Firstly, the autocorrelation functions are calculated for a range of bin sizes. The next step is to fit this data with different PSF sizes. In order to do that, one needs to interact with the user to receive a lower and upper bound of PSF values and the step size for the search.  The fitting has to be carried out for all the autocorrelations in each bin size for every PSF specified by the user. Then the diffusion coefficients need to be plotted against the bin size for every PSF. One can then determine the PSF of the optical system by choosing the PSF which yields a diffusion coefficient independent of the bin size. 

This user-interactive and fast open-source software to evaluate imaging FCS data makes the analysis easier and accessible for a larger community interested in the dynamic behaviour of molecules in model and living systems.

### references


- Schaetzel K & Peters R (1991) Noise on multiple-tau photon correlation data. Vol. 1430 (Kenneth SS, ed.). 109-115. SPIE.

- T. Wohland, R. Rigler, and H. Vogel, The standard deviation in fluorescence correlation spectroscopy Biophys. J. 80, 2987-2999 (2001).



