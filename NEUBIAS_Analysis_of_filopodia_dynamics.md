# Analysis of filopodia dynamics

## Author

Vasja Urbancic & Richard Butler, Gurdon Institute, University of Cambridge

## Abstract


Filopodia are thin cellular protrusions rich in actin filaments. They are abundant on the leading edge of migrating cells and neuronal growth cones, where they serve important roles in signalling, adhesion, guidance and motility. Many aspects of the dynamic behaviour of filopodia remain unknown, including the acute influence of various actin regulatory proteins on the formation of filopodia and on their elongation/shrinkage bahaviour. 

For this reason, it is important to be able to measure protein localisation (as fluorescence within filopodia, filopodia tips and filopodia bases, each tracked over the entire time series), alongside their morphodynamic properties (length, tip extension rate and retraction rate, base extension rate and retraction rate, persistence of tip movement, time spent in extending/retracting/stalling state), and to be able to cross-evaluate the measured fluorescence with the observed morphogical behaviour.

In the workshop we will illustrate how Filopodyan can be used to perform these measurements, and how it enables analyses with multiple different goals: 1. comparing morphological and dynamic properties of filopodia between different datasets, to understand the influence of various treatments/genotypes on filopodial dynamics; 2. investigating correlations between different filopodia metrics, to uncover new relationships between various filopodia properties; 3. analysing the temporal profile of the accumulation of fluorescence at the sites of filopodium formation, in order to understand the molecular events leading to the initiation of a new filopodium; and 4. analysing the temporal cross-correlation of tip fluorescence with tip movement within each filopodium over the entire time series, to understand whether proteins of interest propel filopodia tips or hinder their growth.


## Software Installation


**Software**

* Fiji: can be downloaded from https://imagej.net/Fiji/Downloads (installation guidelines: https://imagej.net/Fiji/Downloads#Installation). 

* R: can be downloaded from https://cran.r-project.org/  (installation guidelines in FAQ section 2.5 on the same website). Existing users please check you are running version 3.0.3 (Sincere Pumpkin Patch) or above. 

**Plugin & Packages:**

* Filopodyan: within Fiji, run the "Update…" command (in Help menu). After update is complete, open "Manage Update Sites", and select Filopodyan (http://sites.imagej.net/Rb7777/) within the provided list. In case of difficulties, perform manual installation as described in the Filopodyan user guide (see Resources), p.2.

* R: several additional packages are necessary to run the code in some of the R scripts provided with workshop materials. These can be downloaded from the CRAN repository by running the installation script 'R-packages-installation.R' (to be provided in the Github folder associated with the workshop) within R.


## Sample Data

- Approximate total size of sample data set: 10 GB
- Capturing conditions
   - organism: *Xenopus laevis* retinal explants cultured *in vitro*
   - labeled protein: mNeonGreen, GAP-RFP, mNeonGreen-ENA
   - microscopy: fluorescence microscopy using highly inclined laminated optical (HILO) sheet illumination, acquisition in a single z plane
   - spatial resolution: 65 nm / pixel
   - time resolution [dt]: 2 s between timepoints
- Location: will be locally distributed in the school. For the purpose of testing the plugin upon installation, a publically available time series may be used, available on: <https://github.com/gurdon-institute/Filopodyan/blob/master/growth-cone-test-file.tif>

## Resources

* Complete Filopodyan Github repository: <https://github.com/gurdon-institute/Filopodyan/ >

* Fiji plugin user guide: <https://github.com/gurdon-institute/Filopodyan/blob/master/Filopodyan%20User%20Guide.pdf>

* Fiji plugin code and documentation: <https://github.com/gurdon-institute/Filopodyan/tree/master/Filopodyan>

* R scripts overview: <https://github.com/gurdon-institute/Filopodyan/blob/master/README.md>

* R scripts code: <https://github.com/gurdon-institute/Filopodyan/tree/master/FilopodyanR>

## References:

Urbancic, V., Butler, R., Richier, B., Peter, M., Mason, J., Livesey, F. J., Holt, C. E., Gallop, J. L. 2017. Filopodyan: An Open-Source Pipeline For The Analysis Of Filopodia. <http://jcb.rupress.org/content/216/10/3405> DOI: 10.1083/jcb.201705113
