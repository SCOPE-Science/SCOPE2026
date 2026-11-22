# A square-and-pronic lattice-count law for uniformly translated square pyramids

## Finding
For every integer \(n\ge1\) and every apex displacement \(a,b\in\mathbb R\), let
\[
P_{n,a,b}=\operatorname{conv}\bigl(([0,n]^2\times\{0\})\cup\{(a,b,1)\}\bigr)\subset\mathbb R^3.
\]
For an independent uniform translation \(T\in[0,1)^3\), set \(N=\#((P_{n,a,b}+T)\cap\mathbb Z^3)\). The law is independent of \(a,b\), and the exact positive-probability classes are precisely the perfect squares and pronic numbers, plus zero:
\[
\begin{aligned}
\Pr(N=0)&=\frac2{3n},\\
\Pr(N=j^2)&=\frac2{3n} \quad(1\le j<n),\\
\Pr(N=j(j+1))&=\frac1{3n}\quad(1\le j<n),\\
\Pr(N=n^2)&=\frac1{3n}.
\end{aligned}
\]
All other integer values have probability zero. In particular the mean and variance are
\[
\boxed{\mathbb E N=\frac{n^2}{3},\qquad\operatorname{Var}(N)=\frac{4n^4+5n^2+1}{45}.}
\]
Under the coupling using the same horizontal and vertical uniform phase at every integer \(n\), \(N/n^2\) converges almost surely to \(U^2\), where \(U\) is uniform on \([0,1]\). Thus the limiting cumulative distribution is \(\sqrt t\) on \(0\le t\le1\), and the coefficient of variation tends to \(2/\sqrt5\), rather than tending to zero as the pyramid volumes grow.

## Assumptions and scope
All lattice points belong to the standard integer lattice \(\mathbb Z^3\); translation is Haar-uniform modulo that lattice, with no averaging over rotations. The pyramid height is exactly one, the base is an axis-parallel square of *integer* side \(n\), and the apex can have arbitrary real horizontal coordinates. Every probability concerns Lebesgue-almost-every translation; configurations with lattice points on the boundary form a null set. Euclidean volume is \(n^2/3\). When \(n=1\), the middle ranges are empty and \(N\) equals zero with probability \(2/3\), one with probability \(1/3\).

## Proof
Write a sampled translation as \(T=(t_1,t_2,t_3)\), with independent uniform components in \([0,1)\). Except on null boundary events, the only integer height crossed by \(P_{n,a,b}+T\) is \(z=1\). At this height the unshifted pyramid section has scale \(t_3\), because the section lies a fraction \(1-t_3\) of the way from the base to its apex. It is a Cartesian square with side length \(L=nt_3\), translated horizontally by
\[
(t_1+(1-t_3)a,\;t_2+(1-t_3)b).
\]
Conditional on \(t_3\), the two fractional positions modulo one remain independent uniform variables; this holds for every real \(a,b\). An interval of length \(L=j+r\), \(j\in\mathbb Z_{\ge0}\), \(0\le r<1\), contains \(j\) or \(j+1\) integer points with probabilities \(1-r\) or \(r\). Consequently the planar square section has \(N=X Y\), where \(X,Y\) are conditionally independent copies of \(j+\operatorname{Bernoulli}(r)\).

Since \(t_3\) is uniform, \(L\) is uniform on \([0,n]\). On each interval \(j\le L<j+1\), \(j=0,\ldots,n-1\), the fractional part \(r\) is uniform, and elementary integration gives
\[
\int_0^1(1-r)^2\,dr=\int_0^12r(1-r)\,dr=\int_0^1r^2\,dr=\frac13.
\]
Thus each \(j\) contributes equal probability \(1/(3n)\) to the values \(j^2\), \(j(j+1)\), and \((j+1)^2\), counting repeated values with multiplicity. The initial two values coincide when \(j=0\), adjacent perfect-square values coincide at every internal boundary, and the terminal square appears once. This gives exactly the stated distribution. The perfect-square and pronic sequences have no positive overlaps, because \(j^2<j(j+1)<(j+1)^2\).

Taking sums against the distribution, or using the conditional variance of each independent interval count, yields
\[
\mathbb E N=\frac{n^2}3,\qquad
\mathbb E N^2=\frac{n^4}{5}+\frac{n^2}{9}+\frac1{45},
\]
so subtracting the square of the mean gives the variance displayed above. These polynomial identities can alternatively be verified by expanding the sums \(\frac1{3n}\sum_{j=0}^{n-1}\bigl(j^{2k}+(j(j+1))^k+(j+1)^{2k}\bigr)\) for \(k=1,2\).

For the limit, conditional on \(t_3\) both interval counts differ from \(nt_3\) by at most one, so \(\lvert N/n^2-t_3^2\rvert\le2/n+1/n^2\) for all generic translated configurations. This deterministic estimate implies the asserted almost-sure law under a common phase coupling, and its distribution is \(\Pr(U^2\le t)=\sqrt t\). The coefficient of variation follows from the explicit mean and variance.

## Verification
The separate standard-library script `verify_pyramid.py` independently checks rational horizontal slice membership for many rational choices of apex and translation, tests the exact mass normalization and the first two moments for 80 values of \(n\), and compares the direct three-term interval formula against the collated square/pronic law. These finite checks are diagnostics; every dimension-three, all-\(n\) assertion follows from the preceding conditional-integer-count argument.

## Relationship to prior work
Schlie's 2026 survey formulates the randomized lattice-point count problem, discusses random-translation expectations and variances, and observes that exact distributions are scarce. Tokmachev (2024) gives a complete translated lattice-triangle distribution and planar variance formulas; that result does not apply to three-dimensional square pyramids. The present formula is an exact three-dimensional family law with sparsely supported square and pronic values and an explicit nonconcentrating anisotropic limit. The previously published Reeve-prism multiplicity law instead concerns a different eight-vertex vertical extrusion of an empty tetrahedron and has a triangular rather than square-root limiting cumulative distribution. Standard facts about random interval occupancy and expected volume are inputs, not claimed as new.

## Limitations
The formula does not assert novelty for basic interval rounding, the random-translation identity \(\mathbb EN=\operatorname{vol}P\), or polygonal results. It does not apply to arbitrarily rotated pyramids, noninteger base side lengths, general bases, or isotropically dilated fixed bodies. The limiting law is an *anisotropic* base-growth phenomenon with fixed lattice-unit height, not a contradiction to isotropic dilation bounds. The originality comparison is necessarily provisional for unindexed material; independent mathematical audit remains unperformed.

## References
1. S. Schlie, *On the randomized lattice-point count problem*, arXiv:2611.16769v1, first public 2026-11-12, https://arxiv.org/abs/2611.16769 (especially Sections 1, 3–4 and the discussion of exact distributional information).
2. A. Tokmachev, *Lattice points inside a random shifted integer polygon*, arXiv:2407.09878v1, first public 2024-07-13, https://arxiv.org/abs/2407.09878 (planar results).
3. *Cubic overlap spectrum of minimal Reeve-prism lattice coverings*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-cubic-overlap-spectrum-of-minimal-reeve-prism-lattice-coverings--144458c7c9ab (distinct simplex-extrusion example).
