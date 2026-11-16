# Sharp axial tilts of spherical Poisson covariances: a dimension-free positivity threshold and universal critical kernels

## Finding

Let \(d\ge2\) be an integer, let \(\sigma\) be normalized surface measure on \(S^d\subset\mathbb R^{d+1}\), let \(v\in S^d\), and let \(0<r<1\). Define
\[
\Pi_r(x,y)=\frac{1-r^2}{(1-2r\,x\cdot y+r^2)^{(d+1)/2}},\qquad K_{r,\varepsilon,v}(x,y)=\Pi_r(x,y)[1+\varepsilon(v\cdot x+v\cdot y)]
\]
for real \(\varepsilon\). Set \(\theta=\varepsilon(1+r)/\sqrt r\). Then:

**(i) Sharp positivity.** The continuous real symmetric kernel \(K_{r,\varepsilon,v}\) is positive semidefinite for every finite configuration in \(S^d\) if and only if
\[
|\varepsilon|\le\frac{\sqrt r}{1+r},\quad\text{equivalently }|\theta|\le1.
\]
Moreover the sharp (in the sense of every finite signed configuration) quadratic-form bounds are
\[
(1-|\theta|)\Pi_r\preceq K_{r,\varepsilon,v}\preceq(1+|\theta|)\Pi_r.
\]
At either endpoint \(|\theta|=1\), no strictly positive constant can replace the zero lower constant. The naturally preconditioned covariance operator has spectrum exactly \([1-|\theta|,1+|\theta|]\).

**(ii) Critical universality.** For every \(|\theta|\le1\), including both equality cases, the kernel is strictly positive definite on every finite set of distinct points and \(C(S^d)\)-universal: its reproducing-kernel Hilbert space is dense in \(C(S^d)\) in the uniform norm.

**(iii) Sharp finite-band diagnostic on \(S^2\).** Let \(\mathcal H_{\le L}\) be the direct sum of spherical harmonics of degrees zero through \(L\). For \(L\ge1\), the covariance quadratic form restricted to \(\mathcal H_{\le L}\) is nonnegative if and only if
\[
|\theta|\le\frac{1}{\xi_{L+1}},
\]
where \(\xi_{L+1}\in(0,1)\) is the largest zero of the classical Legendre polynomial \(P_{L+1}\). The degree-zero restriction is always positive. As \(L\to\infty\), \(\xi_{L+1}\uparrow1\), so each fixed finite-band test permits an interval of supercritical parameters that the full kernel excludes.

**(iv) Explicit positive-valued but indefinite witness.** On \(S^2\), put \(r=1/4\) and \(\varepsilon=9/20\). Then \(K_{r,\varepsilon,v}(x,y)>0\) pointwise for all \(x,y\), yet some finite Gram matrix is indefinite. An explicit finite-harmonic witness has preconditioned angular polynomial \(g(v\cdot z)=(1-v\cdot z)^9\), whose normalized weighted energy equals \(-1/80\).

## Assumptions and scope

All spheres carry normalized surface probability, so \(\int\Pi_s(x,z)\,d\sigma(z)=1\) and \(\Pi_s*\Pi_t=\Pi_{st}\) for \(0<s,t<1\). Positivity is required for all finite signed complex atomic measures, not just pointwise positivity or a fixed harmonic cutoff. The operator \(T_s\) on \(L^2(\sigma)\) is defined by \((T_sf)(x)=\int\Pi_s(x,y)f(y)\,d\sigma(y)\). The kernel is axially invariant about \(v\) but is nonstationary when \(\varepsilon\ne0\): its diagonal depends on latitude. The preconditioned operator is the bounded extension of \(T_r^{-1/2}T_KT_r^{-1/2}\) initially defined on finite harmonic sums (the inverse is not claimed to be bounded on all \(L^2\)).

## Proof

**Step 1: Exact Poisson factorization.** Every harmonic of degree \(\ell\) is an eigenfunction of \(T_s\) with eigenvalue \(s^\ell\), and finite spherical-harmonic sums are dense in \(L^2(\sigma)\). Let \(M_v\) be multiplication by \(t(z)=v\cdot z\), a self-adjoint operator with \(\|M_v\|=1\). Multiplication by a degree-one coordinate takes a degree-\(\ell\) harmonic to components only of degrees \(\ell-1\) and \(\ell+1\). This follows by decomposing the homogeneous polynomial \((v\cdot z)H_\ell(z)\) into its homogeneous harmonic and \(|z|^2\)-times-harmonic parts, then restricting to \(S^d\). Consequently, on every pair of harmonic degrees coupled by \(M_v\),
\[
T_r^{-1/2}(M_vT_r+T_rM_v)T_r^{-1/2}
=(r^{-1/2}+r^{1/2})M_v.
\]
Thus, first on finite harmonic sums and then on all of \(L^2(\sigma)\),
\[
T_K=T_{\sqrt r}(I+\theta M_v)T_{\sqrt r}.
\]
Equating continuous integral kernels gives the exact pointwise factorization
\[
\boxed{K_{r,\varepsilon,v}(x,y)
=\int_{S^d}\Pi_{\sqrt r}(x,z)[1+\theta(v\cdot z)]\Pi_{\sqrt r}(z,y)\,d\sigma(z).}
\]
Indeed, all expansions converge absolutely for fixed \(r<1\), and both kernels are continuous.

**Step 2: Necessity and optimality.** The spectrum of \(M_v\), as multiplication by the latitude on \(L^2(S^d,\sigma)\), is exactly \([-1,1]\). Both open polar caps have positive measure, so essential endpoints are \(\pm1\); neither endpoint has an eigenvector because the poles have measure zero. The range of \(T_{\sqrt r}\) contains every finite harmonic sum and is dense in \(L^2\). Hence \(\langle f,T_Kf\rangle\ge0\) for every \(f\in L^2\) if and only if \(1+\theta t\ge0\) almost everywhere, precisely \(|\theta|\le1\). On a compact space, the continuous kernel is positive semidefinite on all finite atomic configurations if and only if its continuous integral quadratic form is nonnegative for all continuous test densities: one direction uses approximating the integral by finite Riemann sums, the other uses finite atomic measures and continuity. This proves the equivalence and the sharpness of the lower and upper Loewner constants on finite atomic measures. The preconditioned quadratic form is exactly \(I+\theta M_v\); its spectrum is the announced interval. At \(|\theta|=1\), cap-supported test functions concentrating near the vanishing pole force the quotient to zero, so there is no positive uniform lower bound.

**Step 3: Universality and finite-site strictness at equality.** For an arbitrary finite complex Borel measure \(\mu\) on \(S^d\), let
\[
F_\mu(z)=\int_{S^d}\Pi_{\sqrt r}(z,x)\,d\mu(x).
\]
It is continuous and therefore in \(L^2(\sigma)\). Factorization yields
\[
\iint K_{r,\varepsilon,v}(x,y)\,d\mu(x)\,d\overline\mu(y)
=\int_{S^d}(1+\theta t(z))|F_\mu(z)|^2\,d\sigma(z).
\]
For \(|\theta|\le1\), the weight is positive almost everywhere, including at equality since its only zeros are one pole of zero surface measure. Therefore zero energy implies \(F_\mu=0\) in \(L^2\). Each degree-\(\ell\) spherical-harmonic coefficient of \(F_\mu\) is \(r^{\ell/2}\) times the corresponding coefficient of \(\mu\), so all spherical-harmonic moments of \(\mu\) vanish. Density of spherical polynomials in \(C(S^d)\) implies \(\mu=0\). Every nonzero finite signed complex measure thus has strictly positive energy. In particular every nonzero atomic configuration has positive Gram energy. A continuous kernel on a compact space has dense RKHS in \(C(S^d)\) exactly when no nonzero finite signed measure annihilates its RKHS (Riesz representation and Hahn–Banach); such an annihilator has zero kernel energy. Therefore \(K\) is \(C(S^d)\)-universal at all admissible parameters.

**Step 4: Finite harmonic cutoff.** On \(S^2\) rotate \(v\) to the north pole and use the standard normalized complex spherical harmonics \(Y_{\ell m}\). Latitude multiplication preserves magnetic index \(m\) and has exactly the off-diagonal matrix coefficients
\[
\langle Y_{\ell+1,m},M_vY_{\ell m}\rangle
=\sqrt{\frac{(\ell+1)^2-m^2}{(2\ell+1)(2\ell+3)}}
\quad (\ell\ge|m|).
\]
The compression to degrees \(0,\ldots,L\) is a direct sum of real symmetric zero-diagonal tridiagonal blocks indexed by \(m\). Each \(|m|>0\) block has no more entries than, and each off-diagonal is bounded above by, the corresponding principal subpath of the \(m=0\) block. The variational principle together with entrywise positivity (or Perron–Frobenius) shows that the largest absolute eigenvalue of the full compression occurs in the zonal \(m=0\) block. Its off-diagonals are \((\ell+1)/\sqrt{(2\ell+1)(2\ell+3)}\); the three-term determinant recurrence is precisely the monic Legendre recurrence, so its characteristic polynomial is a positive scalar multiple of \(P_{L+1}\). Since the bipartite tridiagonal spectrum is symmetric, its norm equals \(\xi_{L+1}\). The compressed preconditioned form \(I+\theta P_{\le L}M_vP_{\le L}\) is therefore nonnegative exactly when \(|\theta|\xi_{L+1}\le1\). The largest roots tend to one, as the dense polynomial compressions of a norm-one multiplication operator approach its norm.

**Step 5: Rational supercritical witness.** On \(S^2\), \(t=v\cdot z\) is uniformly distributed on \([-1,1]\). For \(\theta>1\), choose \(g_m(t)=(1-t)^m\) and let \(f=T_{\sqrt r}^{-1}g_m\); \(f\) is a finite spherical-harmonic polynomial. Direct integration yields
\[
\frac{\int_{-1}^{1}(1+\theta t)|g_m(t)|^2dt}
{\int_{-1}^{1}|g_m(t)|^2dt}
=1-\theta\frac{m}{m+1}.
\]
This is negative for every integer \(m>1/(\theta-1)\). Negative \(\theta\) uses \(g_m(t)=(1+t)^m\). At \(r=1/4,\ \varepsilon=9/20\), one has \(\theta=9/8\) and \(m=9\), giving \(-1/80\). Meanwhile \(1+\varepsilon(t_x+t_y)\ge1-2(9/20)=1/10>0\), and \(\Pi_{1/4}>0\). Approximating the negative integral quadratic form of \(f\) by finite Riemann sums produces a finite negative Gram quadratic form. This exhibits the pointwise-positive but non-positive-definite phenomenon without relying on numerical extrapolation.

## Verification

The standalone Python 3 standard-library program `CHECKER.py` verifies the exact Legendre recurrence, 12 monic Jacobi characteristic-polynomial identities, the exact rational negative-energy witness, and four independent high-accuracy Poisson-factorization quadratures on \(S^2\). Execute `python3 CHECKER.py`; the expected ending is `PASS: 28 rational Legendre/Jacobi/witness checks; 4 Poisson factorization quadratures`. Those checks are finite corroboration; the harmonic factorization and measure-separation arguments above establish the infinite-dimensional assertions. No independent audit is claimed.

## Relationship to prior work

Jäger and Stallbauer's September 2026 deformation study motivates nonstationary axially symmetric spherical kernels and harmonic coupling. Its public abstract reports explicit coupling coefficients for a deformed isotropic kernel but not an exact sharp axial *amplitude* tilt threshold or the critical universality phenomenon established here. The full manuscript was inaccessible for comparison, so this is a bounded statement about the inspected abstract, not a claim that its full text excludes all equivalent results.

Buhmann and Jäger's earlier full-text study develops general sufficient strict-positivity criteria for nonisotropic and axially symmetric spherical kernels using spherical-harmonic coefficient matrices, including a uniform diagonal-dominance criterion (Theorem 3). It does not state the present exact necessary-and-sufficient threshold, factorization by a weighted Poisson operator, endpoint universality or Legendre-root cutoff. The classical Poisson-semigroup multiplier property and spherical-harmonic coordinate recurrence are existing ingredients used in this proof.

The closest indexed circle result, *Sharp harmonic-modulation cutoff and polygonal singularities for circle Poisson covariances* (2026), considers a sum-angle perturbation on \(S^1\) and develops a defect-bond threshold with polygonal finite-site singularities. Its result neither reduces to nor implies this higher-dimensional axial latitude tilt; in particular our critical kernels are finite-site strictly positive and universal. An indexed isotropic spherical Poisson–Legendre modulation classification instead preserves rotational invariance, whereas the present amplitude tilt has latitude-dependent diagonal. Emery, Jäger and Porcu (2024) give a more general spectral framework for axially symmetric spatio-temporal kernels. Only its public abstract was accessible; whether its full text contains a directly equivalent special case remains unresolved.

## Limitations

The theorem is restricted to \(d\ge2\), \(0<r<1\) and real first-order axial amplitude modulation. It does not classify arbitrary axially symmetric covariance perturbations, noncompact spaces, or singular limiting kernels as \(r\uparrow1\). The finite-degree Legendre result is stated for \(d=2\). The strongest originality uncertainty concerns the uninspected full texts of the motivating 2026 deformation study and Emery–Jäger–Porcu (2024), as well as potential earlier equivalent treatments of nonstationary Poisson semigroups. The result has had mathematical verification within this package, not an independent external scientific audit.

## References

1. Janin Jäger and Fabian Stallbauer, *A Deformation Approach to Axially Symmetric Kernels on the Sphere: Harmonic Coupling and Regularity*, arXiv:2609.27419 (first submitted 2026-09-23), https://arxiv.org/abs/2609.27419.
2. Martin Buhmann and Janin Jäger, *Strict Positive Definiteness of Convolutional and Axially Symmetric Kernels on d-Dimensional Spheres*, Journal of Fourier Analysis and Applications **28** (2022), article 40, DOI:10.1007/s00041-022-09913-x, https://link.springer.com/article/10.1007/s00041-022-09913-x; open-access preprint arXiv:2105.02586.
3. Xavier Emery, Janin Jäger and Emilio Porcu, *Positive semidefinite kernels that are axially symmetric on the sphere and stationary in time: spectral and semi-spectral theory, and constructive approaches*, Stochastic Environmental Research and Risk Assessment **38** (2024), 2315–2329, DOI:10.1007/s00477-024-02681-8, https://doi.org/10.1007/s00477-024-02681-8.
4. *Sharp harmonic-modulation cutoff and polygonal singularities for circle Poisson covariances*, published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-harmonic-modulation-cutoff-and-polygonal-singularities-for--0f4219b7a6a9.
