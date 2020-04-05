# School of Engineering and Applied Science (SEAS), Ahmedabad University
# B.Tech(ICT) Semester IV: Probability and Random Processes (MAT 202)

- Group No : S_M1
- Kaushal Patil (AU1841040), Arpitsingh Vaghela(AU1841034)
- Project Title : Modelling probabilistic fatigue crack propogation data and predicting model parameters

## 1 Introduction

### 1.1 Background

Mechanical modelling tends to be a very complex mathematical task.One of the most important problems realted to modelling probability in mechanics is to find the reliabity of materials that are used to build objects. A lot of research has taken place to compute fatigue effects on materials and structures.There have been a lot of developments in this area after the proposal Paris' Law. Most of the models proposed realted to fatigue crack propogation are deterministic and have some limitations such as that they arise from arbitary empirical assumptions.A proper estimation of fatigue crack porpogation rates with respect to residual stress and stress ratio helps us to estimate optimal materials for mechanical tasks. For e.g. : To determine the type of steel to be used when we are building a bridge. Proper estimation of fatigue crack proporgation and finding its probabilisitic curves also gives great insights to the propertiees of material and can be useful when the material is being improved, i.e. at the time of development on newer types of alloys. 

The First breakthrough in the field of fatigue propogation estimation was the Paris' Law which was followed by various approaches[3].Initially Local strain-based approches were proposed to model fatigue crack propogation on notch based components further a link was established between local strain-based approached to fatigue and Frature mechanics based fatigue crack propogation models.[1,5-10] As research continued models were proposed that using residual stress concepts ecplained stress ratio effects as well as interaction effects on crack growth rates.Several approches were proposed which were analytical and or numerical.[11-14]The underlying concept behind the proposed local approaches for fatigue crack propagation modelling consists of assuming fatigue crack propagation as a process of continuous failure of consecutive representative material elements (continuous re-initializations). Such a kind of approaches has been demonstrated to correlate fatigue crack propagation data from several sources, including the stress ratio effects[10-14]. The crack tip stress-strain fields are computed using elastoplastic analysis, which are applied together a fatigue damage law to predict the failure of the representative material elements. The simplified method of Neuber[15]  or Moftakhar[16] et al. may be used to compute the elastoplastic stress field at the crack tip vicinity using the elastic stress distribution given by the Fracture Mechanics.[1,16-17]  One Such model (given by Noorzi)[1,10-11] the unigrow model, modelled the fatigue crack growth based on elastic–plastic crack tip stress–strain history regarded the process of fatigue crack propogation as a process of successive crack re-initiation in the crack tip region. [1][0]


We take the unigrow model and extend it to relate it with a probabilistic contruct to find probabilistic fatigue crack propagation rates various materials. The Unigrow model to derive probabilistic fatigue crack propogation $ da/dN-\bigtriangleup K $ fields for a particular selected material ((S355) structural mild steel)[0], for distinct stress ratios.The Deterministic model uses Morrows equation, Strain life relation along with the SWT relation to model parameters deterministically.For Probabilistic approach the strain-life field proposed by Castillo and Fernandez-Canteli [20] and Shane-Watson-Topper-life field [0] which are based on Weibull Distribution are used to generalize the results to account for mean stress effects using percentile curves. The simulation was modelled using the data acquired[19,0] and was further extended where we tried to make a prediction model for Threshold value of life time[N0], Endurance limit of strain [E0], Fatigue Limit of SWT parameter[SWT] and the Weibull parameters(lambda(Position),delta(Scale),Beta(Shape)) by Running Batch Gradient Descent[Reference to ML Glossary] on Loss function from [27] and further using probability-weighted moments from [27] to predict N0,E0,SWT and Weibull parameters. The Probabilistic Life time fields are combined with Unigrow model [0-1] to finally compute the probabilistic fatigue crack proppogation field for distinct stress ratios. 


### 1.2 Motivation

The current deterministic works take into account a lot of parameters and some of these parameters cannot be determined easily or at all and hence these works take arbitary assumptions in the process of modelling. To solve this (Our Base Article) proposes a probabilistic model that not only arises from sound statistical and physical assumtions, it also manages to provide a probabilistic definiton of the whole strain-life field. Further, since mechanical modelling is a complex task and takes into account a lot of parameters, we have tried to simplify the process of finding probabilistic fatigue crack propogation fields.Not only this we have tried to use Gradient Descent Regression and Probability-weighted moments method to estimate certain parameters required for the task.

### 1.3 Problem Statement/ Case Study


- To determine probabilistic fields of fatigue crack propogation rates wrt residual stress and stress ratio.
    - Perfomance metric : how closely the computed probabilistic field data and plots matches the computed data and plots given in the base article 
- To propose a probabilistic Shane-Watson-Topper Field using the mathematical modelling of the Strain-Life Field proposed by Cantelli[20].
    - Performance metric : how closely the shape of  p-SWT-n curve match the experimental/deteriminstic data at a given parameter value (probability)
       

## 2 Data Acusition

- Yes, this Special Assignment is Data Dependent.
- The data has been gathered from :
    - Base Article
    - [19] De Jesus, A.M.P., Matos, R., Fontoura, B.F.C., Rebelo, C., Simões da Silva, L., Veljkovic, M., A comparison of the fatigue behavior between S355 and S690 steel grades, Journal of Constructional Steel Research, 79 (2012) 140–150. 
    - sythetic experimental data created by looking at plots in the base article using basic linear equations.

## 3 Probabilistic Model Used/ PRP Concept Used

---
#### General information on Weibul Distribution
---
If $X$ is a random variable denoting the _time to failure_, the __Weibull distribution__ gives a distribution for which the _failure rate_ is proportional to a power of time.

$$
f_X(x) = 
\frac{\beta}{\delta}(\frac{x-\lambda}{\delta})^{\beta-1}e^{-(\frac{x-\lambda}{\delta})^\beta}
$$
$$
F_X(x;\lambda,\delta,\sigma) = 1-e^{-({\frac{x-\lambda}{\delta}})^\beta}
$$

where $\beta > 0$ is the __shape parameter__, 

$\delta > 0$ is the __scale parameter__,

$\lambda > x$ is the __location parameter__ (the minimum value of X).

Percentile points,

$$
x_p = \lambda + \delta(-log(1-p))^{\frac{1}{\beta}}
$$
where $0\leq p\leq 1$ 

__Important Properties of Weibull Distribution__

- Stable with respect to location and scale
$$
X \sim W(\lambda,\delta,\beta) \iff \frac{X-a}{b} \sim W(\frac{\lambda-a}{b},\frac{\delta}{b},\beta)
$$

- It is stable with respect to Minimum Operations.i.e., if $X_1,X_2,X_3,.....X_m$ are independent and identical distribution,then 
$$
X_i\sim W(\lambda,\delta,\beta) \iff min(X_1,X_2,....,X_m) \sim W(\lambda,\delta m^{\frac{1}{\beta}},\beta)
$$
if a set of independent and identical distribution is weibull then its minimum is also a Weibull Random Variable
---
#### Relevant Variable involved for modeling:
---
$P$:Probability of fatigue faliure<br>
$N$:Number of stress cycles to failure<br>
$N_0$:Threshold value of N (min lifetime)<br>
$Ea$: Strain <br>
$Ea_0$: Endurance limit of Ea;<br> 
$SWT$:Smith,Watson and Topper fatigue damage parameter<br> 
$SWT_0$:Fatigue limit<br>

Putting Related variables together we have three varaibles(based on II Theorem)<br>
##### For Strain Life Field
$$

\frac{N}{N_0},\frac{Ea}{Ea_0},P \\
P = q(\frac{N}{N_0},\frac{Ea}{Ea_0})
$$
where $q()$ is a function we are to determine<br>
so P can be any monotone function of $\frac{N}{N_0},\frac{Ea}{Ea_0}$ , as $h(\frac{N}{N_0})$ $\&$ $g(\frac{Ea}{Ea_0})$

We denote them as 
$$
N^* = h(\frac{N}{N_0}) \\
SWT^* = g(\frac{Ea}{Ea_0})
$$

##### For SWT Life Field
$$
\frac{N}{N_0},\frac{SWT}{SWT_0},P \\
P = q(\frac{N}{N_0},\frac{SWT}{SWT_0})
$$
where $q()$ is a function we are to determine<br>
so P can be any monotone function of $\frac{N}{N_0},\frac{SWT}{SWT_0}$ , as $h(\frac{N}{N_0})$ $\&$ $g(\frac{SWT}{SWT_0})$

We denote them as 
$$
N^* = h(\frac{N}{N_0}) \\
SWT^* = g(\frac{SWT}{SWT_0})
$$

---
#### Proper Modelled Construct

---

##### Strain-Life Field

$$
p = F(N^*_f;E^*_a) = 1 - exp(-(\frac{log\frac{N_f}{N_0}log\frac{Ea}{Ea_0}-\lambda}{\delta})^\beta)
$$

here $log(\frac{N_f}{N_0})loglog\frac{Ea}{Ea_0} \geq \lambda$

p is the probability of failure, N0 and εa0 are normalizing values, and λ, δ and β are the non-dimensional Weibull
model parameters.

$$
N^*Ea^* \sim W(\lambda,\delta,\beta) \\
N^*_f\sim W(\frac{\lambda}{Ea^* },\frac{\delta}{Ea^* },\beta) \\
$$

##### Proposed SWT-N or S-N Field

We have proposed SWT field as it has advantages over the normal strain life field as it uses the SWT fatigue damage parameter.Using this Damage Parameter we can account for mean stress effects on fatigue life
prediction.

$$
p = F(N^*_f;E^*_a) = 1 - exp(-(\frac{log\frac{N_f}{N_0}log\frac{SWT}{SWT_0}-\lambda}{\delta})^\beta)
$$

here $log(\frac{N_f}{N_0})loglog\frac{SWT}{SWT_0} \geq \lambda$

p is the probability of failure, N0 and $SWT_0$ are normalizing values, and λ, δ and β are the non-dimensional Weibull
model parameters.

$$
N^*Ea^* \sim W(\lambda,\delta,\beta) \\
N^*_f\sim W(\frac{\lambda}{SWT^* },\frac{\delta}{SWT^* },\beta) \\
$$

---
#### Justification of Weibull for S-N fields
---
Considerations:

- __Weakest Link__: Fatigue lifetime of a longitudinal element is the minimum of its constituting particles.Thus we need minimum model for a longitudinal element $L = ml$

- __Stability__: The distribution function must hold for different lengths.

- __Limit Behaviour__: Need Asymptotic family of Distribution

- __Limited Range__: $N^*$ & $SWT^*$ has finite lower bound,coincide with theoretical end of CDF
$$
N\geq N_0 \\
SWT \geq SWT_0 
$$
- __Compatibility__: $$E(N^*;SWT^*) = F(SWT^*;N^*)$$ i.e., Distribution of $N^*$ can be determined based on given $SWT^*$ and similarly $SWT^*$ from $N^*$.

___All these are Statisfied by Weibull Distribution___

$$E(N^*;SWT^*) = F(SWT^*;N^*)$$
becomes
$$
[\frac{SWT^*-\lambda(N^*)}{\delta(N^*)}] ^{\beta(N^*)} = [\frac{N^*-\lambda(SWT^*)}{\delta(SWT^*)}] ^{\beta(SWT^*)}
$$

Best fitted Solution:
$$
\lambda(N^*) = \frac{\lambda}{N^* - B} \\
\delta(N^*) = \frac{\delta}{N^* - B} \\
\beta(N^*) = \beta
$$
and


$$
\lambda(SWT^*) = \frac{\lambda}{SWT^* - C} \\
\delta(SWT^*) = \frac{\delta}{SWT^* - C} \\
\beta(SWT^*) = \beta
$$

results in,
$$
E[N^*;SWT^*] = F[SWT^*;N^*] \\ \\
= 1 - exp\lbrace -(\frac{(N^*-B)(SWT^*-C)-\lambda}{\delta})^{\beta}\}
$$

since $SWT^* \longrightarrow \infty$ a lower end for $N^* = h(\frac{N}{N_0)}) = h(1)$ must exists such that $B = h(1)$,<br>
similarly for $N^* \longrightarrow \infty$, $C = g(1)$

The percentile curve is constant.
$$
\frac{N^*SWT^*  - \lambda}{\delta} = constant
$$

- The Zero-percentile curve represents the minimum possible $N_f$ for different values of $SWT$ and is a hyperbola
As $log$ is used for $N_f$ and $SWT$ we choose,
$$
h(x)=g(x) = log(x)
$$

therefore,
$$
N^* = log(\frac{N}{N_0}) \\ SWT^* = log(\frac{SWT}{SWT_0}) \\
$$

$B = C = log(1) = 0$
$$E(N^*;SWT^*) = F(SWT^*;N^*) \\
= 1 - exp\{-(\frac{N^*SWT^*}{\delta})^{\beta} \} 
$$

$p$-curves
$$
log(\frac{SWT}{SWT^*}) = \frac{\lambda + \delta[-log(1-p)]^{\frac{1}{\beta}}}{log(\frac{N}{N_0})}
$$

Final Distribution
$$
N^*SWT^* \sim W(\lambda,\delta,\beta) \\
log(\frac{N}{N_0)})log(\frac{SWT}{SWT_0}) \sim W(\lambda,\delta,\beta) \\
log(\frac{N}{N_0)})\sim W(\frac{\lambda}{log(\frac{SWT}{SWT_0}) },\frac{\delta}{log(\frac{SWT}{SWT_0}) },\beta) \\
$$
----
The values for this model are:

|$logN_0$|$logSWT_0$|$\lambda$|$\delta$|$\beta$|
|----|----|----|----|----|
|-4.1079|-4.4317|53.8423|7.2698|3.6226|

|$logN_0$|$log\epsilon_{a0}$|$\lambda$|$\delta$|$\beta$|
|----|----|----|----|----|
|-3.2593|-9.1053|36.6676|5.8941|4.6952|



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
#### Comparison of results:

##### Probabilistic Strain Life Field

![penpaper](images/p_e_n_paper.png) <br>
![penmodel](images/p_e_n_model.png)<br>

__The Above plots are for Strain vs Number of Cycles to Failure for percent of probability along with postulated data (Experimental for 0.5 Percent).__

![psnpaper](images/p_s_n_paper.png) <br>
![psnmodel](images/p_s_n_moedel.png)<br>

__The Above plots are for SWT Damage Parameter vs Number of Cycles to Failure for percent of probability along with postulated data (Experimental for 0.5 Percent).__




### 5.3 New Work Done

Estimating and supplying analysis of parameters assumed/supplied externally and creating a closed form model with no external dependance that computes probabilistic fatigue crack propogation data using only the natural required input paramters.




#### 5.3.1 New Analysis

- To Estimate and Check if the SWT-N parameters can be predicted using gradient descent based regression.
    - Performance metric : To see if the Loss is reduced by Gradient descent or not and if the gradient descent works, if the predicted values match the supplied data.
-  Estimate the parameters of Weibull Distribution using PWM estimation on real and predicted data.
    - Performance metric : To compare and see if the computed Weibull parameters using PWM match those supplied with the paper and if the predicted vs deterministic parameters match.

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




[1] Noroozi, A.H., Glinka, G., Lambert, S., A two parameter driving force for fatigue crack growth analysis, International
Journal of Fatigue, 27 (2005)1277-1296.
[2] Schütz, W., A History of Fatigue, Engineering Fracture Mechanics, 54 (1996) 263-300.
[3] Paris, P.C., Gomez, M., Anderson, W.E., A rational analytic theory of fatigue, Trend Engineering, 13 (1961) 9-14.
[4] Beden, S.M., Abdullah, S., Ariffin, A.K., Review of Fatigue Crack Propagation Models for Metallic Components,
European Journal of Scientific Research, 28 (2009) 364-397.
[5] Coffin, L.F., A study of the effects of the cyclic thermal stresses on a ductile metal, Translations of the ASME, 76
(1954) 931-950.
[6] Manson, S.S., Behaviour of materials under conditions of thermal stress, NACA TN-2933, National Advisory
Committee for Aeronautics, (1954).
[7] Morrow, J.D., Cyclic plastic strain energy and fatigue of metals, Int. Friction, Damping and Cyclic Plasticity, ASTM
STP 378, (1965) 45-87.
[8] Smith, K.N., Watson, P., Topper, T.H., A Stress-Strain Function for the Fatigue of Metals, Journal of Materials, 5(4)
(1970) 767-778.
[9] Shang, D.-G., Wang, D.-K., Li, M., Yao, W.-X., Local stress–strain field intensity approach to fatigue life prediction
under random cyclic loading, International Journal of Fatigue, 23 (2001) 903–910.
[10] Noroozi, A.H., Glinka, G., Lambert, S., A study of the stress ratio effects on fatigue crack growth using the unified
two-parameter fatigue crack growth driving force, International Journal of Fatigue, 29 (2007) 1616-1633.
[11] Noroozi, A.H., Glinka, G., Lambert, S., Prediction of fatigue crack growth under constant amplitude loading and a
single overload based on elasto-plastic crack tip stresses and strains, Engineering Fracture Mechanics, 75 (2008) 188-
206.
[12] Peeker, E., Niemi, E., Fatigue crack propagation model based on a local strain approach, Journal of Constructional
Steel Research, 49 (1999) 139–155.
[13] Glinka, G., A notch stress-strain analysis approach to fatigue crack growth, Engineering Fracture Mechanics, 21
(1985) 245-261.
[14] Hurley, P.J., Evans, W.J., A methodology for predicting fatigue crack propagation rates in titanium based on damage
accumulation, Scripta Materialia, 56 (2007) 681–684.
[15] Neuber, H., Theory of stress concentration for shear-strained prismatic bodies with arbitrary nonlinear stress–strain
law, Trans. ASME Journal of Applied Mechanics, 28 (1961) 544–551.
[16] Moftakhar, A., Buczynski, A., Glinka, G., Calculation of elasto-plastic strains and stresses in notches under multiaxial
loading, International Journal of Fracture, 70 (1995) 357-373.
[17] Reinhard, W., Moftakhar, A., Glinka, G., An Efficient Method for Calculating Multiaxial Elasto-Plastic Notch Tip
Strains and Stresses under Proportional Loading, Fatigue and Fracture Mechanics, ASTM STP 1296, R.S. Piascik, J.C.
Newman, N.E. Dowling, Eds., American Society for Testing and Materials, 27 (1997) 613-629.
[18] Mikheevskiy, S., Glinka, G., Elastic–plastic fatigue crack growth analysis under variable amplitude loading spectra,”
International Journal of Fatigue, 31 (2009) 1828–1836.
[19] De Jesus, A.M.P., Matos, R., Fontoura, B.F.C., Rebelo, C., Simões da Silva, L., Veljkovic, M., A comparison of the
fatigue behavior between S355 and S690 steel grades, Journal of Constructional Steel Research, 79 (2012) 140–150.
[20] Castillo, E., Fernández-Canteli, A., A Unified Statistical Methodology for Modeling Fatigue Damage, Springer, (2009).
[21] Basquin, O.H., The exponential law of endurance tests, In: Proc. Annual Meeting, American Society for Testing
Materials, 10 (1910) 625-630.
[22] Creager, M., Paris, P.C., Elastic field equations for blunt cracks with reference to stress corrosion cracking,
International Journal of Fracture Mechanics, 3 (1967) 247–252.
[23] Molski, K., Glinka, G., A method of elastic-plastic stress and strain calculation at a notch root, Materials Science and
Engineering, 50 (1981) 93-100.
[24] Glinka, G., Development of weight functions and computer integration procedures for calculating stress intensity
factors around cracks subjected to complex stress fields, Progress Report No.1: Stress and Fatigue-Fracture Design,
Petersburg Ontario, Canada, (1996).
[25] Sadananda, K., Vasudevan, A.K., Kang, I.W., Effect of Superimposed Monotonic Fracture Modes on the ΔK and
Kmax Parameters of Fatigue Crack Propagation, Acta Materialia, 51(22) (2003) 3399-3414. 
[26] Kajawski, D., A new (ΔK+Kmax)0.5 driving force parameter for crack growth in aluminum alloys, International
Journal of Fatigue, 23(8) (2001) 733-740.
[27] Castillo, E., Galambos, J., Lifetime Regression Models Based on a Functional Equation of Physical Nature”, Journal
of Applied Probability, 24 (1987) 160-169.
[28] Castillo, E., Fernández-Canteli, A., Hadi, A.S., López-Anelle, M., A Fatigue Model with Local Sensitivity Analysis,
Fatigue and Fracture of Engineering Material and Structure, 30 (2006) 149–168.
[29]ASTM E606: Standard Practice for Strain-Controlled Fatigue Testing, Annual Book of ASTM Standards, ASTM,
West Conshohocken, PA, USA, 03.01 (1998)
[30]ASTM E647: Standard Test Method for Measurement of Fatigue Crack Growth Rates, Annual Book of ASTM
Standards, ASTM, West Conshohocken, PA, USA, 03.01 (2000).
[31] SAS, ANSYS, Swanson Analysis Systems, Inc., Houston, Version 12.0, (2011).
[32] Ramberg, W., Osgood, W.R., Description of the stress-strain curves by the three parameters, NACA TN-902,
National Advisory Committee for Aeronautics, (1943). 