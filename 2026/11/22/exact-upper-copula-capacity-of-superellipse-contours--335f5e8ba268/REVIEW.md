# Scientific review: exact upper copula capacity of superellipse contours

## Correctness — PASS

The event is the equality contour, not a filled region. For every admissible center and pair of positive semiaxes, the folded first-coordinate density of the contour restriction is bounded above by \(2\) because the underlying one-dimensional marginal is Lebesgue uniform. The folded second-coordinate domination, pulled back by the strictly decreasing graph, independently bounds it by \(2|g'|\). These restrictions yield a global upper bound for every copula, without assuming it has a density. A four-sign graph submeasure with the pointwise minimum density attains this bound; the residual marginals are absolutely continuous and permit an explicit product coupling off the zero-area contour. The unique-slope-crossing computation evaluates the integral in the subunit, unit and superunit exponent regimes. The endpoints of the graph have zero mass and do not invalidate the change of variables, including for \(0<p<1\). A same-model replay of the embedded numerical diagnostic checks finite specializations and quadratures but is not used to prove infinite-parameter claims.

## Originality — PASS against inspected evidence

The eligible motivating paper by Trutschnig and Úbeda-Flores (arXiv:2610.33646v1, October 24, 2026, Theorem 4.11) bounds the mass that convex combinations of **associative** copulas assign to positive-slope chains off the diagonal. It does not evaluate maximization over **all** copulas of probability on a closed, nonlinear superellipse contour. Omladič, Vuk and Zalar (arXiv:2611.14008v1, November 10, 2026) derive compatibility tests for finite copula interpolation, not an explicit continuum contour capacity. Subsequent general capacity work by Côté and Wang (arXiv:2611.25237v1, November 18, 2026, §4.2 Proposition 6) credits Kellerer's universal closed-set covering duality; it gives an implicit optimization for *all* closed events, but does not evaluate the superellipse contour capacity as an explicit function of both axes and all positive exponents. Its §4.3 Theorem 2 concerns *convex filled* sets: their capacity is \(2\min(a,b)\) in our axes, while the **boundary** has strictly less capacity for \(p>1\). Perlman and Wellner (2011, full text) study centered circular/elliptical distributions on filled supports, not maximization of mass on an exact contour. Other mathematical-record summaries about \(L^p\)-spherical copula estimators, finite-support sum laws and elliptical geometries did not reveal an implying result; inaccessible full texts were not called not-covering based on summaries alone. Residual risk: a general graph-coupling result may already evaluate this particular curve family.

## Value — PASS

This evaluates a natural, parameterized **exact-contour** event under arbitrary dependence, where a naively appealing convex-hull projection bound gives the wrong answer for every \(p>1\). A single theorem provides the entire exponent transition, including cusp slopes at the diamond, arbitrary semiaxes, the circle/ellipse case, the maximizing submeasure and uniqueness of its folded radial distribution. Distinguishing boundary concentration from filled-region concentration is a structurally motivated statistical-dependence question, not an arbitrary numerical slice of a known table. The result is a natural complete family classification, without claiming a general arbitrary-set capacity formula.

## Closest literature and limitations

- Trutschnig and Úbeda-Flores (2026), arXiv:2610.33646v1, Theorem 4.11: positive-slope chain mass within the convex hull of associative copulas; different coupling class and event geometry.
- Omladič, Vuk and Zalar (2026), arXiv:2611.14008v1: finite-grid copula interpolation feasibility; no nonlinear continuum equality-contour formula.
- Côté and Wang (2026), arXiv:2611.25237v1 (subsequent source): abstract closed-set cover duality and filled-convex-set capacity, not the evaluated contour formula.
- Perlman and Wellner (2011), doi:10.3390/sym3030574: circular and elliptical copulas with filled geometric supports, not arbitrary-copula mass maximization on exact boundaries.
- General closed-set marginal compatibility and Hall/Kellerer duality remain prior work, not claimed new.
- Not proved: unrestricted curve capacities, entire maximizing-copula uniqueness, or multivariate higher-dimensional analogues. Independent validation and exhaustive historical-priority certification remain unperformed.

Self-review: passed. Independent audit: not yet performed.
