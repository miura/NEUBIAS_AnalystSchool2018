# Trouble shooting, Q & A

## CellProfiler 2.2.0 

### Installation for Linux machine: 

Nicolas Chiaruttini

**problem:** There's no easily accessible 2.2.0 version of CellProfiler for Linux. 

Nuno Martins suggested this:

[Source installation (Ubuntu 16.04 LTS)](https://github.com/CellProfiler/CellProfiler/wiki/Source-installation-%28Ubuntu-16.04-LTS%29)

but it did not work for me. 

**solution:** (installation from source did not work, ) So I use a windows VM.


### Installation and JAVA version

Sebastian Haensch

**problem:** CellProfiler 2.2.0 seems to have some trouble on my Windows setup and does not start (CellProfiler starts to shut down immediately without error message). Interestingly the ilastik package installed with it seems to work fine, but I try to figure out whats happening. 

**solution:** Realized that there were errors written in the command line, but CP closed it so fast, that it was barely visible. Startet CP from the command Line and found some errors. It seemed that it could not locate the jvm. It turned out that Windows lost the environmental variables of the directory for jdk and jre. So I set the path for both in the environmental variables manually as JAVA_HOME and JRE_HOME variables. After that I did not even reinstalled CP 2.2.0 and got it finally running.

**Beth Cimini's comment**: Java 9 is incompatible with CP; that's true even for 3.0 (but hopefully not for long).  Apologize for the inconvenience!

## R
### RStudio?

**Question**: Do we need to install an IDE for R ? I installed R on linux, but I only have the command line. Any advice on which IDE ? RStudio ? (Nicolas Chiaruttini)

**Answer**: Thank you for checking. The important thing is to have a script editor and to be able to go easily back and forth between the scripts and the console. If the version you have is command line only (I am not familiar with how it works in linux) and does not permit interactively editing the script on the go and selectively executing parts of the script, then yes, RStudio will make it easier for you. 

For Mac and Windows users: the regular R download from CRAN comes equipped with a script editor functionality (File > Open Document to open a previously written script in script editor, or File > New Document to initiate a new one), from which you can easily run code in blocks or in full. That is completely sufficient for the workshop.

RStudio has a number of added functionalities and a neat GUI, which can make it easier to work with, especially for new users, to familiarise with the scripts, variables, data structure etc. The drawback in our case is that some of the graphics in the provided scripts (which were written in basic R, not RStudio) might not turn out quite right in RStudio, so for visualising the graph output correctly RStudio users might end up needing extra attention for formatting. (Vasja Urbancic)


# ACC

## Nuno Martins

I downloaded the wrong version of ACC, it should be the ACC source code instead of the standalone versions and I think it fixed my issue.