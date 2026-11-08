# The exact diameter law of random central sections of the four-dimensional bidisc

## Finding

Let \(B_2^2\subset\mathbb R^2\) be the closed unit Euclidean disk and let
\[
K=B_2^2\times B_2^2\subset\mathbb R^4.
\]
Let \(L\) be a Haar-uniform random two-dimensional linear subspace of \(\mathbb R^4\), and let \(D=\operatorname{diam}_2(K\cap L)\), using the ambient Euclidean metric. For
\[
2\le s<2\sqrt2,\qquad \alpha(s)=\arccos\left(\frac8{s^2}-1\right),
\]
the complete distribution function is
\[
\boxed{\Pr\{D\le s\}=1-\cos\alpha(s)-\tfrac12\alpha(s)\sin\alpha(s).}
\]
It is zero below \(2\) and one at and above \(2\sqrt2\). The continuous density on \((2,2\sqrt2)\) is
\[
\boxed{f_D(s)=\frac8{s^3}\left(1-\alpha(s)\cot\alpha(s)\right).}
\]
At the upper endpoint the distribution has the **positive atom**
\[
\boxed{\Pr\{D=2\sqrt2\}=\frac\pi4.}
\]
The remaining mass \(1-\pi/4\) is absolutely continuous. Near the lower endpoint, \(\Pr(D\le2+\varepsilon)=\tfrac23\varepsilon^2+O(\varepsilon^3)\) as \(\varepsilon\downarrow0\).

## Assumptions and scope

The body is exactly the Cartesian product of two radius-one, two-dimensional Euclidean disks; it is a centrally symmetric convex body with a nonsmooth boundary. The section is a **linear central plane**, not an affine section, and has normalized Haar distribution on the real (unoriented) Grassmannian \(\mathrm{Gr}(2,4)\). All diameters use the ambient Euclidean metric. The law is not asserted for unequal disk radii, noncentral sections, or higher-dimensional products.

## Proof

**1. Deterministic reduction to a compressed projection.** Write \(\mathbb R^4=A\oplus B\), with both summands two-dimensional, and let \(P_A\) be orthogonal projection onto \(A\). For every Euclidean unit direction \(w\in L\), the radial length of \(K\cap L\) in direction \(w\) is
\[
r_K(w)=\frac1{\max\{\|P_Aw\|_2,\|(I-P_A)w\|_2\}}
=\frac1{\sqrt{\max\{\lambda(w),1-\lambda(w)\}}},\quad
\lambda(w)=\|P_Aw\|_2^2.
\]
Since the section is centrally symmetric, its diameter is twice its maximal radial length. Let \(\lambda_-\le\lambda_+\) denote the two eigenvalues of \(P_A\) compressed to \(L\). The Rayleigh quotient covers exactly \([\lambda_-,\lambda_+]\). Consequently,
\[
D=\frac2{\sqrt{\max\{\tfrac12,\lambda_-,1-\lambda_+\}}}.
\]
In particular \(2\le D\le2\sqrt2\). For \(2<s<2\sqrt2\), put \(t=4/s^2\in(1/2,1)\), and \(c=2t-1=8/s^2-1\). The condition \(D\le s\) says that the whole Rayleigh interval avoids \((1-t,t)\), so
\[
\{D\le s\}=\{\lambda_-\ge t\}\sqcup\{\lambda_+\le1-t\}.
\]
Interchanging \(A\) and \(B\) is an orthogonal symmetry of Haar measure, and exchanges these two disjoint events. Therefore
\[
\Pr(D\le s)=2\Pr(2\lambda_--1\ge c).
\]

**2. Two independent uniform coordinates on the Grassmannian.** Temporarily orient \(L\), choose a positive oriented orthonormal basis \(u,v\), and write its unit decomposable bivector \(\omega=u\wedge v\). Its self-dual and anti-self-dual parts \(\omega_{\pm}=(\omega\pm\star\omega)/2\) each have squared norm \(1/2\), because \(\omega\wedge\omega=0\). The map \(L\mapsto(\sqrt2\omega_+,\sqrt2\omega_-)\) identifies the oriented Grassmannian with \(S^2\times S^2\); by the \(\mathrm{SO}(4)\) action (whose two factors act independently), normalized Haar measure corresponds to the product of uniform measures on these two spheres. The first coordinate of a uniform point of \(S^2\) is uniform on \([-1,1]\).

Define the Plücker coordinates \(p_{ij}=u_iv_j-u_jv_i\). It follows that
\[
U=p_{12}+p_{34},\qquad V=p_{12}-p_{34}
\]
are **independent uniform** variables on \([-1,1]\). Although \(U,V\) change sign under orientation reversal, the event of interest is orientation-independent.

**3. Exact compressed eigenvalues.** Let \(Q\) be the \(4\times2\) matrix with columns \(u,v\) and set \(M=Q^{\mathsf T}(2P_A-I)Q\). Its two eigenvalues are \(2\lambda_\pm-1\). Directly from the Plücker minors (or from the determinant of each two-row block),
\[
\operatorname{tr}M=2(p_{12}^2-p_{34}^2)=2UV,
\qquad
\det M=2(p_{12}^2+p_{34}^2)-1=U^2+V^2-1.
\]
Solving the characteristic quadratic gives
\[
2\lambda_--1=UV-\sqrt{(1-U^2)(1-V^2)},
\quad
2\lambda_+-1=UV+\sqrt{(1-U^2)(1-V^2)}.
\]
Here the square root is real since \(|U|,|V|\le1\). The event \(2\lambda_--1\ge c>0\) is possible only when \(U,V\) have the same sign. Its two same-sign quadrants have equal probability. In the positive quadrant let \(U=\cos a\), \(V=\cos b\), with \(0\le a,b\le\pi/2\). Then
\[
2\lambda_--1=\cos(a+b).
\]
Writing \(\gamma=\arccos c\in(0,\pi/2)\), the condition is exactly \(a+b\le\gamma\).

**4. Evaluation of the angular probability.** Since \(U,V\) are independent uniform \([-1,1]\), the Jacobian on each positive quadrant is \(\sin a\sin b/4\). Including both same-sign quadrants gives
\[
\Pr(2\lambda_--1\ge c)
=\frac12\int_{\substack{a,b\ge0\\a+b\le\gamma}}\sin a\sin b\,da\,db.
\]
The one-dimensional integration yields
\[
\int_0^\gamma\sin a\,[1-\cos(\gamma-a)]\,da
=1-\cos\gamma-\frac\gamma2\sin\gamma.
\]
Multiplication by the factor two from Step 1 proves the cumulative distribution formula for every interior \(s\). Its derivative gives the stated positive density, since \(\alpha'(s)=16/(s^3\sin\alpha(s))\).

**5. The endpoint atom.** The maximal diameter occurs exactly when the Rayleigh interval contains \(1/2\), equivalently \(\det M\le0\). By Step 3 this is \(U^2+V^2\le1\), a unit disk inside the square \([-1,1]^2\). Its probability is its area \(\pi\) divided by the square's area \(4\), proving the atom \(\pi/4\). The CDF's interior limit at the upper endpoint is \(1-\pi/4\), consistent with this jump. At the lower endpoint, \(\alpha\to0\), and the expansion \(1-\cos\alpha-\alpha\sin\alpha/2=\alpha^4/24+O(\alpha^6)\), together with \(\alpha(2+\varepsilon)^2=4\varepsilon+O(\varepsilon^2)\), gives \(2\varepsilon^2/3+O(\varepsilon^3)\).

## Verification

The accompanying `verify.py` is a standard-library independent numerical verifier. It reconstructs five angular probabilities by a separate numerical quadrature, checks the Plücker trace and determinant identities on 240 Haar frames, checks eight section diameters by direct geometric radial searches, and checks 18,000 Haar frames against the endpoint atom and five CDF thresholds. It ran successfully. None of these finite numerical tests replaces the deterministic and measure-theoretic proof above.

## Relationship to prior work

Guedon, Litvak, Tatarko and Vritsiou, *On random diameters of convex bodies* (arXiv:2609.24131v1, first public 21 September 2026), develop general high-probability upper and lower estimates for random-section diameters and apply them to diagonal \(\ell_p\)-ellipsoids. Their accessible complete article, including its examples and two-level diagonal-ellipsoid subsection, does not state a distribution for the product of two Euclidean disks. The bidisc is an \(\ell_\infty\)-sum of two Euclidean planes and is not a diagonal \(\ell_p\)-ellipsoid in the Euclidean metric.

Exact random-radius laws for one-spike Euclidean ellipsoids follow from rank-one compression and beta distributions; the one-spike case has no positive maximal-diameter atom in nondegenerate parameters. Another exact law concerns planar sections of the three-dimensional crosspolytope/octahedron and has no atoms. Neither statement implies the bidisc's new two-coordinate law, where the positive atom is the disk area in a square of independent Grassmannian coordinates. Classical principal-angle and Grassmannian parametrizations underlie the proof; these background facts are not claimed as novel.

## Limitations

This is an exact calculation for one dimension and one natural nonsmooth product body; no full classification of random-section laws for general norm products is claimed. The precise formula may be implicit in older calculations using complex bidisc, double disk, product-cylinder, or principal-angle terminology. Targeted literature and available research-record searches found no equivalent result, but exhaustive historical priority and independent audit remain unperformed. The numerical verifier gives supporting finite checks, not a proof of infinite assertions.

## References

1. O. Guedon, A. E. Litvak, K. Tatarko and B.-H. Vritsiou, *On random diameters of convex bodies*, arXiv:2609.24131v1 (first submitted 21 September 2026), full HTML manuscript at https://arxiv.org/abs/2609.24131.
2. K. Ye and L.-H. Lim, *Schubert varieties and distances between subspaces of different dimensions*, arXiv:1407.0900 (2014); standard principal-angle background.
3. *Exact random-radius law for one-spike ellipsoids in every codimension*, public research record (2026), published-finding corpus/2026: `2026/10/11/SCOPE-exact-random-radius-law-for-one-spike-ellipsoids-in-every-codime--e99f37d3b7ae`.
4. *Exact Haar diameter law for central sections of the regular octahedron*, public research record (2026), published-finding corpus/2026: `2026/10/11/SCOPE-exact-haar-diameter-law-for-central-sections-of-the-regular-octa--4948185eba2f`.
