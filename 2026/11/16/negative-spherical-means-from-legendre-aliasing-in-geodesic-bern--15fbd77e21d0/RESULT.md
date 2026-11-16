# Negative spherical means from Legendre aliasing in geodesic Bernstein sampling

## Finding

For each integer \(n\ge3\), let \(P_k\) denote the ordinary Legendre polynomial normalized by \(P_k(1)=1\). Define the positive-definite zonal kernel \(f_n(\theta)=P_{2n-2}(\cos\theta)\) on the unit two-sphere, where \(0\le\theta\le\pi\) is geodesic angle. Apply the classical degree-\(n\) Bernstein operator in this *angular*, not dot-product, variable:

\[
H_n(\theta)=\sum_{j=0}^{n}\binom nj
 (\theta/\pi)^j(1-\theta/\pi)^{n-j}
 P_{2n-2}(\cos(\pi j/n)).
\]

**Theorem (angular aliasing and a negative spherical mean).** For each fixed \(\theta\in(0,\pi)\), uniformly as \(\theta\) ranges through any compact subinterval,

\[
\sqrt n\,H_n(\theta)\longrightarrow
\frac{\cos(3\theta/2+\pi/4)}{\sqrt{\pi\sin\theta}}.
\]

The normalized constant spherical-harmonic coefficient of \(H_n\), namely

\[
a_{0,n}=\frac12\int_0^\pi H_n(\theta)\sin\theta\,d\theta,
\]

has the sharp limit

\[
\boxed{\displaystyle
\lim_{n\to\infty}\sqrt n\,a_{0,n}
 =-\frac{\sqrt\pi}{4\sqrt2}<0.}
\]

Consequently, for **every sufficiently large integer \(n\)**, the degree-\(n\) geodesic Bernstein operator does not preserve zonal positive definiteness **on the two-sphere itself**: the input \(f_n\) is positive definite on \(S^2\), but its output \(H_n\) is not. The statement does not specify the least such \(n\).

## Assumptions and scope

The sphere is \(S^2=\{x\in\mathbb R^3:|x|=1\}\), with geodesic angle \(\theta=\arccos(x\cdot y)\). Positive definite means that \((f(\arccos(x_i\cdot x_j)))_{i,j}\) is positive semidefinite for every finite point configuration; strict positivity is not required. The Bernstein degree \(n\) and the Legendre input degree \(2n-2\) both vary. The angular sampling nodes are exactly \(\pi j/n\), \(0\le j\le n\). The Schoenberg/Legendre constant coefficient is \(a_0=(1/2)\int_0^\pi h(\theta)\sin\theta\,d\theta\); this normalization is crucial. Only the two-sphere is asserted in the negative-mean conclusion. The interior profile is not claimed uniform up to the endpoints.

## Proof

**1. Input positive definiteness.** By the spherical-harmonic addition formula, \(P_m(x\cdot y)\) is the Gram kernel of the degree-\(m\) spherical-harmonic evaluation map, up to a positive scalar, for each integer \(m\ge0\). Thus each input \(f_n\), where \(m=2n-2\), is positive semidefinite on every finite configuration on \(S^2\).

**2. Sampling aliasing.** Fix \(0<\delta<\pi/2\). The classical interior Darboux asymptotic for Legendre polynomials, uniformly for \(u\in[\delta,\pi-\delta]\), is

\[
P_m(\cos u)=\sqrt{\frac{2}{\pi(m+1/2)\sin u}}
 \cos((m+1/2)u-\pi/4)+O_\delta(m^{-3/2}).
\]

At the grid angle \(u=\pi j/n\) and \(m=2n-2\), the oscillatory phase is exactly

\[
(m+1/2)u-\pi/4=2\pi j-3u/2-\pi/4.
\]

Hence, uniformly over grid points in any fixed interior interval,

\[
\sqrt n\,P_{2n-2}(\cos u)
 \longrightarrow g(u):=\frac{\cos(3u/2+\pi/4)}{\sqrt{\pi\sin u}}.
\]

For fixed \(\theta\in(0,\pi)\), write \(J_n\sim\mathrm{Binomial}(n,\theta/\pi)\). Then \(H_n(\theta)=\mathbb E[P_{2n-2}(\cos(\pi J_n/n))]\). On an interior compact interval, a binomial concentration bound makes the probability of a grid point outside a slightly wider interior interval exponentially small, while \(|P_m(t)|\le1\) on \([-1,1]\). Since \(J_n/n\to\theta/\pi\) in probability, the preceding uniform grid limit and continuity of \(g\) imply the stated compact-uniform limit for \(\sqrt n H_n(\theta)\). This also identifies the phase alias, rather than merely its magnitude.

**3. Exact beta-weight rewriting of the spherical mean.** Let \(b_{n,j}(t)=\binom nj t^j(1-t)^{n-j}\). The beta density \((n+1)b_{n,j}(t)\) is that of a random variable \(U_{n,j}\sim\operatorname{Beta}(j+1,n-j+1)\). Thus exact finite-sum interchange gives

\[
a_{0,n}=\frac{\pi}{2(n+1)}
 \sum_{j=0}^{n}P_{2n-2}(\cos(\pi j/n))
 \mathbb E[\sin(\pi U_{n,j})].
\]

The beta mean is \((j+1)/(n+2)\), deviating from \(j/n\) by at most \(1/(n+2)\); the beta variance is at most \(1/[4(n+3)]\). Taylor's theorem and the uniform first- and second-derivative bounds for sine give

\[
\sup_{0\le j\le n}
\left|\mathbb E\sin(\pi U_{n,j})-\sin(\pi j/n)\right|=O(n^{-1}).
\]

Since \(|P_{2n-2}|\le1\), the accumulated difference after the prefactor \(\pi/[2(n+1)]\) is \(O(n^{-1})\). Therefore

\[
\sqrt n\,a_{0,n}=
 \frac{\pi}{2(n+1)}\sum_{j=0}^n
 \sqrt n\,P_{2n-2}(\cos\theta_j)\sin\theta_j+o(1),
\qquad \theta_j=\pi j/n.
\]

**4. Endpoint domination and exact constant.** The standard uniform Legendre Bernstein bound \(|P_m(\cos u)|\le C(m\sin u)^{-1/2}\) for \(0<u<\pi\), together with \(m=2n-2\), implies

\[
\left|\sqrt n\,P_{2n-2}(\cos\theta_j)\sin\theta_j\right|
 \le C'\sqrt{\sin\theta_j}\quad(1\le j<n).
\]

The terms at both endpoints vanish because of the sine factor. The interior Darboux limit, this integrable endpoint envelope, and splitting the Riemann sum into a fixed interior plus short endpoint pieces show

\[
\lim_{n\to\infty}\sqrt n\,a_{0,n}
=\frac1{2\sqrt\pi}\int_0^\pi
 \sqrt{\sin u}\cos(3u/2+\pi/4)\,du.
\]

With \(v=u-\pi/2\), the integrand's oscillatory factor is \(-\cos(3v/2)\), and the classical beta cosine integral evaluates to

\[
\int_{-\pi/2}^{\pi/2}\sqrt{\cos v}\cos(3v/2)\,dv
=\frac{\pi}{2\sqrt2}.
\]

It follows that the limit equals \(-\sqrt\pi/(4\sqrt2)\), strictly negative.

**5. Spherical obstruction.** By the Schoenberg criterion on \(S^2\), every continuous zonal positive-definite kernel has nonnegative Legendre coefficients, especially its degree-zero coefficient. Equivalently, the constant spherical-harmonic sector of its integral operator must have nonnegative eigenvalue. The computed \(a_{0,n}<0\) for all sufficiently large \(n\) is therefore a direct obstruction on \(S^2\), completing the proof. \(\square\)

## Verification

A standalone `CHECK.py` evaluates the finite Bernstein sum independently by binomial weights, integrates the spherical mean using Gaussian quadrature, compares different quadrature orders, and tests the limiting interior profile and constant. It passed 28 supplementary numerical assertions in the packaged form. Representative values are \(a_{0,40}\approx-0.04041564294\), \(\sqrt{320}\,a_{0,320}\approx-0.30757120860\), and the proven limit is \(-0.313328534328875\ldots\). The calculations support but do not establish the limit, eventual negativity, or optimal finite threshold; these follow only as stated from the analysis above. The checker requires NumPy and SciPy and no network access.

## Relationship to prior work

Otten, Nguyen and Watts (first public preprint 2026-08-05) prove that angular Bernstein interpolation preserves positive definiteness on the circle for all degrees. Their discussion of failure on \(S^2\) concerns the **different affine Bernstein operator in dot-product coordinates**, not the angular operator analyzed here. A published sharp dimension-degree frontier for affine Bernstein kernels likewise does not cover this theorem. A related angular-Bernstein dimension-lifting result shows that degrees at least four can fail to yield a kernel positive definite on **all** spheres simultaneously. That does not imply non-positive-definiteness on \(S^2\) for any such output: the present negative *degree-zero Legendre coefficient* supplies the missing fixed-sphere obstruction, with its exact aliasing profile and decay constant. The classical Darboux Legendre asymptotic, uniform Bernstein bound and Schoenberg characterization are used as established tools rather than claimed as new. An older equivalent angular-aliasing calculation remains possible.

## Limitations

The theorem proves non-preservation on \(S^2\) only for all sufficiently large Bernstein degrees; it does not classify smaller degrees or assert a sharp first failing degree. The input Legendre degree increases with \(n\), so this is not a counterexample for a single fixed input under all fine approximants; classical Bernstein approximation still converges for each fixed continuous input. The normalized monopole limit is exact but no effective cutoff or error bound in \(n\) is claimed. The local profile excludes the endpoints, where the Legendre scaling differs. The conclusion is about positive semidefinite Gram kernels, not strict positive definiteness. There has been no independent mathematical audit.

## References

1. M. Otten, N. Nguyen and T. W. Watts, *Preservation of Positive-Definiteness by Bernstein Operators on the Circle*, arXiv:2608.04836v1, publicly posted 2026-08-05, especially Theorem 1.2 and Section 4. https://arxiv.org/abs/2608.04836
2. I. J. Schoenberg, *Positive definite functions on spheres*, Duke Mathematical Journal 9 (1942), 96–108. https://doi.org/10.1215/S0012-7094-42-00908-6
3. G. Szegő, *Orthogonal Polynomials*, 4th edition, American Mathematical Society, 1975, classical interior Legendre asymptotics and Bernstein-type bounds; see also NIST Digital Library of Mathematical Functions, §18.15. https://dlmf.nist.gov/18.15
4. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, Bernoulli 19 (2013), 1327–1349; arXiv:1111.7077. https://arxiv.org/abs/1111.7077
5. *Sharp dimension–degree frontier and infinite-sphere lift for affine Bernstein kernels*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-dimension-degree-frontier-and-infinite-sphere-lift-for-aff--3785c4062726
6. *A sharp degree frontier for Hilbert-sphere lifting by geodesic Bernstein sampling*, 2026, prior unpublished mathematical research record; comparison limited to its mathematical claim.
