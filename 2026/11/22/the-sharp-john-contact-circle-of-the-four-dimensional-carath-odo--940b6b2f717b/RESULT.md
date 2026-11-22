# The sharp John contact circle of the four-dimensional Carathéodory orbitope

## Finding

Let \(C\subset\mathbb C^2\simeq\mathbb R^4\) be the universal degree-two Carathéodory orbitope
\[
C=\operatorname{conv}\{(e^{i\theta},e^{2i\theta}):0\le\theta<2\pi\}.
\]
Its **unique maximum-volume inscribed ellipsoid** is
\[
E_J=\left\{(z,w):3|z|^2+\frac98|w|^2\le1\right\}.
\]
The entire common boundary of \(E_J\) and \(C\) is one harmonic circle:
\[
\partial E_J\cap\partial C
=\left\{\left(\frac{e^{i\theta}}{\sqrt6},-\frac23e^{2i\theta}\right):0\le\theta<2\pi\right\}.
\]
In the same Euclidean coordinates the minimum-volume enclosing Löwner ellipsoid is
\[
E_L=\{(z,w):|z|^2+|w|^2\le2\},
\]
and its contact set with \(C\) is exactly the generating trigonometric moment curve. This enclosing ellipsoid is also implied by the general orbit-ellipsoid theorem of Barvinok and Blekherman; it is included for a calibrated comparison, **not claimed as an original general principle**.

The four-dimensional Lebesgue volumes and sharp ratios are
\[
\operatorname{Vol}_4(C)=\frac{\pi^2}{3},\quad
\operatorname{Vol}_4(E_J)=\frac{4\pi^2}{27},\quad
\operatorname{Vol}_4(E_L)=2\pi^2,
\]
\[
\boxed{\frac{\operatorname{Vol}_4(E_J)}{\operatorname{Vol}_4(C)}=\frac49},\qquad
\frac{\operatorname{Vol}_4(C)}{\operatorname{Vol}_4(E_L)}=\frac16.
\]
The new claim concerns the complete inner ellipsoid, its exact contact locus, and the sharp occupied-volume fraction for this natural four-dimensional orbitope.

## Assumptions and scope

Coordinates \(z,w\) denote two complex numbers with ordinary real Euclidean norm \(|z|^2+|w|^2\). All volumes are real four-dimensional Euclidean Lebesgue measures in these fixed coordinates. Every candidate ellipsoid is allowed arbitrary center, orientation, and semiaxes; the optimization is not restricted to the rotationally equivariant family. An ellipsoid is full-dimensional and nondegenerate. Contact means membership in both topological boundaries.

The classical Hermitian Toeplitz description of the universal Carathéodory orbitope gives the exact membership criterion
\[
(z,w)\in C\quad\Longleftrightarrow\quad |z|^2+|w-z^2|\le1.
\tag{1}
\]
Here the notation is not an approximation: a Schur complement of the Toeplitz matrix with unit diagonal yields (1). In particular, each fiber above \(z\) with \(|z|\le1\) is a closed complex disk of radius \(1-|z|^2\), centered at \(z^2\).

## Proof

**1. Exact containment of the proposed inscribed ellipsoid.** Put \(t=|z|^2\). If \((z,w)\in E_J\), then \(0\le t\le1/3\) and
\[
|w|\le\frac{2\sqrt2}{3}\sqrt{1-3t}.
\]
The triangle inequality bounds the left side of (1):
\[
|z|^2+|w-z^2|\le2t+\frac{2\sqrt2}{3}\sqrt{1-3t}.
\]
Since \(1-2t>0\) on this interval, the last quantity is at most \(1\) if and only if the squared inequality holds. Its difference is exactly
\[
(1-2t)^2-\frac89(1-3t)=\left(2t-\frac13\right)^2\ge0.
\tag{2}
\]
Thus \(E_J\subset C\), with no numerical or asymptotic assumption.

**2. Entire inner contact set.** Equality in (2) requires \(t=1/6\). Equality in the other steps requires \(|w|=2/3\) and \(w\) to have the phase opposite to \(z^2\). Therefore every and only shared boundary point has the form
\[
(z,w)=\left(\frac{e^{i\theta}}{\sqrt6},-\frac23e^{2i\theta}\right).
\tag{3}
\]
Conversely, each point in (3) satisfies both boundaries exactly, because \(1/6+|-2e^{2i\theta}/3-e^{2i\theta}/6|=1\).

**3. Unrestricted John optimality.** The positive-definite real-linear map
\[
T_J(z,w)=\left(\sqrt3\,z,\frac{3}{2\sqrt2}\,w\right)
\]
sends \(E_J\) to the real four-dimensional unit ball. It sends (3) to the boundary points
\[
u(\theta)=\frac1{\sqrt2}\left(e^{i\theta},-e^{2i\theta}\right)\in\mathbb C^2.
\]
The uniform probability measure on \(\theta\in[0,2\pi)\) satisfies, in real coordinates,
\[
\int u(\theta)\,\frac{d\theta}{2\pi}=0,\qquad
\int u(\theta)u(\theta)^\mathsf T\,\frac{d\theta}{2\pi}=\frac14 I_4.
\tag{4}
\]
Indeed every nonconstant Fourier mode integrates to zero; each diagonal trigonometric square averages \(1/2\), and the extra factor \(1/2\) gives \(1/4\). Five equally spaced phases also give an **exact finite certificate**: for \(\theta_j=2\pi j/5\), the five vectors \(u(\theta_j)\) form a regular four-simplex with pairwise scalar products \(-1/4\). Their equal weights \(4/5\) have zero weighted sum and second-moment matrix \(I_4\). This follows because Fourier sums at nonzero frequencies of magnitude at most four vanish on the fifth roots of unity. Equivalently, multiplying the Haar measure in (4) by \(4\) gives the same centered contact certificate. The sufficiency direction of John's ellipsoid theorem then proves that the unit ball is the largest-volume ellipsoid of \(T_J(C)\), **among all ellipsoids including translated and tilted ones**. Transforming back gives the asserted unique \(E_J\).

**4. Löwner ellipsoid and its full contacts.** Every generator \((e^{i\theta},e^{2i\theta})\) has squared Euclidean norm \(2\), so the ball \(E_L\) contains their convex hull. Strict convexity of the ball implies a nontrivial convex combination of distinct generating points lies strictly inside \(E_L\), hence the complete contact set is the generating curve. After dividing by \(\sqrt2\), the generating curve has the same two harmonic frequencies as (4), now both with positive signs. Its uniform mean is zero and covariance is \(I_4/4\). The dual/Löwner contact criterion proves this ball is the unique minimum-volume ellipsoid containing \(C\). Alternatively this is the special case of Barvinok–Blekherman's general theorem for convex hulls of compact group orbits.

**5. Exact volumes.** Applying Fubini to the disk fibers following (1),
\[
\operatorname{Vol}_4(C)=\int_{|z|\le1}\pi(1-|z|^2)^2\,dA(z)
=2\pi^2\int_0^1r(1-r^2)^2\,dr=\frac{\pi^2}{3}.
\]
The volume of a four-dimensional unit ball is \(\pi^2/2\). The real semiaxes of \(E_J\) are \(1/\sqrt3,1/\sqrt3,2\sqrt2/3,2\sqrt2/3\), so its semiaxis product is \(8/27\), yielding \(4\pi^2/27\). The four semiaxes of \(E_L\) all equal \(\sqrt2\), so its volume is \(2\pi^2\). Both ratios follow by division.

## Verification

The accompanying self-contained `verify.py` reproduces equation (2) at 1,001 exact rational parameters, the exact volume and contact identities, 6,000 randomized unit-boundary containment checks, trigonometric contact-frame quadrature on four finite grids for both signs, and 3,000 exact-locus numerical samples. It uses only Python's standard library and can be run with `python verify.py`. The listed script executed successfully on its included source. These finite checks support implementation accuracy; the continuous-domain and optimality assertions are proved analytically above rather than inferred from sampling.

## Relationship to prior work

Sanyal, Sottile and Sturmfels (2011; open preprint arXiv:0911.5436) established the Toeplitz spectrahedron representation, harmonic coordinates, and face structure of the Carathéodory orbitopes. Their Theorem 5.2 supplies the classical starting point (1); its full Section 5 is not a formula for the maximizing inscribed ellipsoid. Barvinok and Blekherman (2003; arXiv:math/0312268) proved an **all-orbitope minimum-volume enclosing ellipsoid theorem** (Theorem 2.2), which already implies the enclosing ball reported here. It does not state the largest inscribed ellipsoid of this noncentrally symmetric orbitope; its Theorem 2.4 instead concerns the **largest inscribed ellipsoid of the polar body**, which is a distinct problem.

The more recent lead paper by Aloy, Galley, Jones, Ludescher and Müller, *Spin-bounded correlations: rotation boxes within and beyond quantum theory* (arXiv:2312.09278, first posted 2023-12-14), identifies the spin-one rotation state space with the universal four-dimensional Carathéodory orbitope and analyzes its Toeplitz realization (Section VI.2). That work motivates a metric normalization of this concrete body but does not give its John contact circle or \(4/9\) interior ellipsoid volume fraction. Kobert and Scheiderer's *Spectrahedral representation of polar orbitopes* (arXiv:2010.02045) treats semidefinite and face structures of a different (polar-representation) class, not an inner-ellipsoid formula for this orbitope.

The contribution here is the inner contact-circle classification and exact maximal occupied-volume ratio, not a rediscovery of the Toeplitz representation or of the known general Löwner theorem.

## Limitations

The theorem concerns the single degree-two universal Carathéodory orbitope in its specified Euclidean representation. It does not give the John ellipsoid for arbitrary higher-degree or differently weighted circle orbitopes, nor claim that the numerical fraction is invariant under arbitrary changes of base body (both body and ellipsoid volumes transform together under affine maps, so their ratio is affine invariant for this body). Only self-review has been performed; no independent mathematical audit has been performed. Although direct published-source and mathematical-finding comparisons found no covering result for the inner statement, a historically unindexed equivalent or a non-obvious general theorem may exist.

## References

1. A. Aloy, T. D. Galley, C. L. Jones, S. L. Ludescher, M. P. Müller, *Spin-bounded correlations: rotation boxes within and beyond quantum theory*, arXiv:2312.09278 (first posted 2023-12-14), Section VI.2; https://arxiv.org/abs/2312.09278.
2. R. Sanyal, F. Sottile, B. Sturmfels, *Orbitopes*, arXiv:0911.5436, Section 5, Theorem 5.2; https://arxiv.org/abs/0911.5436.
3. A. Barvinok, G. Blekherman, *Convex Geometry of Orbits*, arXiv:math/0312268 (first posted 2003-12-12), Theorems 2.2 and 2.4; https://arxiv.org/abs/math/0312268.
4. T. Kobert, C. Scheiderer, *Spectrahedral representation of polar orbitopes*, arXiv:2010.02045 (first posted 2020-10-05); https://arxiv.org/abs/2010.02045.
5. P. M. Gruber, F. E. Schuster, *An arithmetic proof of John's ellipsoid theorem*, arXiv:1207.7246 (2012); https://arxiv.org/abs/1207.7246.
