# Sharp three-switch boundary for fixed-community sedimentary DNA provenance and selective preservation

## Finding

The following is an exact model-specific threshold for false changes in the relative ordering of two sedimentary DNA markers when their two source communities themselves do not change. Assume \(t\ge 0\) is a *burial-age coordinate* (not necessarily physical core depth). The proportion of source type zero is
\[
p(t)=\frac{1}{1+q e^{\kappa t}},\qquad q,\kappa>0.
\]
Both source endmembers have fixed positive marker profiles. Post-depositional preservation depends on marker identity, not on which source it came from:
\[
C_A(t)=e^{-\lambda_A t}\bigl[p(t)A_0+(1-p(t))A_1\bigr],\quad
C_B(t)=e^{-\lambda_B t}\bigl[p(t)B_0+(1-p(t))B_1\bigr].
\]
Let \(\lambda_A>\lambda_B>0\), \(\delta=\lambda_A-\lambda_B\), \(a=A_0/A_1\), \(b=B_0/B_1\), and \(R=C_A/C_B\). A *strict switch* means a distinct interior time at which \(R=1\) and the sign of \(R-1\) changes. There can be **at most three** strict switches. There are physical positive choices of \(q,A_i,B_i\) exhibiting three for a given pair of endmember *relative contrasts* \(a,b\) and rates \(\kappa,\delta\) **if and only if**
\[
b>a\quad\text{and}\quad 0<\delta<\delta_c,
\qquad \delta_c=\kappa\frac{\sqrt b-\sqrt a}{\sqrt b+\sqrt a}.
\]
For any fixed parameter set satisfying this rate condition, put
\[
H=\kappa(b-a)-\delta(a+b),\quad
x_\pm=\frac{H\pm\sqrt{H^2-4\delta^2ab}}{2\delta},\quad
 t_\pm=\kappa^{-1}\log(x_\pm/q).
\]
Exactly three strict switches on \((0,\infty)\) occur **if and only if** \(q<x_-\), \(R(0)>1\), \(R(t_-)<1\), and \(R(t_+)>1\). These conditions are simultaneously attainable.

## Assumptions and scope

The model is a deterministic idealization of two *constant* source profiles and a smoothly varying source mix. Each positive endmember marker intensity is measured on a common proportional scale; sequencing, primer, and extraction biases are not modeled. Age \(t\) is known, nonnegative and continuous. The two taxon-specific loss rates are each constant across source types and ages, with \(\lambda_A>\lambda_B>0\). The logistic source mixing assumption is imposed, not estimated or claimed universal. These assumptions describe a possible taphonomic confounding mechanism, not a reconstruction of any cited field site.

## Proof

Set \(x=q e^{\kappa t}\), \(K=A_1/B_1>0\). Since \(p(t)=1/(1+x)\),
\[
R(t)=K e^{-\delta t}\frac{x+a}{x+b},\qquad
\frac{d}{dt}\log R(t)=-\delta+\kappa\frac{(b-a)x}{(x+a)(x+b)}.
\]
If \(b\le a\), the right side is negative. If \(b>a\), put \(g(x)=(b-a)x/((x+a)(x+b))\). Direct differentiation gives
\[
g'(x)=\frac{(b-a)(ab-x^2)}{(x+a)^2(x+b)^2},
\quad \max_{x>0}g(x)=g(\sqrt{ab})=\frac{\sqrt b-\sqrt a}{\sqrt b+\sqrt a}.
\]
Thus if \(\delta\ge\delta_c\), \(R\) is strictly decreasing (a single isolated horizontal tangent is possible at equality); it has at most one strict switch. If \(0<\delta<\delta_c\), the log-derivative is negative, then positive, then negative along the full positive \(x\)-axis. Its only two zeros are \(0<x_-<\sqrt{ab}<x_+\), given by the quadratic in the statement. On the actual domain \(x\ge q\), \(R\) consequently has at most two turning points and hence at most three crossings of any positive horizontal level; in particular at most three strict dominance switches. Three require both turning points in the interior and exactly the alternating inequalities displayed in the Finding, which are also sufficient by continuity, strict monotonicity on the three intervals, and \(R(t)\to0\) as \(t\to\infty\).

For sharpness of the *rate* condition for arbitrary \(a<b\) and \(0<\delta<\delta_c\), write \(\gamma=\delta/\kappa>0\) and \(F(x)=x^{-\gamma}(x+a)/(x+b)\). The two critical points satisfy \(F(x_-)<F(x_+)\). Pick \(C\) strictly between \(1/F(x_+)\) and \(1/F(x_-)\). Choose \(q>0\) sufficiently small so that \(q<x_-\) and \(CF(q)>1\). This is possible because \(F(q)\to\infty\) as \(q\downarrow0\). Set \(K=Cq^{-\gamma}>0\). Then \(R(t)=CF(qe^{\kappa t})\) satisfies the three strict inequalities. The endmember intensities can realize arbitrary \(a,b,K>0\): set \(B_1=1\), \(B_0=b\), \(A_1=K\), \(A_0=Ka\).

For a concrete **exact** witness take
\[
\kappa=4,\ q=10^{-4},\ \lambda_A=2,\ \lambda_B=1,\quad
(A_0,A_1,B_0,B_1)=(40,40,9,1).
\]
Then \(a=1\), \(b=9\), \(\delta_c=2>\delta=1\), and with \(x=10^{-4}e^{4t}\), \(u=x^{1/4}\),
\[
R=\frac{4(u^4+1)}{u(u^4+9)},\quad u\ge\frac1{10}.
\]
The equation \(R=1\) is
\[
P(u)=u^5-4u^4+9u-4=0.
\]
The signs at \(u=1/10,1/2,1,2,4\) are, respectively, negative, positive, positive, negative, positive. Thus there is a simple sign-changing root in each disjoint interval \((1/10,1/2)\), \((1,2)\), and \((2,4)\). The upper bound proved above guarantees **exactly** three positive-time switches, without relying on numerical root approximations. Endmember profiles remain constant throughout.

When \(\delta=0\), \(R\) is fractional-linear in \(x\) and monotone or constant, so it never has three strict switches. If the relative abundance profiles coincide, \(a=b\), selective preservation alone is monotone. The three-switch mechanism therefore requires competing variation in provenance and preservation.

## Verification

Run the standalone standard-library script \(\texttt{python3 verify.py}\) in the same directory. It checks the rational witness sign brackets exactly, both critical-point identities numerically against their closed forms, monotonicity and sampled root counts for a reproducible family of parameter sets, and direct original-concentration ratios against the simplified expression. Those numerical tests supplement, but do not replace, the analytic proof. The explicit rational signs plus the calculus argument are the infinite-domain certificate.

## Relationship to prior work

Morlock et al. (2023) experimentally establish that event-layer and background sediment can display different apparent communities without a matching catchment-community change. Sand et al. (2024) discuss preservation and extraction biases from DNA–mineral association; Thorpe et al. (2022) document ecological interpretation of sedDNA time series. These works supply the physical *motivation*, not the logistic age-profile or the exact rate threshold derived here. Standard Chebyshev-system bounds for sums of four distinct real exponentials give the coarse upper bound of three zeros after rearranging \(R=1\). That general zero-count is not claimed to be new. The specific positive-parameter attainability boundary, necessary-and-sufficient three-switch inequalities and sedimentary-bias interpretation are the content of this finding; no directly covering result was located in the inspected literature. No priority certification is asserted.

## Limitations

The model assumes known and continuously varying age, two sediment-source types, identical loss rates across source types for each marker, linear proportional molecular recovery, and a logistic provenance fraction. Real sediment layers may have discontinuities, nonlinear diagenesis, adsorption-dependent preservation, mixed burial ages, detection thresholds, or genuine biological change. No empirical parameter calibration, finite-sampling robustness, or inference of actual historical taxon changes is established. Mathematical coverage may exist under other terminology in older exponential-sum or taphonomic models; a general Chebyshev zero bound already covers the *upper bound alone*.

## References

- Morlock, M. A., et al. (2023). “Erosion regime controls sediment environmental DNA-based community reconstruction.” *Environmental DNA*, DOI: https://doi.org/10.1002/edn3.458 (first published 2023-08-06).
- Sand, K. K., et al. (2024). “Importance of eDNA taphonomy and sediment provenance for robust ecological inference: Insights from interfacial geochemistry.” *Environmental DNA*. https://doi.org/10.1002/edn3.519 (first published 2024-03-11).
- Thorpe, A. C., et al. (2022). “Sedimentary DNA records long-term changes in a lake bacterial community in response to varying nutrient availability.” *Environmental DNA*. https://doi.org/10.1002/edn3.344.
- Approximation Theory, Lecture 6 (University of Cambridge, 2005). “Chebyshev systems.” https://www.damtp.cam.ac.uk/user/na/PartIIIat/b06.pdf.
