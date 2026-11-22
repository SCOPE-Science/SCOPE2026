# Opposite primer-allocation reversals for all-taxon detection and expected richness

## Finding

Two natural detection objectives can prescribe *opposite* primer mixtures at two distinct effort budgets. For three known-present targets, optimizing the probability that **every** target is detected need not agree with optimizing the expected number detected, even when both assays detect every target at a strictly positive rate. In the exactly specified positive-rate example below, the preferred use of assay A first appears and later disappears for each objective, at four distinct exact thresholds.

Set \(z_\pm=(7381\pm\sqrt{31044841})/20202\). For the all-target probability, the unique optimum \(x_F(T)\) uses A precisely for
\[
\log(6/5)<T<\log 10.
\]
For expected richness, the unique optimum \(x_E(T)\) uses A precisely for
\[
-\log z_+<T<-\log z_-.
\]
Whenever A is used, its optimal amount is strictly between zero and \(T\). The four boundaries are strictly ordered:
\[
\log(6/5)<-\log z_+<\log 10<-\log z_-.
\]
Consequently, the all-target optimizer alone uses A on \((\log(6/5),-\log z_+)\), and the expected-richness optimizer alone uses A on \((\log 10,-\log z_-)\); both use A between the middle boundaries, and neither uses A outside the outer boundaries. At every boundary an objective transitioning to B-only has \(x=0\) as its **unique** optimum.

This enter-and-exit behavior for the all-target objective is impossible with just one or two targets, for *any* strictly positive pairs of per-target assay rates; three targets are therefore sharp for this phenomenon.

## Assumptions and scope

There are three known-present, distinct taxa \(i=1,2,3\). One divides a continuously divisible normalized budget \(T>0\) between primer assays A and B: \(x\in[0,T]\) units of A and \(T-x\) units of B. Conditional on target presence, the count of successful detections for taxon \(i\) is a Poisson random variable with mean
\[
\mu_i(x,T)=a_ix+b_i(T-x)=b_iT+d_ix,
\qquad d_i=a_i-b_i.
\]
Counts for distinct taxa are independent. Detecting a taxon means at least one positive count; read counts are not constrained to a fixed sum. No initial presence uncertainty, false detections, shared amplification competition, assay startup cost, or integer read budget is included.

The chosen strictly positive rational rate vectors are
\[
(b_1,b_2,b_3)=(1,2,3),\qquad
(a_1,a_2,a_3)=\left(\frac9{10},\frac{18981}{5800},\frac{7299}{5800}\right),
\]
so \(d=(-580,7381,-10101)/5800\). Each assay independently has a nonzero chance to detect every target at any strictly positive effort. Define
\[
F_T(x)=\prod_{i=1}^3(1-e^{-\mu_i}),\qquad
E_T(x)=\sum_{i=1}^3(1-e^{-\mu_i}).
\]
Both are optimized over the *same* feasible allocation interval. The first is a probability, the second an expected count; they are not interchangeable objectives.

## Proof

**1. Exact optimization gate.** Since all \(\mu_i>0\), maximizing \(F_T\) is equivalent to maximizing its logarithm. Direct differentiation gives
\[
\partial_x\log F_T(x)=\sum_{i=1}^3\frac{d_i}{e^{\mu_i}-1},\quad
\partial_x^2\log F_T(x)=-\sum_{i=1}^3\frac{d_i^2e^{\mu_i}}{(e^{\mu_i}-1)^2}<0.
\]
Likewise
\[
\partial_xE_T(x)=\sum_{i=1}^3d_ie^{-\mu_i},\quad
\partial_x^2E_T(x)=-\sum_{i=1}^3d_i^2e^{-\mu_i}<0.
\]
The displayed strict inequalities hold for every \(T>0\) and \(0\le x\le T\), because at least one \(d_i\ne0\). Hence both objectives have a unique optimizer. At \(x=T\), the \(i=2\) positive contribution is overpowered by the \(i=3\) negative contribution in *both* derivatives: \(a_2>a_3>0\) and \(-d_3>d_2>0\), while \(d_1<0\). Thus both derivatives are strictly negative at \(T\). Strict concavity then says their unique optimizer is \(0\) if and only if the corresponding derivative at \(0\) is nonpositive; otherwise it lies strictly in \((0,T)\). In particular no A-only optimum exists.

**2. All-target thresholds.** Let \(t=e^T>1\). Rational common-denominator simplification yields the exact identity
\[
\partial_x\log F_T(0)
=\sum_{i=1}^3\frac{d_i}{e^{b_iT}-1}
=-\frac{(t-10)(5t-6)(116t+55)}{5800(t-1)(t+1)(t^2+t+1)}.
\]
All denominator factors are positive for \(t>1\); the last numerator factor is positive. Hence the derivative is positive precisely when \(6/5<t<10\), zero at \(t=6/5,10\), negative otherwise. The strict-concavity gate proves the all-target claim including equality cases.

**3. Expected-richness thresholds.** With \(z=e^{-T}\in(0,1)\),
\[
\partial_xE_T(0)=\frac{z}{5800}(-580+7381z-10101z^2).
\]
The quadratic has exactly the two positive roots \(z_\pm=(7381\pm\sqrt{31044841})/20202\), with \(0<z_-<z_+<1\), and is positive exactly between them. Reversing order under \(z=e^{-T}\) gives \(-\log z_+<T<-\log z_-\). Exact evaluations of the quadratic at \(z=5/6\) and \(z=1/10\) give, respectively, \(-5775/4<0\) and \(5709/100>0\); because the roots lie in \((0,1)\) these establish the strict interlacing of the four thresholds. Again strict concavity establishes all equality cases.

**4. Sharp minimum of three taxa for reentry.** For one target the sign of \(\partial_x\log F_T(0)\) is the fixed sign of \(a_1-b_1\). For two targets with distinct B rates \(b_1,b_2>0\), that sign is the sign of
\[
\frac{d_1}{e^{b_1T}-1}+\frac{d_2}{e^{b_2T}-1}.
\]
If the two \(d_i\) have the same weak sign, the derivative cannot change sign (including the degenerate case where both vanish). If their signs differ, a zero would require \((e^{b_2T}-1)/(e^{b_1T}-1)=-d_2/d_1\). The ratio is strictly monotone in \(T>0\), since the derivative of its logarithm is
\[
\frac{b_2}{1-e^{-b_2T}}-\frac{b_1}{1-e^{-b_1T}},
\]
whose sign is the sign of \(b_2-b_1\): the function \(u\mapsto u/(1-e^{-uT})\) has positive derivative for \(u>0\) by \(e^v>1+v\). Equal B rates leave a constant sign, possibly identically zero. Therefore the sign of the derivative at B-only can change at most once for two taxa. If both deviations vanish, every allocation ties but no change of preference occurs. Since the objective is strictly concave in allocation, reentry from B-only to mixing and back is impossible with fewer than three taxa. Our three-target rates attain two crossings.

## Verification

The attached standalone `verify.py` recomputes the threshold polynomial identities over exact rational numbers, checks the exact quadratic discriminant and the strict order of the four boundaries, then independently performs 64,800 randomized objective comparisons to the numerically bisection-derived unique optimum (with a floating-point tolerance of \(3\times10^{-12}\)). It also checks illustrative budgets \(T=0.1,0.3,0.6,2.35,2.8\), and a mesh of two-target ratio monotonicity. These finite checks test implementation; the proof above, not finite sampling, establishes the assertions for all allowed budgets.

Approximate threshold values in ascending order are \(0.182321556794\), \(0.444470419878\), \(2.302585092994\), and \(2.412891184411\). At \(T=0.3\), the all-target objective allocates about \(2.8865\%\) of effort to A, while expected richness chooses B alone. At \(T=2.35\), the all-target objective chooses B alone while expected richness allocates about \(1.2380\%\) to A. These percentages are consequences of the specified hypothetical rates, not estimates of actual primer performance.

To reproduce with Python 3 standard library: `python verify.py`. No external packages or datasets are needed.

## Relationship to prior work

How et al. (2024) directly investigate three primers, heterogeneous taxon sensitivity, and efficient eDNA sampling volumes; their reported objective and empirical sampling design do not give the exact dual-objective, continuously split assay budget construction above. Baetscher et al. (2023) experimentally select a complementary marker *set* for species recovery, using an iterative addition and detection-coverage curve, rather than deriving continuous effort-allocation optima or the two opposing budget intervals. Fukaya et al. (2022; first online 2021) optimize a posterior-expected detected-species utility under replicate and sequencing-depth costs for a single MiFish primer; that is an important broader design framework but does not imply the explicit two-assay all-target-probability phase diagram.

The derivative gate and strict concavity are standard analytic techniques and are not claimed as new in isolation. The specific jointly feasible, strictly positive rational witness, the exact four interlaced boundaries, the two opposite objective disagreements, and the sharp two-target obstruction form the assessed combined result. Broader historical assay-design and optimization literature may have related formulations; priority remains provisional.

## Limitations

This is an idealized Poissonized detection model, not a calibrated eDNA sampling protocol. Real sequence counts may compete for a fixed read depth; species detections can be dependent; PCR efficiencies, false positives, uncertain occurrence, sample volume, technological constraints, and integer budget or primer setup costs matter. The rational rates were constructed mathematically and are not measurements from the cited studies. The result proves existence, exact boundary formulas, and a minimal taxon count; it makes no assertion that every three-target primer pair exhibits these reversals. Self-review is not independent replication or field validation.

## References

- How, C. M., et al. (2024), *Refining Sampling Efforts for Fish Diversity Assessment in Subtropical Urban Estuarine and Oceanic Waters Using Environmental DNA With Multiple Primers*. First published 18 September 2024. DOI: https://doi.org/10.1002/edn3.70013.
- Baetscher, D. S., et al. (2023), *Optimizing a metabarcoding marker portfolio for species detection from complex mixtures of globally diverse fishes*. DOI: https://doi.org/10.1002/edn3.479.
- Fukaya, K., et al. (2022), *Multispecies site occupancy modelling and study design for spatially replicated environmental DNA metabarcoding*. First online 4 October 2021. DOI: https://doi.org/10.1111/2041-210X.13732.
