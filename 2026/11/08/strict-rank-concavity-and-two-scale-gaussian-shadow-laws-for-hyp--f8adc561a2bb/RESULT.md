# Strict rank concavity and two-scale Gaussian shadow laws for hypersimplices

## Finding
For integers \(n\ge3\) and \(1\le k\le n-1\), let \(V_{n,k}\) denote the number of vertices in a Haar-random planar orthogonal shadow of the hypersimplex \(\Delta(n,k)\). The expectation \(F_n(k)=\mathbb E V_{n,k}\) has the exact beta-expectation representation
\[
 F_n(k)=n\mathbb E f(B_{k,n-k}),\qquad
 f(q)=\sqrt2\exp\!\left(-\frac{[\Phi^{-1}(q)]^2}{2}\right),
\]
where \(B_{k,n-k}\sim\operatorname{Beta}(k,n-k)\) and \(f(0)=f(1)=0\). Equivalently,
\[
 F_n(k)=\frac{n(n-1)\binom{n-2}{k-1}}{\sqrt\pi}
 \int_{-\infty}^{\infty}
 e^{-t^2}\Phi(-t)^{k-1}\Phi(t)^{n-k-1}\,dt.
\]
For \(2\le k\le n-2\) its rank profile is strictly discretely concave:
\[
 F_n(k+1)-2F_n(k)+F_n(k-1)<0.
\]
It is symmetric under rank-complementation and uniquely maximized at \(k=n/2\) when \(n\) is even, or precisely at the adjacent middle ranks when \(n\) is odd. Every finite rank satisfies the strict sharp bound \(F_n(k)<\sqrt2 n\).

There are two quantitatively different high-dimensional regimes. If \(k_n/n\to\alpha\in(0,1)\), then
\[
 \frac{F_n(k_n)}n\longrightarrow
 \sqrt2\exp\!\left(-\frac{[\Phi^{-1}(\alpha)]^2}{2}\right).
\]
If \(k\ge1\) is fixed while \(n\to\infty\), then
\[
 \frac{F_n(k)}{\sqrt{2\log n}}\longrightarrow 2\sqrt\pi\,k.
\]
The upper coefficient \(\sqrt2\) is attained asymptotically for middle ranks.

## Assumptions and scope
The hypersimplex is
\[
 \Delta(n,k)=\operatorname{conv}\{\mathbf1_S\in\mathbb R^n:S\subseteq\{1,\ldots,n\},\ |S|=k\}.
\]
Its affine span is the hyperplane \(\sum_i x_i=k\), and its intrinsic tangent space is \(H=\{x:\sum_i x_i=0\}\) of dimension \(n-1\). Choose a two-plane uniformly in the Grassmannian of \(H\) and orthogonally project the polytope onto it. All assertions about the shadow vertex count hold almost surely with respect to this orientation measure. Here \(\Phi\) is the standard normal cumulative distribution function, and the Gaussian quantile is \(\Phi^{-1}\). The beta distribution uses the usual positive-integer shape normalization. We count polygon vertices, equivalently polygon edges.

## Proof
**Gaussian realization and exact crossing count.** A two-row matrix of independent standard Gaussians induces, almost surely, a random two-plane and an invertible linear coordinate change on its image. Subtracting a common translation on \(H\) does not alter the combinatorics. Therefore \(V_{n,k}\) has the same law as the vertex count of
\[
 \operatorname{conv}\Big\{\sum_{i\in S}X_i:|S|=k\Big\},
\]
where the \(X_i\) are independent standard normal planar vectors. In a generic projected configuration, sweeping a supporting direction around the circle changes the maximizing \(k\)-subset only at a tie between two indices \(i,j\), and only when exactly \(k-1\) of the remaining \(n-2\) projected scores are larger than the tied score. Each unordered pair contributes two opposite candidate tie directions. Almost surely no three projected scores tie, and each actual change corresponds to exactly one polygon edge. Thus the total vertex count equals the sum of these successful pair-direction indicators.

For either tie direction \(u\), perpendicular to \(X_i-X_j\), the tied score \(T=(X_i+X_j)\cdot u/2\) has law \(N(0,1/2)\) and is independent of all remaining Gaussian projected scores. Conditional on \(T=t\), the number of larger remaining scores is \(\operatorname{Binomial}(n-2,\Phi(-t))\). Linearity of expectation over the \(2\binom n2\) candidate crossings gives
\[
 F_n(k)=n(n-1)\binom{n-2}{k-1}
 \int_{-\infty}^{\infty}\frac{e^{-t^2}}{\sqrt\pi}
 \Phi(-t)^{k-1}\Phi(t)^{n-k-1}\,dt.
\]
Set \(q=\Phi(-t)\). Its induced density under \(T\sim N(0,1/2)\) is \(\sqrt2\exp(-[\Phi^{-1}(q)]^2/2)=f(q)\). Since
\[
 (n-1)\binom{n-2}{k-1}q^{k-1}(1-q)^{n-k-1}
\]
is the beta \((k,n-k)\) density, the claimed expectation representation follows. This calculation specializes a pre-existing general integral for expected planar \(k\)-facets; the probabilistic crossing principle is not claimed as new.

**Strict rank concavity.** The \(k\)-th order statistic \(U_{(k)}\) of \(n-1\) independent uniform variables is beta \((k,n-k)\). Direct differentiation yields
\[
 f'(q)=-2\sqrt\pi\,\Phi^{-1}(q),\qquad
 f''(q)=-\frac{2\sqrt\pi}{\phi(\Phi^{-1}(q))}<0.
\]
For consecutive order statistics,
\[
 \begin{aligned}
 F_n(k+1)-F_n(k)
 &=n\int_0^1 f'(q)\Pr\{U_{(k)}\le q<U_{(k+1)}\}\,dq\\
 &=n\int_0^1 f'(q)\binom{n-1}{k}q^k(1-q)^{n-1-k}\,dq\\
 &=\mathbb E f'(B_{k+1,n-k}),
 \end{aligned}
\]
where \(1\le k\le n-2\). The latter beta variables are successively increasing order statistics of a sample of \(n\) independent uniforms; hence the sequence of expectations is strictly decreasing because \(f'\) is strictly decreasing. This proves the second-difference inequality. Gaussian symmetry yields \(f(q)=f(1-q)\) and hence \(F_n(k)=F_n(n-k)\), so the strict maximum lies at the central rank or central pair. Also \(0<f(q)\le\sqrt2\), with equality only at \(q=1/2\), a zero-probability event under any beta law, so \(F_n(k)<\sqrt2 n\).

**Dense and sparse limits.** For \(k_n/n\to\alpha\in(0,1)\), the mean of the beta variable is \(k_n/n\) and its variance is \(k_n(n-k_n)/[n^2(n+1)]\). It converges in probability to \(\alpha\); bounded continuity of \(f\) proves the first limit. At \(\alpha=1/2\), its value is \(\sqrt2\), proving sharpness.

For fixed positive \(k\), put \(Q_n\sim\operatorname{Beta}(k,n-k)\) and \(Y_n=nQ_n\). The beta density yields \(Y_n\Rightarrow\operatorname{Gamma}(k,1)\) and \(\sup_n\mathbb E Y_n^s<\infty\) for every fixed positive moment order \(s\). Mills' ratio for the normal lower tail implies
\[
 f(q)\sim 2\sqrt\pi\,q\sqrt{2\log(1/q)}\qquad(q\downarrow0).
\]
Consequently, for fixed \(y>0\),
\[
 \frac{n f(y/n)}{\sqrt{2\log n}}\longrightarrow2\sqrt\pi\,y.
\]
To exchange this limit with expectation, use the bound \(f(q)\le Cq\sqrt{\log(e/q)}\) for \(q\le1/2\). For \(n\ge3\), after the displayed normalization the corresponding integrand with \(q=Y_n/n\) is at most \(C'\{Y_n^{1/2}+Y_n^{3/2}\}\) on \(Y_n\le n/2\). Uniform moments give uniform integrability. On \(Y_n>n/2\), the beta tail is exponentially small in \(n\), while \(f\le\sqrt2\). Hence the expectation converges to \(2\sqrt\pi\,\mathbb EY=2\sqrt\pi k\), proving the sparse-rank statement.

## Verification
The accompanying standalone `verify_shadow.py` independently computes the normal-tie integral (rather than the beta formula) and directly enumerates all \(k\)-element coordinate sums of independent planar Gaussian samples. It compares empirical hull vertex counts with the integral in dimensions \(4,6,8\) and verifies strict discrete concavity numerically for dimensions \(4,6,8,20,80,250\). Running `python verify_shadow.py` with NumPy and SciPy produced `GAUSSIAN_HYPERSIMPLEX_SHADOW_FORMULA_AND_CONCAVITY_CHECKS_PASSED`. Finite experiments are not an infinite proof; the analytical arguments above provide the all-dimensional statement.

## Relationship to prior work
Black and Criado [1] explicitly identify the hypersimplex and its connection to planar \(k\)-sets in their study of random shadows and prove general shadow-size bounds; they do not provide this strictly concave expected-rank profile. The crossing-integral approach belongs to the extensive expected \(k\)-facet literature, notably Bárány–Steiger [2] and Leroux–Rademacher [3]. The integral representation above is a specialization of their general crossing framework, not an assertion of first discovery of that framework. Godland, Kabluchko and Zaporozhets [4] prove broad Gaussian-image face-angle identities, which can encompass expected face numbers implicitly, but do not state the explicit beta-profile, strict rank optimization, or the two asymptotic regimes here. Leroux–Rademacher [5, Theorem 1] also give an exact one-dimensional integral for Gaussian \(k\)-facets in arbitrary dimension, which subsumes the raw Gaussian expectation integral here. Their subsequent asymptotic results emphasize dimension tending to infinity; the strict finite-rank concavity and the two planar rank-scaling limits are the claims distinguished here. The additional results of the present theorem are the explicit concave Gaussian beta kernel, the strict all-finite-rank optimizer, and its sharp dense/fixed-rank scaling laws. Historical priority remains provisional, especially for equivalent statements embedded in older expected \(k\)-set theory.

## Limitations
Only expected shadow vertex counts are addressed. The theorem does not characterize their distribution, concentration, variance, or worst-case \(k\)-set complexity. The dense limit assumes a limiting proportion strictly between zero and one, while the sparse statement fixes \(k\) before taking \(n\) large. A general interpolating law for varying \(k=o(n)\) is not asserted. The cited 1994 source was available only in summary form at the time of this review, so complete historical priority is not established. No independent mathematical review has been performed.

## References
[1] Alexander E. Black and Francisco Criado, *Random Shadows of Fixed Polytopes*, arXiv:2406.06936, first posted June 11, 2024; later published in *Discrete & Computational Geometry* (October 31, 2026). https://arxiv.org/abs/2406.06936

[2] Imre Bárány and William Steiger, *On the Expected Number of k-Sets*, *Discrete & Computational Geometry* 11 (1994), 243–263. https://doi.org/10.1007/BF02574008

[3] Brett Leroux and Luis Rademacher, *Improved Bounds for the Expected Number of k-Sets*, arXiv:2106.04782, June 9, 2021. https://arxiv.org/abs/2106.04782

[4] Thomas Godland, Zakhar Kabluchko, Dmitry Zaporozhets, *Angle Sums of Random Polytopes*, arXiv:2007.02590, July 2020. https://arxiv.org/abs/2007.02590

[5] Brett Leroux and Luis Rademacher, *Estranged Facets and k-Facets of Gaussian Random Point Sets*, arXiv:2307.00687, July 2, 2023. https://arxiv.org/abs/2307.00687
