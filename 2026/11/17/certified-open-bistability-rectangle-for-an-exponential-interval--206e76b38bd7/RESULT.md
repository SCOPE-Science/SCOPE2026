# Certified open bistability rectangle for an exponential interval map

## Finding

For every pair of real parameters in the **open** rectangle
\[
19.05995<a<19.06005,\qquad 0.3960999<b<0.3961001,
\]
the interval map
\[
 f_{a,b}(x)=\frac{x}{x+(1-x)e^{a(x-b)}},\qquad 0\leq x\leq1,
\]
has **exactly two attracting periodic orbits**, both of primitive period four. Here *attracting* means that the absolute value of the derivative of the fourth return is strictly below one. The two cycles are different even after cyclic rephasing. All statements concern the discrete map, not an assertion about an underlying predator–prey differential equation.

The upper bound of two attracting periodic orbits is already known for this bimodal family. The contribution here is an exact, independently checkable, two-dimensional parameter rectangle on which the upper bound is attained by two distinct genuine four-cycles; previously exhibited examples in this family were numerical.

## Assumptions and scope

Let \(a\), \(b\) be arbitrary real parameters in the displayed open rectangle. All interior points satisfy \(0<f_{a,b}(x)<1\). The log-odds coordinate \(s=\log(x/(1-x))\) is a smooth bijection from \((0,1)\) onto \(\mathbb R\). Under this change of coordinates the same map becomes
\[
 H_{a,b}(s)=s+a\bigl(b-\sigma(s)\bigr),\qquad
 \sigma(s)=\frac{1}{1+e^{-s}}.
\]
The boundary fixed points \(x=0\) and \(x=1\) are repelling in the stated parameter rectangle.

Take the two exact rational centers and common radius
\[
 c_1=-7.616520527293,\quad c_2=-7.404707992386,
 \quad r=0.002,\qquad J_i=[c_i-r,c_i+r].
\]
The coordinates are rational decimal certificates, not asserted exact periodic points.

## Proof

**1. Exact conjugacy.** Write \(x=\sigma(s)\). Direct algebra gives
\[
 \log\frac{f_{a,b}(x)}{1-f_{a,b}(x)}
 =\log\frac{x}{1-x}-a(x-b)=H_{a,b}(s).
\]
The conjugacy is smooth and preserves the least periods, attraction and periodic multipliers of interior cycles.

**2. Rigorous fourth-return enclosures.** The attached standalone verifier implements outward-rounded rational interval arithmetic on the grid \(10^{-30}\mathbb Z\). Each elementary addition, product and division rounds the lower and upper bounds outward using integer floors and ceilings. The exponential uses, for \(0\leq t\leq10\), the identity \(e^{-t}=e^{-t/16}{}^{16}\). For \(z=t/16\leq1\), the sum \(S_{23}(z)=\sum_{j=0}^{23}z^j/j!\) has the explicit positive remainder bound
\[
 S_{23}(z)\leq e^z\leq S_{23}(z)+\frac{2z^{24}}{24!}.
\]
Indeed the omitted nonnegative terms have successive ratios no greater than \(1/25\). Inversion and four squarings enclose \(e^{-t}\), and hence enclose \(\sigma(s)\) monotonically at any rational interval endpoint encountered. This is a finite inequality proof over the reals, not a floating-point extrapolation or an infinite-process certificate.

The verifier propagates each \(J_i\) through four copies of \(H_{a,b}\), uniformly for the whole parameter rectangle, to enclose its derivative product
\[
 (H_{a,b}^{4})'(s)=\prod_{j=0}^{3}
 \left(1-a\sigma(H_{a,b}^{j}(s))
 \bigl[1-\sigma(H_{a,b}^{j}(s))\bigr]\right).
\]
When the range of \(\sigma\) crosses \(1/2\), the verifier explicitly includes the maximum \(1/4\) of \(u(1-u)\) rather than relying on endpoint evaluation. The resulting strict rational enclosures imply, uniformly in \((a,b)\) and \(s\in J_i\),
\[
 \sup_{J_1}|(H^4)'|<0.51,
 \qquad \sup_{J_2}|(H^4)'|<0.72,
\]
and the center residuals satisfy
\[
 |H^4(c_1)-c_1|<0.00095,\qquad
 |H^4(c_2)-c_2|<0.00053.
\]
As \(0.00095<(1-0.51)\,0.002\) and \(0.00053<(1-0.72)\,0.002\), the mean value theorem proves that \(H^4(J_i)\) lies strictly inside \(J_i\). It is a strict contraction there, giving exactly one fourth-return fixed point in each \(J_i\) for every admissible parameter pair.

**3. Least periods and inequivalence.** The exact interval computations also show that \(H^2(J_i)\cap J_i=\varnothing\). Hence neither fixed point has period one or two. The verifier furthermore checks \(H^j(J_1)\cap J_2=\varnothing\) for each \(j\in\{0,1,2,3\}\). Therefore the two fixed points belong to different least-period-four cycles. Their fourth-return multipliers are strictly less than one in modulus, so both are hyperbolically attracting.

**4. Exhaustion of attracting cycles.** For completeness, the known upper bound applies here. Indeed \(H_{a,b}\) has two critical points for \(a>4\), since \(H'=1-a\sigma(1-\sigma)\). Writing \(p=\sigma(1-\sigma)\), its Schwarzian derivative away from critical points is
\[
 S H=-\frac{ap\bigl(2+(a-12)p\bigr)}{2(1-ap)^2}<0.
\]
The standard negative-Schwarzian critical-basin theorem, as applied to this same map by Kryzhevich, Avrutin and Söderbacka, bounds the number of attracting periodic orbits by its two critical points. Since two have just been certified, there are exactly two. This does **not** assert that there are only two periodic orbits altogether: repelling cycles can also exist.

## Verification

Run `python3 verify_bistability.py` with Python 3 and its standard library; it requires no external scientific package or input file. The test checks both full-rectangle contraction inequalities, primitive period four, and cross-cycle disjointness. The executed certificate reports, in log-odds coordinates, the following outward rational intervals (decimal figures rounded for display only):

| Base interval | Enclosed fourth-return derivative | Upper bound on center residual | Allowed residual bound |
|---|---|---:|---:|
| \(J_1\) | \([0.1033144,0.5009922]\) | \(0.000949105\) | \(0.000998015\) |
| \(J_2\) | \([0.6260093,0.7110683]\) | \(0.000527116\) | \(0.000577863\) |

The certificate's assertions compare exact grid integers, not these display-roundings. For the first cycle, \(H^2(J_1)\subset(-1.706,-1.681)\); for the second, \(H^2(J_2)\subset(-2.494,-2.469)\). Both are disjoint from their respective base intervals. The code also verifies disjointness between \(J_2\) and all four phases of the first interval.

## Relationship to prior work

Kryzhevich, Avrutin and Söderbacka (2021, arXiv:2108.06739) introduced and analyzed this same bimodal map in a shifted-logistic parametrization. They proved the at-most-two-attractors principle and presented numerical bistability regions, including two period-four attracting orbits. The present finding does **not** claim first discovery of bistability or the upper bound. It upgrades a reported narrow numerical coexistence phenomenon to a **finite, exact, uniform certificate on a specified open two-parameter rectangle** with quantitative contraction margins and distinctness of cycles.

Bielawski and coauthors (2024, arXiv:2411.01495) establish a rotation-like attracting-cycle theorem for a different large-parameter regime and also report numerical behavior. Kryzhevich, Zhang and Chmara (2024, arXiv:2412.16379) discuss the same replicator formulation, its already-known coexistence examples, and a hyperbolic chaotic repeller for sufficiently large coupling. Those theorems do not provide the present fourth-return interval certificate at the displayed parameters.

## Limitations

The theorem describes a deliberately small explicit subregion of the bistability zone; it does not determine the zone's sharp boundary. It does not count repelling period-four cycles, describe basin boundaries, or lift periodic dynamics rigorously to the original three-dimensional predator–prey differential equations. The associated scientific literature contains numerical coexistence evidence at substantially more parameters, so this is not claimed as a newly discovered dynamical phenomenon. Publication priority beyond the inspected literature, especially an unindexed rigorous certificate for this identical parameter rectangle, remains uncertain.

## References

1. S. Kryzhevich, V. Avrutin and G. Söderbacka, *Bistability in a one-dimensional model of a two-predators-one-prey population dynamics system*, arXiv:2108.06739, first posted 2021-08-15, https://arxiv.org/abs/2108.06739.
2. J. Bielawski, T. Chotibut, F. Falniowski, M. Misiurewicz and G. Piliouras, *Interval maps mimicking circle rotations*, arXiv:2411.01495, first posted 2024-11-03, https://arxiv.org/abs/2411.01495.
3. S. Kryzhevich, Y. Zhang and M. Chmara, *Bifurcations and invariant sets for a family of replicator maps from evolutionary games*, arXiv:2412.16379, first posted 2024-12-20, https://arxiv.org/abs/2412.16379.
4. D. Singer, *Stable Orbits and Bifurcation of Maps of the Interval*, SIAM J. Appl. Math. 35 (1978), 260–267, https://doi.org/10.1137/0135020.
