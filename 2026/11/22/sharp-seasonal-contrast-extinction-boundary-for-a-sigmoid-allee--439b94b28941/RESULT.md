# Sharp seasonal-contrast extinction boundary for a sigmoid Allee population

## Finding
Consider two alternating recruitment environments governed by the sigmoid Allee response
\[
F_r(x)=\frac{r x^2}{1+x^2},\qquad r>0,\quad x\geq0.
\]
For any \(a,b>0\), apply \(F_a\) in even years and \(F_b\) in odd years. Define the **seasonal persistence polynomial**
\[
\mathcal H(a,b)=(ab-4)(3ab+4)^3-256(a-b)^2.
\]
The following trichotomy holds over the *entire nonnegative state space*.

1. If \(\mathcal H(a,b)<0\), every orbit tends to extinction.
2. If \(\mathcal H(a,b)=0\), precisely one positive two-season state exists. Its even-year biomass is a semistable threshold: initial biomasses below it tend to extinction, and those above it converge monotonically along even years to the positive two-season state.
3. If \(\mathcal H(a,b)>0\), precisely two positive two-season states exist. The smaller even-year biomass is the unstable survival threshold; every larger even-year biomass converges to the larger, attracting two-season state, while every smaller biomass tends to extinction. Starting exactly at either periodic state stays on that state.

The order of \(a\) and \(b\) does not change which of these three regimes occurs. This classifies both persistence and the global extinction/survival basins, not just local stability.

In particular, let \(g=\sqrt{ab}\) be the fixed geometric-mean recruitment coefficient and write \(a=g e^\theta\), \(b=g e^{-\theta}\). If \(g<2\), every population goes extinct for all contrasts \(\theta\). At \(g=2\), a positive semistable state exists only at \(\theta=0\). For \(g>2\), survival from sufficiently large initial populations is possible exactly when
\[
|\theta|\le\theta_c(g),\qquad
\theta_c(g)=\operatorname{arsinh}\!\left(
\frac{\sqrt{(g^2-4)(3g^2+4)^3}}{32g}\right).
\]
For strictly smaller contrast there are two positive two-season states and the larger is attracting. At equality there is one semistable positive state, and every initial even-year biomass at or above it survives. For larger contrast all states go extinct. Thus maintaining the same geometric mean does **not** maintain persistence.

For an exact comparison with \(ab=9\), the pair \((a,b)=(1,9)\) gives \(\mathcal H=132571>0\), whereas \((a,b)=(1/4,36)\) gives \(\mathcal H=-178229<0\). The second environment alternates more strongly and is universally extinct despite an unchanged geometric mean.

## Assumptions and scope
The recurrence starts at an arbitrary \(x_0\geq0\), and the two positive coefficients alternate deterministically for all time. Biomass is nondimensional and the density-dependent response is exact; there is no immigration, random environmental switching, harvesting, observational error, spatial structure, or unmodeled stage dependence. A "positive two-season state" is a pair \((x,y)\) with \(x>0\), \(y=F_a(x)>0\), and \(F_b(y)=x\); the pair is allowed to have \(x=y\) when \(a=b\). Stability and basin statements refer to the two-year return map on even years and its uniquely determined odd-year images.

## Proof
**1. Reduction to a one-dimensional fixed-point problem.** Let \(G=F_b\circ F_a\). Direct substitution gives, for \(x\geq0\),
\[
G(x)=\frac{ba^2x^4}{(1+x^2)^2+a^2x^4}.
\]
Both seasonal maps are continuous, strictly increasing on positive arguments, nonnegative, and bounded. Consequently, \(G\) is strictly increasing on positive arguments, and every forward orbit of \(G\) converges to a fixed point: after the first step it is monotone and bounded, and continuity identifies its limit. Define
\[
Q_{a,b}(x)=(1+a^2)x^4-ba^2x^3+2x^2+1.
\]
The exact signed-displacement identity, valid for \(x>0\), is
\[
G(x)-x=-\frac{xQ_{a,b}(x)}{(1+x^2)^2+a^2x^4}.
\]
Thus positive periodic states are exactly the positive zeros of this quartic. All sign arguments below are strict away from its zeros.

**2. Exactly zero, one, or two positive periodic states.** For \(x>0\), the equation \(Q_{a,b}(x)=0\) is equivalent to \(b=B_a(x)\), where
\[
B_a(x)=\frac{(1+a^2)x+2/x+1/x^3}{a^2}.
\]
This function tends to infinity at both endpoints of \((0,\infty)\), and
\[
B_a''(x)=\frac{4/x^3+12/x^5}{a^2}>0.
\]
Hence \(B_a\) has exactly one global minimum, at the unique positive solution of
\[
(1+a^2)x^4-2x^2-3=0,
\]
namely \(x_c=\sqrt{(1+\sqrt{4+3a^2})/(1+a^2)}\). Accordingly, if \(b\) lies below, at, or above \(B_a(x_c)\), there are respectively zero, one double, or two simple positive quartic zeros.

**3. An exact algebraic certificate for the regime boundary.** Direct expansion of the Sylvester resultant of \(Q_{a,b}\) and its derivative gives
\[
\operatorname{Disc}_x Q_{a,b}
=-a^4\bigl[27a^4b^4-288a^2b^2-256(a^2+b^2+1)\bigr]
=-a^4\mathcal H(a,b).
\]
Here \(\operatorname{Disc}Q=\operatorname{Res}(Q,Q')/(1+a^2)\), since the quartic has positive leading coefficient \(1+a^2\). The first equality is a polynomial identity; the second follows by expanding \((ab-4)(3ab+4)^3-256(a-b)^2\). To establish which side of the boundary is which, fix \(a>0\). As a polynomial in \(u=b^2\),
\[
\mathcal H(a,\sqrt u)=27a^4u^2-(288a^2+256)u-256(a^2+1)
\]
has exactly one strictly positive root, because its leading coefficient is positive and its constant term is negative. At the sole tangent intersection \(b=B_a(x_c)\), the quartic has a repeated root and therefore zero discriminant. Since \(\mathcal H(a,0)<0\), the sign is negative before this unique boundary and positive afterwards. This proves the sharp polynomial trichotomy without assuming the sign of a quartic discriminant alone counts positive roots.

**4. Global basins and equality.** When there is no positive root, \(Q_{a,b}(x)>0\) for every \(x>0\); hence \(G(x)<x\), so the nonnegative orbit tends to the sole fixed point, zero. At the double root \(x_c\), the same strict inequality holds on either side. Initial conditions below \(x_c\) converge to zero; those above \(x_c\) decrease toward it because the increasing map cannot cross a fixed point. When there are simple roots \(0<x_-<x_+\), \(Q\) is positive below \(x_-\), negative between the roots, and positive above \(x_+\). Monotone bounded iteration then gives extinction below \(x_-\), convergence to \(x_+\) above \(x_-\), and stationarity at \(x_-\) and \(x_+\) themselves. Since \(F_a\) is continuous, the corresponding odd-year limits are uniquely \(F_a\) of the even-year limits. Interchanging the seasons corresponds to shifting the phase of a positive periodic orbit, and the explicit persistence criterion is symmetric in \(a,b\).

**5. Exact contrast threshold and geometric-mean obstruction.** The identity
\[
\mathcal H(a,b)=(g^2-4)(3g^2+4)^3-1024g^2\sinh^2\theta
\]
is immediate from \(ab=g^2\) and \(a-b=2g\sinh\theta\). The displayed regimes follow by comparing this expression to zero. Independently, a positive periodic state \((x,y)\) must satisfy
\[
ab=\left(x+\frac1x\right)\left(y+\frac1y\right)\ge4,
\]
with equality only at \(x=y=1\), which forces \(a=b=2\). This verifies the sharp geometric-mean limit and its equality case directly. For \(g>2\), solving the strict contrast inequality gives the stated unique \(\theta_c(g)\), and the double-root argument gives the equality boundary.

## Verification
The standalone `CHECK.py` uses only Python's standard library. Running `python CHECK.py` verifies the exact displacement identity for rational sample coefficients and biomasses; it computes exact integer Sylvester determinants across an integer parameter grid; and it checks rational persistence/extinction witnesses with fixed product \(ab=9\), the critical homogeneous case, and numerical consistency of the contrast boundary. These finite diagnostics are reproducibility checks, not substitutes for the universal analytic proof. Every statement quantified over all positive coefficients or initial populations follows from the proof above.

## Relationship to prior work
Elaydi and Sacker, *Population models with Allee effect: a new model* (published online 2 December 2009), develop Allee population responses and nonautonomous periodic dynamics. Their broader framework includes rational Allee maps but does not in the inspected full text give the explicit symmetric polynomial regime boundary, all-basin classification, or fixed-geometric-mean contrast threshold here. Luís, Elaydi, and Oliveira (2010) study period-two compositions of **unimodal** Allee maps; the present sigmoid \(F_r\) is globally increasing and is not in that unimodal class. Brett and Kulenović (2014) examine the autonomous sigmoid response and a coupled two-species competitive system, not the alternating single-species composition. Roth and Schreiber (2014) address stochastic environmental fluctuations, not this deterministic two-season exact algebraic boundary. Related published mathematical classifications of other Allee and periodically switched population maps do not imply this family-specific contrast polynomial. Historical priority is not independently certified.

## Limitations
This is a deterministic idealized benchmark, not a field-fitted statement about species persistence. A positive attracting two-season orbit denotes deterministic conditional persistence from sufficiently large initial biomass, not stochastic survival. The result does not extend automatically to density-dependent immigration, random weather, harvesting, noise, different saturating maps, or periods of more than two seasons. General algebraic tools are classical, and no originality is claimed for the discriminant concept, one-dimensional monotone iteration, or the general phenomenon of Allee thresholds. Some older related primary full texts could not be checked comprehensively; historical priority remains a residual risk.

## References
1. S. N. Elaydi and R. J. Sacker, *Population models with Allee effect: a new model*, Journal of Biological Dynamics 4 (2010), 397–408, first online 2009-12-02, https://doi.org/10.1080/17513750903377434.
2. R. Luís, S. Elaydi, and H. Oliveira, *Non-autonomous periodic systems with Allee effects*, Journal of Difference Equations and Applications 16 (2010), 1179–1196, https://doi.org/10.1080/10236190902794951.
3. A. Brett and M. R. S. Kulenović, *Two species competitive model with the Allee effect*, Advances in Difference Equations (2014), article 307, 2014-12-03, https://doi.org/10.1186/1687-1847-2014-307.
4. G. Roth and S. J. Schreiber, *Pushed beyond the brink: Allee effects, environmental stochasticity, and extinction*, arXiv:1405.1686, first posted 2014-05-07, https://arxiv.org/abs/1405.1686.
