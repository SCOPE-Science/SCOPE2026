# An optimal thirty-line icosahedral projective design and the complete qutrit orbit-tomography spectrum

## Finding
Let \(G\) be the order-60 rotational symmetry group of a regular icosahedron acting in its faithful real orthogonal three-dimensional representation, complexified to \(\mathbb C^3\). For every unit \(v\in\mathbb C^3\), put \(P_v=vv^*\) and \(t=|v^{\mathsf T}v|^2\). The rank-one orbit analysis operator on Hermitian \(3\times3\) matrices has frame operator
\[
\mathcal F_v(X)=\sum_{R\in G}\operatorname{tr}(XP_{Rv})P_{Rv},\qquad P_{Rv}=Rvv^*R^{\mathsf T}.
\]
Its complete spectrum, with multiplicities, is
\[
\operatorname{spec}\mathcal F_v=\{20^{[1]},\;[10(1-t)]^{[3]},\;[2(1+3t)]^{[5]}\}.
\]
Consequently, recovery of every Hermitian matrix is possible if and only if \(t<1\). The best possible least frame eigenvalue over all unit fiducials is \(5\), with equality if and only if \(t=1/2\).

Choose orthogonal coordinates in which the icosahedral group contains the half-turn \(J=\operatorname{diag}(-1,-1,1)\). Set
\[
a=\sqrt{\frac{1+1/\sqrt2}{2}},\qquad
b=\sqrt{\frac{1-1/\sqrt2}{2}},\qquad
v_\star=(a,ib,0)^{\mathsf T}.
\]
The orbit of \(P_{v_\star}\) has precisely 30 distinct projectors \(\mathcal O\), each occurring twice in the full 60-element orbit. These 30 unit projectors form a complex projective \(2\)-design, and for every Hermitian \(X\),
\[
\sum_{P\in\mathcal O}\operatorname{tr}(XP)P=\frac52\bigl(X+\operatorname{tr}(X)I_3\bigr).
\]
This operator has spectrum \(\{10^{[1]},(5/2)^{[8]}\}\) and gives the exact reconstruction
\[
X=\frac25\sum_{P\in\mathcal O}\operatorname{tr}(XP)P-\frac1{10}\left(\sum_{P\in\mathcal O}\operatorname{tr}(XP)\right)I_3.
\]
Its least eigenvalue \(5/2\) is globally optimal over all families of 30 unit-norm rank-one projectors in \(\mathbb C^3\), without assuming icosahedral symmetry.

## Assumptions and scope
All operators are real-linear on the nine-dimensional real Hilbert space \(\operatorname{Herm}(3)\) with Frobenius inner product \(\langle X,Y\rangle=\operatorname{tr}(XY)\). Orbit projectors are counted with multiplicities in \(\mathcal F_v\); the 30-projector assertion removes exactly duplicate projectors. A projective \(2\)-design means the second projector moment coincides with the Haar-uniform moment of complex unit lines: \(\frac1{30}\sum_{P\in\mathcal O}P^{\otimes2}=\frac1{6}\Pi_{\mathrm{sym}}\). Here \(\Pi_{\mathrm{sym}}=(I+\mathrm{Swap})/2\) is the orthogonal projector onto the symmetric subspace of \((\mathbb C^3)^{\otimes2}\).

## Proof
**1. The three irreducible sectors.** Each Hermitian matrix decomposes orthogonally into its scalar part, purely imaginary antisymmetric part and real symmetric traceless part:
\[
\operatorname{Herm}(3)=\mathbb RI_3\oplus i\mathfrak{so}(3)\oplus\operatorname{Sym}^2_0(\mathbb R^3),
\]
with respective real dimensions \(1,3,5\). Conjugation by \(G\subset SO(3)\) preserves each sector. The middle sector is equivalent to the natural three-dimensional rotation representation via the axial-vector identification. Their irreducibility follows directly from the class characters: the group has conjugacy-class sizes \(1,15,20,12,12\), with rotation angles \(0,\pi,2\pi/3,2\pi/5,4\pi/5\). The natural character is \(1+2\cos\theta\), whose squared character norm is \((9+15+12(\varphi^2+(1-\varphi)^2))/60=1\), where \(\varphi=(1+\sqrt5)/2\) and \(\varphi^2+(1-\varphi)^2=3\). The traceless quadratic character is \(1+2\cos\theta+2\cos2\theta\), with values \(5,1,-1,0,0\), so its squared character norm is \((25+15+20)/60=1\). The three irreducibles have different dimensions and are inequivalent.

**2. Orthogonal projection norms.** Write \(v=x+iy\), with \(x,y\in\mathbb R^3\) and \(\|x\|^2+\|y\|^2=1\). The rank-one Hermitian projector has real symmetric part \(xx^{\mathsf T}+yy^{\mathsf T}\) and imaginary antisymmetric part \(i(yx^{\mathsf T}-xy^{\mathsf T})\). Since \(t=|v^{\mathsf T}v|^2=1-4(\|x\|^2\|y\|^2-(x\cdot y)^2)\), the squared Frobenius norm of the imaginary sector is \((1-t)/2\). The scalar-sector norm squared is \(1/3\). Because \(\|P_v\|_F^2=1\), the five-dimensional sector has squared norm \((1+3t)/6\).

**3. Orbit twirling and the spectrum.** For an orthogonal irreducible representation, the group average of a rank-one operator on its representation space is the scalar \(\|w\|^2/\dim\) times the identity (real Schur orthogonality; here the three irreducibles are absolutely irreducible, as also follows from their complex character norms). The average cross-blocks vanish because the irreducibles are inequivalent. Multiplying the three sector projection norm squares by \(|G|/\dim\) gives exactly \(20\), \(10(1-t)\), and \(2(1+3t)\), with multiplicities \(1,3,5\). For unit \(v\), Cauchy--Schwarz gives \(0\le t\le1\), and both extremes are attainable; \(2(1+3t)>0\). The least eigenvalue is \(\min\{10(1-t),2(1+3t)\}\), which has its unique maximum at the intersection \(t=1/2\), of value \(5\).

**4. Thirty distinct orbit projectors.** The displayed vector satisfies \(a^2+b^2=1\) and \(t=(a^2-b^2)^2=1/2\). Its projector has real symmetric part \(\operatorname{diag}(a^2,b^2,0)\), with three distinct eigenvalues. Any \(R\in SO(3)\) fixing this projector must therefore be a diagonal sign rotation. Its imaginary antisymmetric part has a nonzero \((1,2)\) entry, so the first two signs must agree. The determinant-one condition forces the third sign to be positive. Therefore its full rotation stabilizer is exactly \(\{I_3,J\}\). Both elements belong to \(G\), giving exactly \(|G|/2=30\) distinct projectors.

**5. Design and global optimality.** The 60-projector operator at \(t=1/2\) is \(5(X+\operatorname{tr}(X)I_3)\). Halving the multiplicities yields the 30-projector identity in the finding. Polarization in matrix entries makes that identity equivalent to the stated Haar second-moment formula, so \(\mathcal O\) is a uniform projective \(2\)-design. On the traceless Hermitian subspace the operator is \((5/2)I\), and on scalar matrices it is \(10I\), proving the spectrum and recovery formula. Finally, for any 30 unit projectors \(Q_j\), the sum of the eight diagonal Rayleigh quotients of their measurement operator over a Frobenius-orthonormal traceless basis is \(30(1-1/3)=20\). Hence its least eigenvalue is bounded above by their average \(20/8=5/2\). The explicit orbit attains equality, proving unrestricted 30-projector optimality.

## Verification
The embedded standalone program `check_icosahedral_design.py` uses SciPy's standard 60-element icosahedral rotation representation. It checks group order and the half-turn, the exact predicted multiplicity pattern numerically for 83 fiducials (80 seeded generic and three special), uniqueness of exactly 30 projectors, all nine matrix-unit identities, full 30-frame eigenvalues, and reconstruction identities. The 83 checks are numerical corroboration; the all-fiducial and unrestricted-optimality assertions follow from the deductive proof above.

## Relationship to prior work
Mohammadpour--Waldron (2023) develops the harmonic Molien-series methodology for complex spherical designs from finite group orbits. Its discussion of the three-dimensional real-reflection group ST23 and Section 7 gives projective harmonic indices for generic orbits but not the present continuously parametrized tomography eigenvalues or this explicit 30-projector optimum. Mohammadpour--Waldron (2019) constructs high-order real and complex designs by combining group orbits; its H3 construction uses unions of smaller real projective orbits, not the single complex 30-projector tomography identity. The general Schur-average and standard projective-design reconstruction identities are classical and not claimed new. The distinct claimed contribution is the closed all-fiducial icosahedral spectrum, sharp stability criterion and concrete stabilizer-two, 30-line optimum.

## Limitations
The result concerns the three-dimensional complexification of the ordinary rotational icosahedral representation, not the two-dimensional binary-icosahedral representation. It gives optimal noiseless linear-lifting conditioning, not phase-retrieval performance with fixed sample noise or a minimal number of projectors. Historical priority of the explicit 30-line design requires further specialist verification; an equivalent construction under a different group/design name might exist. Independent expert checking is not claimed.

## References
- M. Mohammadpour and S. Waldron, *Complex spherical designs from group orbits*, arXiv:2308.02499 (first public 2023-07-21), https://arxiv.org/abs/2308.02499.
- M. Mohammadpour and S. Waldron, *Constructing high order spherical designs as a union of two of lower order*, arXiv:1912.07151 (first public 2019-12-16), https://arxiv.org/abs/1912.07151.
