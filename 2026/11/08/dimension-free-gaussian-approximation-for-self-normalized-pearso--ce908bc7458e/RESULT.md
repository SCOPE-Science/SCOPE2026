# Dimension-free Gaussian approximation for self-normalized Pearson radial fluctuations

## Finding

For each integer \(d\ge2\), choose an arbitrary integer \(n=n_d\ge2\) and an arbitrary random vector \(L=(L_1,\ldots,L_n)\in[0,\infty)^n\), with no independence or moment conditions among its coordinates. Let \(U_1,\ldots,U_n\) be independent uniformly distributed directions on the unit sphere of \(\mathbb R^d\), independent of \(L\). Put
\[
S=\sum_{i=1}^nL_iU_i,\qquad Q(L)=\sum_{1\le i<j\le n}L_i^2L_j^2.
\]
Assume \(\Pr(Q(L)>0)=1\), meaning that at least two step lengths are positive almost surely. Define the conditionally unit-variance radial fluctuation
\[
Z_d=\frac{\sqrt d}{2\sqrt{Q(L)}}\left(\|S\|_2^2-\sum_{i=1}^nL_i^2\right).
\]
Let \(\gamma\) be the standard normal law and let \(W_1\) be the \(1\)-Wasserstein distance on the real line. Then, almost surely with respect to \(L\),
\[
\boxed{W_1\bigl(\mathcal L(Z_d\mid L),\gamma\bigr)\le \frac{25}{\sqrt d}.}
\]
The constant is independent of \(d\), \(n\), the length vector and its joint distribution. Thus \(Z_d\) is asymptotically standard normal even if the number of steps grows arbitrarily fast with dimension, lengths are strongly dependent or have infinite moments, and their distributions change with \(d\). The approximation is conditional on the complete realized length vector, not merely annealed.

## Assumptions and scope

There is no requirement that the length arrays be jointly coupled across dimensions or that \(n_d\) be increasing. All coordinates of \(L\) are finite nonnegative random variables and independent of the directions; the coordinates of \(L\) may be arbitrarily dependent. Conditional on \(L\), \(\mathbb EZ_d=0\) and \(\operatorname{Var}(Z_d)=1\) exactly. The requirement \(Q(L)>0\) is necessary for the stated normalization: with fewer than two positive lengths the centered squared radius is identically zero. The theorem is about normalized squared radii, not about unnormalized almost-sure convergence. The convergence is in distribution and in \(W_1\); no almost-sure coupling assertion is made.

## Proof

Condition on \(L=a\) with \(Q=Q(a)>0\). From the squared-norm identity,
\[
Z_d=\frac{\sqrt d}{\sqrt Q}\sum_{i<j}a_ia_j\langle U_i,U_j\rangle.
\]
For distinct unordered pairs \(\{i,j\}\ne\{k,l\}\), the inner products have zero covariance by independent spherical sign symmetry. Also \(\mathbb E\langle U_i,U_j\rangle^2=1/d\). This proves the exact conditional mean and variance.

Couple the directions to independent standard Gaussian vectors \(G_i\in\mathbb R^d\) by writing \(G_i=\sqrt d\,R_iU_i\), where \(R_i=\|G_i\|_2/\sqrt d\). Each \(R_i\) is independent of its direction, and all radii and directions are mutually independent within their respective families. Define the Gaussian comparison statistic
\[
H_d=\frac{1}{\sqrt{dQ}}\sum_{i<j}a_ia_j\langle G_i,G_j\rangle=\frac1{\sqrt d}\sum_{h=1}^dY_h,
\quad
Y_h=\frac1{\sqrt Q}\sum_{i<j}a_ia_jG_{ih}G_{jh}.
\]
The variables \(Y_h\) are independent and identically distributed, centered, and have variance one. Let \(B\) be the real symmetric matrix with zero diagonal and entries \(B_{ij}=a_ia_j/(2\sqrt Q)\) for \(i\ne j\). Then \(Y_h=g_h^\top Bg_h\), with \(g_h\) standard Gaussian; \(\operatorname{tr} B=0\) and \(2\operatorname{tr}(B^2)=1\). The Gaussian quadratic-form fourth-moment identity gives
\[
\mathbb EY_h^4=3+48\operatorname{tr}(B^4)\le3+48\operatorname{tr}(B^2)^2=15.
\]
Consequently \(\mathbb E|Y_h|^3\le15^{3/4}\). The standard independent-summand Wasserstein Stein inequality, for mean-zero variance-one summands, gives
\[
W_1(\mathcal L(H_d),\gamma)\le\frac{3\mathbb E|Y_1|^3}{\sqrt d}\le\frac{3\cdot15^{3/4}}{\sqrt d}.
\]
For completeness, this inequality follows from the normal Stein equation for a \(1\)-Lipschitz test function, its second-derivative bound of \(2\), and a second-order Taylor expansion around the leave-one-out sum.

The same coupling yields
\[
Z_d-H_d=\frac{\sqrt d}{\sqrt Q}\sum_{i<j}a_ia_j(1-R_iR_j)\langle U_i,U_j\rangle.
\]
Every cross-pair term vanishes after expectation by spherical sign symmetry, including pairs sharing one vertex, and the radii are independent of the directions. Thus, *exactly*,
\[
\mathbb E(Z_d-H_d)^2=\mathbb E(1-R_1R_2)^2
=2\left[1-(\mathbb ER_1)^2\right]
=2\operatorname{Var}(R_1).
\]
Gaussian Poincaré applied to \(g\mapsto\|g\|_2/\sqrt d\), whose gradient has squared norm \(1/d\) almost everywhere, gives \(\operatorname{Var}(R_1)\le1/d\). Hence \(\mathbb E|Z_d-H_d|\le\sqrt{2/d}\). The coupling inequality and the triangle inequality now give
\[
W_1(\mathcal L(Z_d\mid L=a),\gamma)
\le\frac{3\cdot15^{3/4}+\sqrt2}{\sqrt d}<\frac{25}{\sqrt d}.
\]
The bound does not depend on \(a\). Conditioning therefore proves the random-length statement without any integrability hypothesis.

## Verification

An independent finite calculation of the two lowest nontrivial moments gives, writing \(T(a)=\sum_{i<j<k}a_i^2a_j^2a_k^2\),
\[
\mathbb E(Z_d^2\mid L=a)=1,
\qquad
\mathbb E(Z_d^3\mid L=a)=\frac{6T(a)}{\sqrt d\,Q(a)^{3/2}}.
\]
The third-moment identity follows by enumerating ordered triangles of spherical inner products: their expectation is \(1/d^2\), while every other three-edge pattern has an odd-degree vertex and vanishes. It identifies a finite-dimensional skewness contribution; it is not used as a substitute for the Gaussian approximation proof.

Run `python verify.py` with NumPy installed to reproduce the exact finite spherical-moment enumerations for \(d=2,3,4\), the Gaussian quadratic fourth-moment bounds across several arbitrary weight arrays, the Gaussian-radial inequality for \(2\le d\le400\), and seeded numerical diagnostics for both sparse and dense length arrays. Exact enumerations and simulations check finite identities and scaling only; the quantitative statement for every \(d\) follows from the analytic argument above.

## Relationship to prior work

Bignamini, Casini and Martinelli (arXiv:2609.05195, first submitted September 4, 2026), particularly Theorems 4.3 and 5.4 and Lemma 5.3, study high-dimensional Pearson walk radii for dependent step lengths, obtaining first-order convergence and moment bounds. Their arguments do not assert a conditionally standardized normal limit with a uniform \(W_1\) rate for arbitrary length arrays. The pair-product normalization used here is closely related to the moment expression in their Lemma 5.3, but the Gaussian radial coupling and uniform distributional bound are different conclusions.

The classical fixed-step spherical projection theorem of Stam includes fixed-number Gaussian fluctuation special cases. Grundmann's radial-walk theorem (arXiv:1210.7090) and Kabluchko–Marynych's Theorem 3.3 (arXiv:2211.08538) give normal limits in regimes of identically distributed radial increments, including deterministic equal radii. Those results are fully credited for such special cases. They do not, as stated, give this conditional, arbitrary-dependent-length and arbitrary-step-count \(W_1\) inequality. The present result is therefore a quantitative uniform extension, not a claim that high-dimensional Gaussian radial fluctuations themselves were unknown.

## Limitations

The universal constant \(25\) is an explicit upper bound, not claimed optimal. The law can differ from normal substantially at small \(d\). The conclusion is conditional on independence of directions from lengths; it does not extend to direction-dependent lengths. No sharp \(W_1\) lower bound is proved, and this theorem does not characterize almost-sure convergence of the unnormalized squared-radius error. An earlier general-purpose normal-approximation theorem might imply the bound without explicitly discussing Pearson walks; that historical-priority possibility merits separate review.

## References

1. D. A. Bignamini, E. G. Casini, A. Martinelli, *Asymptotic Behaviour for Isotropic Pearson Random Walks*, arXiv:2609.05195v2 (2026); first public version September 4, 2026. https://arxiv.org/abs/2609.05195
2. Z. Kabluchko, A. Marynych, *Random Walks in the High-Dimensional Limit I: The Wiener Spiral*, arXiv:2211.08538 (2022/2023), Theorem 3.3 and Remark 3.4. https://arxiv.org/abs/2211.08538
3. W. Grundmann, *Limit theorems for radial random walks on Euclidean spaces of high dimensions*, 2012 preprint, arXiv:1210.7090, Theorem 1.1. https://arxiv.org/abs/1210.7090
4. A. J. Stam, *Limit theorems for uniform distributions on spheres in high-dimensional Euclidean spaces*, Journal of Applied Probability 19 (1982), 221–228, especially the fixed-step scope reported by Kabluchko–Marynych. https://doi.org/10.2307/3213932
5. Standard Gaussian Poincaré inequality and normal Stein Wasserstein bound; the necessary applications are shown directly in the proof.
