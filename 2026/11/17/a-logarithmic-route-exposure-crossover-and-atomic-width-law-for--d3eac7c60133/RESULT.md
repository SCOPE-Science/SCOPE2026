# A logarithmic route-exposure crossover and atomic width law for parallel-path flow polytopes

## Finding

Fix an integer \(\ell\ge2\). For each integer \(m\ge2\), consider a directed network with one source and one sink, with \(m\) internally edge-disjoint routes of length \(\ell\), and one additional internally edge-disjoint route of length \(L_m\ge2\). Different routes share no edges. Let \(P_m\) denote its polytope of nonnegative unit source-to-sink flows, embedded with the **ordinary Euclidean metric in the original edge coordinates**. Its affine dimension is \(m\). Let \(U_m\) be uniformly distributed on the intrinsic unit sphere in the direction space of \(P_m\). Its directional width is
\[
W_m=\max_{x\in P_m}\langle U_m,x\rangle-\min_{x\in P_m}\langle U_m,x\rangle.
\]
The **exposure indicator** \(J_m\) equals one when the extra route's vertex is either a maximizing or minimizing vertex of this directional functional, and zero otherwise (ties have probability zero).

Put \(c_m=L_m/(\ell\log m)\), and write \(\Phi\) and \(\phi\) for the standard normal cdf and density. The following three laws hold for every allowed sequence of integer exceptional lengths.

**Critical logarithmic regime.** If \(c_m\to c\in(0,\infty)\), with \(Z\sim N(0,1)\), then jointly
\[
\boxed{\left(\sqrt{\frac{m}{\ell\log m}}W_m,J_m\right)
\ \Rightarrow\
\left(\sqrt2+\max\{\sqrt2,\sqrt c\,|Z|\},\mathbf1_{\{|Z|>\sqrt{2/c}\}}\right).}
\]
The limiting width has an atom of mass \(2\Phi(\sqrt{2/c})-1\) at \(2\sqrt2\), and for \(t>2\sqrt2\) its cdf is \(2\Phi((t-\sqrt2)/\sqrt c)-1\). Its non-atomic mass is exactly the limiting probability that the exceptional route is exposed:
\[
\boxed{\lim_{m\to\infty}\Pr(J_m=1)=2\Phi(-\sqrt{2/c}).}
\]
The mean normalized width converges, not merely its distribution:
\[
\boxed{\lim_{m\to\infty}\mathbb E\left[\sqrt{\frac m{\ell\log m}}W_m\right]
=2\sqrt2\,\Phi(\sqrt{2/c})+2\sqrt c\,\phi(\sqrt{2/c}).}
\]

**Short-outlier regime.** If \(c_m\to0\), then \(\sqrt{m/(\ell\log m)}W_m\to2\sqrt2\) in probability and \(\Pr(J_m=1)\to0\).

**Long-outlier regime.** If \(c_m\to\infty\), then \(\sqrt{m/L_m}\,W_m\Rightarrow |Z|\) and \(\Pr(J_m=1)\to1\).

**Exact finite-dimensional angle.** For every \(m\ge2\), \(\ell\ge2\), \(L_m\ge2\),
\[
\boxed{\Pr(J_m=1)=2\int_{-\infty}^{\infty}
\phi(z)\Phi(\sqrt{L_m/\ell}\,z)^m\,dz.}
\]
Each of the two possible exposed extremes has exactly half this probability. The Gaussian integral is also the spherical measure of the union of the two corresponding vertex normal cones.

## Assumptions and scope

Every route has at least two edges so that the network is a simple directed graph with internally disjoint routes; no parallel edges are needed. All edges are distinct and carry the standard unit coordinate metric. All flow values are nonnegative, sum to one at the source, and conserve flow at every internal vertex. All logarithms are natural. The lengths \(\ell\) and \(L_m\) are graph-theoretic counts of edges, not edge costs or Gaussian variances chosen independently of the embedding. The only asymptotic dimension parameter is the number \(m\) of ordinary routes. The small and large limits of \(c_m\) include arbitrary integer roundings.

## Proof

**1. Exact affine and Euclidean reduction.** Each unit flow on disjoint routes assigns a nonnegative common flow value to each route, with all route values summing to one. Thus its vertices \(v_0,v_1,\ldots,v_m\) are the route-edge incidence vectors. Disjoint supports give \(\langle v_i,v_j\rangle=0\) for \(i\ne j\), \(\|v_0\|^2=L_m\), and \(\|v_i\|^2=\ell\) for \(1\le i\le m\). Within their span an isometry takes them to \(\sqrt{L_m}e_0,\sqrt\ell e_1,\ldots,\sqrt\ell e_m\). Their direction hyperplane is
\[
H_m=\left\{y\in\mathbb R^{m+1}:\frac{y_0}{\sqrt{L_m}}+\sum_{i=1}^m\frac{y_i}{\sqrt\ell}=0\right\}.
\]
Let \(g=(Z,G_1,\ldots,G_m)\) have independent standard normal entries, and let \(g_H\) be its orthogonal projection on \(H_m\). Then \(U_m=g_H/\|g_H\|\) is uniform on the intrinsic sphere. If \(b=(L_m^{-1/2},\ell^{-1/2},\ldots,\ell^{-1/2})\), projection gives \(g_H=g-\lambda b\), where \(\lambda=\langle g,b\rangle/\|b\|^2\). Consequently the vertex scores are
\[
\langle U_m,v_0\rangle=\frac{\sqrt{L_m}Z-\lambda}{\|g_H\|},\qquad
\langle U_m,v_i\rangle=\frac{\sqrt\ell G_i-\lambda}{\|g_H\|}.
\]
The common shift cancels in differences. Thus **exactly for every finite dimension**
\[
W_m=\frac{\max\{\sqrt{L_m}Z,\sqrt\ell G_1,\ldots,\sqrt\ell G_m\}-\min\{\sqrt{L_m}Z,\sqrt\ell G_1,\ldots,\sqrt\ell G_m\}}{\|g_H\|}.
\tag{1}
\]
Moreover, \(J_m=1\) exactly when the exceptional independent Gaussian is greater than every ordinary score or less than every ordinary score. This reduction is valid for **spherical** random directions because the projection and positive normalization preserve ordering of all vertex scores.

**2. Finite angle formula.** Conditional on \(Z=z\), the exceptional score is maximum with probability \(\Phi(\sqrt{L_m/\ell}\,z)^m\). Integrating gives the probability that it maximizes. Symmetry of the joint Gaussian scores gives the same probability of being minimum. Since the two events are disjoint for \(m\ge1\) almost surely, their sum proves the exact integral.

**3. Extreme-value and radial norm limits.** For i.i.d. standard normal \(G_i\), elementary Gaussian tail bounds imply
\[
\frac{\max_{1\le i\le m}G_i}{\sqrt{\log m}}\xrightarrow{\Pr}\sqrt2,
\qquad
\frac{\min_{1\le i\le m}G_i}{\sqrt{\log m}}\xrightarrow{\Pr}-\sqrt2.
\tag{2}
\]
For instance, a union bound and Gaussian tail inequality prove the upper bound at \((\sqrt2+\varepsilon)\sqrt{\log m}\), while \(\Phi((\sqrt2-\varepsilon)\sqrt{\log m})^m\to0\) proves the lower bound; symmetry gives the minimum. As \(g_H\) is standard Gaussian on an \(m\)-dimensional subspace, \(\|g_H\|^2\sim\chi_m^2\). Hence \(\|g_H\|/\sqrt m\to1\) in probability. No independence of this norm from the Gaussian scores is asserted or needed.

**4. All three regimes and joint exposure.** If \(c_m\to c\in(0,\infty)\), divide the numerator of (1) by \(\sqrt{\ell\log m}\). Its three possible extremes converge jointly with \(Z\) to \(\sqrt c Z,\sqrt2,-\sqrt2\). Their range is \(\sqrt2+\max\{\sqrt2,\sqrt c |Z|\}\). The exceptional score is a maximum or minimum precisely when it lies outside the ordinary score interval. The limit of that event is \(|Z|>\sqrt{2/c}\); the boundary has probability zero. Continuous mapping and the radial norm law establish the joint distributional assertion and angle limit. The cdf and atom follow directly by integrating \(|Z|\). The same reasoning with \(\sqrt c Z=0\) covers \(c_m\to0\). When \(c_m\to\infty\), instead divide the numerator of (1) by \(\sqrt{L_m}\); both ordinary extremes vanish in probability while the exceptional score tends to \(Z\). The limiting range is \(|Z|\); the exposure event has probability tending to one since \(Z\ne0\) almost surely.

**5. Convergence of critical-regime means.** Suppose \(c_m\to c\in(0,\infty)\). Let \(R_m\) be the numerator of (1). The bound \(R_m\le2(\sqrt{L_m}|Z|+\sqrt\ell\max_i|G_i|)\) and Gaussian union bounds give \(\mathbb E[R_m^4]=O((\ell\log m)^2)\). For \(m>4\), the chi-square inverse moment \(\mathbb E[(m/\|g_H\|^2)^2]=m^2/((m-2)(m-4))\) is bounded as \(m\to\infty\). Cauchy–Schwarz therefore bounds uniformly the second moments of \(\sqrt{m/(\ell\log m)} W_m\), proving uniform integrability; dependence between \(R_m\) and \(\|g_H\|\) causes no issue. Consequently expectations converge to the expectation of the limiting random variable, namely \(2\sqrt2\Phi(\sqrt{2/c})+2\sqrt c\phi(\sqrt{2/c})\), obtained from \(\mathbb E[|Z|\mathbf1_{\{|Z|>t\}}]=2\phi(t)\). This completes the proof.

## Verification

The standalone Python checker `verify.py` independently builds route incidence vectors for four finite networks and computes widths by projection onto the affine-direction space. It confirms their equality with formula (1) over 48 exact geometric scenarios up to floating-point tolerance. A separate integral quadrature computes the exact finite exceptional-normal-cone probability and compares it with 70,000 sampled directions for one network. At three critical ratios it compares 16,000 independent simulated score vectors with the stated exposure limit and a finite-sample extreme-value proxy. It prints `PARALLEL_PATH_WIDTH_PASS` on success. Finite sampling is evidence of consistency only: the all-parameter statement is proved by steps 1–5. At moderate dimensions the Gaussian maximum approaches its leading-order extreme-value scale slowly; the checker accounts for this rather than demanding a falsely rapid convergence.

## Relationship to prior work

Von Bell, Braun, Bruegge, Hanely, Peterson, Serhiyenko and Yip (2022) establish that route-incidence vectors are exactly the vertices of unit-flow polytopes and treat their triangulations and Ehrhart theory (Proposition 2.3 and surrounding discussion). Braun and McElroy (2024) study volume inequalities for flow polytopes. Neither provides the Euclidean random-width and exceptional route normal-cone transition above. The Gaussian maximum law and elementary normal integral used in the proof are classical, and are not claimed as new.

The nearest published orthogonal-simplex result concerns **individual solid-angle ordering and sharp anisotropy inequalities at fixed dimension**, rather than a growing family with one logarithmically long leg and its joint random-width limit. The published labeled orthogonal-simplex angular tomography theorem reconstructs leg lengths from fixed-dimensional solid-angle readings rather than determining this growing-dimensional width distribution. The published two-group heterogeneous-Gaussian maximum calibration concerns a different problem with both group sizes growing and a second-order winning-probability correction; it does not state or imply the present one-outlier flow-simplex width law. The representation as a right simplex is acknowledged explicitly, so the novelty claim rests on the three-regime random Euclidean geometry, the exact exceptional route exposure law, and their joint critical atomic limit, not on the elementary isometry.

## Limitations

The result applies to a specific family of parallel-route DAGs and their full edge-coordinate Euclidean metric. Subdivision or contraction of paths changes that metric and therefore the geometry. The coordinates of a generic unit direction are correlated after affine projection, but the score differences are exactly represented by the independent Gaussian range in (1); no incorrect independence is assumed. No analogous conclusion is asserted for networks whose routes share edges. Historical priority under equivalent anisotropic-simplex or heterogeneous-Gaussian terminology remains provisional; no independent mathematical audit has been performed.

## References

1. M. von Bell, B. Braun, K. Bruegge, D. Hanely, Z. Peterson, K. Serhiyenko and M. Yip, *Triangulations of Flow Polytopes, Ample Framings, and Gentle Algebras*, arXiv:2203.01896v1 (first public 2022-03-03), Proposition 2.3, https://arxiv.org/abs/2203.01896.
2. B. Braun and J. F. McElroy, *Volume inequalities for flow polytopes of full directed acyclic graphs*, arXiv:2405.02433v1 (first public 2024-05-03), https://arxiv.org/abs/2405.02433.
3. *Vertex-angle ordering and sharp anisotropy constants for orthogonal simplices*, published 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-vertex-angle-ordering-and-sharp-anisotropy-constants-for-orthogo--bf52e469aaff (background on right-simplex angular geometry).
4. *Two-term calibration of competing heterogeneous Gaussian maxima*, published 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-two-term-calibration-of-competing-heterogeneous-gaussian-maxima--d469564e3998 (different Gaussian winner asymptotics).

5. *Sharp labeled solid-angle tomography of orthogonal simplices in every dimension*, published 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-labeled-solid-angle-tomography-of-orthogonal-simplices-in--a60d6dc1d5dc (inverse angular geometry).
