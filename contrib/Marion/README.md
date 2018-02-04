# Scripts_FilopodyanR - a case study for the NEUBIAS TS7 in Szeged (27.01 to 30.01.2018)

During the training school number 7 (TS7) http://eubias.org/NEUBIAS/training-schools/analysts/ts7-szeged2018/ organised by NEUBIAS, the Network of European Bioimage Analysts http://eubias.org/NEUBIAS/, I have been working on an image analysis workflow build to analyse the behaviour of filopodia. Filopodia are cytoplasmic protrusions of migrating cells https://www.nature.com/subjects/filopodia.

This workflow is composed of two parts: a Fiji plugin and a collection of R scripts. The R scripts were written to analyse the output of the Fiji plugin. Original R scripts are available here: https://github.com/gurdon-institute/Filopodyan/tree/master/FilopodyanR


The goal of the training school was to discover, explore and deconstruct several workflows, including this one. We had a very limited amount of time to propose solutions to improve or modify the workflow, or reuse some components of the workflow for another purpose.

I chose 1) to improve the compatibility of the R analysis to a general case composed of more than two datasets, and 2) to build a user interface using R Shiny to display the results of the R analysis. Due to the limited time, I made only partial modifications that should be considered as ideas. To run the Shiny app, a) run FilopodyanR_MASTERSCRIPT.R till line 110 included b) Then run Filopodyan3 Module 3.R till line 81 included c) Run the app.R contained in the Filopodia subfolder.

The modified R scripts can be accessed here: https://github.com/marionlouveaux/NEUBIAS2018_TS7/

And here is a snapshot of the Shiny app I made:

![](https://github.com/marionlouveaux/NEUBIAS2018_TS7/blob/master/Filopodia/snapshot_app.png)
