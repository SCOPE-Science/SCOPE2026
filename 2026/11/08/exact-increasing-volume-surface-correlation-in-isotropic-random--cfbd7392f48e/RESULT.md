# Exact increasing volume–surface correlation in isotropic random zonotopes

## Finding
For independent Haar-uniform unit vectors \(U_1,\ldots,U_n\in S^2\), \(n\ge3\), define \(Z_n=\sum_{i=1}^{n}[0,U_i]\). Let \(A_n\) be its ordinary boundary surface area and \(V_n\) its three-dimensional volume. With
\[
\nu=\frac83-\frac{\pi^2}{4}>0,\qquad
\kappa=\frac{\pi^2}{32}-\frac5{18}>0,
\]
their exact correlation is
\[
\operatorname{Corr}(V_n,A_n)=\left(1+\frac{16\kappa}{3(n-2)\nu}\right)^{-1/2}.
\]
It is strictly increasing in the integer \(n\ge3\) and tends to one; more precisely, \(n(1-\operatorname{Corr}(V_n,A_n))\to8\kappa/(3\nu)\). A geometric orthogonal remainder makes this precise at every finite sample size:
\[
V_n-\mathbb EV_n=\frac{n-2}{4}(A_n-\mathbb EA_n)+R_n,
\quad\operatorname{Cov}(R_n,A_n)=0,
\quad\operatorname{Var}(R_n)=\binom n3\kappa.
\]
The separate marginal moment identities are useful known ingredients; the new object here is the coupled law and its exact correlation profile.

## Assumptions and scope
The segment generators have deterministic Euclidean length one and independent directions uniform with respect to normalized surface measure on the two-sphere. The number \(n\) is an integer at least three. Surface area is the ordinary two-dimensional boundary measure of the almost surely full-dimensional zonotope. All expectations and correlations refer to randomness in the generator directions, not to random viewing directions. Translation of the zonotope does not change any assertion.

## Proof
Set \(s_{ij}=\|U_i\times U_j\|\) and \(d_{ijk}=|\det(U_i,U_j,U_k)|\). The intrinsic-volume decomposition of zonotopes gives, almost surely,
\[
A_n=2\sum_{i<j}s_{ij},\qquad V_n=\sum_{i<j<k}d_{ijk}.
\]
For independent uniform sphere directions, the dot product of two directions is uniform on \([-1,1]\); hence \(\mathbb Es_{12}=\pi/4\) and \(\mathbb E_{12}^2=2/3\). Conditional on two directions, the mean absolute projection of a third uniform unit vector onto their unit normal is one half. Thus
\[
\mathbb E(d_{123}\mid U_1,U_2)=\frac12s_{12},\qquad \mathbb E d_{123}=\frac\pi8,
\qquad \mathbb E d_{123}^2=\frac13\mathbb E s_{12}^2=\frac29.
\]
Define the centered pair kernel \(b(U_i,U_j)=\frac12s_{ij}-\frac\pi8\), and the centered triple kernel
\[
g(U_i,U_j,U_k)=d_{ijk}-\frac12(s_{ij}+s_{ik}+s_{jk})+\frac\pi4.
\]
By rotation invariance, \(\mathbb E[b(U_i,U_j)\mid U_i]=0\). The preceding conditional identity gives \(\mathbb E[g(U_i,U_j,U_k)\mid U_i,U_j]=0\), and similarly for every pair. Counting how often each pair occurs in the triple sum yields the exact decomposition
\[
V_n-\mathbb EV_n=(n-2)\sum_{i<j} b(U_i,U_j)+\sum_{i<j<k}g(U_i,U_j,U_k).
\]
Since \(A_n-\mathbb EA_n=4\sum_{i<j}b(U_i,U_j)\), the first term equals \((n-2)(A_n-\mathbb EA_n)/4\). Let the final triple sum be \(R_n\). Degeneracy makes distinct pair kernels uncorrelated and makes the triple kernel orthogonal to every pair kernel, even when indices overlap. Similarly, two distinct triple kernels are uncorrelated because they share at most two indices and conditioning on those shared variables gives zero.

Directly from the moments above,
\[
\operatorname{Var}(2s_{12})=\frac83-\frac{\pi^2}4=\nu,
\quad \operatorname{Var}(b)=\frac16-\frac{\pi^2}{64}=\frac\nu{16},
\]
\[
\operatorname{Var}(d_{123})=\frac29-\frac{\pi^2}{64},
\quad \operatorname{Var}(g)=\operatorname{Var}(d_{123})-3\operatorname{Var}(b)=\frac{\pi^2}{32}-\frac5{18}=\kappa.
\]
The last subtraction is valid because the three pair projections are pairwise orthogonal and \(g\) is orthogonal to them. Consequently,
\[
\mathbb EA_n=\frac\pi2\binom n2,\quad \mathbb EV_n=\frac\pi8\binom n3,
\quad\operatorname{Var}(A_n)=\nu\binom n2,
\]
\[
\operatorname{Var}(R_n)=\kappa\binom n3,\quad
\operatorname{Cov}(V_n,A_n)=\frac{n-2}{4}\nu\binom n2,
\]
\[
\operatorname{Var}(V_n)=\frac{(n-2)^2}{16}\nu\binom n2+\kappa\binom n3.
\]
Both constants are positive (\(\nu\approx0.1993\), \(\kappa\approx0.03065\)). Dividing the covariance by the standard deviations and using \(\binom n3/\binom n2=(n-2)/3\) gives the displayed formula. Its denominator decreases strictly as \(n\) increases, and its Taylor expansion at large \(n\) yields the asserted sharp limit. The positive remainder variance shows the finite-sample correlation is strictly below one.

## Verification
The attached standalone script `verify_zonotope_joint.py` samples independent unit vectors, independently evaluates the parallelogram and absolute-determinant sums, verifies the exact samplewise orthogonal decomposition, and compares empirical variances, covariance, and correlation with the formulas for three sample sizes. It passed its stated numerical tolerances. These finite checks corroborate, but do not replace, the conditional-expectation proof.

## Relationship to prior work
Schneider's 2022 *Random zonotopes and valuations* gives expectations of intrinsic volumes and general one-variable fluctuation theory for sums of independent segments. Joós and Lángi's 2022 *Isoperimetric problems for zonotopes* gives the determinant/intrinsic-volume decomposition. Davydov and Vershik's 1998 work establishes random-zonotope limit theorems. None of their checked relevant results gives the joint finite-sample covariance, the orthogonal third-order remainder, or the strictly increasing explicit correlation profile. Independent marginal distribution formulas alone do not determine a covariance. The proof uses the geometric conditional determinant identity as the additional joint input.

## Limitations
The formulas require fixed unit segment lengths, independent isotropic directions, and three-dimensional Euclidean volume and surface area. They do not assert independence of \(R_n\) and \(A_n\), only zero covariance, nor do they give their full joint distribution. Historical priority remains provisional because equivalent joint moment formulas could appear in other stochastic-geometry literature. No independent mathematical review has occurred.

## References
- R. Schneider, *Random zonotopes and valuations*, arXiv:2202.06774, first posted 2022-02-14, https://arxiv.org/abs/2202.06774.
- A. Joós and Z. Lángi, *Isoperimetric problems for zonotopes*, arXiv:2206.03204, first posted 2022-06-07, https://arxiv.org/abs/2206.03204.
- Yu. Davydov and A. M. Vershik, *Réarrangements convexes des marches aléatoires*, Ann. Inst. H. Poincaré Probab. Stat. 34 (1998), 73–95, https://www.numdam.org/item/AIHPB_1998__34_1_73_0/.
