# Nonmonotone limiting projection-width variance of hypersimplices

## Finding
Let \(0<\alpha\le 1/2\) be fixed, \(k_n=\lfloor \alpha n\rfloor\), and let the hypersimplex \(\Delta(n,k_n)\subset\mathbb R^n\) be the convex hull of the \(0\)-\(1\) vectors with exactly \(k_n\) ones. For sufficiently large \(n\), it is an \((n-1)\)-dimensional Euclidean polytope in the affine hyperplane with coordinate sum \(k_n\). Let \(U_n\) be uniform on the unit sphere of the hyperplane \(\sum_i u_i=0\), and let \(W_n\) be the length of the orthogonal projection of \(\Delta(n,k_n)\) onto the line directed by \(U_n\).

Write \(\phi(t)=(2\pi)^{-1/2}\exp(-t^2/2)\), \(\overline\Phi(t)=\int_t^\infty\phi(s)\,ds\), and \(t=\overline\Phi^{-1}(\alpha)\). Define
\[
\begin{split}
V(t)={}&2\big[(1+t^2)\overline\Phi(t)-t\phi(t)\big]\\
 &-\big[2\phi(t)-2t\overline\Phi(t)\big]^2-2\phi(t)^2.
\end{split}
\]
Then
\[
W_n-2\sqrt n\,\phi(t)\ \xrightarrow{d}\ N(0,V(t)),\qquad
\operatorname{Var}(W_n)\longrightarrow V(t)>0.
\]
Moreover \(\mathbb EW_n=2\sqrt n\,\phi(t)+o(1)\). At half rank, \(V(0)=1-3/\pi\), the known cube-width limit. Yet the function \(V(t)\) is **not monotone**: it has at least one strict interior local minimum in \((1/2,5/4)\) and a distinct strict interior local maximum in \((5/4,2)\). Consequently, although the mean width increases with rank up to half rank, the limiting variance undergoes a genuine dip-and-rebound as the rank fraction varies.

## Assumptions and scope
The rank fraction \(\alpha\) is a fixed number in \((0,1/2]\), not a sequence tending to an endpoint. The normal is Haar-uniform in the *intrinsic* direction space \(\mathbf1^\perp\), not on the ambient sphere. The convention \(k_n=\lfloor \alpha n\rfloor\) is used; finitely many small dimensions with \(k_n=0\) are excluded. The symmetry \(\Delta(n,k)\cong\Delta(n,n-k)\) covers fractions above half rank by reflection. No assertion of exactly two stationary points or of finite-dimensional variance monotonicity is made.

## Proof
**1. Exact support function.** For a vector \(g\in\mathbb R^n\) with coordinates arranged in decreasing order \(g_{[1]}\ge\cdots\ge g_{[n]}\), the maximum of \(\langle g,x\rangle\) over \(\Delta(n,k)\) is \(\sum_{j=1}^k g_{[j]}\). Thus the support-width numerator equals
\[
D_{n,k}(g)=\sum_{j=1}^k\big(g_{[j]}-g_{[n+1-j]}\big).
\]
It is unchanged when all coordinates of \(g\) are shifted by a common constant. For independent standard normals \(G_i\), put \(G^0=G-\overline G\mathbf1\). The normalized vector \(G^0/\|G^0\|\) is Haar-uniform in \(\mathbf1^\perp\), so \(W_n\overset d=D_{n,k_n}(G)/\|G^0\|\).

**2. Fixed-threshold expansion.** Put \(a=\alpha\), \(t=\overline\Phi^{-1}(a)\), and \(\psi_t(x)=(|x|-t)_+\). The upper and lower trimmed Gaussian sums admit the representations
\[
\sum_{j=1}^{k_n}G_{[j]}=k_nt+\sum_{i=1}^n(G_i-t)_++O_{L^1}(1),
\]
\[
-\sum_{j=n-k_n+1}^{n}G_{[j]}=k_nt+\sum_{i=1}^n(-G_i-t)_++O_{L^1}(1).
\]
Here the remainder is also \(O_P(1)\). To justify it without a black-box trimmed-sum theorem, note that each top-\(k\) sum is the minimum over a threshold \(s\) of \(ks+\sum_i(G_i-s)_+\). Its optimizing empirical quantile differs from \(t\) by \(O_{L^2}(n^{-1/2})\) because the normal density is strictly positive at \(t\). The loss from using \(t\) instead of that quantile is at most the product of the quantile displacement and the \(O_{L^2}(\sqrt n)\) discrepancy between the number of observations above \(t\) and \(k_n\). Cauchy--Schwarz yields \(O_{L^1}(1)\); the lower tail is symmetric.

Since
\[
\mathbb E\psi_t(G)=2\phi(t)-2ta,
\]
and \(k_n-na=O(1)\), summing the two expansions gives
\[
D_{n,k_n}(G)=2n\phi(t)+\sum_{i=1}^n\big(\psi_t(G_i)-\mathbb E\psi_t(G)\big)+O_{L^1}(1).
\]

**3. Radial normalization and central limit theorem.** By the ordinary central limit theorem and Gaussian sample-mean bounds,
\[
\|G^0\|=\sqrt n\left(1+\frac{1}{2n}\sum_{i=1}^n(G_i^2-1)+o_P(n^{-1/2})\right).
\]
Expanding the quotient produces
\[
W_n=2\sqrt n\phi(t)+\frac1{\sqrt n}\sum_{i=1}^n\left[\psi_t(G_i)-\mathbb E\psi_t(G)-\phi(t)(G_i^2-1)\right]+o_P(1).
\]
The summands are independent, centered, and square-integrable; the ordinary central limit theorem gives the asserted Gaussian limit. The specific moment identities are
\[
\mathbb E\psi_t(G)^2=2[(1+t^2)a-t\phi(t)],\quad
\operatorname{Cov}(\psi_t(G),G^2)=2\phi(t),\quad
\operatorname{Var}(G^2)=2.
\]
They yield exactly the displayed \(V(t)\). Its positivity follows because a nonzero multiple of \((G^2-1)\) cannot agree almost surely with the piecewise-linear function \(\psi_t(G)\). The expected-width centering follows from the \(O_{L^1}(1)\) trimmed-sum errors and the exact independent Gaussian radial factor \(\mathbb E\|G^0\|=\sqrt2\Gamma(n/2)/\Gamma((n-1)/2)=\sqrt n(1+O(n^{-1}))\).

**4. Convergence of variances.** The width function on the intrinsic unit sphere is Lipschitz with constant at most the diameter \(\sqrt{2\min(k_n,n-k_n)}\le\sqrt n\). Standard spherical concentration therefore bounds every fixed centered moment of \(W_n\), uniformly in \(n\). The convergence in distribution established above, together with \(\mathbb E W_n-2\sqrt n\phi(t)=o(1)\), is consequently uniformly integrable in degree two. Thus \(\operatorname{Var}(W_n)\to V(t)\).

**5. Certified nonmonotonicity.** The supplementary standalone checker uses only exact rational arithmetic. It evaluates rigorous alternating-series enclosures for the normal density and tail at five rational thresholds, using Machin's arctangent identity for \(\pi\) and exact square-root brackets. It proves
\[
\begin{array}{c|c}
t&\text{certified enclosure for }V(t)\\\hline
1/2&(0.01488,0.01489)\\
1&(0.00581,0.00582)\\
5/4&(0.00787,0.00789)\\
3/2&(0.00870,0.00872)\\
2&(0.00541,0.00543).
\end{array}
\]
Continuity ensures a minimum in the interior of \([1/2,5/4]\), since both endpoint values exceed the value at \(1\). It likewise ensures a maximum in the interior of \([5/4,2]\), since both endpoints lie below the value at \(3/2\). The minima and maxima are strict because \(V\) is real analytic and nonconstant. These intervals are disjoint except at an endpoint where neither extremum occurs. This proves the two distinct interior extrema without claiming uniqueness.

## Verification
Run `python3 hypersimplex_width_check.py` with Python 3 and no third-party dependencies. It verifies all five rational interval certificates and the strict orderings, printing `HYPERSIMPLEX_DIRECTIONAL_WIDTH_CERTIFICATES_PASSED`. Optionally, run `python3 hypersimplex_sample_check.py` with only the Python standard library for independently seeded finite-dimensional projection-width simulations. Sampling corroborates but does not prove the limit or nonmonotonicity; the proof and rational enclosures do.

## Relationship to prior work
Casabella, Joswig, and Kastner (arXiv:2402.17665v1, first posted February 27, 2024) study hypersimplex subdivisions and their relation to finite metric spaces. Their definitions identify \(\Delta(n,k)\) as uniform-matroid base polytopes; their results concern subdivisions, not random-direction widths. Kabluchko, Litvak, and Zaporozhets (arXiv:1511.08479, first posted November 26, 2015), derive mean-width connections with Gaussian maxima and projection-width limits for cubes, regular simplices, and regular cross-polytopes. The limit \(V(0)=1-3/\pi\) agrees with their cube result, which is prior work. The rank-dependent formula and nonmonotone interior extrema are not stated by either source and do not follow merely from the three endpoint families treated there. General trimmed-sum and empirical-quantile CLTs provide classical methods, not a claim of new probabilistic machinery. Published-record searching and comparison did not identify a prior determination of the hypersimplex variance profile; historical priority requires independent checking.

## Limitations
The theorem treats only fixed positive rank fractions as dimension tends to infinity. It gives no uniform error estimate over vanishing rank fractions and no exact finite-dimensional variance formula. It proves **at least** two interior stationary points, not exactly two. The method depends on uniform-matroid structure; nothing is asserted for arbitrary matroid base polytopes. Literature coverage may miss equivalent formulas under trimmed-normal/order-statistic terminology. Independent mathematical review has not been performed.

## References
1. L. Casabella, M. Joswig and L. Kastner, *Subdivisions of Hypersimplices: With a View Toward Finite Metric Spaces*, arXiv:2402.17665v1 (February 27, 2024), https://arxiv.org/abs/2402.17665.
2. Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean Width of Regular Polytopes and Expected Maxima of Correlated Gaussian Variables*, arXiv:1511.08479 (November 26, 2015), https://arxiv.org/abs/1511.08479.
