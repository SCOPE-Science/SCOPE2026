# Universal isotropic optimum of isocanted cubes

## Finding

For each integer \(d\ge 2\) and each \(t\ge 0\), put
\[
K_d(t)=[-1,1]^d+[-t,t](1,\ldots,1)\subset\mathbb R^d.
\]
The Minkowski sum is the isocanted cube in its diagonal-zonotope parametrization: in the notation \(\mathcal I_d(\ell,a)\), its parameters are \(\ell=2(1+t)\) and \(a=2t\). In particular, \(a/\ell=t/(1+t)\).

Write \(\operatorname{Cov}(K)\) for the covariance matrix of normalized Lebesgue measure on a full-dimensional convex body \(K\), and define the affine-invariant squared isotropic constant by
\[
L(K)^2=\frac{(\det\operatorname{Cov}(K))^{1/d}}{\operatorname{vol}_d(K)^{2/d}}.
\]
For every \(d\ge2\) and \(t\ge0\), the covariance of \(K_d(t)\) has eigenvalues
\[
\lambda_{\parallel}=\frac{1+2t+dt^2}{3}\quad\text{(multiplicity one)},
\qquad
\lambda_{\perp}=\frac{1+(d+2)t}{3(1+dt)}\quad\text{(multiplicity \(d-1\))},
\]
where the first eigenspace is spanned by \((1,\ldots,1)\), and \(\operatorname{vol}_d K_d(t)=2^d(1+dt)\). Consequently,
\[
\boxed{
\frac{L(K_d(t))^2}{L([-1,1]^d)^2}
=\left[\frac{(1+2t+dt^2)(1+(d+2)t)^{d-1}}{(1+dt)^{d+1}}\right]^{1/d}.}
\]
For every dimension \(d\ge2\), this function is **strictly decreasing** for \(0<t<1\), **strictly increasing** for \(t>1\), and has its **unique global minimum** at \(t=1\), equivalently at the cant ratio \(a/\ell=1/2\). The minimum is exactly
\[
\boxed{\min_{t\ge0}L(K_d(t))^2=\frac{d+3}{12(d+1)^{1+1/d}}.}
\]
It is strictly less than the cube's value \(1/12\) in every dimension \(d\ge2\).

## Assumptions and scope

The dimension \(d\) is an arbitrary integer at least two, \(t\) is any finite nonnegative real number, volume is ordinary \(d\)-dimensional Euclidean Lebesgue measure, and covariance uses the **uniform interior-volume distribution**, not the distribution of independent random zonotope coefficients. The body is centrally symmetric about the origin. The quantity \(L^2\) is affine invariant with the volume normalization shown above. The limiting case \(t=0\) is the cube, and every \(t>0\) is an isocanted cube with \(0<a<\ell\).

## Proof

**Step 1 (geometry and volume).** A point \(x\in K_d(t)\) is precisely a vector satisfying
\[
-(1+t)\le x_i\le1+t\ (1\le i\le d),\qquad
\max_i x_i-\min_i x_i\le2.
\]
Indeed, there must be a common \(u\in[-t,t]\) such that \(|x_i-u|\le1\) for every \(i\), and these inequalities are equivalent to the displayed coordinate and spread constraints. Apart from measure-zero coincident-coordinate configurations, partition \(K_d(t)\) into the \(d!\) chambers of strictly increasing coordinate order. On each chamber set \(S=\max x_i-\min x_i\in(0,2)\), \(U=(\max x_i+\min x_i)/2\), and write \(x_i=U+w_i\), where the ordered \(w_i\) have extreme values \(\pm S/2\). For fixed \(S\), the middle \(d-2\) coordinates range over an ordered simplex of volume \(S^{d-2}/(d-2)!\); the center lies in the interval
\[
-(1+t-S/2)\le U\le1+t-S/2.
\]
The change of variables from minimum/maximum to \(U,S\) has Jacobian one. Thus, with \(H(S)=2(1+t)-S\), the normalizing integral for \(S\) is
\[
I_0=\int_0^2 S^{d-2}H(S)\,dS
=\frac{2^d(1+dt)}{d(d-1)}.
\]
Multiplying by \(d!/(d-2)!=d(d-1)\) proves \(\operatorname{vol}_d K_d(t)=2^d(1+dt)\). This volume formula was already established in the cited 2024 work; the calculation here also fixes the distribution needed for moments.

**Step 2 (exact conditional moments).** The variable \(S\) has density \(S^{d-2}H(S)/I_0\) on \((0,2)\). Conditional on \(S\), the center \(U\) is uniform on \([-H(S)/2,H(S)/2]\). Conditional on \(S,U\), the middle \(d-2\) *unordered* residual coordinates are independent uniform points in \([-S/2,S/2]\), followed by a uniformly random permutation of the \(d\) coordinate labels; the two extremes are \(\pm S/2\). This representation is valid also for \(d=2\), when there are no middle coordinates.

Consequently, conditional on \(S\),
\[
\mathbb E\Big[\sum_i w_i\mid S\Big]=0,\quad
\mathbb E\Big[\big(\sum_i w_i\big)^2\mid S\Big]=\frac{d-2}{12}S^2,\quad
\mathbb E\Big[\sum_i w_i^2\mid S\Big]=\frac{d+4}{12}S^2.
\]
Elementary polynomial integration gives
\[
\mathbb E S=\frac{2(d-1)(1+(d+1)t)}{(d+1)(1+dt)},
\qquad
\mathbb E S^2=\frac{4d(d-1)(1+(d+2)t)}{(d+1)(d+2)(1+dt)},
\]
and
\[
\mathbb E U^2=\frac{\mathbb E H(S)^2}{12},\qquad
\mathbb E H(S)^2=4(1+t)^2-4(1+t)\mathbb E S+\mathbb E S^2.
\]

**Step 3 (diagonalization).** Permutation symmetry forces the covariance to have a single eigenvalue in the direction \(\mathbf1=(1,\ldots,1)\) and another on its orthogonal complement. Central symmetry makes the mean zero. Directly from Step 2,
\[
\lambda_{\parallel}=\frac1d\mathbb E\big(\sum_i x_i\big)^2
=d\mathbb E U^2+\frac{d-2}{12d}\mathbb E S^2.
\]
Subtracting this from the trace \(\mathbb E\sum_i x_i^2=d\mathbb E U^2+(d+4)\mathbb E S^2/12\) yields
\[
\lambda_{\perp}=\frac{(d+1)(d+2)}{12d(d-1)}\mathbb E S^2.
\]
Substitution and simplification give exactly the two eigenvalues stated under Finding. Since the reference cube has \(\operatorname{vol}=2^d\) and covariance \(I_d/3\), its squared isotropic constant is \(1/12\). Taking the determinant and normalizing the volume proves the boxed isotropic-constant identity.

**Step 4 (sharp optimization).** Denote the expression inside the \(d\)-th root of the ratio by \(R_d(t)\). Logarithmic differentiation and exact cancellation give
\[
\frac{d}{dt}\log R_d(t)=
\frac{2d(d-1)t(t-1)}{(1+dt)(1+(d+2)t)(1+2t+dt^2)}.
\]
All denominator factors are strictly positive for \(t\ge0\), and \(d(d-1)>0\). Hence the derivative is negative on \((0,1)\) and positive on \((1,\infty)\); \(t=1\) is the unique global minimizer, including comparison with the boundary \(t=0\). At \(t=1\),
\[
R_d(1)=\frac{(d+3)^d}{(d+1)^{d+1}},
\]
which gives the minimum displayed above. The derivative strictness on \((0,1)\) also proves it lies strictly below \(L([-1,1]^d)^2=1/12\). No finite-dimensional approximation enters this argument.

## Verification

The standalone file `check_isocanted.py` recomputes uniform-volume covariance by an independent exact-rational method: it constructs vertices of the zonotope, triangulates the boundary numerically only to determine its face incidences, and integrates volume and quadratic moments over the resulting origin-based simplices using exact rational determinants. The 12 cases in dimensions two through four (with several rational cant parameters per dimension) match the analytic volume and **all covariance matrix entries** exactly; 592 facet simplices are integrated. Three symbolic checks independently verify the conditional-moment covariance reductions and logarithmic-derivative factorization. Run `python check_isocanted.py` with Python 3, SciPy, NumPy, and SymPy. The observed success marker is `ISOCANTED_COVARIANCE_EXACT_CHECKS_PASSED 12 592 3`. The all-dimensional proof is the displayed integration and algebra, not a finite enumeration.

## Relationship to prior work

De la Puente and Clavería (2020) introduce isocanted alcoved polytopes and establish their combinatorics and zonotope structure. Their later *The volume of an isocanted cube is a determinant* (first publicly posted in June 2024) proves the volume and the Minkowski-sum representation used here. Both contributions are explicitly prior, not new results. The present claim concerns uniform-volume covariance, the exact affine-invariant isotropic constant, and the universal sharp minimizing cant ratio; the identified source results do not calculate these quantities or imply the minimizer. Other related published results treat John/Löwner ellipsoids and extremal Euclidean vertex radii of isocanted cubes, not their uniform interior-volume inertia. An earlier equivalent covariance/inertia computation outside the inspected terminology remains possible; no claim of independently certified priority is made.

## Limitations

The theorem concerns the diagonal-segment zonotope family \(K_d(t)\) with **equal** coordinate lengths and equal cant parameters. It does not optimize over arbitrary zonotopes, anisotropic alcoved bodies, or other convex bodies. The parameter \(t\) is finite; no claim about the degenerate \(t=\infty\) body is needed. Exact covariance formulas do not identify any extremum among all convex bodies. Historical-priority searches cannot rule out differently named earlier formulas.

## References

1. María Jesús de la Puente and Pedro Luis Clavería, *Isocanted alcoved polytopes*, first arXiv version dated 2020-09-29, arXiv:2009.13858, https://arxiv.org/abs/2009.13858. Primary MSC 52B12.
2. M. J. de la Puente and P. L. Clavería, *The volume of an isocanted cube is a determinant*, first arXiv version dated 2024-06-03, arXiv:2406.01565, https://arxiv.org/abs/2406.01565. Theorem 3.1 establishes the volume and its proof gives the zonotope decomposition.
3. M. J. de la Puente, *Isocanted cube: the lower Lebesgue volumes, incidence numbers and symmetries of this d-dimensional tile*, *Extracta Mathematicae* 40 (2025), 1–26, https://doi.org/10.17398/2605-5686.40.1.1. This later work addresses face measures and symmetry rather than uniform interior-volume covariance.
