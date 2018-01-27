# Spatiotemporal quantification of monolayer cell migration

## Author

Assaf Zaritsky, 
UT Southwestern Medical Center, Dallas, TX, USA
Weizmann Institute of Science, Rehovot, Israel

## Abstract

From embryonic development, through synchronized beating of cardiac muscle cells to collective cell death - individual cells use basic cellular machinery to influence and respond to neighboring cells through a complex interplay of chemical and physical cues. How these local interactions are integrated in space and time to induce collective patterns is yet unknown. By designing and applying new analytical methods to migrating monolayers of epithelial cells, we discovered how local mechanical fluctuations induce long-range inter-cellular communication and identified potential molecular pathways driving this communication. 

A key in advancing this project was the ability to quantify spatiotemporal dynamics of a migrating monolayer. In the workshop, we will demonstrate two such methods and discuss how they were applied to learn new biology: (1) Explicit segmention of coordinated migrating cell clusters; (2) Spatiotemporal representation of the onset of monolayer migration; 


## Software Installation

Matlab (2017a or later)

Toolboxes:
Image Processing Toolbox
Statistics and Machine Learning Toolbox


## Sample Data

- Approximate total size of sample data set: 330 MB 
- Capturing conditions
   - organism: Human Bronchial Epithelial Cells
   - labeled protein: none
   - microscopy: Phase contrast
   - spatial resolution: 0.908 um / pixel
   - time resolution [dt]: 5 minutes per frame
- Location: 

Coordination (150MB): https://cloud.biohpc.swmed.edu/index.php/s/Vmh55ha1VWZuvun

Spatiotemporal representation of onset of collective cell migration (180MB): https://cloud.biohpc.swmed.edu/index.php/s/8cR8zgmXkYzn0y7

Rhosin perturbation (4MB): https://cloud.biohpc.swmed.edu/index.php/s/3Rm18Xoq6PQ3YNy


## Resources

Source code:
https://github.com/assafzar/MonolayerKymographs

Main functions to execute:
- mainCoordination
- mainTimeLapse
- mainRhosin


## References:

Nock and Nielsen, Statistical Region Merging (2004)http://ieeexplore.ieee.org/abstract/document/1335450/ (region merging segmentation algorithm)

Zaritsky et al. Propagating waves of directionality and coordination orchestrate collective cell migration (2014) http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003747 (adaptation of the region merging algorithm to explicitly identify clusters of coordinatde migrating cells from velocity fields)

Zaritsky et al. Seeds of locally aligned motion and stress coordinate a collective cell migration (2015) http://jcb.rupress.org/content/early/2017/05/15/jcb.201609095 (new biology from old data by identifying clsuters of coordinated velocity / stress)

Zaritsky, Tseng et al. Diverse roles of guanine nucleotide exchange factors in regulating collective cell migration (2017) www.cell.com/biophysj/abstract/S0006-3495(15)01123-6 (screening spatio-temporal monolayer migration)