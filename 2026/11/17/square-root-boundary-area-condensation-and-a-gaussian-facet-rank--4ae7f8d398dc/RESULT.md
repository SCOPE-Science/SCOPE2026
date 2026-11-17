# Square-root boundary-area condensation and a Gaussian facet-rank law for cube–crosspolytope sums

## Finding
For each integer \(d\ge2\), write \(C_d=[-1,1]^d\), \(B_1^d=\{x\in\mathbb R^d:\sum_{i=1}^d|x_i|\le1\}\), and \(Q_d=C_d+B_1^d\). Equip \(Q_d\) with the ambient Euclidean metric. A facet has **support rank** \(k\) when its outward normal has precisely \(k\) nonzero coordinates.

**Exact area spectrum.** For every \(1\le k\le d\), exactly \(2^k\binom dk\) facets have support rank \(k\), and each has intrinsic \((d-1)\)-dimensional Euclidean area
\[
 A_{d,k}=\frac{2^{d-k}\sqrt{k}}{(k-1)!}.
\]
Thus the total surface-area contribution of rank \(k\) and the complete surface area are
\[
 S_{d,k}=2^d\binom dk\frac{\sqrt{k}}{(k-1)!},\qquad
 S_d=2^d\sum_{k=1}^d\binom dk\frac{\sqrt{k}}{(k-1)!}.
\]

**Area-rank limit law.** Sample a facet with probability proportional to its Euclidean area and denote its support rank by \(K_d\). Then
\[
 \boxed{\frac{K_d-\sqrt d}{d^{1/4}}\Longrightarrow N(0,1/2).}
\]
More precisely, for each fixed real \(y\), uniformly for \(y\) in compact intervals,
\[
 \boxed{d^{1/4}\Pr\!\left(K_d=\lfloor\sqrt d+yd^{1/4}\rfloor\right)
 \longrightarrow \frac{e^{-y^2}}{\sqrt\pi}.}
\]
In contrast, the rank of a **uniformly counted** facet is exactly \(\operatorname{Bin}(d,2/3)\) conditioned to be nonzero, hence is asymptotic to \(2d/3\) in probability. For any \(\varepsilon>0\), facets of rank at most \((1+\varepsilon)\sqrt d\) capture asymptotically all surface area, yet their number is at most \(\exp(O_\varepsilon(\sqrt d\log d))\), a vanishing fraction of the \(3^d-1\) facets.

**Metric growth.** If \(V_d=\operatorname{Vol}_d(Q_d)\), then
\[
 \boxed{\frac{S_d}{V_d}\sim d^{3/4}.}
\]
The underlying exact volume formula \(V_d=2^d\sum_{k=0}^d\binom dk/k!\) is known and is used as an input, not asserted as new.

## Assumptions and scope
The result concerns this particular axis-aligned, unit-scale Euclidean Minkowski sum, not an arbitrary affine realization of the same face lattice. A facet is chosen uniformly with respect to \((d-1)\)-dimensional Hausdorff measure on the polytope boundary, so the probability assigned to a facet equals its area divided by \(S_d\). The Gaussian convergence is as integer \(d\to\infty\). Normal support means the number of nonzero standard-coordinate components, not the dimension of a facet. All finite-dimensional identities hold for every integer \(d\ge2\); no unsupported uniformity for dimension-dependent deformations is asserted.

## Proof
**1. Exhaustive facets and their Euclidean areas.** Coordinate clipping shows
\[
 Q_d=\left\{x\in\mathbb R^d:\sum_{i=1}^d(|x_i|-1)_+\le1\right\}.
\]
Its support function is \(h_{Q_d}(u)=\sum_i|u_i|+\max_i|u_i|\). For a nonzero sign vector \(s\in\{-1,0,1\}^d\) with \(k\) nonzero entries, the supporting hyperplane is \(s\cdot x=k+1\). Equality requires each supported cube coordinate to equal the corresponding sign and a crosspolytope point in the convex hull of the \(k\) signed unit coordinate vectors. The remaining \(d-k\) cube coordinates are free. The exposed face is therefore an orthogonal Cartesian product of a translated regular simplex of dimension \(k-1\) and \([-1,1]^{d-k}\). It has dimension \(d-1\), so is a facet. Conversely, if the nonzero entries of a normal have different absolute magnitudes, the crosspolytope support face has fewer than \(k\) vertices, while the cube support face has \(d-k\) free coordinates; their sum cannot have dimension \(d-1\). Hence the listed sign vectors describe **all** facets, without repeats. This is also consistent with the known sign-vector description in Black and De Loera.

The simplex with vertices \(e_1,\ldots,e_k\) has Euclidean \((k-1)\)-volume \(\sqrt{k}/(k-1)!\), by its edge Gram determinant \(\det(I_{k-1}+\mathbf1\mathbf1^T)=k\). Multiplying by the orthogonal cube factor \(2^{d-k}\) proves \(A_{d,k}\), and choosing supported coordinates and signs gives \(2^k\binom dk\). Summation proves \(S_{d,k}\) and \(S_d\).

**2. Centering and a local discrete Laplace estimate.** Set
\[
 w_{d,k}=\binom dk\frac{\sqrt{k}}{(k-1)!},\quad 1\le k\le d,
 \qquad Z_d=\sum_{k=1}^d w_{d,k}.
\]
The exact successive ratio is
\[
 r_{d,k}=\frac{w_{d,k+1}}{w_{d,k}}
 =\frac{d-k}{k(k+1)}\sqrt{\frac{k+1}{k}},\quad 1\le k<d.
\]
This decreases strictly with \(k\); it equals one near \(k=\sqrt d+O(1)\), making the unique modal region \(m_d=\sqrt d+O(1)\) (with a possible adjacent tie). In any window \(|k-\sqrt d|\le Md^{1/4}\), Taylor expansion of the exact logarithm gives
\[
 \log r_{d,k}=-\frac{2(k-\sqrt d)}{\sqrt d}
 +O_M(d^{-1/2}),
\]
where the error bound may be strengthened to include \(O_M(d^{-1/2})\) uniformly because \((k-\sqrt d)^2/d=O_M(d^{-1/2})\). Summing these ratios from \(\lfloor\sqrt d\rfloor\) to \(\lfloor\sqrt d+yd^{1/4}\rfloor\) gives, uniformly for bounded \(y\),
\[
 \log\frac{w_{d,\lfloor\sqrt d+yd^{1/4}\rfloor}}
 {w_{d,\lfloor\sqrt d\rfloor}}
 =-y^2+o(1).
\]
Here the accumulated Taylor error is \(O_M(d^{-1/4})\), and reversing the sum handles negative \(y\).

For completeness, this local calculation can be normalized without an unproved tail assumption. For \(|j-\sqrt d|\le c\sqrt d\) with any fixed \(0<c<1\), the exact ratio obeys the two-sided form \(\log r_{d,j}=-2\log(j/\sqrt d)+O_c(d^{-1/2})\). It follows by summing and using \(\log(1+t)\ge t/(1+t)\) that there is a positive \(c_1\), independent of large \(d\), with
\[
 \frac{w_{d,k}}{w_{d,\lfloor\sqrt d\rfloor}}
 \le C\exp\!\left(-c_1\frac{(k-\sqrt d)^2}{\sqrt d}\right)
\]
for \(\frac12\sqrt d\le k\le2\sqrt d\). Outside this interval, strict decrease of successive ratios away from the mode makes the tails at least geometrically decreasing after an exponentially small entry weight. The lower side follows likewise by comparing inverse ratios. Thus the mass beyond \(M d^{1/4}\) has a normalized \(O(\int_M^\infty e^{-c_1t^2}\,dt)\) bound, uniformly in large \(d\). Combining this tightness with the local expansion and a Riemann sum yields
\[
 Z_d\sim w_{d,\lfloor\sqrt d\rfloor}\sqrt\pi\,d^{1/4}
\]
and the claimed local Gaussian probability law. Its integrated density is \(e^{-y^2}/\sqrt\pi\), equivalent to \(N(0,1/2)\).

**3. Count/area separation.** The facet count at rank \(k\) is \(2^k\binom dk\), while \(\sum_{k=1}^d2^k\binom dk=3^d-1\). Thus uniform count gives \(\operatorname{Bin}(d,2/3)\) conditioned positive. The Gaussian limit shows that ranks at most \((1+\varepsilon)\sqrt d\) carry asymptotically all area. Their number satisfies
\[
 \sum_{k\le(1+\varepsilon)\sqrt d}2^k\binom dk
 \le \bigl((1+\varepsilon)\sqrt d+1\bigr)(2d)^{(1+\varepsilon)\sqrt d}
 =\exp(O_\varepsilon(\sqrt d\log d)),
\]
which is subexponential in \(d\), whereas the full number is \(3^d-1\).

**4. Area-to-volume growth.** Partitioning \(Q_d\) by excess-coordinate supports in the clipping representation gives the (previously known) volume identity
\[
 V_d=2^d\sum_{k=0}^d b_{d,k},\qquad
 b_{d,k}=\frac{\binom dk}{k!}.
\]
Since \(w_{d,k}=k^{3/2}b_{d,k}\) for every \(k\ge1\),
\[
 \frac{S_d}{V_d}=\frac{\sum_{k=0}^d k^{3/2}b_{d,k}}{\sum_{k=0}^d b_{d,k}}.
\]
The consecutive ratio for the \(b\)-weights is \((d-k)/(k+1)^2\), which is strictly decreasing and crosses one at \(k=\sqrt d+O(1)\). The same ratio-tail argument as in Step 2 gives \(k/\sqrt d\to1\) under the normalized \(b\)-weights; moreover its upper tails decay geometrically past \(2\sqrt d\), so the powers \((k/\sqrt d)^{3/2}\) are uniformly integrable. Consequently the displayed weighted expectation divided by \(d^{3/4}\) tends to one. This proves the final assertion.

## Verification
The standalone `verify.py` constructs every vertex of \(Q_d\) as a signed permutation of \((2,1,\ldots,1)\) and independently computes the convex hull in dimensions \(d=2,3,4,5\). Every triangulated hull facet is assigned to its sign-support rank using its computed Euclidean outward normal. Gram determinants produce individual simplex areas; these are summed and compared against the rank-shell formula. The independently computed hull volumes are compared against the exact volume polynomial. For dimensions \(100,1000,10000\), stable logarithmic factorial sums check the concentration scale, limiting variance and surface-to-volume normalization. The checker prints `CUBE_DIAMOND_SURFACE_PASS` on success. The infinite-dimensional conclusions rely on the analytical ratio and tail arguments above, not on finite experiments.

## Relationship to prior work
Black and De Loera's *Monotone Paths on Cross-Polytopes* (2021) supplies the cube-plus-crosspolytope polar realization of a signohedron and the known signed-support face structure. An earlier published analysis of its canonical Euclidean realization already establishes the same facet-indexing and distance shells \((k+1)/\sqrt{k}\), and is acknowledged as covering those ingredients. Prior work on its Gaussian-exposed polar vertices derives logarithmic support-rank fluctuations, which concerns an entirely different probability measure and body from this area-weighted boundary law. Existing geometric work also provides the full primal volume polynomial and a distinct Mahler-volume saddle-point limit, which do not determine the support-rank area spectrum or its Gaussian limit. The new contribution here is the **Euclidean area-weighted square-root-rank localization, local central limit law and exponential disparity from uniform facet counts**, together with its area-to-volume scaling. The finite facet formula is given explicitly because it is essential for this phenomenon, not because its derivation alone establishes historical originality.

## Limitations
The theorem is about \(C_d+B_1^d\) with unit scales and standard Euclidean measure. It does not assert a uniform law for other aspect ratios, other normalizations, arbitrary affine signohedra, or non-Euclidean surface measures. It makes no claim to a new facet-lattice characterization or a new exact volume polynomial. A known Laguerre/Bessel-polynomial coefficient central-limit theorem might encode the same rank law in different terminology; the current literature comparison lowers but cannot eliminate that historical-priority risk. Independent verification of the full theorem and bibliographic priority has not been performed.

## References
1. A. E. Black and J. A. De Loera, *Monotone Paths on Cross-Polytopes*, arXiv:2102.01237 (first public 2021-02-02), Theorem 1.1(d) and Section 3. https://arxiv.org/abs/2102.01237
2. *Canonical signohedra are tangential with \(d\) exact radial shells*, public mathematical research record (2026), source of previously established facet indexing and distance shells. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-canonical-signohedra-are-tangential-with-d-exact-radial-shells--c04451515c1c
3. *Joint Gaussian width–support-rank fluctuations of canonical signohedra*, public mathematical research record (2026), concerning the **polar** body's Gaussian angular measure. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-joint-gaussian-width-support-rank-fluctuations-of-canonical-sign--ab54f1ffa083
4. *Exponential Mahler growth along the cube–cross-polytope Minkowski interpolation*, public mathematical research record (2026), containing the exact primal-volume polynomial and a distinct optimization. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exponential-mahler-growth-along-the-cube-cross-polytope-minkowsk--237a7d354626
5. *A Poisson–gamma height law for cube–crosspolytope Cayley bodies*, public mathematical research record (2026), treating a different probability law generated by the same mixed-volume polynomial. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-poisson-gamma-height-law-for-cube-crosspolytope-cayley-bodies--1794ea6c2141
