# A sharp activation threshold for cooling a lower-load urban district

## Finding

Consider two thermally coupled urban districts with unequal constant heat sources and a fixed budget of supplementary *proportional* cooling. The budget that minimizes aggregate stationary excess temperature has a unique allocation. Initially all cooling is assigned to the hotter-source district; at one explicitly computable budget threshold, cooling in the weaker-source district becomes optimal. This remains true even when that district has **no external heat source**. In that source-free case, minimizing the hottest district's temperature always prescribes the *opposite* boundary allocation, so the aggregate-temperature and peak-temperature objectives provably disagree above the threshold.

Specifically, let \(a,k,B,H_1>0\) and \(0\le H_2\le H_1\). Put \(u_2=y\), \(u_1=B-y\), with \(0\le y\le B\), and let \(T_1(y),T_2(y)\) be the unique stationary solution of
\[
0=H_1-(a+u_1)T_1-k(T_1-T_2),\qquad
0=H_2-(a+u_2)T_2+k(T_1-T_2).
\]
The objective is \(E(y)=T_1(y)+T_2(y)\); dividing by two would give the equal-area mean and does not change its optimizer.

When \(0\le h=H_2/H_1<1\), define
\[
 b_h=k+h(2a+3k),\qquad
 B_c(h)=\frac{2(1-h)a(a+2k)}{b_h+\sqrt{b_h^2+4h(1-h)a(a+2k)}}.
\]
For \(0<B\le B_c(h)\), **the unique** minimizer is \(y_*=0\). For \(B>B_c(h)\), **the unique** minimizer satisfies \(0<y_*<B/2\) and is
\[
 y_*=\frac{CB-qD_0}{C+\sqrt{C^2+q(CB-qD_0)}},\quad
 q=H_1-H_2,\quad C=H_1(a+2k)+H_2(a+B+2k),\quad
 D_0=a(a+B)+k(2a+B).
\]
For equal heat sources \(H_1=H_2>0\), the unique minimizer is \(y_*=B/2\) at every positive budget.

For the natural zero-source boundary \(H_2=0\), the activation threshold and interior optimal allocation simplify to
\[
 B_c=\frac{a(a+2k)}{k},\qquad
 y_*=\sqrt{k(B+2a+4k)}-(a+2k)\quad(B>B_c).
\]
In particular, \(y_*=\sqrt{kB}-(a+2k)+O(B^{-1/2})\) as \(B\to\infty\), so the unheated district receives an unbounded but vanishing-fraction cooling allocation. Yet for every \(B>0\) and \(H_2=0\), the unique allocation minimizing \(\max(T_1,T_2)\) is \(y=0\). Consequently the two natural heat objectives disagree at *every* \(B>B_c\).

## Assumptions and scope

The model is a **steady two-cell linear heat-balance abstraction**. Both districts have equal thermal capacities or are measured in compatible per-cell excess-temperature units, identical background proportional loss \(a>0\), symmetric linear thermal exchange \(k>0\), nonnegative fixed heat inputs \(H_1\ge H_2\), and nonnegative local proportional cooling controls \(u_1,u_2\) whose sum is the fixed rate budget \(B>0\). Equal unit costs are assumed, and the controls alter proportional cooling coefficients, not externally imposed heat inputs. Temperature means *excess over the common reference environment*, not absolute Celsius temperature. Equal-area exposure is the sum/mean objective. The maximum-temperature objective is considered only in the source-free boundary case. No time-dependent feedback, atmospheric wind field, thermal-radiation nonlinearity, unequal area, equipment saturation, or calibration is assumed.

## Proof

**Stationary solution and positivity.** With \(u_2=y\), \(u_1=B-y\), invert the strictly positive definite matrix
\[
 M(y)=\begin{pmatrix}a+B-y+k&-k\\-k&a+y+k\end{pmatrix}.
\]
Its determinant is
\[
 D(y)=(a+B-y)(a+y)+k(2a+B)=D_0+By-y^2>0.
\]
Hence the equilibrium exists uniquely and
\[
 T_1(y)=\frac{(a+y+k)H_1+kH_2}{D(y)},\qquad
 T_2(y)=\frac{kH_1+(a+B-y+k)H_2}{D(y)}.
\]
The sum is \(E(y)=N(y)/D(y)\) with \(N(y)=C+qy\), \(q=H_1-H_2\ge0\), \(C=H_1(a+2k)+H_2(a+B+2k)>0\).

**Unique global optimum.** Direct differentiation gives
\[
 E'(y)=\frac{Q(y)}{D(y)^2},\qquad
 Q(y)=q y^2+2Cy+qD_0-CB.
\]
For every \(0\le y\le B\), \(Q'(y)=2qy+2C>0\); hence \(E\) either increases throughout or decreases to exactly one interior minimum and then increases. If \(q>0\),
\[
 Q(B/2)=qD(B/2)>0.
\]
Thus any interior optimum is strictly below \(B/2\). The initial derivative is determined by
\[
 \frac{Q(0)}{H_1}=(1-h)a(a+2k)-[k+h(2a+3k)]B-hB^2.
\]
For \(0\le h<1\), this expression strictly decreases from a positive value at \(B=0\) to a negative value, and has one positive root \(B_c(h)\). Rationalizing the positive quadratic root gives the displayed threshold. At the root itself \(Q(0)=0\) while \(Q(y)>0\) for \(y>0\), so the boundary optimum remains unique. For \(B>B_c(h)\), the positive root of \(Q(y)=0\), rationalized to avoid cancellation, equals the displayed \(y_*\). If \(q=0\), then \(Q(y)=C(2y-B)\), proving unique equal splitting.

**Source-free district and opposition of objectives.** With \(H_2=0\), \(h=0\), and hence \(B_c(0)=a(a+2k)/k\). Solving \(Q(y)=0\) explicitly gives \(y_*=\sqrt{k(B+2a+4k)}-(a+2k)\), with the asserted asymptotic expansion. Both temperatures are strictly positive and
\[
 T_1(y)-T_2(y)=\frac{H_1(a+y)}{D(y)}>0.
\]
Therefore the maximum equals \(T_1\), whose derivative is
\[
 T_1'(y)=\frac{H_1(a+y)(a+y+2k)}{D(y)^2}>0.
\]
Its unique minimizer is \(y=0\) at every budget. This proves the strict objective disagreement above \(B_c\), without relying on numerical experiments.

## Verification

The exact rational example \(a=k=H_1=1\), \(H_2=0\), \(B=5\) has threshold \(B_c=3\), with aggregate optimum \(y_*=\sqrt{11}-3\in(316/1000,317/1000)\). Even the simple rational intervention \(y=1/3\) gives
\[
 E(0)=\frac3{13},\qquad E(1/3)=\frac{30}{131}<\frac3{13},
\]
while its hottest district becomes **warmer**:
\[
 T_1(0)=\frac2{13},\qquad T_1(1/3)=\frac{21}{131}>\frac2{13}.
\]
All inequalities are exact. A standalone standard-library checker in `checks/verify.py` verifies derivative identities with exact rational arithmetic, this strict counterpoint, optimality and threshold classifications across seeded parameter tests, and the peak-temperature monotonicity. Run `python3 checks/verify.py` from the artifact root. Finite tests corroborate rather than replace the all-parameter proof above.

## Relationship to prior work

Li et al.'s 2023 preprint [1], subsequently developed into a 2024 journal article [2], motivates optimizing urban greenery to reduce aggregate outdoor heat and spatial inequalities; it estimates green cooling from remote sensing, rather than deriving a coupled two-cell budget threshold. Sellila et al. [3] optimize urban green-space geometry with a numerical 3D porous-city heat equation and explicitly discuss temperature homogenization. Fernández et al. [4] formulate and numerically optimize green-zone placement in a microscale thermal-control model. Quijano and Passino [5] describe laboratory multizone temperature-resource control, principally with heater allocation and feedback rather than a static optimal cooling-rate split. Their exact physical and optimization models differ from the proportional-cooling two-cell model above. The present contribution is the complete analytic activation threshold, the source-free receiving-district effect, and the strict aggregate-versus-peak objective conflict. Standard matrix inversion and one-variable calculus are acknowledged as the proof tools; no general novelty of optimization by such tools is claimed.

## Limitations

This theorem is conditional on an idealized steady, symmetric-exchange, proportional-removal model. It is not an estimate of achievable cooling from green cover, nor a universal urban-greening policy. Different actuator costs, population weights, finite control caps, ambient forcing, nonlinear radiative heat, multiple districts, finite time horizons or climate uncertainty may alter the threshold. The source-free district may still be warm because of exchange; zero **external** source does not mean zero temperature. Literature priority is based on the inspected sources and searches, not independently certified. No independent external mathematical audit has occurred.

## References

[1] Y. Li et al., *Global Inequality in Cooling from Urban Green Spaces and its Climate Change Adaptation Potential*, arXiv:2307.09725, first posted 2023-07-19, https://arxiv.org/abs/2307.09725.

[2] Y. Li et al., *Green spaces provide substantial but unequal urban cooling globally*, Nature Communications 15 (2024), 7108, https://doi.org/10.1038/s41467-024-51355-0 (open-access full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC11369290/).

[3] N. Sellila, M. Louaked, W. Mouhali, and H. Mechkour, *Optimal Control Strategies for Mitigating Urban Heat Island Intensity in Porous Urban Environments*, Mathematics 11 (2023), 4737, https://doi.org/10.3390/math11234737.

[4] F. J. Fernández, L. J. Alvarez-Vázquez, N. García-Chan, A. Martínez, and M. E. Vázquez-Méndez, *Optimal location of green zones in metropolitan areas to control the urban heat island*, Journal of Computational and Applied Mathematics 289 (2015), 412–425, https://doi.org/10.1016/j.cam.2014.10.023.

[5] N. Quijano and K. M. Passino, *Resource Allocation Strategies for Multizone Temperature Control*, IFAC conference paper (2004), https://doi.org/10.1016/S1474-6670(17)30497-4.
