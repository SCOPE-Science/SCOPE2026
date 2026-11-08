# Integral spectrum of the 75-line incidence graph on the Fermat quintic

## Finding
Let \(S\subset\mathbf P^3_{\mathbb C}\) be the smooth Fermat quintic \(\sum_{i=0}^3x_i^5=0\). Let \(\mathcal L\) be its set of 75 projective lines and \(A\) the real symmetric \(75\times75\) matrix with \(A_{LL'}=1\) for two distinct intersecting lines and \(0\) otherwise. Then
\[
\det(tI-A)=(t-18)(t-3)^{38}(t+2)^{24}(t+7)^{12}.
\]
In particular the intersection graph is connected, \(18\)-regular, and integral. Since each line has self-intersection \(-3\), the intersection Gram matrix \(G=A-3I\) has spectrum \(15^{[1]},0^{[38]},(-5)^{[24]},(-10)^{[12]}\). It has rank \(37\), inertia \((1,36,38)\) (positive, negative, zero), and the space of rational numerical relations among the 75 line classes has dimension \(38\).

## Assumptions and scope
All geometry and numerical divisor intersection claims are over \(\mathbb C\). The 75 lines are the three families indexed by coordinate pairings \((01)(23)\), \((02)(13)\), and \((03)(12)\) and independently chosen fifth roots of \(-1\) on the two pairs. Distinct projective lines in a smooth surface meet transversely in the plane spanned by them whenever they meet; their local intersection number is one. The stated spectrum concerns the adjacency matrix of this entire geometric line configuration, not an arbitrary graph or a reduction in positive characteristic.

## Proof
Fix a primitive fifth root of unity \(\zeta\). In each of the three pairings, choose exponents \(a,b\in\{0,1,2,3,4\}\). For each ordered pair of coordinate indices \((i,j)\), use the vector supported in positions \(i,j\), with entries \((-\zeta^a,1)\) or \((-\zeta^b,1)\); their span is a line contained in \(S\). The classical complete-line classification shows that these three families, each of size 25, exhaust the lines on \(S\) [1,2,3].

For two such lines, concatenate the four specified spanning vectors into a \(4\times4\) matrix. Their projective lines meet if and only if its determinant vanishes in \(\mathbb Q(\zeta)\). The attached standalone checker calculates each of the 2,775 determinants by the permutation formula in \(\mathbb Z[\zeta]\). It records a polynomial of degree at most four as five integer coefficients; this polynomial vanishes at \(\zeta\) if and only if all five coefficients agree, by \(\Phi_5(T)=1+T+T^2+T^3+T^4\). Therefore the test is exact, not a test modulo a prime.

This produces the finite \(75\times75\) integral matrix \(A\). The checker verifies by integer matrix multiplication the identity
\[
(A-18I)(A-3I)(A+2I)(A+7I)=0,
\]
and independently checks that every row sum is 18 and that breadth-first traversal visits all 75 vertices. Symmetry makes \(A\) diagonalizable over \(\mathbb R\). Connectivity of the regular graph proves that its eigenvalue 18 has multiplicity one; the annihilating polynomial restricts all other eigenvalues to \(3,-2,-7\). Let their multiplicities be \(u,v,w\). Matrix order, trace, and squared trace yield
\[
 u+v+w=74,\quad 3u-2v-7w=-18,\quad 9u+4v+49w=1026.
\]
Here the squared trace is \(\operatorname{tr}(A^2)=75\cdot18=1350\). The unique solution is \((u,v,w)=(38,24,12)\), proving the adjacency characteristic polynomial.

The adjunction formula for a line on a smooth degree-five surface gives \(L^2=2-5=-3\) [1]. Distinct intersecting lines have local intersection multiplicity one, hence \(G=A-3I\). Its spectral shift gives the asserted rank and inertia. Schütt–Shioda–van Luijk prove that these 75 lines span \(\operatorname{NS}(S)\otimes\mathbb Q\) (in fact the whole Néron–Severi group integrally) and that \(\rho(S)=37\) [3]. Since the intersection pairing is nondegenerate on this rational space, the kernel of \(G\) is exactly the space of numerical relations among the 75 line classes.

## Verification
Run `python3 verify_spectrum.py` (standard library only). The final line is `VERIFY_FERMAT_QUINTIC_LINE_SPECTRUM_OK lines=75 degree=18 connected=1 eigen=18:1,3:38,-2:24,-7:12 Gram_rank=37`. The checker reconstructs the determinant test and matrix from scratch, verifies the degree, connectivity, exact degree-four matrix identity, traces, and multiplicities. This is a complete finite, exact certificate for the geometric 75-line configuration; no finite sampling or numerical eigenvalue approximation is used as a substitute for proof.

## Relationship to prior work
The 75 lines, their three-family parameterization, their intersection tests, their rank-37 Néron–Severi span, and integral generation are **prior results** [1–3]. In particular, [2, Proposition 1.2] supplies the pairwise incidence conditions and explicitly attributes them to [3, equation (6)]. This work does **not** claim a new line classification, intersection rule, Picard rank, or spanning theorem. Its asserted refinement is the explicit full integral adjacency spectrum and the numerical-relations eigenspace multiplicities, not reported in the relevant portions of [1–3]. Other articles could already contain an equivalent spectral computation; this is a priority limitation.

## Limitations
The polynomial certificate depends on reproducing the finite checker; the mathematical reduction from exact determinant enumeration to the global graph spectrum is rigorous, but no independent expert audit has occurred. The result does not describe the integer lattice structure of the relation kernel, its discriminant group, nor any characteristic-\(p\) exceptional lines. The spectral statement is stronger than the known rank statement, but the published pairwise incidence criteria permit its independent derivation; thus historical novelty must be interpreted as the explicit spectrum, not as an independent incidence classification.

## References
[1] S. Rams and M. Schütt, *Counting lines on surfaces, especially quintics*, arXiv:1803.03548, first posted 2018-03-09, https://arxiv.org/html/1803.03548v2.

[2] S. Andria, J. Rojas and W. Mangueira, *Maximal number of Skew lines on Fermat Surfaces*, arXiv:2403.15666, first posted 2024-03-23, https://arxiv.org/html/2403.15666v2, especially Proposition 1.2.

[3] M. Schütt, T. Shioda and R. van Luijk, *Lines on Fermat surfaces*, arXiv:0812.2377, first posted 2008-12-12, https://arxiv.org/html/0812.2377v3, sections 2, 4, 6.2.
