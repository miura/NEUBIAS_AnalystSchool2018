# High Content Image Data Screening and Analysis

## Author

Csaba Molnar, BIOMAG Group, Biological Research Centre, Szeged

## Abstract

In this workshop we aim to implement an image-based analysis of a biological system by profiling the phenotipic response of a cancer cell line following perturbation with a small-molecule compound library.
(...being extended...)

<!---_(Please describe 1.biological motivation, 2.what is to be measured and 3.the goal of analysis.)_--->

## Software Installation

All the following softwares are recommended to be installed by the time of the TS.

Required softwares:

- __Matlab R2015b or newer version with Image
Processing Toolbox, Statistics and Machine Learning Toolbox, and Bioinformatics Toolbox__
    - Demo licences for __Matlab R2017b__ are provided during the Training School TS7.
    - The participants who applied for demo licences get the location and installation guide via e-mail from the hungarian distributor of Matlab.
    - Installation guide is available [here](https://www.mathworks.com/help/install/ug/install-mathworks-software.html)
    - The demo licence packages contain all the necessary toolboxes.
    - Note: old laptops and computer with 32-bit processors are not capable of running this newest version of Matlab. For those who has 32-bit workstations the R2015b version is required, but they should state their demo licence demand separately!
    <!--- - __Python 2.7 (no newer!)__ with libraries *****MISSING
  - Download Python 2.7 installer from [here](https://www.python.org/download/releases/2.7/)
  - Instruction for installation can be found [here](https://www.youtube.com/watch?v=gD4eulxGNok)--->
- __CellProfiler 2.2.0__
  - Download CellProfiler 2.2.0 release from [here](http://cellprofiler.org/previous_releases/).
  - Be aware of non-English characters in the path of your home directory! If you have those, you have to change the plugin directory by editing registry.
- __Advanced Cell Classifier__
  - Download ACC 3.0 from [here](http://www.cellclassifier.org/download/). You can use Win standalone version, or you can run it's source code in Matlab.
  - Download [ExportToACC](http://eucaiorg.ipage.com/ACC/wp-content/uploads/2016/07/ExportToACCmodule.zip) CellProfiler module for saving data in ACC format. Copy exporttoacc.py file into the CellProfiler's plugins directory (File->Preferences->CellProfiler plugins directory).

## Sample Data

- Approximate total size of sample data set: ~2GB raw data -> ~10GB in total
- Capturing conditions
   - organism: human MCF-7 breast cancer cells
   - labeled: DNA (DAPI), F-actin (Phalloidin) and B-tubulin (anti–β-tubulin antibody)
   - microscopy: fluorescent, ImageXpress 5000A high-content imaging platform (Molecular Devices), ×20 PanFluor ELWD Ph1 DM objective, 16-bit camera binning resolution of 1
   - spatial resolution: .
   - time resolution [dt]: -.
- Location: local storage
    * Mount the drive available at address __\\\HVPC\TS__. Username: __INF\ts2018__, password: __Training__.
    * The input data is in folder __TS7/Csaba/Data/WorkingData__.
    * Backup data (in case of any errors) can be found in __TS7/Csaba/Data/BackupData__.
    * All the Matlab scripts (including the source of ACC) __TS7/Csaba/CodeandSoftware__.

## Resources

- Repository of TS7 on [GitHub](https://github.com/miura/NEUBIAS_AnalystSchool2018) (being prepared)
- Also in Dropbox [workflow.zip](https://www.dropbox.com/s/p28g99qqatoaxd0/workflow.zip?dl=0)
- Advanced Cell Classifier [http://www.cellclassifier.org/](http://www.cellclassifier.org/)
- CellProfiler [http://cellprofiler.org/releases/](http://cellprofiler.org/releases/)
- Image data were selected from the Broad Bioimage Benchmark Collection ([BBBC021](https://data.broadinstitute.org/bbbc/BBBC021/))


## References:

- _Caie D. et. al._: High-Content Phenotypic Profiling of Drug Response Signatures across Distinct Cancer Cells [http://mct.aacrjournals.org/content/9/6/1913](http://mct.aacrjournals.org/content/9/6/1913)
- _Caicedo C. et. al._: Data-analysis strategies for image-based cell profiling [https://www.nature.com/articles/nmeth.4397](https://www.nature.com/articles/nmeth.4397)
