# An explicit second-chaos law for three-dimensional central simplicial depth

## Finding

Let \(Y_1,Y_2,\ldots\) be independent directions uniformly distributed on the unit two-sphere \(S^2\subset\mathbb R^3\). For every integer \(n\ge4\), define the empirical central simplicial depth
\[
D_n=\binom n4^{-1}\sum_{1\le i<j<k<\ell\le n}
\mathbf1\{0\in\operatorname{conv}(Y_i,Y_j,Y_k,Y_\ell)\}.
\]
Then \(\mathbb ED_n=1/8\) exactly. Define \(a_m=4^{-m}\binom{2m}{m}\), and for every \(m\ge0\),
\[
\lambda_m=\frac{a_{m+1}^2-a_m^2}{8(4m+3)}<0.
\]
If \(Q_m\) are independent chi-squared variables with \(4m+3\) degrees of freedom, then
\[
 n(D_n-1/8)\ \xrightarrow{\mathrm d}\ 
 Z=6\sum_{m=0}^{\infty}\lambda_m\bigl(Q_m-(4m+3)\bigr).
\]
The series converges both in \(L^2\) and almost surely; it has the equivalent, nonnegative-series representation
\[
Z=\frac34-6\sum_{m=0}^{\infty}|\lambda_m|Q_m.
\]
Its upper support endpoint is exactly \(3/4\), its lower support endpoint is unbounded, and it is not Gaussian. In particular,
\[
\lim_{n\to\infty}n^2\operatorname{Var}(D_n)
=\operatorname{Var}(Z)=\frac{9(\pi^2-8)}{8\pi^2}.
\]
Every conclusion holds without change for independent nonzero random vectors in \(\mathbb R^3\) whose directions are uniform on \(S^2\): their radial distributions need not be specified because positive radial rescaling preserves containment of the origin.

## Assumptions and scope

All samples are independent and directions have the normalized rotation-invariant probability law \(\sigma\) on \(S^2\). Continuity ensures that the origin lies on no random tetrahedral face with positive probability. The event uses the closed convex hull, but strict versus non-strict containment makes no difference almost surely. The asymptotic statements hold for integer \(n\to\infty\) with no thinning or parameter tuning. The result concerns a fixed central query point and a three-dimensional sample with uniform angular law, not arbitrary non-isotropic distributions or moving query points.

## Proof

**1. Conditional angular containment.** For distinct, nonantipodal fixed directions \(x,y\in S^2\), let \(\theta=\arccos\langle x,y\rangle\in(0,\pi)\). Let \(Z,W\) be independent uniform directions. The plane through \(0,x,y\) separates \(Z,W\) with probability \(1/2\). On this event their connecting segment intersects the plane at a point \(T\); rotational invariance around the normal to that plane makes the direction of \(T\) uniform on its unit circle. The origin belongs to \(\operatorname{conv}(x,y,Z,W)\) exactly when the ray \(-T\) is in the positive planar cone spanned by \(x,y\), whose opening angle is \(\theta\). Consequently
\[
 \Pr\{0\in\operatorname{conv}(x,y,Z,W)\mid x,y\}
 =\frac{\theta}{4\pi}.
\]
By rotational invariance, the one-vertex conditional expectation is constant and equals the unconditional value \(1/8\), also given by Wendel's formula for four symmetric directions in three dimensions. Thus the first-order Hoeffding projection vanishes, while the canonical second-order projection of the indicator kernel is
\[
h_2(x,y)=\frac{\arccos\langle x,y\rangle-\pi/2}{4\pi}.
\]
Its one-argument integrals vanish because the geodesic angle between fixed \(x\) and uniform \(Y\) has density \(\sin\theta/2\) on \([0,\pi]\).

**2. Spectrum.** The self-adjoint Hilbert--Schmidt integral operator \(Tf(x)=\int h_2(x,y)f(y)\,d\sigma(y)\) is rotationally invariant. By the Funk--Hecke identity, every degree-\(\ell\) real spherical harmonic is an eigenfunction with eigenvalue
\[
 \mu_\ell=\frac1{8\pi}\int_{-1}^{1}
 (\arccos t-\pi/2)P_\ell(t)\,dt
\]
and multiplicity \(2\ell+1\). Parity gives \(\mu_0=\mu_{2j}=0\). For \(\ell=2m+1\), integration by parts using
\( (2\ell+1)P_\ell=P_{\ell+1}'-P_{\ell-1}' \), and
\(\int_0^\pi P_{2j}(\cos t)\,dt=\pi a_j^2\), gives \(\mu_{2m+1}=\lambda_m\). In particular \(\lambda_0=-1/32\) and \(\lambda_1=-1/512\). Orthogonality and square integrability justify the spectral expansion and the convergence of its squared eigenvalue sum.

**3. Limit.** The order-four Hoeffding decomposition, using the zero first projection, is
\[
 D_n-1/8=6U_{n,2}(h_2)+4U_{n,3}(h_3)+U_{n,4}(h_4),
\]
where the three kernels are canonical and bounded. Canonical order-three and order-four terms have respective variances \(O(n^{-3})\) and \(O(n^{-4})\), so multiplication by \(n\) makes them vanish in \(L^2\). The standard spectral proof for a canonical order-two \(U\)-statistic yields
\[
nU_{n,2}(h_2)\xrightarrow{\mathrm d}
\sum_{m\ge0}\lambda_m(Q_m-(4m+3)),
\]
first for a finite harmonic truncation by the multivariate central limit theorem and then for the full kernel by the uniform Hilbert--Schmidt tail bound. Multiplying by six proves the asserted limit.

**4. Variance and one-sided support.** Since \(\theta\) has density \(\sin\theta/2\), its mean is \(\pi/2\) and variance is \((\pi^2-8)/4\). Thus
\[
\|h_2\|_{L^2(\sigma^2)}^2
=\frac{\pi^2-8}{64\pi^2}
=\sum_{m\ge0}(4m+3)\lambda_m^2.
\]
The orthogonal Hoeffding decomposition gives \(n^2\operatorname{Var}(D_n)\to 72\|h_2\|_2^2\). Moreover \(a_m\downarrow0\), so
\(\sum_{m\ge0}(4m+3)|\lambda_m|=\frac18\sum_{m\ge0}(a_m^2-a_{m+1}^2)=1/8\).
This proves the representation \(Z=3/4-6\sum_m|\lambda_m|Q_m\), with convergence in \(L^1\) and hence almost surely. Each summand is nonnegative; finite prefixes can be arbitrarily small with positive probability, while an independent far tail has arbitrarily small mean. Hence \(3/4\) is the exact upper endpoint. The first chi-squared term gives an unbounded lower tail, precluding a Gaussian law.

## Verification

A standalone reproducibility script at `verification/check.py` verifies the closed-form Funk--Hecke eigenvalues by high-accuracy numerical quadrature, checks the spectral variance sum, tests the conditional angular formula against seeded direct tetrahedral sampling, and compares finite empirical depth moments with the predicted exact mean and asymptotic variance. Run it using Python 3 with the dependencies in `verification/requirements.txt`:

```sh
python -m pip install -r verification/requirements.txt
python verification/check.py
```

These finite checks support the calculations but do not certify an infinite-dimensional statement. The proof above supplies the infinite-limit justification through Hoeffding projection and harmonic spectral theory.

## Relationship to prior work

Wendel (1962) establishes the unconditional central containment probability \(1/8\), not the dependence across overlapping tetrahedra. Liu (1988, 1990) introduces simplicial depth and its statistical interpretation. Afshani, Sheehy and Stein (arXiv:1512.04856) study deterministic and randomized algorithms for evaluating simplicial depth, not this explicit three-dimensional sampling fluctuation law. General results for degenerate \(U\)-statistics imply an abstract second-chaos limit once the projection is known, but do not themselves compute the geodesic projection, its complete odd-degree spectrum, the \((\pi^2-8)\) variance constant, or the sharp upper endpoint. Jentsch, Nagy and Wendler (arXiv:2608.11131) discuss degenerate depth statistics and resampling, primarily emphasizing bivariate degeneracy; their complete text was not accessible for an exhaustive priority comparison.

## Limitations

The spectral law is proved only for a spherical-uniform angular distribution in ambient dimension three. It does not provide finite-sample quantiles, convergence rates, or coverage calibration for anisotropic observations. The general degeneracy mechanism is established earlier; the new asserted content is the explicit three-dimensional angular projection, complete harmonic spectrum, exact asymptotic variance, and one-sided support. Priority against every earlier specialized or unavailable full-text theorem is not independently established; in particular, accessible portions of the 1992 general limit-theorem literature and the 2026 resampling paper do not suffice to exclude unlocated equivalent specializations. Independent mathematical audit has not been performed.

## References

- J. G. Wendel, "A Problem in Geometric Probability," *Mathematica Scandinavica* 11 (1962), 109--112. https://doi.org/10.7146/math.scand.a-10655
- R. Y. Liu, "On a notion of simplicial depth," *PNAS* 85 (1988), 1732--1734. https://doi.org/10.1073/pnas.85.6.1732
- R. Y. Liu, "On a notion of data depth based on random simplices," *Annals of Statistics* 18 (1990), 405--414. https://doi.org/10.1214/aos/1176347507
- P. Afshani, D. R. Sheehy and Y. Stein, "Approximating the Simplicial Depth," arXiv:1512.04856 (2015). https://arxiv.org/abs/1512.04856
- L. Dümbgen, "Limit theorems for the simplicial depth," *Statistics & Probability Letters* 14 (1992), 119--128. https://doi.org/10.1016/0167-7152(92)90075-G
- C. Jentsch, S. Nagy and M. Wendler, "Resampling simplicial depth," arXiv:2608.11131 (2026). https://arxiv.org/abs/2608.11131
