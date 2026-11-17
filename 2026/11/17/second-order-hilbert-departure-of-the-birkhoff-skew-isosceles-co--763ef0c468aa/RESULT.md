# Second-order Hilbert departure of the Birkhoff skew-isosceles constant on real \(\ell_p^2\)

## Finding
For \(1<p<\infty\), let \(X_p=(\mathbb R^2,\|\cdot\|_p)\), and write \(x\perp_B y\) if \(\|x+ty\|_p\ge\|x\|_p\) for every real \(t\). Define the natural skew-isosceles discrepancy at parameter one by
\[
D(p)=\sup\{\|x+y\|_p-\|x-y\|_p:\ \|x\|_p=\|y\|_p=1,\ x\perp_B y\}.
\]
Let \(u>0\) be the unique positive root of \(u\tanh u=1\), and set \(r_0=e^{-u}\). Define
\[
C=\frac{1}{\sqrt2\sinh u},\qquad
K=\frac{\sqrt2\,r_0\log r_0}{4(1+r_0^2)^2}\bigl[(1+r_0^2)\log2-(1-r_0)^2\log(1-r_0)
-(1+r_0)^2\log(1+r_0)-2(1-2r_0^2)\log r_0\bigr].
\]
Then, as \(\varepsilon=p-2\to0\) from either side,
\[
\boxed{D(2+\varepsilon)=C|\varepsilon|+K\varepsilon|\varepsilon|+O(|\varepsilon|^3).}
\]
Numerically \(r_0=0.3012910191606573\ldots\), \(C=0.4686303660085660\ldots\), and \(K=-0.2630288808938024\ldots<0\). In particular, the second-order departures on the two sides of the Hilbert exponent are asymmetric, even after the absolute first-order cusp is removed.

There exists \(\eta>0\) such that, for every \(0<|p-2|<\eta\), the supremum is attained in exactly one reduced Birkhoff direction, modulo sign changes and coordinate permutations. For its unique coordinate ratio \(r_p\in(0,1)\),
\[
r_p=r_0+\kappa(p-2)+O((p-2)^2),\qquad
\kappa=-\frac{K'(r_0)}{g''(r_0)}=0.2298733594466300\ldots,
\]
where \(g(r)=-\sqrt2\,r\log r/(1+r^2)\) and \(K(r)\) is the displayed elementary expression with \(r_0\) replaced by \(r\). Every sequence of unit Birkhoff pairs with discrepancy \(D(p)-o(|p-2|)\), as \(p\to2\) and \(p\ne2\), has reduced coordinate ratio tending to \(r_0\). These statements concern only the real two-dimensional plane and the fixed skew parameter one.

## Assumptions and scope
The field is real, \(1<p<\infty\), and the Birkhoff relation is ordered: \(x\perp_B y\) need not imply \(y\perp_B x\). All norming pairs have unit \(p\)-norm. The range \(|p-2|<\eta\) is existential, not a claimed explicit universal numeric interval. The branch at \(p=2\) is degenerate: \(D(2)=0\), and all Hilbert-orthogonal pairs have zero discrepancy. The assertion of unique reduced maximizers excludes \(p=2\).

## Proof
**1. Complete reduction, including signs and boundary.** The space \(\ell_p^2\) is smooth for \(1<p<\infty\). Hence \(x\perp_B y\) holds exactly when \(\sum_{i=1}^2 |x_i|^{p-2}x_i y_i=0\). By signed-coordinate isometries, put \(x=(a,ra)\) with \(0\le r\le1\) and \(a=(1+r^p)^{-1/p}\). The two unit Birkhoff partners are \(\pm(-r^{p-1}b,b)\), where \(b=(1+r^{p(p-1)})^{-1/p}\). Replacing \(y\) by \(-y\) interchanges the two norms in the discrepancy. Thus
\[
D(p)=\max_{0\le r\le1}|F(p,r)|,
\]
where
\[
F(p,r)=\left((a-r^{p-1}b)^p+(ra+b)^p\right)^{1/p}
-\left((a+r^{p-1}b)^p+(b-ra)^p\right)^{1/p}.
\]
The displayed differences inside powers are nonnegative: after raising inequalities to the power \(p\), both reduce to \(r^{p^2}\le1\). In particular, the reduction includes the endpoint ratios \(r=0,1\), at which \(F(p,r)=0\) for all \(p>1\). Compactness guarantees attainment.

**2. The uniform first derivative and unique limiting direction.** For every \(r\in[0,1]\), \(F(2,r)=0\). For \(0<r<1\), at \(p=2\) the two vector sums have the same multiset of absolute coordinates, namely \(\{(1-r)/\sqrt{1+r^2},(1+r)/\sqrt{1+r^2}\}\). In differentiating their \(p\)-norms, the explicit derivatives of the norm exponent therefore cancel. What remains is the derivative of their Euclidean inner-product cross term. Since
\[
\langle x,y\rangle_2=\frac{r-r^{p-1}}{(1+r^p)^{1/p}(1+r^{p(p-1)})^{1/p}},
\]
we obtain
\[
\left.\partial_pF(p,r)\right|_{p=2}
=\sqrt2\left.\partial_p\langle x,y\rangle_2\right|_{p=2}
=-\frac{\sqrt2\,r\log r}{1+r^2}=g(r).
\]
The same identity extends continuously to \(r=0,1\), setting \(0\log0=0\). Continuity of \(\partial_pF\) on a compact product neighborhood of \(\{2\}\times[0,1]\) follows from the elementary continuous extensions \(s^\alpha\log^j s\to0\) as \(s\downarrow0\) for positive \(\alpha\); both vector norms stay uniformly bounded away from zero. Thus \(F(2+\varepsilon,r)/\varepsilon\to g(r)\) uniformly for \(0\le r\le1\).

For \(0<r<1\), put \(r=e^{-v}\). Direct differentiation shows that stationary points of \(g\) are exactly the positive roots of \(v=\coth v\). The left side increases and the right side decreases strictly, so the root \(u\) is unique. Since \(g(0)=g(1)=0\) and \(g>0\) in the interior, \(r_0=e^{-u}\) is the unique global maximizer and \(g''(r_0)<0\). Its value is \(g(r_0)=u/(\sqrt2\cosh u)=1/(\sqrt2\sinh u)=C\). Uniform convergence proves the first-order coefficient and localization of every asymptotically maximizing ratio.

**3. Second derivative and exact curvature.** For \(r\) in an interior neighborhood of \(r_0\), all four relevant scalar coordinates are strictly positive. Consequently \(F\) is real analytic jointly in \(p,r\) there. Taylor expansion gives
\[
F(2+\varepsilon,r)=\varepsilon g(r)+\varepsilon^2 K(r)+O(\varepsilon^3),
\]
uniformly with the first two \(r\)-derivatives locally, where direct differentiation of the explicit formula for \(F\) yields
\[
K(r)=\frac{\sqrt2\,r\log r}{4(1+r^2)^2}
\left[(1+r^2)\log2-(1-r)^2\log(1-r)-(1+r)^2\log(1+r)-2(1-2r^2)\log r\right].
\]
This identity can be reconstructed without symbolic software by twice differentiating \(a=(1+r^p)^{-1/p}\) and \(b=(1+r^{p(p-1)})^{-1/p}\) and applying the chain rule to \(\exp\bigl[p^{-1}\log\sum_j z_j(p)^p\bigr]\). The packaged script implements these derivatives and simplifies their difference symbolically.

The constant \(K=K(r_0)\) is strictly negative: \(u>1\) implies \(0<r_0<e^{-1}<2/5\). The square-bracket expression defining \(K(r_0)\) is positive because its first two terms \((1+r_0^2)\log2\) and \(-(1-r_0)^2\log(1-r_0)\) are positive, \(\log(1+r_0)\le r_0\) bounds its only potentially negative log term below by \(-(7/5)^2(2/5)\), and \(-2(1-2r_0^2)\log r_0>2(1-2(2/5)^2)>1.36\). The prefactor \(r_0\log r_0\) is negative.

**4. Uniqueness and optimizer drift.** Define \(H(p,r)=F(p,r)/(p-2)\) for \(p\ne2\) and \(H(2,r)=g(r)\). This extends analytically near \((2,r_0)\). As \(g''(r_0)<0\), the implicit-function theorem gives a unique nearby critical branch \(r_p\), with \(r_2=r_0\), and its second derivative in \(r\) remains negative. Uniform first-order convergence and the strict global maximum of \(g\) exclude all maximizers outside this neighborhood. Because changing the sign of \(y\) changes the sign of \(F\), maximizing the signed discrepancy is equivalent to maximizing \(|F|\); in the localized neighborhood the sign of \(F\) is that of \(p-2\), and the branch uniquely maximizes \(H\). Differentiating \(\partial_rH(p,r_p)=0\) gives \(r'_2=-K'(r_0)/g''(r_0)=\kappa\).

Finally \(r_p-r_0=O(|p-2|)\); substituting into the Taylor expansion and using \(g'(r_0)=0\) yields \(F(p,r_p)=(p-2)C+(p-2)^2K+O(|p-2|^3)\). Taking absolute values proves the stated two-sided expansion, and the uniform gap away from the unique maximum proves the assertion for every near-maximizing sequence.

## Verification
Run `python check.py` with SymPy, mpmath and SciPy. It reconstructs \(\partial_pF(2,r)=g(r)\) and \(\tfrac12\partial_p^2F(2,r)=K(r)\) as symbolic identities, checks the derivatives independently at nine interior ratios to high precision, and compares six near-Hilbert numerical optimizations with the cubic-error prediction. The proof above, rather than these finite samples, supplies the quantifiers, uniqueness, and the asymptotic remainder.

## Relationship to prior work
Qi, Li, Yin, Liu, Bi, Fu and Li introduced the skew Birkhoff-isosceles quantity and established general geometry bounds and Hilbert-space behavior. Their accessible full text does not compute this two-sided exponent-perturbation curvature for the real \(\ell_p^2\) plane. Related published findings include a fixed-\(p=4\), small-skew-parameter expansion and the first-order near-Hilbert slope for a *different* approximate Birkhoff-symmetry parameter. Indeed, the latter first-order slope is numerically \(\sqrt2 C\), so the leading coefficient here is not advanced as an independent new phenomenon. The specific second-order skew-isosceles coefficient \(K\), its sign asymmetry and the unique optimizer-drift law concern a different invariant and are not consequences of the available stated results without additional analysis. This is a best-knowledge literature assessment, not a claim of exhaustive bibliographic uniqueness.

## Limitations
The result is local in \(p\) near two, real two-dimensional, and at skew parameter one; it does not determine \(D(p)\) for every \(p\), all dimensions, or arbitrary skew parameters. No explicit value of the neighborhood radius \(\eta\) is asserted. Primary literature beyond the accessible sources, including older unindexed asymmetry formulas, may contain equivalent statements. Numerical optimizations do not certify global uniqueness: that conclusion follows from compact uniform convergence and the implicit-function argument. Independent validation has not been performed.

## References
- J. Qi, Q. Li, Z. Yin, Q. Liu, J. Bi, Y. Fu and Y. Li, *Generalized geometric constants related to Birkhoff orthogonality in Banach spaces*, arXiv:2602.13974v1 (first public 15 February 2026), https://arxiv.org/abs/2602.13974.
- J. Bi, Q. Liu and Y. Li, *Two Geometric Constants Measuring Differences Between Orthogonality Types in Banach Spaces*, Mediterranean Journal of Mathematics 23 (2026), article 29, DOI:10.1007/s00009-025-03024-9 (related but distinct orthogonality metrics).
- *Sharp second-order small-skew law for Birkhoff geometry in real \(\ell_4^2\)*, publicly indexed mathematical finding (different perturbation: skew parameter tending to zero at fixed exponent four).
- *Sharp \(C\)-symmetry of two Hilbert summands and its near-Hilbert slope*, publicly indexed mathematical finding (different invariant, first-order exponent asymptotics).
