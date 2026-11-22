# Exact minimal hybrid observations for a decaying environmental pulse and a passive sampler

## Finding
Consider an initially empty passive sampler exposed to a freely decaying environmental signal. The two positive decay rates cannot be labelled from the *entire passive trace* alone. Nevertheless, for any fixed spacing \(\Delta>0\), a small, precisely specified combination of active and passive observations identifies all model parameters, including when the decay rates coincide.

**Calibrated uptake.** When sampler uptake gain \(k>0\) is known, the three exact scalars \(C(\Delta)\), \(P(\Delta)\), \(P(2\Delta)\) uniquely identify environmental decay \(\lambda>0\), sampler loss \(\delta>0\), and initial environmental concentration \(C_0>0\). Three is the minimum number of scalar observations among this experiment's active and passive readouts for generic global identification.

**Uncalibrated uptake.** When \(k\) is unknown and positive, the four scalars \(C(\Delta)\), \(C(2\Delta)\), \(P(\Delta)\), and \(P(2\Delta)\) uniquely identify \((\lambda,\delta,k,C_0)\). In the generic distinct-rate model, fewer than two distinct-time active and two distinct-time passive observations cannot globally identify all four parameters, even if arbitrarily many readouts of the other type are collected. Both inverse formulas remain nonsingular at \(\lambda=\delta\) for admissible strictly interior parameters.

## Assumptions and scope
Let \(C(t)\) denote the ambient concentration after a single pulse at time zero, and \(P(t)\) the amount retained by a passive device, for \(t\geq0\). Assume the exactly linear, nondepleting kinetic model
\[
\dot C=-\lambda C,\quad C(0)=C_0>0,\qquad
\dot P=k C-\delta P,\quad P(0)=0,
\]
with \(\lambda,\delta,k>0\). An *active* measurement gives exact \(C(t)\); a *passive* measurement gives exact \(P(t)\) at the indicated time, from the same deployment initiated at zero. The gain \(k\) is either separately calibrated or completely unknown, as specified. Multiple passive readings are assumed non-destructive. The model excludes continued shedding, back-reaction on ambient signal, time-varying hydraulic transport, nonlinear capacity, and measurement noise. It is a theoretical identifiability statement, not a validated model of any particular field material.

By integrating the linear equations,
\[
C(t)=C_0e^{-\lambda t},\qquad
P(t)=kC_0\frac{e^{-\lambda t}-e^{-\delta t}}{\delta-\lambda}
\]
for distinct rates, with the continuous coincident-rate expression \(P(t)=kC_0t e^{-\lambda t}\) when \(\delta=\lambda\). Define dimensionless survival factors
\[
a=e^{-\lambda\Delta},\qquad b=e^{-\delta\Delta},\qquad
L(u)=\begin{cases}\dfrac{u-1}{\log u},&u>0,\ u\ne1,\\[3pt]1,&u=1.\end{cases}
\]
Thus \(0<a,b<1\), and \(L\) is the logarithmic mean of \(1\) and \(u\). Writing \(C_j=C(j\Delta)\), \(P_j=P(j\Delta)\), direct substitution gives
\[
C_1=C_0a,\quad C_2=C_0a^2,\quad
P_1=k\Delta C_0a L(b/a),\quad
\frac{P_2}{P_1}=a+b.
\]
These identities are continuous at \(a=b\).

## Proof
### Known uptake gain: three observations suffice
From \(C_1,P_1,P_2\), form two positive observables
\[
r=\frac{P_2}{P_1},\qquad z=\frac{P_1}{k\Delta C_1}.
\]
The model identities imply \(r=a+b\) and \(z=L(b/a)\). To invert the latter, note the integral representation
\[
L(u)=\int_0^1 u^s\,ds,
\]
valid for all \(u>0\), including \(u=1\). Consequently \(L\) is continuous and strictly increasing, mapping \((0,\infty)\) onto \((0,\infty)\); its derivative is
\[
L'(u)=\int_0^1 s u^{s-1}\,ds>0,
\qquad L'(1)=\frac12.
\]
Thus there is exactly one \(u>0\) satisfying \(L(u)=z\). The unique reconstruction is
\[
\boxed{
 a=\frac{r}{1+u},\quad b=\frac{ru}{1+u},\quad
 \lambda=-\frac{\log a}{\Delta},\quad
 \delta=-\frac{\log b}{\Delta},\quad C_0=\frac{C_1}{a}.}
\]
For exact observations from an admissible model, the reconstructed \(a,b\) lie in \((0,1)\). The construction proves global uniqueness for every positive rate, not only generically. Because \(L'(1)=1/2\), the inverse of \(L\) is continuously differentiable at \(u=1\); the remaining operations have nonzero denominators and smooth logarithms at \(a=b\in(0,1)\). Hence rate collision causes no local singularity in this reconstruction.

Three is minimal for identification of the three free model parameters by two types of continuous scalar readout. Indeed, any two-scalar observation map is continuous on an open subset of \(\mathbb R^3\); such a map cannot be one-to-one on an open subset (an immediate consequence of invariance of domain, after embedding the target \(\mathbb R^2\) as a plane in \(\mathbb R^3\)). More concretely, using \(C_1,P_1\) alone fixes the ratio \(b/a\), but allows a continuum of admissible positive choices for \(a\) and corresponding \(b\), with \(C_0=C_1/a\). Two passive samples admit a rate-swap ambiguity, and two active samples contain no sampler-loss information.

### Unknown uptake gain: two of each type suffice and are necessary
Given \(C_1,C_2,P_1,P_2\), compute
\[
\boxed{
 a=\frac{C_2}{C_1},\qquad b=\frac{P_2}{P_1}-a,
 \qquad C_0=\frac{C_1}{a},
 \qquad k=\frac{P_1}{\Delta C_1L(b/a)},
 \qquad
 \lambda=-\frac{\log a}{\Delta},\quad
 \delta=-\frac{\log b}{\Delta}.}
\]
For admissible exact data, \(a,b\in(0,1)\) and \(k,C_0>0\), proving global identification and constructive feasibility. Since \(L(1)=1\), this formula also extends smoothly across coincident rates. Unlike differentiating a recovered passive-only two-exponential signal, it does not divide by \(a-b\).

For necessity of at least two active times when \(k\) is unknown, fix any *single* active observation time \(\tau>0\), and any distinct positive rates. Define an alternative model by swapping the rate names, \(\lambda'=\delta\), \(\delta'=\lambda\), and setting
\[
C_0'=C_0e^{(\delta-\lambda)\tau},\qquad
k'=kC_0/C_0'.
\]
Then \(C_0'e^{-\lambda'\tau}=C_0e^{-\lambda\tau}\), while the full passive traces are identical, because \(P(t)\) depends symmetrically on the unordered pair of rates and on the product \(kC_0\). Hence *even an arbitrarily dense passive trace plus only one active time* is not generically globally identifying. Zero active times certainly do not resolve the ambiguity. Conversely, with two active times, \(\lambda,C_0\) are recovered from their exponential ratio, but a single passive observation supplies only one equation for the two remaining unknowns \(\delta,k\): for every admissible \(\delta>0\), choosing the positive gain to match the observed \(P_1\) produces the same three observations. Thus at least two distinct-time observations of each type are required. Our four-scalar design meets both lower bounds.

### Passive-only ambiguity and the collision contrast
The passive recurrence can identify only *unlabelled* exponential factors. For example, three passive observations give
\[
s=\frac{P_2}{P_1}=a+b,\qquad
ab=s^2-\frac{P_3}{P_1},
\]
so \(a,b\) are the unordered roots of \(\xi^2-s\xi+ab=0\). Permuting the two rates leaves all passive measurements unchanged, a classical flip-flop phenomenon in two-exponential kinetics (not an originality claim here).

In addition, for a fixed positive common rate \(r_0\) and small symmetric splitting \(\lambda=r_0+\varepsilon\), \(\delta=r_0-\varepsilon\), the whole passive trajectory is
\[
P(t)=kC_0e^{-r_0t}\frac{\sinh(\varepsilon t)}{\varepsilon}
=kC_0te^{-r_0t}\left(1+\frac{\varepsilon^2t^2}{6}+O(\varepsilon^4)\right).
\]
Thus passive-only readings have quadratic sensitivity to this symmetric splitting at a collision, and exactly zero ability to tell the rate labels apart. By contrast, the active reading changes to first order when environmental rate \(\lambda\) changes and the initial concentration is held fixed, and both mixed inverse maps above are locally smooth at equality. This is a structural conditioning comparison, not a uniform noisy-error guarantee over the whole parameter space.

## Verification
The self-contained standard-library script `verify.py` independently generates exact model observations, reconstructs parameters through both formulas (including equal and nearly equal rates), tests the passive rate-swap ambiguity, and checks the quadratic collision behavior. It records 128,008 successful supplementary numerical assertions with a fixed seed. Such finite tests support implementation fidelity; the analytic arguments above establish the claims for all admissible parameters. Run from the same directory with `python3 verify.py`.

## Relationship to prior work
Chen and colleagues (2024) showed that passive eDNA sampling can complement active water filtration for rare species and explicitly flagged uncertain sampled water volume as a barrier to estimating ambient concentrations. Their empirical work does not establish this idealized pulse-kinetic inverse theorem. Hawker (2009) already derives the response of a first-order passive sampler to an exponentially decreasing ambient concentration and demonstrates recovery from a richer temporal sampler response with calibration; neither this response law nor that broad inference principle is claimed new. Kuan, Wright and Duffull (2023) explicitly describe the two-exponential flip-flop parameter-permutation ambiguity, which this result incorporates as known background. The structural-identifiability theory of linear compartmental systems likewise covers general observability and identifiability principles; the distinct contribution claimed here is the exact *finite hybrid measurement count and constructive formulas for both calibration regimes*, with a nonsingular collided-rate branch, rather than an assertion that rate exchange or hybrid observability is previously unknown. Closely related identifiability formulas may exist elsewhere; historical priority is not certified.

## Limitations
No claim is made about realistic stochastic eDNA shedding, mixing, assay detection limits, device saturation, non-destructive re-reading feasibility in field deployments, or real monitoring accuracy. Data are exact, paired, same-scale quantitative measurements, and the sampler gain in the calibrated regime must be known independently. Near-vanishing signals and large time intervals can be numerically ill-conditioned despite smoothness at equal interior rates. General observation schedules other than the stated evenly spaced design are not classified. The lower bounds refer to scalar readouts of the specified active/passive types with unknown parameters as stated, and generic global identifiability, not pointwise identifiability on special lower-dimensional parameter submanifolds.

## References
1. Chen, X., Li, S., Zhao, J. and Yao, M. (2024). *Passive eDNA sampling facilitates biodiversity monitoring and rare species detection.* Environment International 187, 108706. First publicly available April 26, 2024. https://doi.org/10.1016/j.envint.2024.108706
2. Kuan, W.-L., Wright, D. F. B. and Duffull, S. B. (2023). *The influence of flip-flop in population pharmacokinetic analyses.* CPT: Pharmacometrics & Systems Pharmacology. https://doi.org/10.1002/psp4.12909
3. Ovchinnikov, A., Pogudin, G. and Thompson, P. (2019). *Input-output equations and identifiability of linear ODE models.* https://arxiv.org/abs/1910.03960
4. *Critical Review of Factors Governing Data Quality of Integrative Samplers Employed in Environmental Water Monitoring* (2016). Discussion of accumulative sampling and kinetic calibration. https://pmc.ncbi.nlm.nih.gov/articles/PMC4822337/
5. Hawker, D. W. (2009). *Modeling the response of passive samplers to varying ambient fluid concentrations of organic contaminants.* Environmental Toxicology and Chemistry 29, 591–596 (2010), first published December 2, 2009. https://doi.org/10.1002/etc.69
6. Alsammani, A. (2026). *A Tutorial on Symbolic Structural Identifiability Analysis of ODE Models in Julia.* Bulletin of Mathematical Biology. https://doi.org/10.1007/s11538-026-01779-0
