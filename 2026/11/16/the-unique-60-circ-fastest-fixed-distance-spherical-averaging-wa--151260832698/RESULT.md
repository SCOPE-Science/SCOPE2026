# The unique \(60^\circ\) fastest fixed-distance spherical averaging walk on \(\mathbb{CP}^2\)

## Finding
On the complex projective plane with normalized Fubini–Study metric, let \(T_\theta\) average a function uniformly over the geodesic distance sphere of radius \(\theta\), for \(0\le\theta\le\pi/2\). On the mean-zero space \(L^2_0(\mathbb{CP}^2)\), the unique optimal fixed distance is \(\theta=\pi/3\), and
\[
\min_{0\le\theta\le\pi/2}\|T_\theta\|_{L^2_0\to L^2_0}=\frac18.
\]
At this distance, precisely spherical harmonic degrees \(n=1\) and \(n=2\) attain the norm, both with eigenvalue \(-1/8\). Their respective dimensions are \(8\) and \(27\), giving a \(35\)-dimensional extremal space. Every other nonconstant degree has strictly smaller multiplier magnitude. For every integer \(k\ge1\), the unique distance minimizing \(\|T_\theta^k\|_{L^2_0\to L^2_0}\) remains \(\pi/3\), with sharp norm \(8^{-k}\).

## Assumptions and scope
Write \(\mathbb{CP}^2=\{[z]:z\in\mathbb C^3\setminus\{0\}\}\), and use unit representatives to define
\[
d_{FS}([u],[v])=\arccos |\langle u,v\rangle|\in[0,\pi/2].
\]
The Haar-invariant probability measure is denoted \(\mu\). For each \(x\) and \(\theta\), the unique stabilizer-invariant probability measure on \(\{y:d_{FS}(x,y)=\theta\}\) is \(\sigma_{x,\theta}\); define
\[
(T_\theta f)(x)=\int f(y)\,d\sigma_{x,\theta}(y).
\]
At \(\theta=0\), this is identity. At the diameter \(\theta=\pi/2\), the distance sphere is interpreted with its unique invariant probability measure. The norm is the ordinary Hilbert-space operator norm for mean-zero square-integrable functions, **not** total-variation mixing from a point mass. A single deterministic distance is optimized; probability mixtures of distances are not included.

## Proof
The isometry-invariant averaging operator is self-adjoint and diagonal under the multiplicity-free spherical-harmonic decomposition
\[
L^2(\mathbb{CP}^2,\mu)=\bigoplus_{n=0}^{\infty}\mathcal H_n,
\qquad \dim \mathcal H_n=(n+1)^3.
\]
Here \(\mathcal H_0\) consists of constants. With \(x=\cos(2\theta)\in[-1,1]\), the normalized spherical-function formula gives
\[
T_\theta|_{\mathcal H_n}=\phi_n(x)I,\qquad
\phi_n(x)=\frac{P_n^{(1,0)}(x)}{n+1},\qquad P_n^{(1,0)}(1)=n+1.
\]
Consequently \(\|T_\theta\|_{L^2_0\to L^2_0}=\sup_{n\ge1}|\phi_n(x)|\). The first two multipliers are
\[
\phi_1(x)=\frac{1+3x}{4},\qquad
\phi_2(x)=\frac{5x^2+2x-1}{6}.
\]
If \(|\phi_1(x)|\le1/8\), necessarily \(-1/2\le x\le-1/6\). On this interval the factorization
\[
\phi_2(x)+\frac18=\frac56\left(x+\frac12\right)\left(x-\frac1{10}\right)
\]
is nonpositive, and strictly negative unless \(x=-1/2\). Outside the interval \(|\phi_1(x)|>1/8\). Therefore \(\sup_{n\ge1}|\phi_n(x)|\ge1/8\) for all \(x\), and equality is possible **only** at \(x=-1/2\), corresponding to \(\theta=\pi/3\).

To prove that all infinitely many modes obey the bound at this candidate, use the elementary Jacobi–Legendre identity
\[
(1-x)P_n^{(1,0)}(x)=P_n(x)-P_{n+1}(x),
\]
where \(P_n=P_n^{(0,0)}\). At \(x=-1/2\), \(\phi_1=\phi_2=-1/8\). Exact Legendre recurrence gives the following complete finite interval:

| Degree \(n\) | Multiplier \(\phi_n(-1/2)\) |
|---|---|
| 3 | \(31/256\) |
| 4 | \(-17/640\) |
| 5 | \(-47/1024\) |
| 6 | \(373/7168\) |
| 7 | \(-1633/131072\) |
| 8 | \(-829/32768\) |
| 9 | \(39857/1310720\) |

Each listed magnitude is strictly less than \(1/8\). For every \(n\ge10\), the classical bound \(|P_n(t)|\le1\) for \(-1\le t\le1\) implies
\[
|\phi_n(-1/2)|\le\frac{2}{(n+1)(3/2)}=\frac4{3(n+1)}\le\frac4{33}<\frac18.
\]
Thus no other nonconstant harmonic degree attains the norm. Finally, \(\dim\mathcal H_n=(n+1)^3\) gives \(8+27=35\) extremal dimensions. Since \(T_\theta\) is self-adjoint, \(\|T_\theta^k\|=\|T_\theta\|^k\) for all positive integers \(k\), proving the power statement and retaining uniqueness.

## Verification
The standalone standard-library Python script `verify_cp2.py` computes rational Legendre recurrences, independently reconstructs Jacobi spherical multipliers from terminating hypergeometric sums, checks all finite comparison values and the explicit strict large-degree envelope, and cross-checks the multiplicity formula. It reports 280 passed exact assertions. All-degree control is the displayed Legendre bound, not finite enumeration; global optimality is the displayed two-multiplier inequality, not a numerical sweep.

## Relationship to prior work
Brandolini–Gariboldi–Gigante–Monguzzi [1] give spherical harmonics and Jacobi-polynomial formulae on compact two-point homogeneous spaces, applied to **ball-discrepancy lower bounds**. Their ball-integrated Jacobi multipliers are not fixed-distance **surface-averaging** multipliers, and their results do not optimize the operator norm over geodesic distances. Tóth [2] develops isotropic projective random-walk kernels with normalized Jacobi multipliers and analyzes fidelity, diffusion, and first-passage statistics, but does not identify the minimum of the infinite-degree spectral supremum, its unique \(60^\circ\) optimizer, or the two equality degrees. The classical spherical-function classification of Grünbaum–Pacharoni–Tirao [3] provides a more general matrix-valued representation framework rather than this extremal design result. Bettiol–Lauret–Piccione [4] study the Laplace spectrum of **distance spheres as manifolds**, not the averaging operator on the ambient projective plane.

The classification does not follow from the distinct fixed-angle problems on \(S^2\), \(\mathrm{SO}(3)\), or \(\mathrm{SU}(2)\): their representation spectra use Legendre polynomials or group characters, whereas the present normalized multiplier is the asymmetric Jacobi family \(P_n^{(1,0)}/(n+1)\). The exact minimizer and its two negative equality sectors require the comparison above. Absence of a directly matching published statement in searched records is not proof of absolute historical novelty.

## Limitations
The theorem concerns one fixed geodesic step on \(\mathbb{CP}^2\), not other projective dimensions, arbitrary radial step distributions, finite-support axis/direction rules, non-isotropic Markov kernels, or optimal total-variation mixing from a singular initial measure. Exact global optimization of a mixture of angles has a different feasible set. Historical-priority checks are best-knowledge rather than independent certification, and older specialized spherical-design or Jacobi-minimax literature could contain an equivalent statement.

## References
[1] L. Brandolini, B. Gariboldi, G. Gigante, A. Monguzzi, *Single radius spherical cap discrepancy on compact two-point homogeneous spaces*, arXiv:2406.03830 (first public June 6, 2024), *Mathematische Zeitschrift* 308, 52 (2024), https://arxiv.org/abs/2406.03830 , https://doi.org/10.1007/s00209-024-03615-4 .

[2] G. I. Tóth, *Isotropic random walks and Brownian diffusion on complex projective space*, arXiv:2606.11438 (first public June 9, 2026), https://arxiv.org/abs/2606.11438 .

[3] F. A. Grünbaum, I. Pacharoni, J. Tirao, *Matrix valued spherical functions associated to the complex projective plane*, arXiv:math/0108042 (2001), *Journal of Functional Analysis* 188 (2002), 350–441, https://arxiv.org/abs/math/0108042 .

[4] R. G. Bettiol, E. A. Lauret, P. Piccione, *Full Laplace spectrum of distance spheres in symmetric spaces of rank one*, arXiv:2012.02349 (first public December 4, 2020), *Bulletin of the London Mathematical Society* 54 (2022), 1683–1704, https://arxiv.org/abs/2012.02349 .
