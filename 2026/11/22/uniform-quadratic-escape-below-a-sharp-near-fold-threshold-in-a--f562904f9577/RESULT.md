# Uniform quadratic escape below a sharp near-fold threshold in a fixed-point-free planar map

## Finding
For the four-parameter real-plane map
\[
F_{a,b,c,d}(x,y)=\left(x+y,\ y-a|y|-xy+bx^2-cy^2+d\right),\qquad a,b,c,d>0,
\]
put
\[
c_{\rm esc}=\frac{2+b}{4}-\frac{a^2}{4d}.
\]
If \(0<c\le c_{\rm esc}\), **every forward orbit escapes to spatial infinity**, uniformly at least at square-root speed: for each fixed parameter tuple there is a constant \(\gamma>0\), independent of the initial point, such that
\[
\liminf_{n\to\infty}\frac{\max\{|x_n|,|y_n|\}}{\sqrt n}\ge\gamma.
\]
For strict \(c<c_{\rm esc}\), one may take \(\gamma=\sqrt{2\delta/(1+b)}\), where
\[
\delta=d-\frac{a^2}{4k}>0,\qquad k=\frac{2+b}{4}-c.
\]
At the boundary \(c=c_{\rm esc}>0\), the same escape conclusion holds with some strictly positive parameter-dependent constant, despite the vanishing one-step drift at two isolated points. Therefore, the entire parameter chamber contains no bounded forward trajectories, nonempty compact invariant sets, or invariant Borel probability measures of any support.

The first parameter at which a primitive real two-cycle can exist, for fixed positive \(a,b,d\) with \(c_{\rm esc}>0\), is
\[
c_{\rm fold}=\frac{2+b}{4}-\frac{a^2}{4K},\qquad K=d+\frac{4b}{(1+b)^2},
\]
strictly above the escape boundary by
\[
\boxed{c_{\rm fold}-c_{\rm esc}=\frac{a^2b}{dK(1+b)^2}>0.}
\]
For the published numerical parameter slice \((a,b,d)=(1/100,1/10,1/10)\), the escape chamber ends at \(c_{\rm esc}=2099/4000\), and the established two-cycle fold occurs at \(c_{\rm fold}=1093979/2084000\): the exact gap is only \(1/5210\). No claim is made about the entire narrow intervening region.

## Assumptions and scope
All four parameters are strictly positive real numbers and the phase space is the whole plane. The escape theorem has nonempty parameter scope precisely when \(a^2<d(2+b)\), making \(c_{\rm esc}>0\). Escape means \(\max\{|x_n|,|y_n|\}\to\infty\), not merely nonexistence of a bounded complete orbit. A forward orbit is generated recursively by \((x_{n+1},y_{n+1})=F_{a,b,c,d}(x_n,y_n)\). The normalization is exactly the printed map, without time rescaling or truncation. The formula for \(c_{\rm fold}\) is a cycle-existence comparator, not a claimed global recurrence threshold.

## Proof
**1. A positive quadratic coboundary.** Define the real polynomial potential and coefficient
\[
W(x,y)=y+\frac{1+b}{2}x^2,\qquad k=\frac{2+b}{4}-c.
\]
Direct substitution, using \(x'=x+y\), yields the **exact identity for every real \((x,y)\)**
\[
\boxed{W(F(x,y))-W(x,y)
=b\left(x+\frac y2\right)^2+ky^2-a|y|+d.}
\]
When \(0<c\le c_{\rm esc}\), \(k\ge a^2/(4d)>0\). Completing the square gives
\[
W(F(x,y))-W(x,y)
=b\left(x+\frac y2\right)^2+k\left(|y|-\frac{a}{2k}\right)^2+\delta,
\qquad \delta=d-\frac{a^2}{4k}\ge0.
\]
For \(c<c_{\rm esc}\), \(\delta>0\); iteration yields \(W(x_n,y_n)\ge W(x_0,y_0)+n\delta\). Put \(R_n=\max\{|x_n|,|y_n|\}\). Since \(W(x_n,y_n)\le R_n+(1+b)R_n^2/2\), it follows that
\[
\liminf_{n\to\infty}R_n/\sqrt n\ge\sqrt{2\delta/(1+b)}>0.
\]

**2. The equality case is strictly escaping too.** At \(c=c_{\rm esc}>0\), \(\delta=0\) and the drift is the continuous coercive function
\[
Q(x,y)=b\left(x+\frac y2\right)^2+k\left(|y|-\frac a{2k}\right)^2\ge0.
\]
Its zero set consists of \(P_+=(-z/2,z)\) and \(P_-=(z/2,-z)\), with \(z=a/(2k)>0\). From either point the first coordinate \(x'=x+y\) excludes a return to itself, so the only candidate zero-to-zero transition is \(P_\pm\to P_\mp\). But zero drift at the starting point forces \(W(F(P_\pm))=W(P_\pm)\), and these two points have distinct \(W\)-values: their squared first coordinates agree while their second coordinates differ by \(2z\). Thus neither directed transition is possible, and \(Q+Q\circ F\) is everywhere strictly positive. It is continuous and coercive: if \(|y|\) or \(|x+y/2|\) tends to infinity, then \(Q\) tends to infinity, and \(Q\circ F\ge0\). Hence it attains a positive global minimum \(\eta\), giving
\[
W(F^2(x,y))-W(x,y)\ge\eta
\]
for every initial point. The one-step drift is also nonnegative, hence \(W(x_n,y_n)\ge W(x_0,y_0)+\eta\lfloor n/2\rfloor\). The same quadratic comparison yields \(\liminf R_n/\sqrt n\ge\sqrt{\eta/(1+b)}>0\). Finally, an invariant Borel probability \(\mu\) would satisfy \(\mu(B_R)=\int\mathbf1_{B_R}(F^n(u))\,d\mu(u)\to0\) for every bounded ball \(B_R\), by pointwise escape and dominated convergence. Exhaustion by bounded balls contradicts total mass one.

**3. The exact comparator to two-cycle onset.** In any genuine two-cycle the two successive vertical coordinates are \(z\) and \(-z\), with \(z>0\), and the coordinates can be written \((X-z/2,z)\) and \((X+z/2,-z)\). The two second-coordinate return residuals are \(bX^2+kz^2-az+d\pm z[2-(1+b)X]\). Their difference gives \(X=2/(1+b)\); their vanishing is then equivalent to
\[
kz^2-az+K=0,\qquad K=d+\frac{4b}{(1+b)^2}>d.
\]
Conversely each positive root yields a genuine two-cycle by direct substitution. When \(c<c_{\rm fold}\), \(k>a^2/(4K)>0\) and the discriminant is negative; at \(c=c_{\rm fold}\) the positive double root \(z=a/(2k)\) first appears. There are no fixed points because \(F(x,0)=(x,bx^2+d)\) never fixes its argument. Thus the stated first two-cycle parameter and the exact positive gap follow by elementary algebra. No inference about other recurrent orbits in the gap is made.

## Verification
The accompanying standalone `verify_escape.py` checks the exact coboundary identity, the mandatory two-cycle midpoint, and the escape-to-fold gap formula symbolically, as well as three rational parameter examples. Run with Python 3 and SymPy installed: `python3 verify_escape.py`. This finite symbolic check supports the algebraic identities; the global assertion is proved by the coercivity and iteration argument above. The endpoint proof excludes individual transitions between the zero-drift points, not just a two-cycle.

## Relationship to prior work
Huynh et al. (2019) introduced this map and reported a parameter-dependent period-doubling transition and chaotic numerical trajectories. The related map of Panahi, Sprott and Jafari (2018) is smooth and their analysis emphasizes numerical attractors, basins and Lyapunov spectra, not the positive-\(a\) all-trajectory theorem. A published same-map calculation for the numerical slice \((a,b,d)=(1/100,1/10,1/10)\) supplies exact primitive two-cycle and stability intervals, but no general all-orbit escape implication: absence of period-two cycles by itself does not rule out compact higher-period or nonperiodic dynamics. The two-cycle fold is used only to quantify the near-sharp escape bound, not counted as a new result.

## Limitations
The sufficient escape chamber is not proved optimal: the interval \(c_{\rm esc}<c<c_{\rm fold}\) remains unclassified, as do other parameter regimes. No uniform escape constant over all allowed parameter values is asserted, and the endpoint rate constant is existential. The theorem neither excludes nor classifies chaotic attractors at the larger parameter values used for numerical experiments. Relevant broader recurrence literature may contain equivalent coercive-potential inequalities in a different notation, although no decisive same-map theorem was identified in the checked material.

## References
1. V. V. Huynh, A. Ouannas, X. Wang, V.-T. Pham, X. Q. Nguyen, F. E. Alsaadi, “Chaotic Map with No Fixed Points: Entropy, Implementation and Control,” *Entropy* **21** (2019), 279, https://doi.org/10.3390/e21030279.
2. S. Panahi, J. C. Sprott, S. Jafari, “Two Simplest Quadratic Chaotic Maps Without Equilibrium,” *International Journal of Bifurcation and Chaos* **28** (2018), 1850144, https://sprott.physics.wisc.edu/pubs/paper500.pdf.
3. “Two disjoint attracting two-cycle bands in a fixed-point-free quadratic map” (2026), [record and proof](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-two-disjoint-attracting-two-cycle-bands-in-a-fixed-point-free-qu--cc95e26c74ab).
4. C. García-Grimaldo, E. Campos-Cantón, “Comparative Analysis of Chaotic Features of Maps Without Fixed Points,” in *Complex Systems and Their Applications* (2022), pp. 151–176, https://doi.org/10.1007/978-3-031-02472-6_8 (abstract consulted; chapter text not available).
