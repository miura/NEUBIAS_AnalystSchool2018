![NEUBIAS](http://eubias.org/NEUBIAS/wp-content/uploads/2016/12/NEUBIAS_COST_Logos.png)

# NEUBIAS Bioimage Analyst School 2018

Dates: Jan 27 - 30th, 2018
Place: Szeged, Hungary

Organizers: Kota Miura, Chong Zhang & Jean-Yves Tinevez

## Aim

The school aims at providing bioimage analysts with practical access to the latest bioimage analysis workflows and their components. Many software/library packages are updated and new ones are appearing on daily basis, but analysts tend to be constrained to what one knows already and omit the use of new components. They are too busy. We hope that this school will become a good chance for analysts to be exposed to the latest scene in the bioimage analysis, of various workflows and workflow components, to widen their scope and broaden their skills.

The school program is largely renovated from last year, based on the feed-backs of participants. 

## Place and Time

### Place
Irinyi Building, University of Szeged  

**Address:**  
**Szeged, Tisza Lajos krt. 103.**   
[Google Map](https://goo.gl/maps/Ht6XGuZ8Szt)

![](imgs/TS_venue.png)

### Time

Jan 27 (Sat) 11:00  - Jan 30 (Tue) 19:00, 2018 

Registration on the fist day starts  from 10am.  

**For more detailed schedule, see [here](https://docs.google.com/spreadsheets/d/1WCevAgjsBsMp7i2cOdKCES6arct8oC_nhGJfWr-PQs0/edit?usp=sharing).**

## The program 

The school is based on the concepts of "workflows and components" in bioimage analysis ([more details here](https://www.authorea.com/users/90123/articles/211121-workflows-and-components-of-bioimage-analysis-the-neubias-concept)) and will be with four types of modules: **Workflow Deconstruction**, **Algorithms of Workflow Components**, **Forums** and **Implementation**. 

In **Workflow Deconstruction**, we reproduce, trace and modify bioimage analysis workflows. Invited speakers and selected workflow authors from participants present their bioimage analysis workflow in details: the biological problem, algorithms of components including statistical analysis, how they are assembled into the workflow to output either numbers, plots or visualization results. In parallel with these explanations, participants will load those components and reproduce the workflow on their own laptop (reproduce the workflow). Interactive discussion on each of the components, the overall design of the workflow and capability of running the workflow in various environments are moderated. 

In **Algorithms of Workflow Components**, invited speakers present in-depth explanation about workflow components. These talks are aimed at encouraging participants to expand their knowledge towards the utilization of more efficient, more precise algorithms in their workflow. Following discussions are moderated. 

1. Discussion and comparison with similar components (plugins, a function in a library, etc) implemented for similar purpose
2. Discussion on interoperability. How to use that component in various ecosystems e.g. Java, Python, MATLAB, R. 

In **Forums**, we will discuss various aspects related to bioimage analysis - with interests surrounding analysts as a profession  (e.g. How do we teach bioimage analysis?). Discussion results are summarized and will be reported to the NEUBIAS community.

In **Implementation**, participants are split into several groups, and each group implements one of the following issues:


1. Modification of workflows presented in the school, for either 
   1. the full workflow running in different ecosystems
   2. a part of the workflow replaced with a different component. 
2. Comparison and benchmarking of workflow components with similar algorithms. The target components should be selected by each group. 

## Participation

Participants are expected to be bioimage analysts, analyzing biological image data on daily basis. 

We expect a fluency in at least one programming language. We do not teach coding, but intensively do coding using several different languages. Skills / flexibility to follow such sessions are a prerequisite. 

Please bring your own laptop! We do not provide machines.  

There will be no helpers during all sessions. We rather promote attending bioimage analysts to to help each other, also for the networking 

During registration, the applicant is asked to submit at least one bioimage analysis workflow that one has authored / worked on (starting with a specific biological question, describe the workflow in a short paragraph and the type of results: numbers, plots and/or visualization - does not have to be a published paper). Among these applicants, some are selected for presentation as "Workflow Deconstruction" session and lead the session. 

## Workflow Deconstruction: Details

  * Tracing the workflow, starting with sample image data, understand the biological problem, do image processing and data analysis, ends up in numbers, plots or visualizations. 
  * Explanation for each step (or each component) are given and interesting algorithms are picked up and discussed in details. 
  * Each participant uses ones own laptop to reproduce / modify the workflow
  * Interactions: questions on components, a proposal for alternative solutions, discussion on capability in other ecosystems. 
  * Invited "workflow authors" + Selected "workflow authors" from applicants (registration form should include an abstract of submission of interesting workflow)

### Invited Workflow Deconstruction Authors

1. Assaf Zaritsky
   * Cell migration / membrane dynamics analysis / statistics workflows
     * [Instructions (installations and misc)](https://github.com/miura/NEUBIAS_AnalystSchool2018/blob/master/Assaf/NEUBIAS_SzegedSchool_AssafZar.md)
     * [repo](https://github.com/assafzar/MonolayerKymographs) 
     * [slides PDF](Assaf/collectiveMigrationWorkflowDeconstruction.pdf)
   * Assaf will also give talks in the symposium. 

2. Molnár Csaba
   *  High Content Image Data Screening and Analysis
     * [Instructions (installations and misc)](https://github.com/miura/NEUBIAS_AnalystSchool2018/blob/master/Csaba/NEUBIAS2018%20Szeged%20TS7%20High%20Content%20Screening.md)
     * [repo](https://github.com/csmolnar/NEUBIAS_2018_TS7_HCS) 
   *  Csaba is also a local organizer of the conference. 
3. Vasja Urbancic
   * Filopodia Dynamics and Automated Image Analysis (Filopodyan)
     * [Instructions (installations and misc)](https://github.com/miura/NEUBIAS_AnalystSchool2018/blob/master/Vasja/NEUBIAS_Analysis_of_filopodia_dynamics.md)
     * TroubleShooting cases and QAs
         * [CellProfiler](TroubleShooting-QA.md#cellprofiler-220)
         * [R](https://github.com/miura/NEUBIAS_AnalystSchool2018/blob/master/TroubleShooting-QA.md#r)
   * [The Paper](http://jcb.rupress.org/content/early/2017/07/28/jcb.201705113) 

## Workflows, Student Presentations

Selected workflows contributed by students

- Jagadish Sankaran (National University of Singapore)
  - [2D FCS](https://github.com/miura/NEUBIAS_AnalystSchool2018/blob/master/Submitted_Workflow_Presentations.md#2d-fcs)
- Hendrik Deschout (Centre for Cellular Imaging, University of Gothenburg)
  - [Clustering of Single Molecule Localizations](https://github.com/miura/NEUBIAS_AnalystSchool2018/blob/master/Submitted_Workflow_Presentations.md#clustering-of-single-molecule-localizations)
- Tobias Rasse (ALMF, EMBL)
  - [Parameter sweeping for cell shape segmentation](https://github.com/miura/NEUBIAS_AnalystSchool2018/blob/master/Submitted_Workflow_Presentations.md#parameter-sweeping-for-cell-shape-segmentation)
- Ziqiang Huang (Light Microscopy Facility CRUK Cambridge)
  - [3D morphometry of Synapses](https://github.com/miura/NEUBIAS_AnalystSchool2018/blob/master/Submitted_Workflow_Presentations.md#3d-mprphometry-of-synapses)
- Tong Li (Centre de Biologie Intégrative, Laboratory of Cellular and Molecular Biology of Control of Proliferation)
  - [Mitosis detection and Analysis of Features](https://github.com/miura/NEUBIAS_AnalystSchool2018/blob/master/Submitted_Workflow_Presentations.md#mitosis-detection-and-analysis-of-features) 

## Components and their algorithms

"Components": One-hour talks introducing workflow components. Not only about algorithms, they are developing, but more with an overview.

* Invited speakers
  * Jean-Yves Tinevez ([Link](https://research.pasteur.fr/en/member/jean-yves-tinevez/))
     * Title: A short dive into single-particle tracking core algorithms in BioImaging
     * Abstract
  * Tobias Pietzsch ([Link](https://github.com/tpietzsch)) and Florian Jug ([Link](https://github.com/fjug))
     * Title: Big Data and 3D Visualization
     * [Abstract](https://github.com/miura/NEUBIAS_AnalystSchool2018/blob/master/component_talks.md#big-data-and-3d-visualization)
     * [slides PDF](https://imagej.net/_images/9/9b/Jug_BigDataAnd3dViz.pdf)
  * Anna Kreshuk ([Link](https://hciweb.iwr.uni-heidelberg.de/Staff/akreshuk))
     * Title: Pipelining with ilastik
         * Introduction to Ilastik and the headless usage
     * Abstract
     * Anna will also appear in the symposium and give a more general talk about iLastik 
  * Vannary Meas-Yedid Hardy ([link](https://research.pasteur.fr/en/member/vannary-meas-yedid-hardy/))
     * Title: Image Segmentation
     * Abstract 
  * Fabrice Cordelieres ([Link](https://www.researchgate.net/profile/Fabrice_Cordelieres))
     * Title: Deconstructing co-localisation workflows: from co-expression assessment to super-resolved co-distribution analysis
     * [Abstract](https://github.com/miura/NEUBIAS_AnalystSchool2018/blob/master/component_talks.md#deconstructing-co-localisation-workflows-from-co-expression-assessment-to-super-resolved-co-distribution-analysis)
     * [slides PDF](https://github.com/fabricecordelieres/Training_material/blob/master/English/18-01-28%20NEUBIAS-Colocalisation/18-01-28%20NEUBIAS-Colocalisation.pdf)

## NEUBIAS lectures

- Kota Miura
   - Title: [Natural History of Fake Image Data](https://docs.google.com/presentation/d/1qEqPXI9QVwtAVFSVPamQ7EE1ZCSmhMq0XrlrwVnuS5A/edit?usp=sharing)


## Forums

Forums are moderated in between sessions. 

- Discussion on working environments: how each is interacting with biologists, how they are teaching. Recommended teaching methods, failed teaching methods. 
- "Bioimage analysis workflow of the year": share your opinion / comments on recent bioimage analysis workflows that impressed you. 
- [slides](https://docs.google.com/presentation/d/15mVT4exg_pD5QyEOTbEB6a3a5Sf_4YZMiqT3o-pS0Pk/edit#slide=id.g329124a171_0_15)


## Implementations / Presentations

School participants are asked to present their implementations (by group) on the last day of the school. 7 groups, 15 minutes presentation + 5 minutes questions and answers. 






