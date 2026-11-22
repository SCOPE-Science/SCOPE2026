# Sharp affine anisotropy cone for Poisson covariance kernels on spheres

## Finding
Fix an integer \(d\ge 2\), a Poisson scale \(0<r<1\), a real scalar \(a\), and a vector \(v\in\mathbb R^d\). On \(\mathbb S^{d-1}\), let \(\sigma\) denote normalized surface measure and define
\[
P_r(x,y)=\frac{1-r^2}{(1-2r\langle x,y\rangle+r^2)^{d/2}},\qquad
K_{r,a,v}(x,y)=P_r(x,y)\bigl(a+\langle v,x+y\rangle\bigr).
\]
**Theorem (complete affine cone).** The following are equivalent:

1. \(K_{r,a,v}\) is positive semidefinite on every finite subset of \(\mathbb S^{d-1}\), for arbitrary complex coefficients.
2. \(a\ge (1+r)\lVert v\rVert/\sqrt r\).

Every nonzero kernel in this cone is strictly positive definite on every finite set of pairwise distinct sites, **including the sharp boundary** \(a=(1+r)\lVert v\rVert/\sqrt r\). The only positive-semidefinite member that is not strictly positive definite is the zero kernel \(a=0\), \(v=0\).

There is an exact dimension-independent Poisson-bridge factorization. Writing \(s=\sqrt r\),
\[
K_{r,a,v}(x,y)=\int_{\mathbb S^{d-1}}P_s(x,z)P_s(y,z)
\Bigl(a+\frac{1+s^2}{s}\langle v,z\rangle\Bigr)\,d\sigma(z).
\]
Equivalently, the first moment of the positive Poisson-bridge density is
\[
\int_{\mathbb S^{d-1}}z P_s(x,z)P_s(y,z)\,d\sigma(z)
=\frac{s}{1+s^2}(x+y)P_{s^2}(x,y).
\]
The positivity threshold is dimension-free, despite the dimension-dependent Poisson kernel. At the boundary, the factorization weight vanishes at exactly one point when \(v\ne0\), but no finite-site interpolation singularity occurs.

## Assumptions and scope
The sphere is the Euclidean unit sphere in \(\mathbb R^d\), \(d\ge2\). All integrals use **probability** surface measure; this normalization gives the Poisson-semigroup identity \(T_sT_t=T_{st}\). Parameters \(a\) and \(v\) are real, with no sign restriction on \(a\) imposed in advance. The result concerns positive semidefiniteness of every finite Gram matrix, not merely pointwise nonnegativity of the kernel. Strict positive definiteness means positive Gram quadratic form for all nonzero complex coefficients at pairwise distinct sites. Neither endpoint \(r=0\) nor \(r=1\) is covered.

## Proof
**1. Degree selection and Poisson eigenvalues.** Let \(\mathcal H_n\) be the real or complex spherical harmonics of exact degree \(n\). The probability-normalized spherical Poisson operator
\[
(T_t f)(x)=\int_{\mathbb S^{d-1}}P_t(x,y)f(y)\,d\sigma(y)
\]
acts by \(t^n\) on \(\mathcal H_n\) for every integer \(n\ge0\) and \(0<t<1\). Hence \(T_s^2=T_{s^2}\) and \(T_s\) is self-adjoint, injective, compact, with dense range.

For a fixed \(v\in\mathbb R^d\), multiplication \(M_v f(z)=\langle v,z\rangle f(z)\) sends \(\mathcal H_n\) into \(\mathcal H_{n-1}\oplus\mathcal H_{n+1}\), with the negative-degree summand omitted. To verify this critical selection rule without relying on a Clebsch–Gordan table, extend a degree-\(n\) harmonic to its homogeneous harmonic polynomial \(H_n\) on \(\mathbb R^d\). For \(n\ge1\), the decomposition
\[
\langle v,X\rangle H_n(X)=
\underbrace{\left(\langle v,X\rangle H_n(X)-\frac{|X|^2}{2n+d-2}\partial_vH_n(X)\right)}_{\text{harmonic of degree }n+1}
+\frac{|X|^2}{2n+d-2}\partial_vH_n(X)
\]
uses \(\Delta(\langle v,X\rangle H_n)=2\partial_vH_n\) and \(\Delta(|X|^2\partial_vH_n)=2(2n+d-2)\partial_vH_n\). After restriction to \(|X|=1\), the second summand has degree \(n-1\). For \(n=0\), multiplication produces degree one only.

**2. Exact operator intertwining.** Relative to the mutually orthogonal decomposition into \(\mathcal H_n\), all matrix blocks of \(M_v\) vanish unless the two degrees differ by one. When \(|m-n|=1\), its block in \(T_sM_vT_s\) has scalar coefficient \(s^{m+n}\), while the same block in \(M_vT_{s^2}+T_{s^2}M_v\) has scalar coefficient \(s^{2m}+s^{2n}=s^{m+n}(s+s^{-1})\). Thus, as bounded operators,
\[
T_sM_vT_s=\frac{s}{1+s^2}\bigl(M_vT_{s^2}+T_{s^2}M_v\bigr).
\]
The integral operator of \(K_{r,a,v}\) is \(aT_{s^2}+M_vT_{s^2}+T_{s^2}M_v\). Consequently it factors **exactly** as
\[
T_s\left(aI+(s+s^{-1})M_v\right)T_s.
\]
Both sides have continuous integral kernels because the Poisson eigenvalues decay geometrically; comparing kernels gives the factorization in the finding. Taking \(a=0\) and varying \(v\) yields the vector-valued bridge moment identity.

**3. Necessity and sufficiency of the cone.** Define the continuous multiplier \(W(z)=a+(s+s^{-1})\langle v,z\rangle\). Its minimum is \(a-(s+s^{-1})\lVert v\rVert\). If this is nonnegative, the factorized quadratic form is an integral of \(W(z)|T_sf(z)|^2\), so every finite Gram form is nonnegative.

Conversely suppose the minimum is negative. There is an open spherical cap on which \(W<0\). Select a nonzero smooth function supported inside that cap, and approximate it in \(L^2(d\sigma)\) by a spherical polynomial \(g\), close enough that \(\int W|g|^2\,d\sigma<0\). Since \(T_s\) is invertible on each finite sum of \(\mathcal H_n\), there is a spherical polynomial \(f\) with \(T_sf=g\). The quadratic form of the continuous integral operator of \(K\) on \(f\) is strictly negative. By continuity and approximation of double integrals by finite quadrature sums, some finite weighted Gram quadratic form is strictly negative. Hence the kernel is not positive semidefinite. This proves the claimed if-and-only-if without extrapolating from finite numerical tests.

**4. Strict finite-site positivity at the boundary.** For a nonzero finite complex atomic measure \(\mu=\sum_{j=1}^N c_j\delta_{x_j}\) at distinct sites, let \(h(z)=\int P_s(z,x)\,d\mu(x)\). Its continuous spherical-harmonic coefficients are \(s^n\) times those of \(\mu\). If \(h\) vanished identically, every spherical-harmonic moment of \(\mu\) would vanish; density of polynomial restrictions in continuous functions on the sphere would give \(\mu=0\), a contradiction. Thus \(h\) is nonzero and continuous. For any nonzero member of the cone, \(W\ge0\) and its zero set is either empty or a singleton, so \(\int W|h|^2\,d\sigma>0\). This integral is exactly the finite Gram form. The zero kernel is the sole exception.

## Verification
Run `python3 check_poisson.py` with Python 3, NumPy and SciPy installed. The standalone checker verifies 1,681 exact rational Fourier-block identities on the circle at \(s=1/2\), an exact negative quadratic-form witness just beyond the claimed threshold, 24 independent spherical Poisson-bridge quadratures using Legendre and azimuthal integration, and 36 circle quadratures. The maximum absolute residuals in the latter two groups were \(4.11\times10^{-14}\) and \(1.51\times10^{-14}\), respectively.

The exact negative certificate uses \(r=1/4\), \(a=1\), \(v=(9/20,0)\) on the circle (in standard Cartesian coordinates). Setting \(s=1/2\) and taking a normalized degree-six alternating Dirichlet polynomial concentrated at the negative pole, the factorized quadratic form equals \(-1/26\). This is a finite spherical-polynomial witness of failure; the analytic proof above supplies necessity in every dimension and for all parameters.

## Relationship to prior work
Buhmann and Jäger's 2021 preprint, *Strict positive definiteness of convolutional and axially symmetric kernels on d-dimensional spheres* (arXiv:2105.02586; subsequently Journal of Fourier Analysis and Applications 28:40, 2022), studies block coefficient positivity of axially symmetric kernels. Its Theorem 2 and Proposition 1 supply abstract tests for all such kernels; they do **not** state the explicit affine-Poisson parameter cone or the Poisson-bridge moment identity. The present proof makes a specific infinite matrix test tractable by exact degree-one intertwining.

Guella and Jäger's *Strictly positive definite non-isotropic kernels on two-point homogeneous manifolds: the asymptotic approach* (arXiv:2205.07396; subsequently Positivity 28:4, 2024) focuses on diagonal harmonic coefficient series and positive support conditions; the present kernel has genuine adjacent-degree off-diagonal terms.

The indexed *Sharp harmonic-modulation cutoff and polygonal singularities for circle Poisson covariances* studies \(P_r(\theta-\phi)[1+\varepsilon\cos(k(\theta+\phi))]\). Its Fourier couplings change frequency indices by \(2k\) and produce a special singular polygon at its boundary. The current *coordinate-affine* perturbation couples adjacent harmonic degrees, works in every dimension, and is strictly positive on finite sets even at its boundary. Neither statement implies the other by identifying parameters or taking a corollary.

The 2024 work of Emery, Jäger and Porcu on axially symmetric space-time kernels was also located, but its complete text was unavailable for direct theorem-by-theorem comparison. Its accessible description concerns spectral and constructive classes in a broader space-time setting, and any concealed exact equivalent is a residual priority risk.

## Limitations
The result is for affine dependence on the two spatial locations and the classical Poisson coefficient progression. It does not classify higher-degree anisotropy, arbitrary radial spectral sequences, or temporally varying covariances. At the cone boundary the integral multiplier is not bounded below by a positive constant, even though every finite distinct-site Gram matrix is strictly positive. An exact first-priority claim is not made: relevant published records and accessible full texts were compared, while unindexed precedents and the inaccessible space-time paper remain possible overlaps. There has been no independent mathematical audit.

## References
1. M. Buhmann and J. Jäger, *Strict positive definiteness of convolutional and axially symmetric kernels on d-dimensional spheres*, first public preprint 2021-05-06, arXiv:2105.02586, https://arxiv.org/abs/2105.02586; full-text version https://link.springer.com/article/10.1007/s00041-022-09913-x.
2. J. C. Guella and J. Jäger, *Strictly positive definite non-isotropic kernels on two-point homogeneous manifolds: the asymptotic approach*, 2022 preprint arXiv:2205.07396, https://arxiv.org/abs/2205.07396; full text https://link.springer.com/article/10.1007/s11117-023-01022-3.
3. *Sharp harmonic-modulation cutoff and polygonal singularities for circle Poisson covariances*, indexed 2026 finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-harmonic-modulation-cutoff-and-polygonal-singularities-for--0f4219b7a6a9.
4. X. Emery, J. Jäger and E. Porcu, *Positive semidefinite kernels that are axially symmetric on the sphere and stationary in time: spectral and semi-spectral theory, and constructive approaches*, Stochastic Environmental Research and Risk Assessment 38 (2024), 2315–2329, https://doi.org/10.1007/s00477-024-02681-8 (abstract compared; full text not inspected).
