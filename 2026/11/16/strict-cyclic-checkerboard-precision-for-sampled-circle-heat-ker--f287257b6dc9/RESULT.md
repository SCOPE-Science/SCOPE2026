# Strict cyclic checkerboard precision for sampled circle heat kernels

## Finding
Let \(n\ge2\) be any integer and \(t>0\). On the unit circle \(\mathbb T=\mathbb R/\mathbb Z\), define the real, positive-definite heat/squared-exponential covariance
\[
H_t(x)=\sum_{k\in\mathbb Z}e^{-t k^2}e^{2\pi i kx}.
\]
Let \(\Sigma^{(n,t)}=(H_t((i-j)/n))_{0\le i,j<n}\) and \(Q^{(n,t)}=(\Sigma^{(n,t)})^{-1}\). For all \(0\le i,j<n\), with the cyclic distance \(d_n(i,j)=\min\{|i-j|,n-|i-j|\}\),
\[
\boxed{\quad (-1)^{d_n(i,j)}Q^{(n,t)}_{ij}>0.\quad}
\]
In particular every off-diagonal precision entry is strictly nonzero for every circle size and every positive parameter. Thus equispaced samples of the real Gaussian field with covariance \(H_t\) have a **complete conditional-dependence graph**. The signs of the corresponding conditional partial correlations are \((-1)^{d_n(i,j)+1}\).

This holds for both odd and even sample sizes: on odd cycles there is no globally consistent alternating vertex coloring, yet the *shorter-distance* precision sign law still holds.

## Assumptions and scope
The covariance is defined by the absolutely convergent Fourier series displayed above; no intrinsic geodesic-distance Gaussian kernel is being substituted for it. The parameter \(t\) is any strictly positive real number. The sample sites are exactly \(i/n\), with \(n\ge2\); sites are distinct. The covariance matrix is real symmetric and positive definite since its discrete Fourier eigenvalues are strictly positive sums of positive Fourier coefficients. We do not claim the result for irregular sites, higher-dimensional tori, arbitrary spectral weights, or the geodesic squared-distance Gaussian. All Fourier sums and products below converge absolutely for fixed positive \(t\).

## Proof
**Step 1: discrete spectrum and theta-product factorization.** The Fourier eigenvalues, with \(z_r=e^{2\pi i r/n}\), are
\[
\lambda_r=n\sum_{h\in\mathbb Z}e^{-t(r+nh)^2}
=\sqrt{\frac\pi t}\sum_{h\in\mathbb Z}q^{h^2}z_r^h,
\qquad q=e^{-\pi^2/(tn^2)}\in(0,1).
\]
The equality follows from Poisson summation. Jacobi's triple-product identity gives
\[
\lambda_r=C_t\prod_{m=1}^\infty
(1+\alpha_m z_r)(1+\alpha_m z_r^{-1}),
\quad \alpha_m=q^{2m-1}\in(0,1),\quad
C_t=\sqrt{\pi/t}\prod_{m=1}^\infty(1-q^{2m})>0.
\]
The factors are positive for unit-modulus \(z_r\), which also verifies nonsingularity. The sequence \((\alpha_m)\) is summable.

**Step 2: a strictly decreasing checkerboard Fourier kernel on *even* cycles.** Work first on the doubled cycle \(\mathbb Z/(2n)\mathbb Z\), and evaluate the positive spectral multiplier
\[
F(z)=\prod_{m\ge1}\frac1{(1+\alpha_m z)(1+\alpha_m z^{-1})}
\]
on all \(2n\)-th roots of unity. For a single \(\alpha\in(0,1)\), the discrete inverse Fourier coefficient at \(0\le j<2n\) is
\[
 b_\alpha(j)=\frac{(-1)^j(\alpha^j+\alpha^{2n-j})}
 {(1-\alpha^2)(1-\alpha^{2n})}.
\]
Indeed, the bi-infinite Laurent coefficients of \((1+\alpha z)^{-1}(1+\alpha z^{-1})^{-1}\) are \((-\alpha)^{|j|}/(1-\alpha^2)\); summing the aliases modulo \(2n\) gives this identity. Thus the checkerboard-twisted coefficients \(u_\alpha(j)=(-1)^j b_\alpha(j)\) are positive, symmetric, and **strictly decreasing** with \(d_{2n}(0,j)\) from zero through \(n\): the successive difference for \(0\le j<n\) is
\[
\alpha^j+\alpha^{2n-j}-\alpha^{j+1}-\alpha^{2n-j-1}
=(1-\alpha)(\alpha^j-\alpha^{2n-j-1})>0.
\]

We need one elementary cyclic-convolution fact. If \(u,v\) are nonnegative functions on \(\mathbb Z/(2n)\mathbb Z\), symmetric and nonincreasing with cyclic distance from zero, then so is \(u*v\). Moreover, if \(u\) is strictly decreasing and \(v(0)>v(1)\), their convolution is strictly decreasing. To see this, express each radial decreasing function as a nonnegative combination of indicators of centered cyclic balls \(B_r=\{j:d_{2n}(j,0)\le r\}\), \(0\le r\le n\). The convolution of two ball indicators is \(|B_r\cap(j+B_s)|\), which is nonincreasing as the shorter center separation \(j\) runs from zero to \(n\). Here is an explicit check of that fact. For \(r,s<n\), put \(L=2n\) and let \(T(h)\) for nonnegative integer \(h\) equal \(\min(2r+1,2s+1)\) if \(h\le|r-s|\), \(r+s+1-h\) if \(|r-s|<h\le r+s\), and zero otherwise. Then the intersection count is \(T(j)+T(L-j)\) for \(0\le j\le n\). The first term decreases from a plateau, and the second can increase only once \(j\ge L-(r+s)\ge|r-s|\), where the first term decreases by exactly the amount of the possible increase. Hence their sum never increases. If either ball has radius \(n\), its indicator is constant. For strictness, write \(v=\epsilon\,\mathbf1_{\{0\}}+v_0\) with \(\epsilon=v(0)-v(1)>0\) and \(v_0\) nonnegative radial nonincreasing; then \(u*v=\epsilon u+u*v_0\) is strictly decreasing.

On an even cycle, the parity character \((-1)^j\) respects cyclic convolution: \((-1)^j(a*b)(j)=(((-1)^\cdot a)*((-1)^\cdot b))(j)\). Consequently each finite product of inverse factors has strictly positive, symmetric, strictly distance-decreasing twisted inverse Fourier coefficients. For the infinite product, fix a sufficiently large finite initial product and group all remaining factors into a tail. Since \(\sum_{m>M}\alpha_m\to0\), the twisted Fourier coefficient vector of the tail converges in \(\ell^1\) to the point mass at zero as \(M\to\infty\) (one may bound each factor's deviation from the point mass by \(O(\alpha_m/(1-\alpha_m)^2)\)). Its exact limit is a positive, symmetric, nonincreasing function by convergence of the finite tail products; for sufficiently large \(M\) it satisfies \(v(0)>v(1)\). Applying the preceding strict-convolution argument to the first \(M\) factors and this tail proves that the infinite-product doubled-cycle Fourier coefficients have the form
\[
\widehat F_{2n}(j)=(-1)^j a_{d_{2n}(0,j)},
\qquad a_0>a_1>\cdots>a_n>0.
\]

**Step 3: fold the doubled cycle to the requested sample size.** Since the set of \(n\)-th roots is the even-indexed subset of the \(2n\)-th roots, inverse discrete Fourier transformation yields
\[
Q^{(n,t)}_{0j}=C_t^{-1}\big(\widehat F_{2n}(j)+\widehat F_{2n}(j+n)\big)
= C_t^{-1}(-1)^j\big(a_{d_{2n}(0,j)}+(-1)^n a_{d_{2n}(0,j+n)}\big).
\]
For \(0\le j<n\), the two distances on the right are respectively \(j\) and \(n-j\). Thus
\[
Q^{(n,t)}_{0j}=C_t^{-1}(-1)^j\big(a_j+(-1)^n a_{n-j}\big).
\]
If \(n\) is even, both amplitudes add, so the sign is \((-1)^j=(-1)^{d_n(0,j)}\), including the antipodal case. If \(n\) is odd, the strict decrease of the \(a\)'s shows that \(a_j-a_{n-j}\) is positive for \(j<n/2\) and negative for \(j>n/2\). Therefore its sign cancels the parity discrepancy across the shorter arc, yielding precisely \((-1)^{d_n(0,j)}\). Since the precision is circulant, translating indices gives the assertion for all pairs. Nonvanishing is strict. For a real nondegenerate Gaussian vector, two distinct coordinates are conditionally independent given the others exactly when the corresponding precision entry is zero; the sign of their conditional partial correlation is the negative of that entry's sign. This completes the proof.

## Verification
The included standalone `checker.py` (run as `python checker.py`, requires SymPy and mpmath) independently evaluates exact rational inverses for finite products, a complete rational family of centered-ball circular-convolution tests, and high-precision Poisson/Fourier formulas for the actual heat covariance. Its bundled output `checker.log` records **39,574 passing checks**, divided into 3,759 exact rational-spectrum comparisons, 33,626 discrete arc-convolution tests, and 2,189 high-precision heat-covariance checks. The infinite-family theorem is proved in the preceding steps, not by numerical sampling. Small near-zero floating-point terms are excluded from sign *testing* when below the declared numerical precision threshold; this exclusion plays no role in the proof.

## Relationship to prior work
Borovitskiy, Terenin, Mostowsky and Deisenroth (arXiv:2006.10160, first publicly submitted June 17, 2020) give the spectral construction of squared-exponential and Matérn kernels on compact manifolds, with the circular squared-exponential kernel represented by a Jacobi theta series. Their setting covers exactly the covariance family used here, but the inspected main text and circle appendix do not give the strict all-size inverse sign classification. Da Costa, Mostajeran and Ortega (arXiv:2302.10623) study the *intrinsic geodesic squared-distance* Gaussian on the circle; that is a different kernel and lacks positivity for all finite configurations. Belton, Guillot, Khare and Putinar (arXiv:2006.16213) study total positivity and Pólya frequency functions, providing important general background, but their inspected work does not state this cyclic heat covariance precision classification. Standard theta-factorization and cyclic convolution are explicitly used, not claimed as new. Existing results for sampled finite-order circular Matérn fields do establish an analogous sign pattern for a different Fourier-weight family and do not imply the present infinite-smoothness heat-kernel assertion by specialization.

## Limitations
The sign theorem is restricted to exactly equispaced samples on the unit circle and to the heat kernel with strictly positive parameter. It does not give magnitudes or sharp asymptotic decay of the precision entries. General Pólya-frequency/variation-diminishing theory may contain equivalent implications not identified in the checked sources; historical priority is therefore provisional pending independent literature verification. Numerical signs near extreme parameter limits can be ill-conditioned, but the analytic inequalities are strict. Independent mathematical auditing has not been performed.

## References
- V. Borovitskiy, A. Terenin, P. Mostowsky and M. P. Deisenroth, *Matérn Gaussian processes on Riemannian manifolds*, arXiv:2006.10160, publicly submitted 2020-06-17, https://arxiv.org/abs/2006.10160 .
- N. Da Costa, C. Mostajeran and J.-P. Ortega, *The Gaussian kernel on the circle and spaces that admit isometric embeddings of the circle*, arXiv:2302.10623, publicly submitted 2023-02-21, https://arxiv.org/abs/2302.10623 .
- A. Belton, D. Guillot, A. Khare and M. Putinar, *Totally positive kernels, Pólya frequency functions, and their transforms*, arXiv:2006.16213, https://arxiv.org/abs/2006.16213 .
- Jacobi triple-product identity and Poisson summation, classical Fourier analysis (used as established identities, not claimed as discoveries).
