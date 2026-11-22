# A parity law for short-window ecological surveys and an exact five-visit clustering threshold

## Finding
Consider \(n\ge3\) nonadaptive observations of an intermittently available, continuously present target under a stationary *symmetric* two-state continuous-time Markov availability model. Each observation independently detects an available target with the same probability \(p\in(0,1)\), with no false positives. The first observation is fixed at time \(0\), the last at time \(T>0\), and coincident observation attempts are permitted and conditionally independent. Write \(\gamma>0\) for the total switching intensity. The unique schedule maximizing the chance of **at least one detection** is time-reflection symmetric for every \(n,p,\gamma,T\). Moreover, at every fixed \(n\) and \(p\in(0,1)\), all sufficiently short horizons have an exact parity-dependent optimal clustering pattern: for even \(n\), all time elapses in the single central inter-observation gap; for odd \(n\), the horizon is split equally between the two central gaps. No other gaps are positive.

For \(n=5\), the complete all-horizon optimum is explicit. Put
\[
\rho=\left(\frac{p}{2-p}\right)^2,\qquad
T_c=\frac2\gamma\log\frac{2}{1+\rho},\qquad K=e^{-\gamma T/2}.
\]
For \(0<T\le T_c\), the unique optimal visit times are \((0,0,T/2,T,T)\). For \(T>T_c\), there is exactly one root \(u\in(K,1)\) of
\[
\rho u^3+u^2-K(u+1)=0,
\]
and the unique optimal gap vector is \((x,y,y,x)\), where
\[
x=-\gamma^{-1}\log u,\qquad y=T/2-x>x>0.
\]
Thus the two replicate pairs at the endpoints separate at the exact threshold; thereafter the two inner intervals remain strictly longer than the outer ones. At \(p=1\) (outside the general short-horizon statement), uniform spacing is uniquely optimal for any \(n\) and \(T\).

## Assumptions and scope
The target is present in the larger region but its material is only locally available for detection when \(Z_t=1\). The Markov chain has states \(0\) (unavailable) and \(1\) (available), equal rates \(\gamma/2\) in either direction, and stationary initial law \(\Pr(Z_0=0)=\Pr(Z_0=1)=1/2\). For \(0=t_1\le\cdots\le t_n=T\), let \(g_i=\gamma(t_{i+1}-t_i)\), so every \(g_i\ge0\) and \(\sum_{i=1}^{n-1}g_i=\gamma T\). Conditional on the complete state sequence, detections are independent, with probability \(p\) in state \(1\) and zero in state \(0\). We optimize only the probability of at least one positive observation, with fixed visit count, fixed horizon and fixed endpoint times. Survey time is not optimized jointly with costs, occupancy estimation or adaptive choices. A common-time replicate is a separate independent detection attempt, not a single sample read twice.

## Proof
**1. Positive exponential expansion and strict convexity for every \(n\).** Define spin \(S_i=1-2Z_{t_i}\in\{-1,1\}\), and let \(c=1-p/2\), \(b=p/2\). With \(q=1-p\), no-detection probability is
\[
F_n(g)=\mathbb E\prod_{i=1}^n(1-pZ_{t_i})
=\mathbb E\prod_{i=1}^n(c+bS_i).
\]
The symmetric stationary chain has \(\mathbb E S_i=0\), and, for any even ordered subset \(i_1<\cdots<i_{2k}\),
\[
\mathbb E\prod_{j=1}^{2k}S_{i_j}
=\exp\!\left(-\sum_{r=1}^k\sum_{m=i_{2r-1}}^{i_{2r}-1}g_m\right).
\]
This follows by iterating \(\mathbb E(S_j\mid S_i)=e^{-(g_i+\cdots+g_{j-1})}S_i\). Odd spin moments are zero. Therefore
\[
F_n(g)=\sum_{k=0}^{\lfloor n/2\rfloor}c^{n-2k}b^{2k}
\sum_{i_1<\cdots<i_{2k}}\exp\!\left(-\sum_{r=1}^k\sum_{m=i_{2r-1}}^{i_{2r}-1}g_m\right).
\]
Every summand is a positive coefficient times an exponential of a linear functional, hence convex on the nonnegative orthant. For every gap \(j\), the adjacent-pair subset \(\{j,j+1\}\) contributes \(c^{n-2}b^2e^{-g_j}\) with strictly positive coefficient. Thus the Hessian dominates a positive diagonal matrix and \(F_n\) is strictly convex on the full gap space. The feasible simplex has a unique minimizer. Stationarity and detailed balance make \(F_n(g_1,\ldots,g_{n-1})=F_n(g_{n-1},\ldots,g_1)\); uniqueness forces the minimizing gaps to be reflection-symmetric.

**2. All visit counts: short-horizon parity law.** At \(g=0\), all samples see one latent state and \(F_n(0)=(1+q^n)/2\). Differentiating the exact hidden-state sum at this origin gives
\[
\left.\frac{\partial F_n}{\partial g_j}\right|_{g=0}
=-\frac14(1-q^j)(1-q^{n-j}),\qquad 1\le j\le n-1.
\]
Indeed, a first-order transition only in gap \(j\) changes the no-detection expectation from \((1+q^n)/2\) to \((q^j+q^{n-j})/2\), with switch probability \(g_j/2+O(g_j^2)\). The magnitude \((1-q^j)(1-q^{n-j})\) is strictly greatest at the central gap when \(n\) is even, or at the two adjacent central gaps when \(n\) is odd. The strict derivative margin against other gaps persists throughout a sufficiently small feasible simplex by continuity, so the first-order necessary and sufficient conditions of convex minimization exclude every noncentral gap. For even \(n\), the entire horizon therefore lies in the unique central gap. For odd \(n\), reflection symmetry and uniqueness split the horizon equally between the two central gaps. This proves the parity statement (including \(n=3\)); the smallness bound depends on \(n\) and \(p\), and the statement does not claim a uniform bound in \(n\).

**3. Complete sharp five-visit phase.** For five visits, symmetry makes the four dimensionless gaps \((\gamma x,\gamma y,\gamma y,\gamma x)\), where \(x+y=T/2\). Put \(u=e^{-\gamma x}\), \(v=e^{-\gamma y}=K/u\), with \(K\le u\le1\). Expanding the even-subset formula gives
\[
F_5=c^5+c^3b^2(2u+2v+2uv+2uv^2+v^2+u^2v^2)
+cb^4(2uv+2u^2v+u^2).
\]
After substituting \(v=K/u\), the derivative in \(u\) is exactly
\[
\frac{dF_5}{du}=\frac{2c^3b^2}{u^3}(u+K)
\bigl(\rho u^3+u^2-K(u+1)\bigr),\qquad \rho=(b/c)^2.
\]
The factor in parentheses is negative at \(u=K\) (its value is \(K(\rho K^2-1)\)), and at \(u=1\) its value is \(1+\rho-2K\). Its derivative \(3\rho u^2+2u-K\) is strictly increasing in \(u>0\), so this cubic has exactly one positive root, with a negative-to-positive sign crossing. For \(K\ge(1+\rho)/2\) the minimum lies at \(u=1\), i.e. \(x=0,y=T/2\); for \(K<(1+\rho)/2\) it lies at the unique root in \((K,1)\). Because \(\rho<1\), the root equation yields \(K=u^2(1+\rho u)/(1+u)<u^2\), which is equivalent to \(x<y\). The boundary corresponds to the stated \(T_c\), including equality. Strict convexity proves that this symmetric candidate is the unique *global* optimum, not merely a local extremum. When \(p=1\), a non-detection requires all sampled states to be unavailable; its probability is \(\tfrac12\prod_i(1+e^{-g_i})/2\). Strict convexity of \(\log(1+e^{-g})\) and Jensen's inequality give uniformly spaced gaps for all \(n\).

## Verification
Run `python3 check.py` with the Python standard library. The script uses rational hidden-state path enumeration and an independent spin-moment expansion; they agree for all tested rational lag and detection parameters. It independently checks the five-visit symbolic expression, the exact interior stationary point, the strict ordering of gap types, and a finite grid of competitors across three detection qualities and six horizon regimes. The script reports **31,924 successful assertions**. These calculations corroborate the exact identities; finite grids are not proofs of all-horizon optimality. The convexity argument and cubic sign classification supply the infinite-parameter proof.

For an exact interior example, take \(p=1/2\), \(\gamma=1\), \(u=3/4\), \(v=13/28\). Then \(\rho=1/9\), \(K=39/112\), and \(T=2\log(112/39)>2\log(9/5)=T_c\). The optimal five gaps are
\[
\bigl(\log(4/3),\log(28/13),\log(28/13),\log(4/3)\bigr),
\]
with strictly longer inner intervals. Unlike a floating-point solution, the cubic vanishes exactly with these rational exponential factors.

## Relationship to prior work
Jensen and colleagues (2022) document temporal changes and within-time replication in coastal eDNA sampling; Preston and colleagues (2023) demonstrate autonomous eDNA sampling along a long marine transect. They motivate temporal sampling design but do not model a stationary Markov availability state or optimize fixed-count observation times. MacKenzie and Royle (2005) and Guillera-Arroita, Ridout and Morgan (2010) analyze occupancy sampling allocations and estimator precision, not the stated no-detection scheduling functional. A closely related publicly available four-visit mathematical result gives the sharp endpoint-doublet transition for \(n=4\), including unequal stationary availability; a related three-visit result allows different detection qualities. Neither result states or implies the general-\(n\) strict convexity/parity classification or the five-visit exact cubic and threshold without further analysis. The Markov transition identity, even-moment expansion, and ordinary convex optimization are standard tools and are not claimed as new. Historical priority is provisional; broader, uninspected optimal sensor-scheduling literature could subsume part of the conclusion.

## Limitations
These conclusions assume symmetric stationary availability, identical observation quality, no false positives, conditional independence of replicates (even simultaneous ones), fixed endpoints, and a fixed number of nonadaptive attempts. The analysis does not assert empirical optimality for eDNA in drifting water, circadian signals, correlated technical replicates, species abundance estimation or field scheduling with minimum separation, limited sample-storage capacity or travel costs. If visits must be distinct, the short-horizon clustered optimum becomes an unattained supremum approachable by small positive gap perturbations. The five-visit phase diagram is exact only for the stated model; no full arbitrary-horizon classification for every \(n\) is claimed.

## References
1. Jensen, M. R., et al. (2022), “Short-term temporal variation of coastal marine eDNA,” *Environmental DNA* 4, 747–762. First public 2022-02-23. https://doi.org/10.1002/edn3.285 (see 2023-06-13 corrigendum https://doi.org/10.1002/edn3.396).
2. Preston, C., et al. (2023), “Autonomous eDNA collection using an uncrewed surface vessel over a 4200-km transect of the eastern Pacific Ocean,” *Environmental DNA* 6, e468. First public 2023-08-29. https://doi.org/10.1002/edn3.468.
3. MacKenzie, D. I. and Royle, J. A. (2005), “Designing occupancy studies: general advice and allocating survey effort,” *Journal of Applied Ecology* 42, 1105–1114. https://doi.org/10.1111/j.1365-2664.2005.01098.x.
4. Guillera-Arroita, G., Ridout, M. S. and Morgan, B. J. T. (2010), “Design of occupancy studies with imperfect detection,” *Methods in Ecology and Evolution* 1, 131–139. https://doi.org/10.1111/j.2041-210X.2010.00017.x.
5. “A sharp endpoint-doublet transition for four surveys of Markovian ecological availability” (2026). Public result: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-endpoint-doublet-transition-for-four-surveys-of-markovia--83d0ec176818.
6. “A sharp three-visit scheduling law for intermittently available species” (2026). Public result: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-three-visit-scheduling-law-for-intermittently-available--58658da993e0.
