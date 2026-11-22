# Santaló volume of the regular-simplex Cayley bipolar cubes: an exact profile and an asymptotic factor of \(e\)

## Finding

For every integer \(n\ge2\), let \(v_1,\ldots,v_{n+1}\in\mathbb R^n\) be the vertices of a regular simplex centered at the origin and normalized by \(\langle v_i,v_i\rangle=1\) and \(\langle v_i,v_j\rangle=-1/n\) when \(i\ne j\). Put \(Q_n=\operatorname{conv}\{v_i\}\), so \(Q_n^\circ=-nQ_n\), and consider the centered-height Cayley polytope
\[
C_n=\operatorname{conv}\bigl((Q_n,-1)\cup(Q_n^\circ,1)\bigr)\subset\mathbb R^{n+1}.
\]
By Pavlík's 2026 construction, its polar about an interior point is a combinatorial \((n+1)\)-cube. This work determines the full polar-volume profile, Santaló center, and asymptotic volume product of that specific geometric realization.

For \(-1<z<1\) put \(a_{n,k}(z)=(1-z)(n+1-k)+(1+z)nk\), for \(1\le k\le n\). The exact volume product about the axial point \((0,z)\) is
\[
\boxed{\displaystyle
\mathcal P_n(z):=\operatorname{vol}_{n+1}(C_n)\operatorname{vol}_{n+1}\bigl((C_n-(0,z))^\circ\bigr)
=\frac{2^{n+2}(n+1)^{2n-1}}{n!(1-z^2)\prod_{k=1}^n a_{n,k}(z)}.}
\tag{1}
\]
The unique Santaló point is \((0,z_n)\), where \(z_n\in(0,1)\) is the unique solution of
\[
\boxed{\displaystyle
\frac{2z_n}{1-z_n^2}=
\sum_{k=1}^n\frac{(n+1)(k-1)}{(1-z_n)(n+1-k)+(1+z_n)nk}.}
\tag{2}
\]
It tends toward the larger polar-simplex base at an exact first-order rate \(n(1-z_n)\to2\). Most notably, although every polar is combinatorially a cube, its *Santaló* volume product tends to a constant multiple of the \((n+1)\)-simplex reference product:
\[
\boxed{\displaystyle
\lim_{n\to\infty}\frac{\mathcal P_n(z_n)}{(n+2)^{n+2}/((n+1)!)^2}=e.}
\tag{3}
\]
The first nontrivial displacement is already nonzero: \(z_2=(2\sqrt{13}-5)/9\), and \(\mathcal P_2(z_2)=(351\sqrt{13}-945)/32\).

## Assumptions and scope

All volumes use ordinary Euclidean Lebesgue measure in the indicated affine dimension, and polarity is \(K^\circ=\{y:\langle x,y\rangle\le1\ \forall x\in K\}\) with the origin in the interior. The axial point \((0,z)\) is in the interior for \(-1<z<1\); the polar-volume identity (1) uses that point, whereas (3) uses the unique Santaló point. The reference \((n+2)^{n+2}/((n+1)!)^2\) is the established volume product of an \((n+1)\)-simplex at its centroid, not the symmetric cube benchmark. The shape \(C_n\) is a particular Cayley realization, not an arbitrary realization of the combinatorial cube.

## Proof

**1. The Cayley construction and its primal volume.** The regular-simplex identities imply \(Q_n^\circ=-nQ_n\). Pavlík proves that this regular simplex satisfies the interval condition (I) and that translating and polarizing \(\operatorname{Cay}(Q_n,Q_n^\circ)\) gives the claimed combinatorial cube; see [1, Theorem 5.2 and Proposition 5.6]. The symmetry also shows the distinguished axial line is invariant under the full vertex-permutation group.

For the standard simplex \(\Delta_n=\{x_i\ge0,\ \sum_i x_i\le1\}\), an elementary orthant decomposition gives, for \(a,b\ge0\),
\[
\operatorname{vol}_n(a\Delta_n-b\Delta_n)
=\frac1{n!}\sum_{k=0}^n\binom nk^2 a^{n-k}b^k.\tag{4}
\]
Indeed, in an orthant with exactly \(k\) negative coordinates, membership is equivalent to the positive-coordinate sum being at most \(a\) and the absolute negative-coordinate sum being at most \(b\). Its contribution is \(a^{n-k}b^k/((n-k)!k!)\), and there are \(\binom nk\) such orthants. Affine equivalence, with the same linear map applied to both reflected simplices, transfers (4) to \(Q_n\). Integrating horizontal sections of \(C_n\), at heights \(2t-1\), gives
\[
\operatorname{vol}_{n+1}(C_n)
=2\operatorname{vol}_n(Q_n)\int_0^1\sum_{k=0}^n\binom nk^2(1-t)^{n-k}(nt)^k\,dt
=2(n+1)^{n-1}\operatorname{vol}_n(Q_n).\tag{5}
\]
The beta integral \(\int_0^1 t^k(1-t)^{n-k}dt=k!(n-k)!/(n+1)!\) and the binomial theorem give the last equality. An edge determinant yields \(\operatorname{vol}_n(Q_n)=(n+1)^{(n+1)/2}/(n!n^{n/2})\); hence
\[
\operatorname{vol}_{n+1}(C_n)=\frac{2(n+1)^{(3n-1)/2}}{n!n^{n/2}}.\tag{6}
\]

**2. Exact axial polar volume.** Write a dual point as \((u,s)\in\mathbb R^n\times\mathbb R\) and let \(t_i=\langle u,v_i\rangle\). The defining inequalities of \((C_n-(0,z))^\circ\) are
\[
t_i-(1+z)s\le1,\qquad -nt_i+(1-z)s\le1\qquad(1\le i\le n+1).
\]
Thus, for fixed \(u\), the possible \(s\) form an interval whose length is
\[
\frac{2-(1-z)\max_i t_i+(1+z)n\min_i t_i}{1-z^2},
\]
when its numerator is nonnegative, and the fiber is empty otherwise. Since \(\sum_i t_i=0\) and \(\sum_i t_i^2=(n+1)\|u\|^2/n\), the \(u\)-to-\(t\) map multiplies Euclidean lengths by \(\sqrt{(n+1)/n}\).

Divide the sum-zero \(t\)-hyperplane into the \((n+1)!\) ordered chambers, and on any one write successive gaps \(g_j=t_{(j+1)}-t_{(j)}\ge0\), \(1\le j\le n\). Then
\[
\min_i t_i=-\frac1{n+1}\sum_{j=1}^n(n+1-j)g_j,\qquad
\max_i t_i=\frac1{n+1}\sum_{j=1}^njg_j.
\]
The gap-to-\(t\) Euclidean Jacobian is \(1/\sqrt{n+1}\), as follows by taking the determinant of the tridiagonal Gram matrix of the successive-difference basis. The total Jacobian from gaps to \(u\) is therefore \((n/(n+1))^{n/2}/\sqrt{n+1}\). The fiber length on that chamber becomes
\[
\frac{2-\frac1{n+1}\sum_{j=1}^n[(1-z)j+(1+z)n(n+1-j)]g_j}{1-z^2}.
\]
Integrating this linear tent over its positive simplex of support, multiplying by \((n+1)!\) chambers, and reindexing \(k=n+1-j\), yields
\[
\operatorname{vol}_{n+1}((C_n-(0,z))^\circ)
=\frac{2^{n+1}n^{n/2}(n+1)^{(n-1)/2}}
{(1-z^2)\prod_{k=1}^n a_{n,k}(z)}.\tag{7}
\]
Multiplication by (6) proves (1).

**3. The unique Santaló point.** The vertex-permutation symmetries of \(Q_n\) preserve \(C_n\) and fix exactly the axial line. The Santaló point is unique, belongs to the interior, and is fixed by every affine symmetry; it is therefore \((0,z_n)\) for some \(-1<z_n<1\). Differentiating (1) gives
\[
\frac{d}{dz}\log\mathcal P_n(z)
=\frac{2z}{1-z^2}-\sum_{k=1}^n\frac{(n+1)(k-1)}{a_{n,k}(z)}.\tag{8}
\]
Here \(a_{n,k}'(z)=(n+1)(k-1)\). The derivative of (8) is strictly positive, because
\[
\frac{d^2}{dz^2}\log\mathcal P_n(z)
=\frac{2(1+z^2)}{(1-z^2)^2}
+\sum_{k=1}^n\left(\frac{(n+1)(k-1)}{a_{n,k}(z)}\right)^2>0.
\]
For \(n\ge2\), (8) is negative at \(z=0\) and tends to \(+\infty\) as \(z\uparrow1\). Hence there is exactly one zero, in \((0,1)\), and it is the Santaló minimizer. At \(n=2\) the equation reduces to \(9z^2+10z-3=0\), giving the stated radical and product.

**4. Asymptotics.** Set \(z=1-s/n\) for a fixed \(s>0\). Uniformly for \(s\) in compact subsets of \((0,\infty)\), equation (8), divided by \(n\), tends to \(1/s-1/2\): the first term has limit \(1/s\), while the second is a Cesàro mean with all but a vanishing fraction of its summands tending to \(1/2\). Because (8) is strictly increasing in \(z\), evaluating at \(s=2-\varepsilon\) and \(s=2+\varepsilon\) traps its unique zero and proves \(n(1-z_n)\to2\).

More precisely, with \(z=1-s/n\), for \(1\le k\le n\),
\[
a_{n,k}(z)=2nk\left(1-\frac{s}{2n}
+\frac{s(n+1-k)}{2n^2k}\right).
\]
Uniformly for compact positive \(s\)-intervals, a logarithmic expansion followed by summation gives
\[
\sum_{k=1}^n\log a_{n,k}(1-s/n)
=n\log(2n)+\log(n!)-s/2+o(1),
\]
since \(\sum_{k=1}^n(n+1-k)/k=O(n\log n)\). Also \(1-(1-s/n)^2=2s/n+O(n^{-2})\), and \((n+1)^{2n-1}=n^{2n-1}e^{2+o(1)}\). Substitution in (1) yields
\[
\mathcal P_n(1-s/n)
=\frac{n^n}{(n!)^2}\exp\left(2+\frac s2+\log\frac2s+o(1)\right).
\]
At \(s=n(1-z_n)\to2\), this becomes \(\mathcal P_n(z_n)\sim e^3 n^n/(n!)^2\). The \((n+1)\)-simplex reference product is asymptotic to \(e^2 n^n/(n!)^2\), which proves (3).

## Verification

Run `python verify_cayley.py` with Python 3, NumPy and SciPy. The program checks the planar radical and exact rational coefficients, then builds the primal convex hull and polar halfspace intersection independently for dimensions \(n=2,\ldots,6\). Its 35 independent volume comparisons at the midpoint, Santaló point, and an additional off-center point match (6) and (7) to relative tolerance \(5\cdot10^{-8}\). It also checks the derivative sign bracketing and reports approaching values of \(n(1-z_n)\) and the normalized product for dimensions up to 2000. These finite computations support, but do not replace, the all-dimensional proof above.

## Relationship to prior work

Pavlík [1, Theorem 5.2 and Proposition 5.6] establishes the combinatorial cube realization via the polar of the Cayley polytope of a regular simplex and its polar. That is the motivating construction; the referenced paper does not evaluate its volume profile, Santaló point, or volume-product limit. The known exact Santaló profile of reflected-simplex Minkowski sums [2] concerns the fixed-dimensional *horizontal sections* appearing in (5), not the \((n+1)\)-dimensional Cayley body, whose off-center polar requires the separate fiber computation (7). A different evaluation for ratio-bounded central simplex polytopes [3] concerns polytopes inside a single simplex hyperplane with pairwise ratio constraints, rather than the two-level Cayley geometry. General Santaló-center theory [4] provides uniqueness but neither (1) nor (3). A broader implicit overlap in older literature is possible, but no equivalent explicit specialization was identified in the inspected materials.

## Limitations

The exact results concern a **regular** simplex with the specified height and polarity conventions, although its volume product is invariant under invertible linear transformations of the whole \((n+1)\)-space. The result does not minimize volume product over all combinatorial cubes, all Cayley realizations, or all convex bodies. The asymptotic comparison is with the simplex reference product, not with the symmetric Hanner-polytope benchmark. The analytic proof uses standard uniqueness of the Santaló point and standard beta integration. Its historical priority remains open to independent literature examination.

## References

[1] Jan Pavlík, *Face lattices of polytopes and bipolar polytopes*, arXiv:2611.13896v1, first posted 2026-11-10 UTC, especially Section 5.1 and Proposition 5.6. https://arxiv.org/abs/2611.13896

[2] *Strict Mahler-product monotonicity along simplex asymmetric difference bodies*, published research record, 2026-10-11, especially the reflected-simplex volume formula and sorting-chamber calculation. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-strict-mahler-product-monotonicity-along-simplex-asymmetric-diff--516fa817d276

[3] *Exact polar volumes of ratio-bounded simplex central polytopes*, published research record, 2026-11-08, particularly its polar-volume formula. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-polar-volumes-of-ratio-bounded-simplex-central-polytopes--d79d6553a85b

[4] *Matching centroids by a projective transformation*, Geometriae Dedicata, 2023, particularly the characterization and uniqueness of the Santaló point. https://doi.org/10.1007/s10711-023-00789-9
