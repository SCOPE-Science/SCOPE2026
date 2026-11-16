# Exact fixed-distance spectral minimax on every sphere of ambient dimension at least five

## Finding

For an integer ambient dimension \(d\ge5\), let \(T_{d,\theta}\) denote averaging at one fixed geodesic distance \(\theta\) on the unit sphere \(S^{d-1}\). Its exact best contraction on the mean-zero \(L^2\) space is

\[
\min_{0\le\theta\le\pi}\|T_{d,\theta}\|_{L^2_0\to L^2_0}=\frac1d.
\]

There are exactly two optimal angles, \(\theta=\arccos(1/d)\) and \(\theta=\arccos(-1/d)\). The worst-case eigenspaces are precisely spherical-harmonic degrees one and two, of respective dimensions \(d\) and \(d(d+1)/2-1\). All other nonconstant degrees have strictly smaller multiplier magnitude. For every integer \(k\ge1\), the same angles uniquely minimize the norm of the \(k\)-step operator, with optimum \(d^{-k}\).

## Assumptions and scope

Fix an integer \(d\ge5\); \(\sigma\) is the rotation-invariant probability measure on \(S^{d-1}\subset\mathbb R^d\). For \(0\le\theta\le\pi\) and every integrable \(f\), set

\[
(T_{d,\theta}f)(u)=\mathbb E_{v\in S^{d-2}_u}\,f(\cos\theta\,u+\sin\theta\,v),
\]

where \(S^{d-2}_u\) is the unit tangent sphere in \(u^\perp\), with normalized rotation-invariant measure. The shell operator is a rotationally equivariant self-adjoint Markov contraction preserving \(\sigma\), and leaves \(L^2_0=\{f:\int f\,d\sigma=0\}\) invariant. Its adjointness follows from the symmetric joint distribution of the two endpoints of a random fixed-distance pair.

This is a single fixed-angle kernel, not a mixture over geodesic angles. At \(\theta=0,\pi\), the operator is defined by its deterministic endpoint value. Norms refer to the entire mean-zero \(L^2\) space, not any finite spherical-harmonic truncation.

## Proof

**1. Exact diagonalization.** Put \(x=\cos\theta\). Rotational invariance, the spherical-harmonic addition formula, and the Funk–Hecke theorem imply that each harmonic degree \(n\ge0\) is an eigenspace with real scalar

\[
p_{n,d}(x)=\frac{C_n^{(d-2)/2}(x)}{C_n^{(d-2)/2}(1)},\qquad p_{0,d}=1.
\]

Here \(C_n^\alpha\) is the classical Gegenbauer polynomial. The spherical-harmonic decomposition is orthogonal and complete, so

\[
\|T_{d,\theta}\|_{L^2_0\to L^2_0}=\sup_{n\ge1}|p_{n,d}(x)|.
\]

For clarity, the first three nonconstant multipliers, directly from the standard polynomial recurrence, are

\[
p_{1,d}(x)=x,\quad
p_{2,d}(x)=\frac{dx^2-1}{d-1},\quad
p_{3,d}(x)=\frac{x((d+2)x^2-3)}{d-1}.
\]

**2. The sharp global lower bound.** For any \(x\in[-1,1]\) with \(|x|\ge1/d\), the degree-one multiplier has magnitude at least \(1/d\). If \(|x|<1/d\), then

\[
|p_{2,d}(x)|=\frac{1-dx^2}{d-1}>\frac1d.
\]

Thus the norm is at least \(1/d\) everywhere, and equality can occur *only* when \(x\in\{-1/d,1/d\}\). At either candidate, degrees one and two attain magnitude exactly \(1/d\).

**3. A uniform infinite-degree certificate.** Let \(U\) be the first coordinate of a uniform point on \(S^{d-2}\subset\mathbb R^{d-1}\). The normalized Gegenbauer polynomial has the exact integral representation

\[
p_{n,d}(x)=\mathbb E\big(x+i\sqrt{1-x^2}\,U\big)^n.
\]

One direct derivation is to average the degree-\(n\) homogeneous harmonic polynomials \(z\mapsto(z_1+i\,\xi\cdot z')^n\) over \(\xi\in S^{d-2}\). Each polynomial is harmonic, since its defining complex vector has zero complex squared length. Their average is rotation-invariant about the first axis and equals one at the north pole, and so is the normalized zonal harmonic of that degree. This also establishes the integral representation without an unproved asymptotic bound.

The coordinate moments are \(\mathbb EU^2=1/(d-1)\) and \(\mathbb EU^4=3/((d-1)(d+1))\). At \(|x|=1/d\), write \(Z=x+i\sqrt{1-x^2}\,U\). Since \(|U|\le1\), we have \(|Z|\le1\). An exact fourth-moment calculation gives

\[
\mathbb E|Z|^4=x^4+\frac{2x^2(1-x^2)}{d-1}+\frac{3(1-x^2)^2}{(d-1)(d+1)}
=\frac{3d+2}{d^3}<\frac1d,
\]

where the strict inequality follows from \(d^2-3d-2>0\) for \(d\ge5\). Therefore, *simultaneously for every* \(n\ge4\),

\[
|p_{n,d}(x)|\le\mathbb E|Z|^n\le\mathbb E|Z|^4<\frac1d.
\]

Degree three is also strictly below the optimum because

\[
|p_{3,d}(\pm1/d)|=\frac1d\frac{3-(d+2)/d^2}{d-1}<\frac1d
\]

for \(d\ge5\). This proves both attainment and strict exclusion of all higher harmonic degrees, *without* truncating the infinite spectrum.

**4. Multiplicities and powers.** The degree-one harmonic dimension is \(d\) and the degree-two harmonic dimension is \(d(d+1)/2-1\), hence total \((d^2+3d-2)/2\). The operator is self-adjoint and diagonal in spherical harmonics, so \(\|T_{d,\theta}^k\|=\|T_{d,\theta}\|^k\) for all positive integers \(k\). Monotonicity of the positive \(k\)-th power preserves the exact two-angle optimizer set.

## Verification

The accompanying self-contained `check_hypersphere_fixed_step.py` computes normalized Gegenbauer multipliers by an exact rational recurrence:

\[
p_{n+1,d}(x)=\frac{(2n+d-2)x\,p_{n,d}(x)-n\,p_{n-1,d}(x)}{n+d-2}.
\]

Its run reported **59,232 exact rational assertions**, checking the first multipliers, parity, the fourth-moment identity and bound, the first 160 degrees for ambient dimensions 5 through 100, and a finite two-sector minimax grid. Those finite checks are reproducibility tests rather than proofs of the infinite-dimensional theorem; Steps 1–4 provide the proof for all allowed degrees and dimensions.

Run with `python3 check_hypersphere_fixed_step.py` using Python's standard library.

## Relationship to prior work

The 2023 study by Schär and Stier establishes Wasserstein contraction for an angle-*randomized* geodesic walk. Its transition explicitly integrates the angle over a full circle; the sharp deterministic-angle \(L^2\) minimax problem here is different. Mangoubi and Smith (2016) allow fixed geodesic steps on positively curved manifolds and establish general Wasserstein mixing estimates; their reported bounds and conditions do not imply the exact spherical Gegenbauer minimax, two optimizer angles, and equality sectors given here. Caillol (2004) develops Gegenbauer harmonic expansions for continuous hyperspherical diffusion with heat eigenvalues, rather than discrete one-shell operators optimized over step angles.

Earlier low-dimensional spherical cases are not the subject of this theorem: only ambient dimensions at least five are claimed. The low-degree character multipliers are classical; the new statement is the sharp *all-degree/all-dimension* deterministic-shell optimization in the specified range, together with its strict equality classification.

## Limitations

No conclusion is drawn for ambient dimensions below five, for mixtures of shell distances, for spatially inhomogeneous transitions, for total-variation convergence from a point mass, or for Wasserstein-optimal steps. There is no independent audit. Specialized early spectral-radius results might affect priority despite the literature comparisons reported here.

## References

- Philip Schär and Thilo D. Stier, *A Dimension-Independent Bound on the Wasserstein Contraction Rate of a Geodesic Random Walk on the Sphere*, arXiv:2309.09097, first posted 2023-09-16. https://arxiv.org/abs/2309.09097
- Oren Mangoubi and Aaron Smith, *Rapid Mixing of Geodesic Walks on Manifolds with Positive Curvature*, arXiv:1609.02901, first posted 2016-09-09. https://arxiv.org/abs/1609.02901
- J.-M. Caillol, *Random Walks on Hyperspheres of Arbitrary Dimensions*, arXiv:cond-mat/0401209, first posted 2004-01-13. https://arxiv.org/abs/cond-mat/0401209
