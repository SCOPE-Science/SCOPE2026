# Euclidean facet-area boundary layers of Fibonacci stable-set polytopes

## Finding
For each integer \(n\ge 2\), consider the path stable-set polytope in its standard Euclidean coordinate realization
\[
P_n=\{x\in\mathbb R^n:x_j\ge0\ (1\le j\le n),\ x_j+x_{j+1}\le1\ (1\le j<n)\}.
\]
Define polynomials \(A_0(t)=1\) and, for integers \(r\ge1\),
\[
A_r(t)=\int_0^t A_{r-1}(1-u)\,du,\qquad a_r=A_r(1).
\]
Then \(P_n\) has exactly \(2n-1\) facets. The complete indexed intrinsic Euclidean facet-measure profile is
\[
\begin{aligned}
C_{n,j}&=\mathcal H^{n-1}(P_n\cap\{x_j=0\})=a_{j-1}a_{n-j},&&1\le j\le n,\\
H_{n,j}&=\mathcal H^{n-1}(P_n\cap\{x_j+x_{j+1}=1\})
=\sqrt2\int_0^1 A_{j-1}(1-t)A_{n-j-1}(t)\,dt,&&1\le j<n.
\end{aligned}
\]
All entries are explicitly computable using rational polynomial arithmetic, apart from the universal \(\sqrt2\) factor of the \(H\)-class. The volume is \(\operatorname{Vol}_n(P_n)=a_n=E_n/n!\), where \(E_n\) is the Euler zigzag number, and the generating function is exactly
\[
\sum_{r=0}^{\infty}A_r(t)z^r
=\cos(zt)+\tan\left(\frac\pi4+\frac z2\right)\sin(zt)
\qquad(|z|<\pi/2,\ 0\le t\le1).
\]
The area sums satisfy
\[
\sum_{j=1}^n C_{n,j}=2n\operatorname{Vol}_n(P_n),\qquad
\sum_{j=1}^{n-1}H_{n,j}=\sqrt2\,n\operatorname{Vol}_n(P_n).
\]
Thus the surface-area-to-volume ratio is exactly \(n(2+\sqrt2)\); this sum identity is a direct divergence-theorem consequence and is included as a consistency relation, not a priority claim.

The **boundary-layer statement** distinguishes individual facets even though their total area is fixed. Put \(\lambda=2/\pi\). For each fixed integer \(j\ge1\), as \(n\to\infty\),
\[
\frac{C_{n,j}}{\operatorname{Vol}_n(P_n)}\longrightarrow a_{j-1}\lambda^{-j},
\qquad
\frac{H_{n,j}}{\operatorname{Vol}_n(P_n)}\longrightarrow
\sqrt2\,\lambda^{-j-1}\int_0^1 A_{j-1}(1-t)\sin\frac{\pi t}{2}\,dt.
\]
In contrast, for every sequence of indices \(j=j_n\) with both \(j_n\to\infty\) and \(n-j_n\to\infty\),
\[
\frac{C_{n,j_n}}{\operatorname{Vol}_n(P_n)}\to2,
\qquad
\frac{H_{n,j_n}}{\operatorname{Vol}_n(P_n)}\to\sqrt2.
\]
The first two positions give the explicit, non-bulk limits
\[
\begin{array}{c|cc}
&j=1&j=2\\ \hline
C_{n,j}/\operatorname{Vol}_n(P_n)&\pi/2&\pi^2/4\\
H_{n,j}/\operatorname{Vol}_n(P_n)&\pi/\sqrt2&\sqrt2(\pi^2/4-\pi/2)
\end{array}
\]
(with the second edge defined for \(n\ge3\)). Reflection of the path gives the corresponding opposite-end limits.

## Assumptions and scope
The ambient metric is the *unscaled* standard Euclidean metric of \(\mathbb R^n\). All facet measures are ordinary \((n-1)\)-dimensional Hausdorff measures, not lattice-normalized volumes. The polytope equals the convex hull of the indicator vectors of independent vertex sets of the path on \(n\) vertices. The statement treats every \(n\ge2\), not a sampled subfamily. Fixed-index and bulk limits are separate quantifications; no global maximum/minimum classification of individual facet areas is claimed.

## Proof
**1. Facet completeness and volume.** The affine coordinate reflections \(y_j=x_j\) for odd \(j\), \(y_j=1-x_j\) for even \(j\), map \(P_n\) isometrically to the order polytope of the alternating fence \(y_1\le y_2\ge y_3\le\cdots\). Standard order-polytope triangulation gives volume \(E_n/n!\). The listed \(n\) coordinate and \(n-1\) edge inequalities each support a genuine facet (set all uninvolved coordinates small and positive, while making the selected inequality an equality). Their intersection is full dimensional, so no other facets occur.

**2. Slicing recurrence.** Let \(A_r(t)\) be the ordinary volume of the \(r\)-vertex path polytope restricted by its last coordinate \(x_r\le t\), with \(A_0=1\). At \(x_r=u\), the previous coordinate satisfies \(x_{r-1}\le1-u\). Reflecting the shorter path proves \(A_r'(t)=A_{r-1}(1-t)\) and \(A_r(0)=0\) for positive \(r\). Fixing \(x_j=0\) separates the remaining constraints into the independent left and right paths, proving \(C_{n,j}=a_{j-1}a_{n-j}\). Fixing \(x_j=t,x_{j+1}=1-t\) leaves independent paths of lengths \(j-1\) and \(n-j-1\), with endpoint bounds \(1-t\) and \(t\). The induced metric on the hyperplane contributes line-element \(\sqrt2\,dt\); Fubini gives the stated formula for \(H_{n,j}\).

**3. Exact generating function.** Set \(F(z,t)=\sum_{r\ge0}A_r(t)z^r\), initially as a formal power series. The recurrence gives \(F_t(z,t)=zF(z,1-t)\), hence \(F_{tt}=-z^2F\), and \(F(z,0)=1\). Writing \(F=\cos(zt)+b(z)\sin(zt)\), the reflected derivative condition at \(t=0\) forces \(b=\cos z/(1-\sin z)=\tan(\pi/4+z/2)\). This verifies the full generating function; in particular \(F(z,1)=\tan(\pi/4+z/2)\) and reproduces the Euler zigzag volume series.

**4. Uniform singularity estimate.** The nearest pole of \(\tan(\pi/4+z/2)\) is simple, at \(z=\pi/2\), with principal part \(2/(\pi/2-z)\). Its next pole is at \(z=-3\pi/2\). Subtracting the first principal part and applying Cauchy's coefficient estimate on \(|z|=\pi\) yields, uniformly in \(0\le t\le1\),
\[
A_r(t)=\frac4\pi\left(\frac2\pi\right)^r\sin\frac{\pi t}{2}
+O(\pi^{-r}),\qquad
 a_r=\frac4\pi\left(\frac2\pi\right)^r+O(\pi^{-r}).
\]
The error is exponentially smaller than the displayed leading term when \(r\to\infty\). For fixed \(j\), substitute the asymptotic for the opposite, growing tail in the exact facet formulas and divide by \(a_n\). If both tails grow, substitute on both sides and evaluate
\(\int_0^1\sin(\pi(1-t)/2)\sin(\pi t/2)\,dt=1/\pi\). This gives the two bulk limits. The displayed endpoint constants follow from \(A_0(t)=1\), \(A_1(t)=t\), and direct one-dimensional integration. The uniform estimate also justifies the varying-index bulk limit, including indices approaching an endpoint more slowly than linearly.

**5. Aggregate area identities.** Every outward unit facet normal for \(x_j=0\) has support offset zero at the origin, while for \(x_j+x_{j+1}=1\) it has support offset \(1/\sqrt2\). The divergence theorem applied to \(X(x)=x\) gives \(n\operatorname{Vol}_n(P_n)=\sum_jH_{n,j}/\sqrt2\). Applying the same identity to \(X(x)=x-\tfrac12\mathbf1\), all edge facets have zero support offset and every coordinate facet has offset \(1/2\); hence \(n\operatorname{Vol}_n(P_n)=\sum_j C_{n,j}/2\). Summation completes the proof.

## Verification
The included `verify_facets.py` independently enumerates alternating permutations of sizes \(2\) through \(9\), counts neighboring consecutive ranks as edge-face certificates, and compares them with exact rational polynomial integrals. It also checks all coordinate-face volumes, both divergence identities, and the asymptotic constants at dimension \(40\). It prints `PATH_FACET_AREA_PASS` on success. All infinite-dimensional and varying-index statements above follow from the analytic generating-function argument, not the finite checker.

## Relationship to prior work
The 2018 stable-set-polytope study of Aliniaeifard, Benedetti, Bergeron, Li and Saliola treats vertices, one-skeleta, facet descriptions and combinatorial diameter, but does not state Euclidean facet measures in its inspected text. Coons and Sullivant (first preprint January 2019) establish the alternating-fence order-polytope description, unimodular triangulations, Ehrhart information and Euler zigzag volume used here; their inspected article does not state the indexed Euclidean facet-area formulas or boundary-layer limits. The 2021 work of von Bell and collaborators treats triangulations and volumes of related generalized snake order polytopes, not this standard-metric facet profile. The separate indexed-area and boundary-layer results here are not consequences of knowing only the total volume or Ehrhart polynomial. Related transfer-operator analyses of fence polytope clearance statistics exist; the distinction is between a global tilted observable and the ordinary measure of every individually labelled boundary facet.

## Limitations
The theorem does not evaluate higher Steiner coefficients, prove sharp global facet-area extrema, or address weighted paths or arbitrary graphs. The total surface-to-volume identity is elementary and is not itself a novelty claim. The priority assessment is not exhaustive: an unindexed source could contain equivalent facet-resolved measurements, especially under alternating-permutation or order-statistic terminology. Independent external validation has not been performed.

## References
1. F. Aliniaeifard, C. Benedetti, N. Bergeron, S. X. Li, F. Saliola, *Stable set polytopes and their 1-skeleta*, arXiv:1804.00360, first public version 2018-04-02, https://arxiv.org/abs/1804.00360 .
2. J. I. Coons and S. Sullivant, *The \(h^*\)-polynomial of the order polytope of the zig-zag poset*, arXiv:1901.07443, first public version 2019-01-22, https://arxiv.org/abs/1901.07443 .
3. M. von Bell et al., *Triangulations, order polytopes, and generalized snake posets*, arXiv:2102.11306, first public version 2021-02-22, https://arxiv.org/abs/2102.11306 .
4. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23, cited for the classical order-polytope triangulation.
