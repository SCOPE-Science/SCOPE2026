# Perimeter-normalized random zonogons: universal second-order area law and a sharp spike obstruction

## Finding
Let \(\Theta_1,\ldots,\Theta_n\) be independent uniform angles in \([0,\pi)\), and let \(w_{n,1},\ldots,w_{n,n}>0\) be deterministic weights with sum one. Consider the planar zonogon
\[
Z_n=\sum_{j=1}^n[0,w_{n,j}(\cos\Theta_j,\sin\Theta_j)].
\]
Its perimeter is exactly \(2\). Write \(A_n\) for its area and \(D_n=n(\pi^{-1}-A_n)\) for its rescaled disk-area deficit. Define \(\rho_n=n\sum_jw_{n,j}^2\).

**Diffuse universality.** Suppose \(\rho_n\to\rho<\infty\) and
\[
\frac{\max_jw_{n,j}}{(\sum_jw_{n,j}^2)^{1/2}}\longrightarrow0.
\]
Then \(\rho\ge1\) and
\[
D_n\ \Longrightarrow\ D_\rho:=\frac{2\rho}{\pi}\sum_{m=1}^\infty\frac{E_m}{4m^2-1},
\qquad E_1,E_2,\ldots\ \text{independent }\operatorname{Exp}(1).
\]
The limit has mean \(\rho/\pi\), variance \(\rho^2(1/4-2/\pi^2)\), and Laplace transform for \(s\ge0\)
\[
\mathbb E[e^{-sD_\rho}]=
\frac{\sqrt{1-2\rho s/\pi}}{\sin\!\bigl((\pi/2)\sqrt{1-2\rho s/\pi}\bigr)},
\]
where the ratio is continuously extended at zero, and where for \(2\rho s/\pi>1\) the equivalent real expression is \(b/\sinh(\pi b/2)\) with \(b=\sqrt{2\rho s/\pi-1}\).

In particular, for independent positive segment lengths \(L_j\), independent of the directions, with \(0<\mathbb EL_1<\infty\) and \(\mathbb EL_1^2<\infty\), choosing \(w_{n,j}=L_j/\sum_{k=1}^nL_k\) gives the same limit in distribution with the sole radial parameter
\[
\rho=\frac{\mathbb EL_1^2}{(\mathbb EL_1)^2}.
\]
Thus the *entire* non-Gaussian second-order shape law depends on the length distribution only through this moment ratio.

**Sharp obstruction.** Fix \(c>0\), and for integers \(n>c^2\) take \(w_{n,1}=c/\sqrt n\) and \(w_{n,j}=(1-c/\sqrt n)/(n-1)\) for \(2\le j\le n\). Then \(\rho_n\to1+c^2\), but the limit is instead
\[
D_n\Longrightarrow D_c^{\mathrm{spike}}=\frac2\pi\sum_{m\ge1}\frac{|G_m+c|^2}{4m^2-1},
\]
where the \(G_m\) are independent circular complex Gaussians with independent real and imaginary parts \(N(0,1/2)\). In particular,
\[
\operatorname{Var}(D_c^{\mathrm{spike}})
=(1/2-4/\pi^2)(1/2+c^2)
< (1+c^2)^2(1/4-2/\pi^2)=\operatorname{Var}(D_{1+c^2}).
\]
The equal quadratic weight statistic \(\rho_n\) therefore does not determine the limit once a single segment remains of central-limit scale.

## Assumptions and scope
Directions are independent and Haar-uniform on the unoriented circle; weights may be deterministic, or produced by independent positive lengths independent of those directions. For the iid-length case, only a finite positive first moment and finite second moment are assumed. All convergence is in distribution; no total-variation or rate claim is made. The deterministic triangular-array theorem requires the two displayed conditions and no unmentioned regularity. Equality of the orientation's absolute signs is irrelevant because the zonogon is translation invariant.

For any positive deterministic weights of sum one, the finite-dimensional identities are exact:
\[
\mathbb E_\Theta D_n=\frac{n}{\pi}\sum_{i=1}^nw_{n,i}^2,\qquad
\operatorname{Var}_\Theta(D_n)
=n^2\left(\frac12-\frac4{\pi^2}\right)
\sum_{1\le i<j\le n}w_{n,i}^2w_{n,j}^2.
\]
For random lengths the identities apply conditionally on all lengths, not as unconditional equalities with weights replaced by their expectations.

## Proof
The zonotope area formula (the two-dimensional segment mixed-volume formula) gives
\[
A_n=\sum_{i<j}w_{n,i}w_{n,j}|\sin(\Theta_i-\Theta_j)|.
\]
The perimeter of a line segment counted as a convex body is twice its length, and the planar perimeter is Minkowski additive; therefore \(\operatorname{perim}(Z_n)=2\sum_jw_{n,j}=2\). The disk with perimeter two has area \(1/\pi\), so \(D_n\ge0\) by the isoperimetric inequality.

The uniformly and absolutely convergent Fourier series
\[
|\sin t|=\frac2\pi-\frac4\pi\sum_{m\ge1}\frac{\cos(2mt)}{4m^2-1}
\]
and the telescoping identity \(\sum_{m\ge1}(4m^2-1)^{-1}=1/2\) yield, *without a remainder*,
\[
D_n=\frac{2n}{\pi}\sum_{m\ge1}\frac{|S_{n,m}|^2}{4m^2-1},
\qquad S_{n,m}=\sum_{j=1}^nw_{n,j}e^{2im\Theta_j}.
\tag{1}
\]
Indeed, \(\sum_{i<j}w_iw_j\cos(2m(\Theta_i-\Theta_j))=(|S_{n,m}|^2-\sum_iw_i^2)/2\), and the diagonal contributions cancel exactly after summing the Fourier coefficients.

For each fixed \(M\), the random vectors consisting of the real and imaginary parts of \(\sqrt n S_{n,1},\ldots,\sqrt n S_{n,M}\) form sums of independent centered bounded trigonometric vectors. The covariance is \((\rho_n/2)I_{2M}\), by Fourier orthogonality on \([0,\pi)\). Since \(\rho_n\to\rho\) and \(\max_j\sqrt n w_{n,j}\to0\), the multivariate Lindeberg theorem implies convergence to independent circular complex Gaussians \(\sqrt\rho G_1,\ldots,\sqrt\rho G_M\). Consequently each limiting squared modulus is \(\rho E_m\), with independent \(\operatorname{Exp}(1)\) variables.

The infinite series passage is rigorous rather than a finite truncation claim: using \(\mathbb E_\Theta|S_{n,m}|^2=\sum_jw_{n,j}^2\) gives the *exact tail estimate*
\[
\mathbb E_\Theta\left[\frac{2n}{\pi}\sum_{m>M}\frac{|S_{n,m}|^2}{4m^2-1}\right]
=\frac{\rho_n}{\pi(2M+1)}.
\tag{2}
\]
The uniformly bounded \(\rho_n\), Markov's inequality, and convergence of finite mode vectors prove the full weak limit in (1). Independently, \(\mathbb E|G_m|^2=1\) and \(\operatorname{Var}|G_m|^2=1\). Summing the first two coefficient series yields the stated limiting mean and variance. Multiplication of the exponential Laplace transforms and the classical product
\[
\prod_{m\ge1}\left(1+\frac{2\rho s/\pi}{4m^2-1}\right)^{-1}
=\frac{\sqrt{1-2\rho s/\pi}}{\sin((\pi/2)\sqrt{1-2\rho s/\pi})}
\]
proves the closed transform; continuity covers its transition to the hyperbolic branch.

For iid lengths, the strong laws give \(n\sum_jw_{n,j}^2=(n^{-1}\sum_jL_j^2)/(n^{-1}\sum_jL_j)^2\to\rho\). The finite second moment also gives \(\max_{j\le n}L_j^2/n\to0\) in probability (union bound and \(t\Pr(L_j^2>t)\to0\)). Combined with the strong law for \(n^{-1}\sum L_j^2\), this verifies the diffuse condition in probability. Conditioning on the lengths and applying the deterministic convergence result (or the triangular-array characteristic-function proof directly) gives the unconditional limit.

For the spike construction, the first trigonometric term of \(\sqrt n S_{n,m}\) is \(c e^{2im\Theta_1}\); the other \(n-1\) terms tend jointly to independent circular Gaussians \(G_m\), independent of \(\Theta_1\). Conditional on \(\Theta_1\), rotational invariance shows that the squared moduli are independent, each distributed as \(|G_m+c|^2\). The same tail bound (2), now with \(\rho_n\to1+c^2\), validates infinite-mode convergence. The square modulus has mean \(1+c^2\) and variance \(1+2c^2\). Summing coefficient squares gives the displayed spike variance and its strict separation from the diffuse limit for every \(c>0\).

For the exact finite-n mean and variance, the centered pair kernel \(|\sin(\Theta_i-\Theta_j)|-2/\pi\) has variance \(1/2-4/\pi^2\) and any two distinct pair terms have zero covariance, even if the pairs share one index, because the conditional mean in that index is zero. This proves both finite-n identities.

## Verification
The standalone `weighted_zonogon_check.py` reconstructs areas via the pairwise determinant formula and independently via planar convex hulls of all segment endpoint sums for small \(n\). It checks the normalized perimeter, compares a truncated Fourier energy to the geometric deficit, and tests the Laplace transforms against seeded Monte Carlo samples for equal, binary, and single-spike length arrays. These finite checks verify normalization and sample behavior; the infinite limits and uniqueness of the two laws are supplied by the proofs above. Run `python weighted_zonogon_check.py` with NumPy and SciPy available.

## Relationship to prior work
Rolf Schneider's *Random zonotopes and valuations* (public preprint 2022-02-14, arXiv:2202.06774) establishes general expectation identities and an ordinary nondegenerate \(\sqrt n\)-central limit theorem for random-zonotope valuations under suitable hypotheses; its Section 4 does not determine the perimeter-normalized **degenerate** second-order area law or its deterministic-weight spike boundary. The general zonotope area formula is classical and is not claimed as new. An existing exact Fourier limit for sums of equally weighted independent rotations of a single fixed full-dimensional planar convex body provides important related prior coverage; its equal-weight spectral method is not claimed as original here. That fixed-body model does not cover the variable-length deterministic universality criterion or the one-spike noncentral boundary.

Buffière and Marchal's *Fluctuations of lattice zonotopes and polygons* (public preprint 2023-03-31, arXiv:2303.18045) gives Gaussian boundary fluctuations under a discrete lattice-zonotope sampling model, distinct from the continuous independent uniform directions and arbitrary radial weights here.

Joós and Lángi's *Isoperimetric problems for zonotopes* (public preprint 2022-06-07, arXiv:2206.03204), particularly Sections 3–4, develops sharp deterministic zonotope volume/intrinsic-volume inequalities and an expected-volume construction for equal-length random directions; it does not give the full second-order distribution, arbitrary-length universality, or the one-spike obstruction.

Giné's 1975 Sobolev-uniformity framework (DOI 10.1214/aos/1176343283) provides important general prior spectral machinery for circular directional statistics. Its existence limits any novelty claim for the unweighted Fourier-series method alone; the specific geometric perimeter-normalization universality across variable length laws and the explicit one-spike breakdown constitute the present contribution. Earlier general degenerate-U-statistic limit theorems are also credited as background rather than claimed as inventions.

## Limitations
No claim is made for nonuniform or dependent directions, weights violating the diffuse criterion except for the explicit one-spike construction, heavy-tailed iid lengths with infinite second moment, or convergence of arbitrary unbounded moments without additional uniform-integrability assumptions. The single-spike example establishes failure of universality *without* the diffuse hypothesis; it does not claim a full classification of every possible nondiffuse limit. Historical priority is provisional, particularly concerning weighted versions of classical Sobolev circular statistics not indexed under random-zonotope terminology. Independent mathematical validation has not been carried out.

## References
1. R. Schneider, *Random zonotopes and valuations*, arXiv:2202.06774v1 (first public posting February 14, 2022), sections 1, 3, 4. https://arxiv.org/abs/2202.06774
2. T. Buffière and P. Marchal, *Fluctuations of lattice zonotopes and polygons*, arXiv:2303.18045v1 (first public posting March 31, 2023), introduction and limit-theorem statements. https://arxiv.org/abs/2303.18045
3. E. Giné, *Invariant tests for uniformity on compact Riemannian manifolds based on Sobolev norms*, Annals of Statistics 3 (1975), 1243–1266. DOI: 10.1214/aos/1176343283.
4. A. Joós and Z. Lángi, *Isoperimetric problems for zonotopes*, arXiv:2206.03204v1 (first public posting June 7, 2022), sections 3–4. https://arxiv.org/abs/2206.03204
5. Classical planar zonotope area and perimeter identities, and classical multivariate triangular-array central limit theorem; used as known tools.
