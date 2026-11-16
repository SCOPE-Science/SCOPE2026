# Sharp sextic onset and rigidity for harmonic polynomials vanishing on cube edges

## Finding
Let \(Q=[-1/2,1/2]^3\) and \(E\subset Q\) be the union of its twelve edges. For every real or complex polynomial \(P\in\mathbb C[x,y,z]\) satisfying \(\Delta P=0\) in \(\mathbb R^3\) and \(P|_E=0\), either \(P=0\), or \(\deg P\ge6\). Moreover, the complete space of such polynomials of degree at most six is exactly
\[
\{c(x^2-y^2)(x^2-z^2)(y^2-z^2):c\in\mathbb C\}.
\]
Thus the least degree is six and its nonzero achiever is unique up to a scalar. The same statements hold over the real coefficients.

## Assumptions and scope
Here \(\Delta=\partial_x^2+\partial_y^2+\partial_z^2\), total polynomial degree is used, and vanishing means the entire twelve line segments, not merely their vertices or midpoints. Polynomial continuation converts vanishing on each edge segment into vanishing on its supporting affine line. The same claim is valid for any centered axis-aligned cube by scaling and translation. No assertion is made for general entire harmonic functions or for higher-dimensional cubes.

## Proof
**Algebraic reduction.** Scale coordinates so the edges belong to \([-1,1]^3\). Set \(u=x^2-1\), \(v=y^2-1\), \(w=z^2-1\). Every polynomial has a unique parity decomposition
\[
P(x,y,z)=\sum_{\varepsilon\in\{0,1\}^3}
 x^{\varepsilon_1}y^{\varepsilon_2}z^{\varepsilon_3}
 Q_\varepsilon(u,v,w).
\]
This follows from division of polynomials in each variable by its quadratic relation. The twelve supporting lines and the Laplacian are each invariant under coordinate sign flips. Sign averaging shows that each parity summand separately vanishes on the lines and is harmonic. On the lines parallel to the first coordinate, \(v=w=0\) and \(u\) varies through an infinite set, with analogous statements under permutation. Hence each \(Q_\varepsilon\) vanishes on all three coordinate axes in \((u,v,w)\), which is equivalent by monomial inspection to
\[
Q_\varepsilon\in J:=(uv,uw,vw).
\]
Because the decomposition does not mix highest monomials, the bound \(\deg P\le6\) gives \(\deg Q_\varepsilon\le\lfloor(6-|\varepsilon|)/2\rfloor\).

**Harmonicity.** On the \(\varepsilon\)-parity summand, the Laplacian becomes
\[
L_\varepsilon Q=\sum_{j=1}^3 \bigl(4(u_j+1)\partial_{u_j}^2Q+(2+4\varepsilon_j)\partial_{u_j}Q\bigr),
\quad (u_1,u_2,u_3)=(u,v,w).
\]
If \(|\varepsilon|=3\), the degree bound and the minimal degree two of \(J\) force \(Q=0\). If \(1\le|\varepsilon|\le2\), then \(Q=a uv+b uw+c vw\). Put \(A_j=2+4\varepsilon_j\). The three coefficients of \(u,v,w\) in \(L_\varepsilon Q\) form the matrix
\[
\begin{pmatrix}A_2&A_3&0\\A_1&0&A_3\\0&A_1&A_2\end{pmatrix}
\begin{pmatrix}a\\b\\c\end{pmatrix}.
\]
Its determinant is \(-2A_1A_2A_3\ne0\); thus all non-even parity components vanish.

**Even sector and an exact rank certificate.** For \(\varepsilon=(0,0,0)\), the ten-dimensional space of polynomials in \(J\) of degree at most three has ordered basis
\[
B=(uv,uw,vw,u^2v,uv^2,u^2w,uw^2,v^2w,vw^2,uvw).
\]
The operator \(L_0\) maps this space into the nine-dimensional span of
\[
R=(u^2,v^2,w^2,uv,uw,vw,u,v,w).
\]
Form the integer coefficient matrix \(M_{ij}=[R_i](L_0B_j)\). The nine-column submatrix consisting of columns \(1,2,3,4,5,6,7,8,10\) has determinant exactly \(110592\). Hence \(\operatorname{rank}L_0=9\) and its kernel in this ten-dimensional space has dimension one. The nonzero polynomial
\[
V=(u-v)(u-w)(v-w)
\]
belongs to this kernel: direct differentiation gives \(L_0V=0\). It therefore spans the kernel. Replacing \(u,v,w\) by \(x^2-1,y^2-1,z^2-1\) gives exactly the stated sextic. This proves both nonexistence in lower degree and uniqueness through degree six.

## Verification
The standalone `CHECK.py` uses exact symbolic arithmetic (no numerical tolerances). It constructs the full \(9\times10\) matrix, verifies its rank, its stated \(9\times9\) minor, and injectivity on all six nonzero parity sectors that may occur. It separately differentiates the sextic and restricts it to every one of the twelve supporting lines. Run with Python 3 and SymPy as specified in `requirements.txt`: `python CHECK.py`. This finite exact computation certifies the finite-dimensional linear-algebra step; the proof above explains why it exhausts all polynomial degrees at most six.

## Relationship to prior work
Ioann Vasilyev, *On the zero sets of harmonic polynomials* (first posted 30 June 2025, arXiv:2506.24116), solves Wavre's cube-edge existence problem in arbitrary dimensions and explicitly presents the above Vandermonde-type harmonic polynomial. The construction and harmonicity of that polynomial are **prior work**, not claimed here. The additional theorem is the sharp lower bound on possible degree and the full one-dimensional classification of minimal-degree harmonic polynomials for the three-dimensional cube. Vasilyev's discussion says it does not provide a complete classification of harmonic functions vanishing on the cube edges. Classical reflection-group discriminants concern polynomial vanishing on whole reflection hyperplanes; they do not by themselves settle arbitrary nonhomogeneous harmonic polynomials vanishing only on this affine union of lines. Known results on sampling spherical harmonics at cube vertices concern a strictly weaker condition and cannot imply the present edge-line classification.

## Limitations
This is a polynomial degree-six onset and rigidity result, not a classification at every degree or for all entire harmonic functions. Older unpublished or differently phrased results on cube-skeleton vanishing ideals might cover the statement; publication priority has not been independently audited. The displayed determinant is verifiable with the supplied exact checker. The theorem does not assert uniqueness after degree six.

## References
1. Ioann Vasilyev, *On the zero sets of harmonic polynomials*, arXiv:2506.24116, v1 posted 2025-06-30. https://arxiv.org/abs/2506.24116 ; full text https://arxiv.org/pdf/2506.24116.
2. A. Logunov and E. Malinnikova, *On ratios of harmonic functions*, Adv. Math. 274 (2015), 241–262; arXiv:1402.2888. Different zero-set ratio problem.
3. A. Logunov and E. Malinnikova, *Ratios of harmonic functions with the same zero set*, GAFA 26 (2016), 909–925; arXiv:1506.08041. Different Harnack/ratio problem.
