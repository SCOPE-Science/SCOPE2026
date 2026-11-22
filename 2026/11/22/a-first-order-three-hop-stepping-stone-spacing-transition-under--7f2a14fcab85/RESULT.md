# A first-order three-hop stepping-stone spacing transition under inverse-quadratic dispersal

## Finding

For a three-hop route with two intermediate habitat patches, the optimal arrangement jumps discontinuously from equal spacing to two equal short gaps and one longer gap at one precise separation. This occurs even though equal spacing remains locally optimal beyond the jump. The shortest serial route exhibiting such a discontinuous global transition has three hops; the corresponding two-hop transition is continuous.

Let the endpoint distance divided by the dispersal scale be \(s>0\). Define
\[
a(s)=\frac{2}{s+\sqrt{s^2-8}},\qquad s\ge 2\sqrt2.\]
There is a unique \(s_*\in(2\sqrt2,3)\) solving
\[
\left(1+\frac{s_*^2}{9}\right)^3
=\frac{\left(1+a(s_*)^2\right)^3}{a(s_*)^2},
\]
with numerical value \(s_*=2.847567859346252638\ldots\). The maximizers are exactly the equal triple for \(s<s_*\); the equal triple and three permutations of \((a(s_*),a(s_*),1/a(s_*))\) for \(s=s_*\); and just those three permutations for \(s>s_*\). Every gap is strictly positive in every optimum, so intermediate patches never coincide with endpoints at an optimum.

## Assumptions and scope

Fix \(L,\ell>0\) and two freely locatable, individually identical, pointlike intermediate patches between fixed endpoint patches at coordinates \(0\) and \(L\). Their three nonnegative successive gaps \((d_1,d_2,d_3)\) satisfy \(\sum_{i=1}^{3}d_i=L\). Each required forward hop of length \(d\) succeeds with probability
\[
p(d)=\frac{1}{1+(d/\ell)^2}.
\]
Assume conditional independence of the three required hops. The end-to-end success objective is their product, not expected population growth, a competing-path network metric, or long-run establishment probability. Write \(x_i=d_i/\ell\), so \(x_i\ge0\) and \(\sum x_i=s=L/\ell\). The product to maximize is
\[
P(x_1,x_2,x_3)=\prod_{i=1}^3(1+x_i^2)^{-1}.
\]
All claims quantify over every real \(s>0\) and all feasible real gap triples, including boundary configurations.

## Proof

**Step 1: interior reduction.** Maximizing \(P\) is equivalent to minimizing \(G=\sum_{i=1}^3 g(x_i)\), with \(g(u)=\log(1+u^2)\). The compact feasible simplex has a minimizer. A feasible point with a zero gap and a positive gap \(y\) cannot minimize: shifting \(\varepsilon>0\) from \(y\) to the zero coordinate has first derivative \(g'(0)-g'(y)=-2y/(1+y^2)<0\). Thus every minimizer is strictly interior.

**Step 2: all stationary patterns.** Stationarity gives
\[
g'(x_i)=\frac{2x_i}{1+x_i^2}=\lambda\quad\text{for every }i.
\]
For positive \(u,v\), equality of these derivatives is equivalent to \((u-v)(1-uv)=0\). Hence all coordinates are equal or take the two reciprocal values \(u\) and \(1/u\). If two coordinates exceed \(1\), transferring a small amount between them has second derivative \(2g''(u)<0\) at equality, and is not a local minimum. Apart from uniform spacing, any possible nonuniform minimum therefore has form \((x,x,1/x)\) up to permutation with \(0<x<1\), and necessarily
\[
s=2x+\frac1x,\qquad x_{\pm}(s)=\frac{s\pm\sqrt{s^2-8}}4.
\]
Such candidates first exist at \(s=2\sqrt2\). For \(2\sqrt2<s<3\), \(x_+(s)>1/\sqrt2\), and the second variation along \((1,1,-2)\) equals
\[
2g''(x)+4g''(1/x)=\frac{4(1-x^2)(1-2x^2)}{(1+x^2)^2}<0
\]
on that upper branch. For \(s>3\), the upper branch has two coordinates above \(1\), also ruling it out. The remaining nonuniform candidate is \(x=x_-(s)=a(s)\in(0,1/\sqrt2)\). It is a strict local minimum: the second variation is positive along both tangent directions \((1,-1,0)\) and \((1,1,-2)\), which diagonalize the tangent quadratic form by symmetry. At the bifurcation value \(2\sqrt2\) the branches merge, but direct objective comparison below rules them out as a global minimum.

**Step 3: exact global threshold.** Uniform spacing gives denominator product
\[
D_{\mathrm{eq}}(s)=\left(1+\frac{s^2}{9}\right)^3.
\]
The only surviving nonuniform candidate gives
\[
D_{\mathrm{asym}}(s)=\left(1+a(s)^2\right)^2\left(1+a(s)^{-2}\right)
=\frac{\left(1+a(s)^2\right)^3}{a(s)^2}.
\]
At \(s=2\sqrt2\), \(D_{\mathrm{asym}}=27/4\), \(D_{\mathrm{eq}}=4913/729\), and \(D_{\mathrm{asym}}-D_{\mathrm{eq}}=31/2916>0\). At \(s=3\), the products are \(125/16<8\) respectively. Define \(\Delta(s)=\log D_{\mathrm{asym}}(s)-\log D_{\mathrm{eq}}(s)\). Along the stationary asymmetric branch, constrained differentiation gives the envelope identity
\[
\Delta'(s)=g'(a(s))-g'(s/3).
\]
For \(2\sqrt2<s<3\), \(a(s)<s/3<1\) and \(g'\) is strictly increasing on \((0,1)\); hence \(\Delta'(s)<0\). The two opposite endpoint signs imply exactly one crossing \(s_*\), with the claimed complete global classification. If \(s>3\), the equal stationary configuration has \(g''(s/3)<0\), so it cannot minimize; only the lower asymmetric branch remains. At \(s=3\), direct comparison already favors asymmetry. If \(s<2\sqrt2\), no distinct positive stationary triple is possible, and the equal triple minimizes. Strict inequalities outside the crossing exclude all other minimizers.

**Step 4: discontinuity and shortest route.** At the crossing, \(a(s_*)\approx0.629489479444055\), whereas the equal gap is \(s_*/3\approx0.949189286448751\); these triples are distinct. Uniform spacing remains strictly locally optimal throughout \(s<3\) because \(g''(s/3)>0\). For a two-hop route with gaps \(u,v\ge0\), \(u+v=s\), the exact identity
\[
(1+u^2)(1+v^2)=s^2+(uv-1)^2
\]
proves that the unique optimum is equal spacing for \(0<s\le2\), while for \(s>2\) the two optimal gaps are \((s\pm\sqrt{s^2-4})/2\) in either order. Those gaps approach \(1,1\) as \(s\downarrow2\), giving a continuous two-hop transition. A one-hop route has no gap-placement decision.

## Verification

A standalone Python-standard-library script, `verify.py`, reproduces a 65-digit bisection of the threshold, checks the exact endpoint comparisons, tests random feasible triples across the pre- and post-transition regimes, validates the two-hop identity, and checks local-branch conditions. Executing `python verify.py` yielded `CHECKS_PASSED 76359`. These finite numerical tests are corroboration; the infinite-parameter theorem rests on the analytic proof above. Every result is dimensionless; physical distances follow by multiplication by \(\ell\).

## Relationship to prior work

Lapin et al. (2024) prioritize real-world forest stepping-stone habitats using multiple ecological indicators, motivating spatial connectivity but not solving the continuous two-stone placement optimization. Saura, Bodin and Fortin (2014; first online 2013) already formulate dispersal connectivity through successive stepping-stone stages and maximum-product path ideas, which are not claimed as new here; their network analysis does not give the present inverse-quadratic three-gap global threshold. Chapman, Dytham and Oxford (2007; online 2006) compare empirical long-distance dispersal kernels but do not optimize fixed three-stage spacing. Skelsey, With and Garrett (2013; published online 2012) analyze landscape heterogeneity and dispersal scales for different model outputs. Existing two-hop placement analyses do not logically decide the three-hop discontinuous global switch. The claim is confined to the specific normalized three-stage kernel and objective.

## Limitations

The independent sequential-hop, exact inverse-quadratic success model is not field-calibrated. No stochastic population persistence, patch area/quality, capacity, competing routes, travel time, individual movement trajectories, habitat-selection effects or correlated hops are modeled. The transition does not assert that actual conservation design should cluster stepping stones; fitted species- and landscape-specific modeling remains necessary. The comparison with inspected literature supports no known covering theorem, not a proof of absolute historical priority. Broad generalizations to other numbers of stages or exponents are not established.

## References

- Lapin, K., Hoffmann, J. A., Braun, M., and Oettel, J. (2024). *Identification and prioritization of stepping stones for biodiversity conservation in forest ecosystems*. Conservation Science and Practice. First online June 14, 2024. https://doi.org/10.1111/csp2.13161
- Saura, S., Bodin, Ö., and Fortin, M.-J. (2014). *Stepping stones are crucial for species' long-distance dispersal and range expansion through habitat networks*. Journal of Applied Ecology 51:171–182. First online October 1, 2013. https://doi.org/10.1111/1365-2664.12179
- Chapman, D. S., Dytham, C., and Oxford, G. S. (2007). *Modelling population redistribution in a leaf beetle: an evaluation of alternative dispersal functions*. Journal of Animal Ecology 76:36–44. First online December 20, 2006. https://doi.org/10.1111/j.1365-2656.2006.01172.x
- Skelsey, P., With, K. A., and Garrett, K. A. (2013). *Why dispersal should be maximized at intermediate scales of heterogeneity*. Theoretical Ecology. https://doi.org/10.1007/s12080-012-0171-3
