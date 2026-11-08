# Two-equator tomography of cubic spherical harmonics: the 60- and 90-degree blind-spot law

## Finding

Let \(d\ge3\) be an integer, let \(u,v\in S^{d-1}\) be real unit vectors and put \(c=u\cdot v\). Denote by \(\mathcal H_3^d\) the complex vector space of restrictions to \(S^{d-1}\) of homogeneous harmonic cubic polynomials in \(d\) real variables. For each unit normal \(u\), set \(E_u=\{x\in S^{d-1}:u\cdot x=0\}\). Observe the complete complex-valued trace on both equators, rather than merely their integrals, through
\[
R_{u,v}f=(f|_{E_u},f|_{E_v}).
\]
The source carries uniform probability-surface \(L^2\) norm and the target carries the average of uniform probability-equatorial squared norms. The rank and nullspace are unchanged under any pair of strictly positive target weights.

When the equators are distinct, i.e. \(|c|<1\), **the exact nullspace is**
\[
\ker R_{u,v}=\Big\{(u\cdot x)(v\cdot x)(w\cdot x): w\in\ker\big[cI+vu^T+uv^T\big]\Big\}.
\]
The mapping from \(w\) to the displayed polynomial is injective, and hence the complete nullity classification is
\[
\dim\ker R_{u,v}=\begin{cases}
d-2,&c=0,\\
1,&|c|=1/2,\\
0,&0<|c|<1,\ |c|\ne1/2.
\end{cases}
\]
For coincident equators (\(|c|=1\)), \(\dim\ker R_{u,v}=d(d-1)/2\). Since
\[
\dim\mathcal H_3^d=\frac{d(d-1)(d+4)}6,
\]
the rank at every angle is the ambient dimension minus the listed nullity.

Thus **two distinct generically oriented full equators are sufficient for exact recovery of every pure cubic spherical harmonic in every dimension \(d\ge3\)**; one equator never suffices. The only distinct-equator blind spots occur at the perpendicular orientation and at acute dihedral angle \(60^\circ\). At a right angle, the blind family has dimension \(d-2\). At \(60^\circ\), the blind family is one-dimensional for every dimension.

## Assumptions and scope

All normals are real and unit length. Cubic spherical harmonics may have complex coefficients, but the Laplacian is the ordinary real-coordinate Euclidean Laplacian, extended complex linearly. An \(L^2\)-zero trace means zero almost everywhere on the equator, and by continuity hence pointwise zero. Each equator has dimension \(d-2\ge1\). The assertions concern *full function-valued equatorial traces*, not the Funk transform, cap integrals, point-sampling, mixed harmonic degrees, or the stability condition number. The angle between **unoriented hyperplanes** is \(\arccos|c|\in[0,\pi/2]\).

## Proof

**1. Algebraic reduction to a cubic product.** Let \(p\in\mathcal H_3^d\) have zero trace on \(E_u\). If \(y\in u^\perp\setminus\{0\}\), homogeneity gives \(p(y)=\|y\|^3p(y/\|y\|)=0\), and also \(p(0)=0\). Thus \(p\) vanishes identically on the real hyperplane \(u^\perp\). Choose an orthogonal coordinate system with \(u=e_1\); the coefficient of the zeroth power of the first coordinate is therefore the zero polynomial. Hence the linear form \(L_u(x)=u\cdot x\) divides \(p\) in \(\mathbb C[x_1,\dots,x_d]\). The same holds for \(L_v\). For distinct equators these two linear forms are nonproportional and irreducible, hence relatively prime; consequently \(p=L_uL_vL_w\) for a unique linear form \(L_w=w\cdot x\), with \(w\in\mathbb C^d\). Uniqueness follows from the polynomial ring being an integral domain. Conversely every such product vanishes on both equators.

**2. Exact harmonicity criterion.** Differentiate the product of three linear forms twice. Since \(\nabla L_u=u\), \(\nabla L_v=v\), \(\nabla L_w=w\),
\[
\Delta(L_uL_vL_w)=2\big[(u\cdot v)L_w+(u\cdot w)L_v+(v\cdot w)L_u\big]
=2\big[(cI+vu^T+uv^T)w\big]\cdot x.
\]
Thus the product is harmonic exactly when \(A_cw=0\), where \(A_c=cI+vu^T+uv^T\). This is an exact linear criterion over \(\mathbb C\), not a dimensional heuristic.

**3. Diagonalize the criterion at every distinct angle.** Since \(|c|<1\), the nonzero vectors \(u+v,u-v\) are orthogonal; together with the \((d-2)\)-dimensional orthogonal complement of \(\operatorname{span}\{u,v\}\), they decompose \(\mathbb C^d\). Direct calculation gives
\[
A_c(u+v)=(1+2c)(u+v),\quad
A_c(u-v)=(2c-1)(u-v),\quad
A_cw=cw\quad(w\perp u,v).
\]
The eigenvalues are therefore \(1+2c\), \(2c-1\), and \(c\) with multiplicity \(d-2\). The determinant is \(c^{d-2}(4c^2-1)\). Exactly one eigenvalue vanishes when \(c=\pm1/2\), whereas \(d-2\) vanish when \(c=0\); the three possibilities are disjoint. When \(c=1/2\), a generator of the exceptional nullspace is \(L_uL_vL_{u-v}\); when \(c=-1/2\), it is \(L_uL_vL_{u+v}\). When \(c=0\), all and only \(L_uL_vL_w\) with \(w\perp u,v\) are invisible. All other distinct orientations are injective.

**4. Coincident-equator comparison and minimality.** If \(|c|=1\), the two observations are repetitions of the same equator. Rotate \(u\) to \(e_1\) and write \(x=(t,y)\), where \(y\in\mathbb R^{d-1}\). Any cubic vanishing at \(t=0\) has the unique form
\[
p(t,y)=t\big(a t^2+t\,b\cdot y+y^TCy\big),
\]
where \(a\in\mathbb C\), \(b\in\mathbb C^{d-1}\), and \(C\) is a complex symmetric \((d-1)\times(d-1)\) matrix. Taking the Laplacian gives
\[
\Delta p=(6a+2\operatorname{tr}C)t+2b\cdot y.
\]
Thus harmonicity imposes \(b=0\) and \(\operatorname{tr}C=-3a\). The free parameters are exactly the entries of \(C\), giving \((d-1)d/2\) dimensions. This proves that a single equator is never injective. Two distinct nonresonant equators *are* injective by Step 3, so two is the exact minimal number of full equators needed when their orientations may be chosen.

Finally, the general spherical-harmonic dimension is \(\binom{d+2}{3}-d=d(d-1)(d+4)/6\) because the Laplacian maps homogeneous cubics onto linear forms: explicitly \(\Delta[(\|x\|^2)(w\cdot x)]=2(d+2)(w\cdot x)\). Subtracting the proven nullities gives all ranks.

## Verification

The standalone symbolic checker `verify_two_equators.py` verifies, with exact rational and radical arithmetic, the Laplacian/product identity, determinant, eigenspaces, and nullities for dimensions \(3\le d\le8\), orthogonal, \(60^\circ\)-resonant, and generic orientations. It separately constructs the coefficient matrix of homogeneous cubics and verifies the one-equator harmonic nullity without using the explicit formula. The executable reports `TWO_EQUATOR_CUBIC_CHECKS_PASS 291`. The checker is illustrative finite validation; Steps 1–4 are a proof for all integers \(d\ge3\) and all real orientations.

For a concrete \(60^\circ\) witness, take \(u=e_1\), \(v=e_1/2+(\sqrt3/2)e_2\). Then
\[
L_uL_vL_{u-v}=\tfrac14(x_1^3-3x_1x_2^2).
\]
At a right angle, \(u=e_1\), \(v=e_2\), the \(d-2\) independent polynomials \(x_1x_2x_j\) for \(3\le j\le d\) exhibit the entire kernel.

## Relationship to prior work

The known \(60^\circ\) three-hyperplane cubic nodal example is standard: Han's *Harmonic functions and nodal sets*, Section 3.1, explicitly discusses \(\operatorname{Re}(x_1+ix_2)^k\) and its \(k\) equally angled nodal hyperplanes. Olofsson and Wittsten (2022) similarly discuss harmonic polynomial zeros on arithmetic families of planar rays. More importantly, Gröchenig and Jaming (2016), Theorem 4.2, classify when the union of hyperplanes is a Heisenberg uniqueness set for *all* measures supported on the sphere: the associated reflection group must be infinite. For two equators this excludes every rational-multiple-of-\(\pi\) dihedral angle from universal measure uniqueness, but it already guarantees the nonresonant irrational-angle part of the present recovery conclusion (via the spherical harmonic Fourier/Bessel transform identity). The new *finite-degree refinement* is that, for pure cubics, **only** the two rational-angle values \(60^\circ\) and \(90^\circ\) remain exceptional, with different exact nullities. Thus generic uniqueness, Coxeter/reflection methods and the planar sectoral example are acknowledged prior mathematics, rather than claimed as novel. Nafees et al. (2017) optimize finite iso-latitude sampling, and Zandieh–Han–Avron (2022) consider randomized harmonic reconstruction; neither states this finite-degree two-equator exact rank table. An equivalent refinement could still be implicit in earlier nodal-set or reflection literature.

## Limitations

There is no claimed quantitative lower singular-value bound near exceptional angles; exact injectivity may coexist with poor conditioning. The result is not about arbitrary mixtures of degrees, finite point samples, non-great latitudes, or nonlinear phase retrieval. All equatorial traces are assumed accessible with full continuous information. The exact rank argument is elementary, and related geometric uniqueness facts may be implicit in earlier harmonic-nodal-set or reflection-principle literature; historical priority remains provisional. Independent mathematical validation has not been performed.

## References

1. W. Nafees, Z. Khalid, R. A. Kennedy, and J. D. McEwen, *Optimal-Dimensionality Sampling on the Sphere: Improvements and Variations*, arXiv:1709.02497 (first posted 2017-09-08), https://arxiv.org/abs/1709.02497.
2. A. Olofsson and J. Wittsten, *Uniqueness theorems for weighted harmonic functions in the upper half-plane*, arXiv:2201.04575 (first posted 2022-01-12), https://arxiv.org/abs/2201.04575.
3. A. Zandieh, I. Han, and H. Avron, *Near Optimal Reconstruction of Spherical Harmonic Expansions*, arXiv:2202.12995 (first posted 2022-02-25), https://arxiv.org/abs/2202.12995.
4. X. Han, *Harmonic functions and nodal sets*, Section 3.1, https://www.csun.edu/~xiaolong/Han_Nodal.pdf (accessed for its chapter on homogeneous harmonic polynomial nodal hyperplanes).
5. K. Gröchenig and P. Jaming, *The Cramér–Wold theorem on quadratic surfaces and Heisenberg uniqueness pairs*, arXiv:1608.06738 (first posted 2016-08-24), especially Theorem 4.2, https://arxiv.org/abs/1608.06738.
