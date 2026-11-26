# A three-facet positivity cone for mixed dipole–quadrupole spherical Poisson covariances

## Finding

Fix \(0<r<1\) and real \(b,c\). On the unit two-sphere \(\mathbb S^2\subset\mathbb R^3\), let
\[
K_{r,b,c}(x,y)=\frac{1-r^2}{(1-2r\langle x,y\rangle+r^2)^{3/2}}\left[1+b\langle x,y\rangle+cP_2(\langle x,y\rangle)\right],\qquad P_2(t)=\frac{3t^2-1}{2}.
\]
The kernel is positive semidefinite for every finite set of sphere points **if and only if**
\[
\begin{aligned}
L_0&=1+br+cr^2\ge0,\\
L_1&=1+\frac{1+2r^2}{3r}b+\frac{2+3r^2}{5}c\ge0,\\
L_\infty&=1+\frac{1+r^2}{2r}b+\frac{3+2r^2+3r^4}{8r^2}c\ge0.
\end{aligned}
\]
Each condition is irredundant: for fixed \(r\), each defines a genuine boundary segment or ray of the admissible coefficient region. **Every** admissible kernel, even at a boundary intersection, is strictly positive definite on every finite collection of pairwise distinct points.

The new phenomenon is a three-obstruction reduction of infinitely many signed Legendre inequalities. In particular, degree one yields a genuinely independent constraint alongside the constant and high-degree tests. The already established pure quadrupole \(b=0\) specialization is not claimed as new.

## Assumptions and scope

All harmonic expansions and integral operators use normalized rotation-invariant surface measure on \(\mathbb S^2\). Positive semidefiniteness means nonnegativity of every finite Gram quadratic form, for arbitrary complex coefficients; strict positive definiteness is required only at pairwise distinct sites with a nonzero coefficient vector. The parameter \(r\) is fixed in \((0,1)\), with no assertion at either endpoint; \(b,c\) are arbitrary real numbers, not assumed nonnegative. There is no claim for higher sphere dimensions or for nonzonal perturbations.

## Proof

**1. Legendre multipliers.** The spherical Poisson addition formula is
\[
\frac{1-r^2}{(1-2rt+r^2)^{3/2}}=\sum_{n=0}^{\infty}(2n+1)r^nP_n(t).
\]
The recurrence \((2n+1)tP_n=(n+1)P_{n+1}+nP_{n-1}\), followed by \(P_2(t)=(3t^2-1)/2\), gives an absolutely convergent expansion
\[
K_{r,b,c}(t)=\sum_{n=0}^{\infty}(2n+1)r^n H_nP_n(t),\qquad H_n=1+bA_n+cB_n,
\]
where the exact multipliers for every nonnegative integer \(n\) are
\[
A_n=\frac{n/r+(n+1)r}{2n+1},
\]
\[
B_n=\frac32\left[\frac{n(n-1)}{(2n-1)(2n+1)r^2}+\frac{(n+1)^2}{(2n+1)(2n+3)}+\frac{n^2}{(2n+1)(2n-1)}+\frac{(n+1)(n+2)r^2}{(2n+1)(2n+3)}\right]-\frac12.
\]
At \(n=0\), terms with zero numerator are interpreted as zero; the displayed rational formula is defined there. Thus \((A_0,B_0)=(r,r^2)\), \((A_1,B_1)=((1+2r^2)/(3r),(2+3r^2)/5)\), and
\[
(A_\infty,B_\infty)=\left(\frac{1+r^2}{2r},\frac{3+2r^2+3r^4}{8r^2}\right).
\]
Consequently \(H_0=L_0\), \(H_1=L_1\), and \(\lim_{n\to\infty}H_n=L_\infty\).

**2. Exact three-point convexity.** For every integer \(n\ge2\), define
\[
D_n=(2n-1)(2n+1)(2n+3)(r^2+15),
\]
\[
\begin{aligned}
w_{n,0}&=\frac{3(n-1)[(10-2r^2)n+r^2+15]}{D_n},\\
w_{n,1}&=\frac{15n[(2n-1)r^2+6n+9]}{D_n},\\
w_{n,\infty}&=\frac{4n(n-1)[(2n-1)r^2+30n+45]}{D_n}.
\end{aligned}
\]
Direct polynomial expansion yields the three exact identities
\[
\begin{aligned}
w_{n,0}+w_{n,1}+w_{n,\infty}&=1,\\
A_n&=w_{n,0}A_0+w_{n,1}A_1+w_{n,\infty}A_\infty,\\
B_n&=w_{n,0}B_0+w_{n,1}B_1+w_{n,\infty}B_\infty.
\end{aligned}
\]
All three weights are strictly positive for \(n\ge2\) and \(0<r<1\). Hence
\[
\boxed{H_n=w_{n,0}L_0+w_{n,1}L_1+w_{n,\infty}L_\infty\quad(n\ge2).}
\]
Schoenberg's characterization of continuous isotropic positive-definite kernels on \(\mathbb S^2\) says exactly that every Legendre coefficient must be nonnegative. The three stated inequalities suffice by this identity. They are necessary by testing degrees zero and one and taking the limit of the nonnegative sequence \(H_n\).

**3. Irredundancy and strictness.** The degree-zero and degree-one boundary lines intersect at \((b,c)=(-6/r,5/r^2)\), where \(L_\infty>0\). The degree-one and limiting-degree boundary lines meet at
\[
(b,c)=\left(-\frac{9r(3r^2+5)}{6r^4+31r^2+15},\frac{20r^2}{6r^4+31r^2+15}\right),
\]
where \(L_0>0\). A point with \(L_\infty=0\), \(L_0>0\) and \(L_1>0\) is \((b,c)=(0,-8r^2/(3+2r^2+3r^4))\). These witnesses, together with small feasible motions along the boundary lines, show that no inequality is implied by the other two.

The determinant of the affine-coordinate matrix with rows \((1,1,1)\), \((A_0,A_1,A_\infty)\) and \((B_0,B_1,B_\infty)\) equals
\[
\frac{(1-r^2)^2(r^2+15)}{120r^3}>0.
\]
Therefore \(L_0,L_1,L_\infty\) cannot all vanish simultaneously. Since each \(H_n\) with \(n\ge2\) is a strict positive convex combination, every admissible kernel has \(H_n>0\) for all \(n\ge2\). Both parity classes contain infinitely many strictly positive Legendre coefficients; the strict spherical Schoenberg criterion gives strict positive definiteness for distinct-site finite matrices.

**4. Ultraviolet face and exact boundary decay.** If \(L_\infty=0\), then \(L_0,L_1\ge0\) and at least one is positive. Expanding the weights at fixed \(r\) gives
\[
H_n=\frac{3(10-2r^2)L_0+15(2r^2+6)L_1}{8(r^2+15)}\frac1n+O_r(n^{-2}),
\]
with a strictly positive coefficient. Thus every fixed high degree is positive at equality even though the limiting constraint is saturated; if \(L_\infty<0\), all sufficiently high-degree coefficients are negative. The corresponding normalized-surface harmonic eigenvalues are \(r^nH_n\), not \((2n+1)r^nH_n\).

## Verification

The standalone `check.py` establishes five symbolic coefficient/convexity identities, exact boundary-intersection identities and positive determinant, checks selected exceptional degrees, and compares the predicted Legendre coefficients with independently integrated Gauss–Legendre quadrature values. It passed 220 assertions covering four radii, five parameter sets per radius, and degrees zero through nine. These finite checks are supplementary: the infinite-dimensional assertion is proved by the exact rational identity and Schoenberg's theorem, not by enumeration.

To reproduce: execute `python check.py` with Python 3, SymPy and NumPy installed. The code uses no external services or proprietary data.

## Relationship to prior work

Schoenberg's coefficient criterion and its modern reviews provide the general decision principle. The multiquadric family with exponent \(3/2\) includes the unmodulated spherical Poisson spline, as discussed by Gneiting. Jäger and Buhmann–Jäger develop spherical kernel positivity and strictness in general harmonic coefficient structures. These sources do not, in the portions examined, state the three explicit joint affine inequalities, the strictly positive barycentric decomposition for every degree, or the sharp degree-one facet. The previously established pure quadrupole case is recovered by setting \(b=0\); that one-dimensional slice is explicitly outside this finding's novelty claim. A more general, unindexed result might imply the joint classification and remains a priority risk.

## Limitations

This is a two-sphere and fixed-scale \(0<r<1\) theorem, not a classification for all dimensions or all finite-degree angular modulations. The strictness statement concerns every finite set of distinct sites, not a uniform spectral lower bound over increasing harmonic degree. The source comparison does not prove absolute publication priority. Independent validation or audit has not been performed.

## References

1. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, Bernoulli 19 (2013), 1327–1349; arXiv:1111.7077, Sections 3–4, especially Schoenberg's Theorem 1 and the multiquadric/Poisson spline discussion. https://arxiv.org/abs/1111.7077
2. J. Jäger, *Strictly positive definite kernels on the 2-sphere: beyond radial symmetry*, arXiv:2005.02798v1 (first publicly posted 2020-05-06), Sections 1–3. https://arxiv.org/abs/2005.02798
3. M. Buhmann and J. Jäger, *Strict positive definiteness of convolutional and axially symmetric kernels on d-dimensional spheres*, arXiv:2105.02586v1 (2021-05-06), Sections 2–4. https://arxiv.org/abs/2105.02586
