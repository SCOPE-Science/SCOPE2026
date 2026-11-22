# A sharp universal ceiling on periodic over random nectar harvesting

## Finding

Consider one replenishing nectar patch visited by a focal harvester. Its nectar stock has a saturating exponential recovery law, visits remove a fixed positive fraction of current nectar, and unrelated competitors remove the entire stock at independent Poisson times. At the **same mean return interval**, deterministic periodic visits always give higher long-run mean intake than Poisson visits; their **relative** gain never exceeds

\[
\mathcal R_* =\frac{1+x_*}{x_*}(1-e^{-x_*})
=1.298425607525639\ldots,
\]

where \(x_*\) is the unique strictly positive root of

\[
e^{x_*}=1+x_*+x_*^2,\qquad x_*=1.79328213290076\ldots.\]

This is a sharp universal **29.842560752564\%** ceiling on the extra intake attributable solely to regular rather than exponential intervisit timing in this model. It is attained **if and only if** the focal animal harvests all available nectar at every visit and \((r+\lambda)m=x_*\). The fact that systematic visits can help with decelerating regeneration is established prior work; the result asserted here is the sharp global *relative* ceiling, its equality conditions, and its partial-harvest/independent-competitor robustness.

## Assumptions and scope

The state \(X(t)\) is a nectar quantity in \([0,C]\), with \(C>0\). Between all visits, it satisfies \(\dot X=r(C-X)\), where \(r>0\). Independent competitors arrive as a homogeneous Poisson process of rate \(\lambda\ge0\) and immediately empty the patch. A focal animal visits at independent and identically distributed positive intervisit times \(T_j\), independent of competitors, with finite mean \(m=\mathbb ET_j\in(0,\infty)\). At each focal visit it collects fraction \(q\in(0,1]\) of stock just before the visit and leaves \((1-q)\) of it. Events are instantaneous; simultaneous visits have probability zero, and there is no travel-cost term. No optimization over the average visit frequency is claimed.

Define \(H(T)\) as the long-run focal nectar volume harvested per unit chronological time. The corresponding Poisson focal schedule has independent exponential gaps of mean \(m\), while the periodic schedule has \(T=m\) almost surely. Set \(\alpha=r+\lambda\), \(x=\alpha m>0\), and \(\phi=\mathbb E e^{-\alpha T}\).

## Proof

**Exact renewal formula.** Let \(Z_j\) be the stock just after focal visit \(j\), and \(Y_{j+1}\) the stock just before the next visit. Conditional on \(Z_j=z\) and the following gap \(T=t\), independent Poisson clearing and deterministic recovery imply the linear first-moment equation \(u'=rC-(r+\lambda)u\). Consequently,

\[
\mathbb E[Y_{j+1}\mid Z_j=z,T=t]
=\frac{rC}{\alpha}(1-e^{-\alpha t})+ze^{-\alpha t}.
\]

At each focal visit, \(Z_{j+1}=(1-q)Y_{j+1}\). Because the next gap is independent of the current stock,

\[
\mathbb E Z_{j+1}=(1-q)\left[\frac{rC}{\alpha}(1-\phi)+\phi\mathbb E Z_j\right].
\]

The affine recurrence contracts, since \((1-q)\phi<1\); the underlying visit-to-visit state also contracts under common driving events. Thus its stationary previsit mean is

\[
\mathbb E Y=\frac{rC}{\alpha}\frac{1-\phi}{1-(1-q)\phi}.
\]

The bounded-reward renewal law gives the exact long-run rate

\[
\boxed{H(T)=\frac{qrC}{\alpha m}\frac{1-\phi}{1-(1-q)\phi}.}\tag{1}
\]

The same expression holds for deterministic return intervals, by periodic stationary averaging. A finite initial transient does not change the long-run rate.

**Regular timing is best at fixed average rate.** Since \(s\mapsto e^{-\alpha s}\) is strictly convex, Jensen's inequality gives \(\phi\ge e^{-\alpha m}\), with equality only for \(T=m\) almost surely. The factor \((1-\phi)/(1-(1-q)\phi)\) is strictly decreasing in \(\phi\), its derivative being \(-q/[1-(1-q)\phi]^2\). Hence regular timing uniquely maximizes the rate over all positive independent renewal gaps of mean \(m\). This qualitative mechanism is not asserted to be new.

**Exact comparison against random timing.** For deterministic gaps, \(\phi=e^{-x}\). For exponential gaps of mean \(m\), \(\phi=1/(1+x)\). Formula (1) gives

\[
H_{\mathrm{per}}=\frac{qrC}{\alpha m}\frac{1-e^{-x}}{1-(1-q)e^{-x}},\qquad
H_{\mathrm{Poi}}=\frac{qrC}{x+q}.
\]

Therefore their ratio and its excess over one are

\[
\mathcal R_q(x)=\frac{(x+q)(e^x-1)}{x(e^x-1+q)},\qquad
\mathcal R_q(x)-1=\frac{q(e^x-1-x)}{x(e^x-1+q)}>0.
\]

For fixed \(x>0\), writing \(E=e^x-1>x\), the derivative with respect to \(q\) is \(E(E-x)/[x(E+q)^2]>0\). Thus \(\mathcal R_q(x)\le\mathcal R_1(x)\), strictly unless \(q=1\). For complete focal harvest,

\[
\mathcal R_1(x)=\frac{1+x}{x}(1-e^{-x}),\qquad
\mathcal R_1'(x)=\frac{e^{-x}(1+x+x^2)-1}{x^2}.
\]

Let \(f(x)=e^x-1-x-x^2\). Then \(f(0)=f'(0)=0\) and \(f''(x)=e^x-2\) changes sign exactly once on \((0,\infty)\). It follows that \(f'\) decreases and then increases, crossing zero exactly once on \((0,\infty)\); hence \(f\) decreases and then increases, crossing zero exactly once more at \(x_*\). In turn \(\mathcal R_1'\) is positive for \(0<x<x_*\) and negative for \(x>x_*\). Moreover \(\mathcal R_1(x)\to1\) at both endpoints \(x\downarrow0\) and \(x\to\infty\). The maximum is unique, equals the stated \(\mathcal R_*\), and is attained exactly at \(q=1\) and \(x=x_*\). This condition is feasible for every \(r>0\) and \(\lambda\ge0\) by choosing \(m=x_*/(r+\lambda)\). The value of \(C\) cancels from the ratio.

## Verification

`CHECKER.py` is a standalone Python standard-library diagnostic. Running `python CHECKER.py` produced 90,810 passing checks, including randomized analytic-formula comparisons, two-point renewal Jensen tests, finite simulations of both focal clocks with explicit independent competitor events, a numerical root bracket, and derivative-sign samples. Its numerical root is \(x_*\approx1.793282132900761\) and its ceiling \(\mathcal R_*\approx1.298425607525639\). Computed checks are supplemental; the full-parameter quantifiers and uniqueness follow from the proof above.

## Relationship to prior work

Possingham (1989) already established the **qualitative** effect of systematic return timing when nectar replenishment decelerates; his journal issue abstract explicitly states this. Ohashi and Thomson (2005) provide a detailed simulation of periodic traplining versus random searching, using linear replenishment or linear replenishment with a hard cap, and complete harvest. Korman et al. (2020) analyze discrete-round linearly replenished cacti with stochastic emptying by competitors and purely stochastic focal visits. These known results motivate but do not, in the inspected material, state the quantitative sharp ratio across exponential saturation, partial focal harvesting, and independent Poisson competition. A broader unexamined renewal-harvesting result could nevertheless imply the ratio without matching its terminology.

## Limitations

This is a one-patch, fixed-mean, exponential-recovery benchmark. It assumes a fixed fractional harvest, competitor clearing events independent of the focal animal, stationary parameters, and no handling or travel costs; it is not a result for spatial route optimization or for empirically calibrated nectar dynamics. Historical originality remains provisional: the full texts of Possingham (1988, 1989) could not be obtained for a complete mathematical implication comparison; the 1989 abstract and secondary discussions were inspected. The exact estimate assumes volume intake, not energetic profitability or pollination success. The high-precision constant is a numerical evaluation of an implicitly and uniquely defined real number.

## References

- Possingham, H. P. (1988). *A model of resource renewal and depletion: applications to the distribution and abundance of nectar in flowers.* Theoretical Population Biology 33, 138–160. https://doi.org/10.1016/0040-5809(88)90010-X.
- Possingham, H. P. (1989). *The distribution and abundance of resources encountered by a forager.* The American Naturalist 133, 42–60. https://doi.org/10.1086/284900.
- Ohashi, K. and Thomson, J. D. (2005). *Efficient harvesting of renewing resources.* Behavioral Ecology 16, 592–605. First online February 16, 2005. https://doi.org/10.1093/beheco/ari031.
- Korman, A., Emek, Y., Collet, S., Goldshtein, A. and Yovel, Y. (2020). *Exploitation of Multiple Replenishing Resources with Uncertainty.* arXiv:2007.09640. https://arxiv.org/abs/2007.09640.
