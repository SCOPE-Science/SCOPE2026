# Three habitats are sharp for re-entrant optimal range under increasing environmental variance

## Finding
Consider a regional population assigning nonnegative fixed fractions \(x_i\) to \(n\) habitats, with \(\sum_i x_i=1\), local mean growth rates \(r_i\), and a positive-definite environmental covariance matrix \(\Sigma\). If environmental variability is multiplied by \(v>0\), the almost-sure low-density growth exponent is
\[
G_v(x)=r^{\mathsf T}x-\frac v2x^{\mathsf T}\Sigma x.
\]
Call the optimal habitat range **re-entrant** if a habitat has zero optimal allocation at all sufficiently small \(v>0\), strictly positive allocation for an intermediate interval, and zero allocation again at all sufficiently large \(v\). **At least three habitats are necessary and sufficient for this phenomenon.** In particular, for three habitats take
\[
r=(2,1,0)^{\mathsf T},\qquad
\Sigma=\begin{pmatrix}2&-1&-2\\-1&2&2\\-2&2&3\end{pmatrix}.
\]
The unique optimizer for every \(v>0\) is exactly
\[
x^*(v)=\begin{cases}
(1,0,0),&0<v\le1/3,\\
(1/2+1/(6v),\ 1/2-1/(6v),\ 0),&1/3\le v\le5/3,\\
(3/5,\ (5-v)/(5v),\ (3v-5)/(5v)),&5/3\le v\le5,\\
((5v+2)/(9v),\ 0,\ (4v-2)/(9v)),&v\ge5.
\end{cases}\]
The formulas agree at the transition points. Habitat 2 is first selected for \(v>1/3\) but is excluded again for every \(v\ge5\). This return to a smaller range happens **before regional extinction**: the optimized exponent is positive exactly for \(0<v<5+3\sqrt3\), zero at that threshold, and negative for larger \(v\). At \(v=6\), the three isolated habitat exponents are \(-4,-5,-9\), yet the optimal regional allocation \((16/27,0,11/27)\) has positive exponent \(13/27\).

## Assumptions and scope
Fix \(n\ge1\), \(r\in\mathbb R^n\), \(\Sigma\in\mathbb R^{n\times n}\) symmetric positive definite, and \(v>0\). Let \(W\) be a Brownian vector with covariance \(d\langle W_i,W_j\rangle_t=\Sigma_{ij}\,dt\). For each **fixed**, time-independent allocation \(x\) on the probability simplex, define the scalar regional low-density population by
\[
\frac{dN_t}{N_t}=(r^{\mathsf T}x)\,dt+\sqrt v\sum_i x_i\,dW_i(t),\qquad N_0>0.
\]
The outcome optimized is its almost-sure log-growth exponent, not instantaneous mean abundance, finite-population extinction probability, a density-regulated equilibrium, or the evolutionary stability of an allocation. Strategies are allowed to depend on the known variance parameter \(v\), but are fixed over biological time. Covariance, means, and feasible habitat set otherwise remain unchanged.

## Proof
Itô's formula and the strong law for Brownian motion give \(\lim_{t\to\infty}t^{-1}\log(N_t/N_0)=G_v(x)\) almost surely. Since \(\Sigma\) is positive definite, \(G_v\) is strictly concave in \(x\); hence its optimizer is unique. Write the marginal gradient \(g_i(x)=r_i-v(\Sigma x)_i\). A feasible \(x\) is optimal exactly when there is \(\ell\) such that \(g_i=\ell\) on all positive coordinates and \(g_i\le\ell\) at zero coordinates.

For one habitat, there is no possible re-entry. For two habitats, relabel so \(r_1\ge r_2\), put \(D=\Sigma_{11}+\Sigma_{22}-2\Sigma_{12}>0\), and optimize over the second-habitat share \(u\in[0,1]\). Direct differentiation gives
\[
u^*(v)=\operatorname{clip}_{[0,1]}\!\left(\frac{\Sigma_{11}-\Sigma_{12}}D-\frac{r_1-r_2}{vD}\right).
\]
This is nondecreasing in \(v\). An initially absent habitat with strictly smaller mean therefore cannot subsequently disappear after entering. If both means tie, the unique optimizer is independent of \(v\). Thus no one- or two-habitat model permits re-entry.

For the displayed three-habitat matrix, the leading principal minors are \(2,3,1\), so \(\Sigma\) is positive definite. Applying the marginal-gradient criterion to the four stated candidates gives the following complete checks. For \((1,0,0)\), the differences \(g_2-g_1=3v-1\) and \(g_3-g_1=4v-2\) are nonpositive through \(v=1/3\). For the positive support \(\{1,2\}\), stationarity gives the second branch and the inactive difference \(g_3-g_1=(3v-5)/6\), nonpositive through \(v=5/3\). On the all-positive branch the three gradients are exactly equal, and its coordinates are nonnegative precisely for \(5/3\le v\le5\). Finally, on support \(\{1,3\}\), stationarity gives the fourth branch and \(g_2-g_1=-(v-5)/9\le0\) for \(v\ge5\). The branches agree at the boundaries, and strict concavity proves global optimality and uniqueness over every \(v>0\), not just the sampled values in the checker.

On the final branch, direct substitution gives
\[
G_v(x^*(v))=\frac{-v^2+10v+2}{9v},\qquad v\ge5.
\]
At \(v=5\), this equals \(3/5>0\). For any fixed \(x\), \(G_v(x)\) strictly decreases in \(v\) since \(x^{\mathsf T}\Sigma x>0\); therefore its maximized value also strictly decreases. The unique positive zero of the displayed final-branch expression is \(5+3\sqrt3>5\), establishing the complete persistence interval. For \(v=6\), the optimizer and regional exponent are \((16/27,0,11/27)\) and \(13/27\); the isolated exponents are \(r_i-3\Sigma_{ii}=(-4,-5,-9)\). This proves the stated contrast between locally declining habitats and regionally growing mixtures.

## Verification
Run `python verify.py` with SymPy 1.10 or later from the extracted package directory. The checker verifies the exact covariance principal minors, symbolic gradient equalities and inactive-coordinate differences for all four branches, three boundary joins, and 150 rational noise values by independent enumeration of every feasible active-set stationary solution. It also checks the exact persistence expression and the locally declining, regionally growing witness at \(v=6\). These computations are independent corroboration; the proof above handles all real \(v>0\).

## Relationship to prior work
Schreiber (2012) studies evolutionary patch selection with density feedback and spatially correlated environmental fluctuations, including use of sink patches, expansion under increasing fluctuation, and environmental-correlation-driven contraction. The present claim concerns a distinct *fixed, low-density log-growth maximization* and proves an exact nonnested support trajectory under a common scalar variance increase while covariance shape stays constant. It does not assert a conclusion about Schreiber's density-dependent evolutionary stable strategies.

Markowitz (1952) introduced the mathematically equivalent expected-return/variance geometry; its critical-line approach, and the later active-set implementation of Bailey and López de Prado (2013), can solve general instances of this convex quadratic problem. The KKT method and mean–variance objective are known and not claimed as new. The isolated contribution here is the sharply minimal dimension of **entry followed by exit**, the exact four-phase rational ecological witness, and the fact that range contraction occurs strictly before regional loss of stochastic persistence while all isolated habitats can be declining. No general novelty claim about parametric quadratic programming is made.

## Limitations
The stochastic dynamics assume a prescribed, arbitrarily rapidly redistributable fixed allocation and Brownian environmental forcing with a specified covariance. Ecological data are not used to estimate the matrix. The theorem is about almost-sure low-density growth; it does not establish numerical abundance, coexistence, finite-population survival, adaptive dispersal mechanisms, or ecosystem conservation effectiveness. Generic quadratic-programming solution techniques can regenerate the calculations; that mathematical equivalence is a material historical-priority risk for broader claims. Other exact support-path examples may exist in optimization literature.

## References
- S. J. Schreiber, "The Evolution of Patch Selection in Stochastic Environments," *The American Naturalist* 180 (2012), 17–34. First published online 17 May 2012. https://doi.org/10.1086/665655 . Lawful author manuscript: https://schreiber.faculty.ucdavis.edu/wp-content/uploads/sites/568/2019/08/2012_schreiber_AmNat.pdf
- H. Markowitz, "Portfolio Selection," *The Journal of Finance* 7 (1952), 77–91. https://doi.org/10.1111/j.1540-6261.1952.tb01525.x . Accessible archival text: https://traders.berkeley.edu/papers/Markowitz.pdf
- D. H. Bailey and M. López de Prado, "An Open-Source Implementation of the Critical-Line Algorithm for Portfolio Optimization," *Algorithms* 6 (2013), 169–196. https://doi.org/10.3390/a6010169 .
