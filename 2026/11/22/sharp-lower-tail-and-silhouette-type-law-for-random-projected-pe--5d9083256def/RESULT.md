# Sharp lower-tail and silhouette-type law for random projected perimeters of a regular tetrahedron

## Finding
Let \(T\) be the regular tetrahedron with vertices
\[
(1,1,1),\quad(1,-1,-1),\quad(-1,1,-1),\quad(-1,-1,1).
\]
Its edges have length \(2\sqrt2\). For a Haar-uniform direction \(U\in S^2\), write \(P(U)\) for the Euclidean perimeter of the orthogonal projection of \(T\) onto \(U^\perp\), and let \(N(U)\) be its generic number of vertices. Then
\[
P_*:=\min_{u\in S^2}P(u)=2\sqrt2+2\sqrt6,
\]
with precisely twelve oriented minimizers: all signed coordinate permutations of \((1,1,0)/\sqrt2\).

Define
\[
\phi_*:=\arctan\sqrt2,\qquad
A_4:=\frac18\int_0^{\phi_*}\frac{d\phi}{(\sqrt2-\sqrt{2/3}\cos\phi)^2},\qquad
A_3:=\frac3{32\sqrt2}.
\]
The **sharp random lower-tail** and **conditional silhouette law** are
\[
\Pr\{P\le P_*+\varepsilon}\}=\frac{12}{\pi}(A_4+A_3)\varepsilon^2+o(\varepsilon^2),
\qquad
\lim_{\varepsilon\downarrow0}\Pr\{N=3\mid P\le P_*+\varepsilon}\}=\frac{A_3}{A_4+A_3}.
\]
The lower-tail coefficient is \(1.1953469179961405\ldots\); the limiting triangular-silhouette fraction is \(0.2118330336632897\ldots\), and the quadrilateral fraction is its complement.

There is a **marked geometric limit**. Near any one minimizer \(u_0=(1,1,0)/\sqrt2\), choose tangent orthonormal vectors \(e_p=(1,-1,0)/\sqrt2\), \(e_q=(0,0,1)\) and represent a direction by \(u(p,q)=(u_0+pe_p+qe_q)/\sqrt{1+p^2+q^2}\). Conditionally on \(P\le P_*+\varepsilon\), the scaled pair \((p/\varepsilon,q/\varepsilon)\) converges weakly to the **uniform area distribution** on \(D=\{F(p,q)\le1}\), with
\[
F(p,q)=\begin{cases}
2\sqrt2\sqrt{p^2+q^2}-2\sqrt{2/3}|p|,&|q|\le\sqrt2|p|,\\
4|q|/\sqrt3,&|q|\ge\sqrt2|p|.
\end{cases}
\]
The twelve minimizing neighborhoods receive asymptotically equal conditional mass. The triangular portion of \(D\) is exactly \(|q|>\sqrt2|p|\).

## Assumptions and scope
All results refer to the **single fixed coordinate tetrahedron** above, to an **unbiased uniform normal** on \(S^2\), and to **orthogonal**, not perspective, projection. The perimeter surplus \(\varepsilon\) is an absolute Euclidean length. The exceptional normal directions with coincident projected vertices have zero spherical measure; at those directions the perimeter remains well-defined, and \(N\) is used only almost surely. Antipodal normals give the same projection, but both are counted in the uniform spherical law. The conditional tangent limit means the usual weak convergence of bounded continuous test functions, with local frames transported by the symmetries of the tetrahedron. The equality of the two formulas defining \(F\) at \(|q|=\sqrt2|p|\) is immediate.

## Proof
**1. Exact perimeter and silhouette partition.** By tetrahedral symmetries and invariance of perimeter under central inversion, it suffices to write the sorted absolute normal coordinates as \(x\ge y\ge z\ge0\), \(x^2+y^2+z^2=1\). Put \(f(t)=\sqrt{2-t^2}\). Each edge of the tetrahedron has length \(2\sqrt2\) and its projected length is \(2f(u\cdot e)\), where \(e\) is the corresponding unnormalized half-edge difference of Euclidean norm \(\sqrt2\). An edge belongs to the projected hull when its two incident face normals have opposite viewing signs. Checking the four signed face forms gives, away from their zero sets,
\[
\begin{aligned}
P(u)&=2\bigl[f(x-y)+f(y-z)+f(x-z)\bigr],&&x<y+z\quad (N=3),\\
P(u)&=2\bigl[f(x+y)+f(x-y)+f(x+z)+f(x-z)\bigr],&&x>y+z\quad (N=4).
\end{aligned}
\tag{1}
\]
At \(x=y+z\) both expressions agree by continuity; these branch formulas can also be checked by direct planar convex hulls of the four vertices. This exact distinction is crucial: the lower-tail event is not determined by the known area distribution.

**2. The sharp global minimum in the triangular branch.** Set \(d_1=x-y\), \(d_2=y-z\), \(d_3=x-z=d_1+d_2\). The triangular inequality \(x\le y+z\) implies \(y\ge d_3\); also \(x\ge d_3\), so \(1\ge x^2+y^2\ge2d_3^2\). In particular \(0\le d_i\le1/\sqrt2\). Concavity of \(f\) gives its endpoint chord lower bound
\[
f(t)\ge\sqrt2-(2-\sqrt3)t\qquad(0\le t\le1/\sqrt2).
\]
Equation (1) therefore implies
\[
\frac{P(u)}2\ge3\sqrt2-(2-\sqrt3)(d_1+d_2+d_3)
=3\sqrt2-2(2-\sqrt3)d_3\ge\sqrt2+\sqrt6.
\]
Equality forces \(d_3=1/\sqrt2\) and \(x=y=1/\sqrt2\), \(z=0\).

**3. The sharp global minimum in the quadrilateral branch.** Let \(r=\sqrt{y^2+z^2}\), \(x=\sqrt{1-r^2}\). Since \(x\ge y+z\), one has \(0\le r\le1/\sqrt2\) and \(x\ge r\). For fixed \(x\), define \(h_x(s)=f(x+\sqrt s)+f(x-\sqrt s)\) on the relevant interval. This is **strictly concave** in \(s\): the absolutely convergent binomial expansion \(f(v)=\sqrt2\,[1-\sum_{k\ge1}a_k v^{2k}]\), with all \(a_k>0\), makes every nonlinear power of \(s\) in \(h_x\) nonpositive, and the coefficient of \(s^2\) strictly negative (also by continuity at boundary). Hence
\[
h_x(y^2)+h_x(z^2)\ge h_x(r^2)+h_x(0).
\]
Using \(x^2+r^2=1\), \(f(x+r)=x-r\), \(f(x-r)=x+r\), and \(f(x)=\sqrt{1+r^2}\), (1) gives
\[
P(u)\ge4\bigl(\sqrt{1-r^2}+\sqrt{1+r^2}\bigr)
\ge4\left(\frac1{\sqrt2}+\sqrt{3/2}\right)=P_*.
\]
The function in parentheses decreases strictly on \((0,1/\sqrt2]\). Equality requires \(r=1/\sqrt2\), \(y=r\), \(z=0\), yielding \(x=y=1/\sqrt2\), \(z=0\). In the full sphere, these yield exactly twelve signed and permuted oriented normal vectors, isolated from each other.

**4. First-order tangent geometry.** Fix \(u_0\) and \(u(p,q)\) as in the finding. By coordinate sign symmetries, the perimeter and silhouette label depend locally only on \(|p|,|q|\). In the first quadrant, \(x-y=\sqrt2p/\sqrt{1+p^2+q^2}\) and \(z=q/\sqrt{1+p^2+q^2}\). Thus the triangle branch is precisely \(q>\sqrt2p\). Substitution into (1), with \(s=\sqrt{p^2+q^2}\downarrow0\), yields the **uniform angular** expansion
\[
P(u(p,q))-P_*=F(p,q)+O(s^2).
\tag{2}
\]
Indeed the quadrilateral branch has linear term \(2\sqrt2s-2\sqrt{2/3}p\), while the triangular branch has \(4q/\sqrt3\). The branches agree at their common ray and their error bounds are uniform on its two closed angular sectors. Since \(F\) is continuous, positive away from the origin, and homogeneous of degree one, its sublevel set \(D\) is compact with positive finite area.

**5. Exact tangent areas and probability normalization.** Put \(p=s\cos\phi\), \(q=s\sin\phi\) for \(0\le\phi\le\pi/2\), and \(\phi_*=\arctan\sqrt2\). Then the polar radial gauge \(F(s\cos\phi,s\sin\phi)/s\) is
\[
b(\phi)=\begin{cases}
2(\sqrt2-\sqrt{2/3}\cos\phi),&0\le\phi\le\phi_*,\\
(4/\sqrt3)\sin\phi,&\phi_*\le\phi\le\pi/2.
\end{cases}
\]
The quadrantal quadrilateral area of \(D\) is \(A_4=\frac12\int_0^{\phi_*}b(\phi)^{-2}d\phi\); the quadrantal triangular area is
\[
A_3=\frac12\int_{\phi_*}^{\pi/2}b(\phi)^{-2}\,d\phi
=\frac3{32}\cot\phi_*=\frac3{32\sqrt2}.
\]
All four quadrants have equal areas. In the normalized chart \(u(p,q)\), the surface Jacobian is \((1+p^2+q^2)^{-3/2}dp\,dq\). By (2), scaling \((p,q)=\varepsilon(v,w)\), boundedness of \(D\), and dominated convergence, the spherical measure of one neighborhood under \(P\le P_*+\varepsilon\) is \(4(A_4+A_3)\varepsilon^2+o(\varepsilon^2)\). Multiply by twelve disjoint minimizing charts and divide by \(4\pi\) to obtain the first probability formula. Restricting to the triangular sectors gives the conditional fraction \(A_3/(A_3+A_4)\). The same change of variables proves joint weak convergence of the chart label and the rescaled direction: the label is uniform on twelve points and, conditionally on any label, the rescaled pair has normalized Lebesgue measure on \(D\). No finite computation is substituted for this limiting argument.

## Verification
Run `python3 checker.py` from the extracted package with Python 3, NumPy and SciPy available. The checker independently builds a two-dimensional convex hull of the four projected vertices on 2,000 deterministic pseudorandom normals and compares the resulting perimeter and vertex count with (1); also checks extremal bounds, the tangent expansions over an angular grid, exact quadrantal-area constants and small-perimeter probabilities obtained by direct one-dimensional spherical integration. It passed 6,199 assertions on the preparation system. The reported decimal coefficients are numerical quadrature outputs, not independently certified interval enclosures. The proof of the infinite-dimensional statements is entirely in Steps 1–5; random computations and quadrature serve only as reproducibility diagnostics.

## Relationship to prior work
The regular tetrahedron and the Haar projection model are classical. Vickers and Brown (2001) derive the **projected-area** density of the regular tetrahedron and discuss a **joint area–perimeter** distribution for ellipsoids, cylinders and other bodies; their inspected article does not derive the perimeter lower-tail or its triangular-versus-quadrilateral partition for the tetrahedron. Finch (first publicly posted 2012-03-12) investigates random tetrahedral projected-area and projected-perimeter moments and area–perimeter covariance; that integral information does not imply the displayed perimeter-tail coefficient or conditional angular limit. Published further work derives the mixed area–perimeter moment of a regular tetrahedron, the complete **area**-and-silhouette-type law, and a third-order **area**-tail silhouette bias. Their explicitly stated formulas do not cover a *perimeter*-conditioned near-minimum probability or its asymmetric type frequency. This is a comparison of mathematical implications, not a claim that differing titles alone establish priority.

## Limitations
The theorem applies to a single regular tetrahedron in the stated coordinate normalization and Haar-uniform orthogonal projections. It does not yield the full projected-perimeter distribution, other shapes, perspective views, a finite-sample estimator, or a rigorously enclosed decimal for the displayed coefficient. The leading probability asymptotic and weak limit are proved, but no higher-order error coefficient is claimed. Earlier equivalent stereological expressions could exist; the literature search cannot certify universal historical novelty. Independent audit has not yet been performed.

## References
1. S. R. Finch, “Planar Projections and Second Intrinsic Volume,” arXiv:1203.2464v1 (first public 2012-03-12), https://arxiv.org/abs/1203.2464.
2. G. T. Vickers and D. J. Brown, “The Distribution of Projected Area and Perimeter of Convex, Solid Particles,” *Proceedings of the Royal Society A* 457 (2001), 283–306, https://doi.org/10.1098/rspa.2000.0667.
3. “Exact elliptic mixed shadow moment and negative covariance of a regular tetrahedron,” published result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-elliptic-mixed-shadow-moment-and-negative-covariance-of-a--6552ca8e2b99.
4. “A third-order silhouette-type bias at minimum projected area of a regular tetrahedron,” published result, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-third-order-silhouette-type-bias-at-minimum-projected-area-of--ac110ced4659.
5. “Complete type-resolved shadow-area law for a regular tetrahedron,” published result, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-complete-type-resolved-shadow-area-law-for-a-regular-tetrahedron--9659c168bd2e.
