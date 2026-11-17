# A Gaussian rank-window curvature crossover and exact second intrinsic volumes of hypersimplices

## Finding

Let \(H_{n,k}\) be the standard Euclidean hypersimplex. Its **complete ridge-curvature decomposition**, and hence its second Steiner intrinsic volume, is

\[
V_{n-3}(H_{n,k})
=\frac{\binom n2\sqrt{n-2}}{2\pi(n-3)!}
\left\{\alpha_n\left[E_{n-3,k-1}+E_{n-3,k-3}\right]
+2\beta_n E_{n-3,k-2}\right\},
\]

where \(\alpha_n=\arccos(-1/(n-1))\), \(\beta_n=\arccos(1/(n-1))\), and \(E_{N,j}\) counts permutations on \(N\) labels having \(j\) descents (zero if \(j<0\) or \(j\ge N\)). Define \(C_{=}(n,k)\) and \(C_{\ne}(n,k)\) as the first and second summands, respectively. The ratio is

\[
R_{n,k}=\frac{C_{=}(n,k)}{C_{\ne}(n,k)}
=\frac{\alpha_n}{\beta_n}
\frac{E_{n-3,k-1}+E_{n-3,k-3}}{2E_{n-3,k-2}}.
\]

In the Gaussian rank window, put \(z_n=(k-n/2)/\sqrt{(n-2)/12}\). Whenever \(z_n\to z\in\mathbb R\),

\[
\lim_{n\to\infty} n(R_{n,k}-1)
=6(z^2-1)+\frac4\pi.
\]

Thus for \(|z|<\sqrt{1-2/(3\pi)}\), mixed ridge curvature strictly dominates eventually, while for \(|z|>\sqrt{1-2/(3\pi)}\), equal-coordinate ridge curvature strictly dominates eventually. The limiting threshold is approximately \(0.8875772694\). The boundary case is not asserted by this first-order calculation.

## Assumptions and scope

The integers satisfy \(n\ge4\) and \(2\le k\le n-2\). All lengths, volumes and angles are computed in the affine hyperplane \(\sum_i x_i=k\) with the Euclidean metric inherited from \(\mathbb R^n\). The hypersimplex is

\[
H_{n,k}=\left\{x\in[0,1]^n:\sum_{i=1}^{n}x_i=k\right\}.
\]

Its intrinsic dimension is \(d=n-1\). Intrinsic volumes are normalized by the ordinary Euclidean Steiner formula

\[
\operatorname{Vol}_{d}(H_{n,k}+t B_d)
=\sum_{j=0}^{d}\kappa_{d-j} V_j(H_{n,k})t^{d-j},
\]

where \(\kappa_2=\pi\) and \(B_d\) is the intrinsic Euclidean unit ball. In particular, the coefficient discussed here is \(V_{d-2}=V_{n-3}\), not the surface-area coefficient. For \(n=4\), the ridge measure is one-dimensional and the formulas remain valid.

## Proof

**1. Coordinate facet and ridge census.** Every facet is of the form \(x_i=0\) or \(x_i=1\), for \(1\le i\le n\). A ridge formed by imposing two distinct coordinate equations \(x_i=s\), \(x_j=t\), with \(s,t\in\{0,1\}\), has remaining coordinates in the hypersimplex of \(n-2\) coordinates and rank \(k-s-t\). It has dimension \(n-3\) exactly when \(1\le k-s-t\le n-3\). The mixed choice \((s,t)=(0,1)\) is always admissible in the stated range; the zero/zero choice requires \(k\le n-3\), and the one/one choice requires \(k\ge3\). Every ridge has exactly two containing facets; there is no overcounting beyond the two choices in each unordered coordinate pair.

**2. Euclidean ridge measures.** By the unit-cube slicing/Eulerian identity, the intrinsic \((m-1)\)-volume of the hypersimplex on \(m\) coordinates at integer rank \(r\) equals \(\sqrt{m}\,E_{m-1,r-1}/(m-1)!\). The factor \(\sqrt m\) converts coordinate-slice coarea density to hypersurface measure. Taking \(m=n-2\) gives ridge measure

\[
\operatorname{Vol}_{n-3}(F_{i,s}\cap F_{j,t})
=\frac{\sqrt{n-2}}{(n-3)!}
E_{n-3,k-s-t-1},
\]

with the zero convention automatically suppressing the non-ridges. The cube slicing identity follows from decomposing the cube into unit simplices indexed by descents, or by the Irwin–Hall density of sums of uniforms. This identity itself is prior work, not claimed here.

**3. All exterior angles.** Write \(u_i=e_i-\mathbf1/n\), the projection of the coordinate unit vector to the sum-zero tangent space. The outward normal of \(x_i=s\) is \((2s-1)u_i/\|u_i\|\). Since \(\|u_i\|^2=(n-1)/n\) and \(\langle u_i,u_j\rangle=-1/n\) for distinct coordinates, the exterior angle is exactly \(\alpha_n=\arccos[-1/(n-1)]\) when \(s=t\), and \(\beta_n=\arccos[1/(n-1)]\) when \(s\ne t\). These are the only two possible exterior ridge angles, and both occur in nontrivial ranks except that some equal-coordinate ridge types disappear near the two extreme ranks.

**4. Ridge curvature and intrinsic volume.** The normal 2-cone at a ridge is a planar sector whose normalized circular angle is its exterior angle divided by \(2\pi\). The polyhedral intrinsic-volume face formula therefore gives

\[
V_{n-3}(H_{n,k})
=\sum_{\text{ridges }F}
\operatorname{Vol}_{n-3}(F)\frac{\phi(F)}{2\pi}.
\]

For each unordered pair of distinct coordinates there is one zero/zero ridge candidate, one one/one candidate, and two mixed candidates. Substituting Steps 2 and 3 yields exactly the displayed Eulerian formula and its positive decomposition into \(C_{=}\) and \(C_{\ne}\). The mixed summand is always strictly positive.

**5. Gaussian-window limit.** Put \(M=n-2\) and \(x=k-n/2\). Let \(g_M\) be the density of a sum of \(M\) independent uniform variables on \([-1/2,1/2]\), with variance \(\sigma_M^2=M/12\). The classical exact Eulerian–Irwin–Hall identity gives

\[
\frac{E_{n-3,k-2}}{(n-3)!}=g_M(x),\quad
\frac{E_{n-3,k-1}+E_{n-3,k-3}}{(n-3)!}=g_M(x+1)+g_M(x-1).
\]

The density has Fourier inversion

\[
g_M(x)=\frac1{2\pi}\int_{\mathbb R}e^{-itx}
\left(\frac{\sin(t/2)}{t/2}\right)^{M}\,dt.
\]

After substituting \(t=v/\sigma_M\), the characteristic factor is \(\exp[-v^2/2-v^4/(20M)+O(M^{-2}v^6)]\) in bounded-frequency regions. Outside this region, the sinc-power Fourier tail is uniformly integrable with polynomial weights; this justifies differentiation and a compact-standardized-window local Gaussian expansion. Uniformly for \(|z|\le K\) and \(x=\sigma_M z\), this yields

\[
g_M(x)=\sigma_M^{-1}\bigl[\varphi(z)+O_K(M^{-1})\bigr],\qquad
 g_M''(x)=\sigma_M^{-3}\bigl[\varphi''(z)+O_K(M^{-1})\bigr],
\]

and \(\sup_{|u|\le1}|g_M^{(4)}(x+u)|=O_K(\sigma_M^{-5})\), where \(\varphi\) is the standard normal density. The centered Taylor formula and \(\varphi''(z)/\varphi(z)=z^2-1\) now give

\[
\frac{g_M(x+1)+g_M(x-1)}{2g_M(x)}
=1+\frac{g_M''(x)}{2g_M(x)}+O_K(M^{-2})
=1+\frac{6(z^2-1)}{M}+O_K(M^{-2}).
\]

Finally, \(\alpha_n=\pi/2+\arcsin[1/(n-1)]\), \(\beta_n=\pi/2-\arcsin[1/(n-1)]\), so

\[
\frac{\alpha_n}{\beta_n}=1+\frac4{\pi n}+O(n^{-2}).
\]

Multiplication and \(M=n-2\) yield \(n(R_{n,k}-1)=6(z_n^2-1)+4/\pi+o(1)\), proving the claimed limit and strict signs away from its two zeros.

## Verification

The standalone script `hypersimplex_curvature_checker.py` reconstructs every admissible coordinate ridge from the actual zero/one vertex sets for dimensions \(n=4,\ldots,9\), computes intrinsic Euclidean ridge measures using numerical orthonormal bases and convex-hull volume, independently reconstructs the outward-normal angles, and compares the two total curvature classes with the Eulerian expressions. It checked 1,812 actual ridge profiles. A separate exact-integer Eulerian recurrence checks the Gaussian-window expansion at dimensions \(n=80,160,320,640\). Output includes `HYPERSIMPLEX_CURVATURE_PASS`. These finite checks corroborate the analytic proof but do not constitute an infinite-dimensional certificate.

To replay: `python hypersimplex_curvature_checker.py` with Python 3, NumPy and SciPy. The script is bundled with this note.

## Relationship to prior work

The hypersimplex, its Eulerian normalized volume and its simplex tilings are classical. Parisi, Sherman-Bennett and Williams study positroid tiles, facets, and the Eulerian hypersimplex triangulation, notably in Sections 7 and 10 of their 2021 preprint. Stanley's 1977 cube-triangulation result supplies the classical Eulerian input. General Steiner and polyhedral-normal-cone formulas are established background. The contribution here is the **coordinate-ridge angle-weighted second intrinsic volume** together with a sharp sign-changing Gaussian-rank curvature balance, not the Eulerian facet-volume identity or Gaussian local central limit principle separately.

Published studies of hypersimplex minimum width, facial distance and random shadow complexity address distinct invariants and do not state or imply the ridge-curvature formula or its \(\sqrt{n}\)-rank crossover. This priority comparison is not a proof that no equivalent formula exists in unindexed or differently named literature.

## Limitations

The all-parameter exact formula is proved only for standard, unweighted hypersimplices in their inherited Euclidean metric. The asymptotic transition is a compact standardized central-rank statement: it is not a uniform estimate over ranks near \(k=2\) or \(k=n-2\). At the critical standardized values, the first-order term vanishes, so no sign is claimed without further-order analysis. Neither an independent audit nor exhaustive historical priority verification has been performed.

## References

1. M. Parisi, M. Sherman-Bennett and L. Williams, *The m=2 amplituhedron and the hypersimplex: signs, clusters, triangulations, Eulerian numbers*, arXiv:2104.08254, first public version April 16, 2021, https://arxiv.org/abs/2104.08254 . Full preprint, especially Sections 7 and 10, inspected for the established Eulerian volume and tile geometry.
2. R. P. Stanley, *Eulerian partitions of a unit hypercube*, in *Higher Combinatorics*, 1977, classical source for Eulerian hypersimplex triangulations, referenced by [1].
3. N. Li, *Ehrhart h*-vectors of hypersimplices*, arXiv:1104.5292, April 28, 2011, https://arxiv.org/abs/1104.5292 . Background on Ehrhart and Eulerian invariants.
4. *The Hadwiger theorem on convex functions, III: Steiner formulas and mixed Monge–Ampère measures*, 2022, https://doi.org/10.1007/s00526-022-02288-3 . Used solely for classical Steiner normalization, not as evidence of novelty.
