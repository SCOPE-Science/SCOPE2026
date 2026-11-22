# Sharp multistability bounds for parallel quadratic phosphorus recycling

## Finding

Consider a nonnegative phosphorus concentration \(P(t)\) in a well-mixed, idealized lake, with \(m\) parallel saturating recycling channels. Its autonomous equation is
\[
\dot P=F_m(P)=L-aP+\sum_{j=1}^{m}r_j\frac{P^2}{K_j^2+P^2},\qquad P\geq0.
\]
For each integer \(m\geq0\), **there are at most \(2m+1\) distinct positive steady states and at most \(m+1\) asymptotically stable positive steady states. Both bounds are sharp simultaneously:** for every \(m\), there are strictly positive parameters (and no channels when \(m=0\)) having exactly \(2m+1\) *simple* positive steady states, of which exactly \(m+1\) are attracting and \(m\) repelling. Thus allowing any finite number of these positive recycling channels yields no universal finite cap on the number of stable nutrient regimes in this one-state idealization. This is a counting-and-attainability theorem, not a claim that a particular lake exhibits three or more regimes.

An explicit two-channel case has
\[
L=\frac1{10},\quad a=1,\quad(K_1,r_1)=(1,\tfrac74),\quad(K_2,r_2)=(50,300).
\]
Its vector field has signs \((+,-,+,-,+,-)\) at the six ordered concentrations \((0,\tfrac15,1,2,6,500)\). Therefore it has exactly five simple positive equilibria: three attracting and two repelling.

## Assumptions and scope

The parameters \(L,a,K_j,r_j\) are strictly positive real numbers, and \(m\) is any fixed nonnegative integer. Recycling terms each have quadratic Hill form \(r_j P^2/(K_j^2+P^2)\), depending on the *same* state variable; there is no assumed independence of dynamic reservoirs. The system is deterministic, well mixed, continuous in time, and has instantaneous recycling, fixed loading and linear removal. A steady state means a root of \(F_m\) at \(P>0\). An asymptotically stable steady state means a point locally attracting from both sides in the nonnegative state space. The number of equilibria is counted without multiplicity unless explicitly stated.

Because \(F_m(0)=L>0\) and \(F_m(P)\le L-aP+\sum_j r_j\), the half-line is forward invariant, solutions exist globally, and all nonnegative trajectories are ultimately bounded.

## Proof

**1. Algebraic bound.** Define the strictly positive denominator
\[
D_m(P)=\prod_{j=1}^{m}(K_j^2+P^2).
\]
For \(m=0\), use the empty-product convention \(D_0=1\). Then
\[
Q_m(P)=D_m(P)F_m(P)=(L-aP)D_m(P)+P^2\sum_{j=1}^{m}r_j\prod_{i\ne j}(K_i^2+P^2).
\]
This polynomial has degree exactly \(2m+1\): its highest-degree coefficient is \(-a\), because the recycling sum has degree at most \(2m\). No nonnegative denominator vanishes. Thus \(F_m\) has at most \(2m+1\) positive zeros, including any multiplicities.

**2. Attractor bound.** Between two distinct asymptotically stable scalar equilibria there must be at least one other equilibrium. Indeed a locally asymptotically stable equilibrium has a positive vector field on a sufficiently short interval to its left and negative field on a sufficiently short interval to its right; continuity then forces a zero between any two such attracting states. Consequently \(s\) distinct attracting positive equilibria require at least \(2s-1\) distinct roots. By step 1, \(s\le m+1\). This holds even if some zeros are nonhyperbolic.

**3. Sharpness for every integer \(m\).** Fix \(L=1/10\) and \(a=1\). Begin with \(m=0\), when \(F_0(P)=1/10-P\). It has alternating signs \((+,-)\) at the ordered witnesses \((0,1)\). Suppose \(F_m\) has \(2m+2\) ordered nonnegative witness points, starting at zero, at which its signs alternate from \(+\) to \(-\), so its last witness has negative sign. Choose \(K\) arbitrarily large and add one positive channel with \((K_{m+1},r_{m+1})=(K,3K)\):
\[
F_{m+1}(P)=F_m(P)+\frac{3KP^2}{K^2+P^2}.
\]
For each *fixed* old witness, the added term tends to zero as \(K\to\infty\); hence all old strict signs persist for all sufficiently large \(K\). Choose such \(K\) beyond the last old witness, and also satisfying \(K>L+\sum_{j=1}^{m}r_j\). At \(P=K\),
\[
F_{m+1}(K)\ge L-K+3K/2=L+K/2>0.
\]
At \(P=4K\), using the upper bound of each old recycling term by \(r_j\), and the added term by \(3K\),
\[
F_{m+1}(4K)<L+\sum_{j=1}^{m}r_j-4K+3K<0.
\]
Thus the two new ordered witnesses \(K\) and \(4K\) extend the alternating-sign list to \(2m+4\) points. The intermediate value theorem produces at least \(2m+3\) distinct positive roots. Step 1 produces at most that many with multiplicity, so there are **exactly** \(2m+3\), all simple. At successive simple roots the vector field changes sign alternately \(+\) to \(-\) (attracting), then \(-\) to \(+\) (repelling). This completes the induction, including the claim of \(m+1\) stable equilibria at stage \(m\).

**4. Exact two-channel witness.** For the parameters in the Finding section, direct rational substitution gives
\[
\begin{array}{c|rrrrrr}
P&0&1/5&1&2&6&500\\\hline
F_2(P)&1/10&-906517/32500520&9499/100040&-13/626&7199/117290&-50783079899/252501010
\end{array}
\]
All six signs are strict, and the numerator after clearing denominators has degree five. Therefore no further equilibrium, tangency or repeated root is possible.

## Verification

Run `python3 verify.py` with Python 3 and its standard library. The script uses exact rational arithmetic to evaluate the two-channel witness, constructs denominator-cleared polynomials, verifies their leading coefficients, and generates five successive alternating-sign configurations (from zero through four channels). It checks 58 exact assertions. These finite tests *supplement* the inductive proof; they are not substituted for the all-\(m\) argument.

## Relationship to prior work

Zeng et al. (2017) analyze a one-state lake-phosphorus model with one Hill-type recycling contribution and its familiar two-attractor/one-repeller bistable regime. The result here does not claim that ordinary bistability, Hill saturation, or scalar feedback is new. Feliu and Wiuf (2015) establish network-theoretic tests for relevant positive feedbacks in multistationary systems; their graph criteria are not an exact count for the present scalar additive quadratic-Hill family. Duncan et al. (2021) analyze equilibria of networks with steep sigmoidal nonlinearities using switching limits. Their arXiv preprint, including Theorem 3.13, addresses sufficiently steep perturbations of switching systems; it does not supply an exact finite-parameter polynomial degree bound or an all-\(m\) constructive realization for this scalar quadratic-Hill family. Earlier related mathematical analysis of two sigmoid phosphorus-feedback terms already exhibits five positive steady states; the two-channel existence phenomenon is not claimed as new *across all sigmoids*. The distinctive claim is the exact bound and sharp all-\(m\) construction for strictly positive **quadratic Hill** recycling channels.

Zhao et al. (first online October 2, 2024) documented multiple physical pathways for internal lake phosphorus loading, distinguishing resuspension-dominated shallow regions from diffusion-dominated deeper ones. Their observational study motivates multiple recycling contributions but does not specify or validate these particular Hill laws. This mathematical result does not follow from that field study.

## Limitations

The parameters constructed to saturate the bound may be widely separated, and the theorem does not constrain them to field-observed ranges. A positive recycling term is not equivalent to an independent sediment state or a distinct experimentally separable biological mechanism. Adding stochasticity, finite residence-time delays, spatial heterogeneity, feedback through temperature or oxygen, and dynamic sediment pools can change the equilibrium or stability picture. Stability here is deterministic and local; no claim about noise-induced transitions, basin weights or practical management policy is made. Historical originality is subject to the usual risk of unlocated equivalent results for sums of sigmoid response functions. An independently performed scientific audit is not included.

## References

1. Zhao, S., Hermans, M., Niemistö, J., Vesterinen, J., and Jilbert, T. *Stratification controls the magnitude of in-lake phosphorus cycling: insights from a morphologically complex eutrophic lake.* Hydrobiologia, first published online 2024-10-02. https://doi.org/10.1007/s10750-024-05701-4
2. Zeng, C., et al. *Stochastic ecological kinetics of regime shifts in a time-delayed lake eutrophication ecosystem.* Ecosphere 8, e01805 (2017), first published 2017-06-16. https://doi.org/10.1002/ecs2.1805
3. Feliu, E., and Wiuf, C. *Finding the positive feedback loops underlying multi-stationarity.* BMC Systems Biology 9, 22 (2015). https://doi.org/10.1186/s12918-015-0164-0
4. Duncan, W., Gedeon, T., Kokubu, H., Mischaikow, K., and Oka, H. *Equilibria and Their Stability in Networks with Steep Sigmoidal Nonlinearities.* SIAM Journal on Applied Dynamical Systems (2021). https://doi.org/10.1137/21M1398331
5. Gonsiorczyk, T., et al. *Rapid Eutrophication of a Clearwater Lake: Trends and Potential Causes Inferred From Phosphorus Mass Balance Analyses.* Global Change Biology (2024). https://doi.org/10.1111/gcb.17575
