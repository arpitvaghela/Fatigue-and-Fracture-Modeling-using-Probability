# School of Engineering and Applied Science (SEAS), Ahmedabad University
# B.Tech(ICT) Semester IV: Probability and Random Processes (MAT 202)

- Group No : S_M1
- Kaushal Patil (AU1841040), Arpitsingh Vaghela(AU1841034)
- 

## 1 Introduction

### 1.1 Background

One of the most important problems realted to probability in mechanics is to find the reliabity of materials that are used to build objects. A lot of research has taken place to compute fatigue effects on materials and structures.There have been a lot of developments in this area after the proposal Paris' Law. Most of the models proposed realted to fatigue crack propogation are deterministic and have some limitations such as that they arise from arbitary empirical assumptions. A proper estimation of fatigue crack porpogation rates with respect to residual stress and stress ratio helps us to estimate optimal materials for mechanical tasks. For e.g. : To determine the type of steel to be used when
we are building a bridge.

Initially Local strain-based approches were proposed to model fatigue crack propogation further a link was established between local strain-based approached to fatigue and Frature mechanics based fatigue crack propogation models. As research continued models were proposed that using residual stress concepts ecplained stress ratio effects as well as interaction effects on crack growth rates.Several approches were proposed which were analytical and or numerical.
The underlying concept behind the proposed local approaches for fatigue crack propagation modelling consists of
assuming fatigue crack propagation as a process of continuous failure of consecutive representative material elements
(continuous re-initializations). Such a kind of approaches has been demonstrated to correlate fatigue crack propagation data from several sources, including the stress ratio effects(refer our paper somewhere here). The crack tip stress-strain fields are computed using elastoplastic analysis, which are applied together a fatigue damage law to predict the failure of the representative material elements. The simplified method of Neuber  or Moftakhar et al. may be used to compute the elastoplastic stress field at the crack tip vicinity using the elastic stress distribution given by the Fracture Mechanics.  One Such model (given by Noorzi) the unigrow model, modelled the fatigue crack growth based on elastic–plastic crack tip stress–strain history regarded the process of fatigue crack propogation as a process of successive crack re-initiation in the crack tip region. 

Give references and explain research hierachy
5,6,7,8,9,1,10,11,12,13,14,16,17

We take the unigrow model and extend it to relate it with a probabilistic contruct to find probabilistic fatigue crack propagation rates various materials. 

Form the third paragraph using:

- How we first find the fatigue crack propogation rates deterministically
    - Morrows equation
    - Strain life relation
    - Stress relation
    - SWT relation
- we use the porbabilistic p ea n or p swt n fields based on weibull distribution to compute the probabilistic fields for fatigue crack propogation rates
    - Strain life field
    - SWT-N field
    
### 1.2 Motivation

The current deterministic works take into account a lot of parameters and some of these parameters cannot be determined easily or at all and hence these works take arbitary assumptions in the process of modelling. To solve this (Our Base Article) proposes a probabilistic model that not only arises from sound statistical and physical assumtions, it also manages to provide a probabilistic definiton of the whole strain-life field. Further, since mechanical modelling is a complex task and takes into account a lot of parameters, we have tried to simplify the process of finding probabilistic fatigue crack propogation fields.Not only this we have tried to use Least Square regression and maximum likely hood method to estimate certain parameters required for the task.

### 1.3 Problem Statement/ Case Study

- To determine probabilistic fields of fatigue crack propogation rates wrt residual stress and stress ratio.
    - Perfomance metric : how closely the computed probabilistic field data matches the experimental/deteriminstic data at a given parameter value (probability).

## 2 Data Acusition

- Yes, this Special Assignment is Data Dependent.
- The data has been gathered from :
    - Base Article
    - [19] De Jesus, A.M.P., Matos, R., Fontoura, B.F.C., Rebelo, C., Simões da Silva, L., Veljkovic, M., A comparison of the fatigue behavior between S355 and S690 steel grades, Journal of Constructional Steel Research, 79 (2012) 140–150. 

## 3 Probabilistic Model Used/ PRP Concept Used

Add Stuff Here From Sir Arpitsinhs's Notebook.

## 4 Pseudo Code/ Algorithm

Add Stuff Here From Sir Arpitsinhs's Notebook.

## 5 Coding and Simulation

### 5.1 Simulation Framework

We have used the Following parameters values for the simulations:

- parameters with short details and their values .( Maybe a Table).

### 5.2 Reproduced Figures

- Used tools:
    - Python
    - Matplotlib
    - Numpy
- Comparison of reproduced results and results from the paper along with slight explaination

### 5.3 New Work Done

Estimating and supplying analysis of parameters assumed/supplied externally and creating a closed form model with no external dependance that computes probabilistic fatigue crack propogation data using only the natural required input paramters.

#### 5.3.1 New Analysis

- Calculating weibull parameters using maximum likely hood func(compare them with those supplied in paper).
- Calculation SWT and Nf values using least squares regression and comparing them with those supplied in the paper.

#### 5.3.2 New Coding / Algorithm

- Coding and algorithm details here

#### 5.3.3 New Results

- Comparision of computed and given parameters.

#### 5.3.4 New Inferences

- Something like: parameter can be estimated using simple closed form coded solutions and shouldn't be estimated and or computed externally.

Students are advised to share the new derivations with results in correlation with the reproduce results.
Write clear inference for the new results. You are also advised to add new analysis along with the codes.

## 6 Inference Analysis/ Comparison

Add Stuff Here From Sir Arpitsinhs's Notebook.

## 7 Contribution of team members

### 7.1 Technical contribution of all team members

### 7.2 Non-Technical contribution of all team members

## 8 Submission checklist for uploading on Google Drive

This section provides the submission checklist for smooth and efficient submission process. (This is for your
reference and please remove this while writing your report).
- Soft copy of this project Report
- Soft copy of Abstract
- Soft copy of Concept Map 1 and 2
- Soft copy of base article
- Soft copy of analysis (hand written)(jupyter notebooks)
- Folder of matlab(python) codes (with proper naming)
- Folder of reproduced results in .fig and .jpg format
- latex (.tex) file of the project report.
