# The unique nonordinary fiber of a genus-four cyclic-trigonal pencil in characteristic thirteen

## Finding
Let \(k=\overline{\mathbf F}_{13}\). For each \(a\in k\) with \(a^5\ne 2\), let \(C_a\) be the smooth projective model of
\[
y^3=x^5+ax^2+1.
\]
These curves have genus four. The Jacobian of \(C_a\) is ordinary for every \(a\ne0\). The only nonordinary fiber in the entire smooth marked pencil is \(C_0\), whose Jacobian has \(13\)-rank zero and Cartier \(a\)-number two. The Newton polygon of its Jacobian has slopes \(1/4\) and \(3/4\), each with multiplicity four. In particular, this is a nonordinary but nonsupersingular genus-four Jacobian in an otherwise ordinary one-dimensional pencil. At \(a=0\), the curve also has the enhanced automorphism \((x,y)\mapsto(\zeta_5x,y)\), in addition to its cyclic degree-three deck transformations.

## Assumptions and scope
All parameters are geometric elements of an algebraically closed field of characteristic thirteen. The equation describes a cyclic degree-three cover of \(\mathbf P^1\), with branch points the five roots of \(x^5+ax^2+1\) and infinity. The degree-five polynomial has discriminant \(4(a^5-2)\) in characteristic thirteen, so separability, and hence smoothness of its projective normalization, is equivalent to \(a^5\ne2\). The genus follows from the tame Riemann--Hurwitz formula: six fully ramified branch points yield \(2g-2=-6+6(3-1)=6\).

## Proof
A holomorphic differential basis is \(dx/y\), followed by \(dx/y^2\), \(x\,dx/y^2\), and \(x^2\,dx/y^2\). Indeed, at the unique point at infinity, \(v(x)=-3\), \(v(y)=-5\), and \(v(dx)=-4\). For the cyclic cover \(y^3=f(x)\) in characteristic \(p=13\), the Cartier operator on the \(j\)-th character block is computed by extracting the coefficient of \(x^{13(r+1)-i-1}\) from \(f(x)^{4j}\), for output basis index \(r\) and input index \(i\). Taking the \(13\)-th root of coefficients does not change vanishing or ranks and is trivial for coefficients specialized to \(\mathbf F_{13}\). Over the parameter field, the displayed matrices have coefficients before the inverse-Frobenius operation, which preserves the determinant's zero set and rank.

For \(j=1\), the one-dimensional block is \((-a)\). For \(j=2\), the three-dimensional coefficient block is
\[
M(a)=\begin{pmatrix}
2a^6-a&-6a^3&4a^5+2\\
4a^5+4&4a^2&-6a^4\\
0&-5a&0
\end{pmatrix}\pmod {13}.
\]
Exact polynomial arithmetic gives \(\det M(a)=3a(a^5-2)^2\), so the determinant of the unrooted coefficient matrix is \(-3a^2(a^5-2)^2\). Consequently the full Cartier operator is invertible at every smooth parameter other than \(a=0\). At \(a=0\), its first block vanishes and
\[
M(0)=\begin{pmatrix}0&0&2\\4&0&0\\0&0&0\end{pmatrix},\quad
\operatorname{rank}M(0)=2,\quad M(0)^3=0.
\]
Thus the Cartier \(a\)-number is \(4-2=2\). Because all coefficients lie in \(\mathbf F_{13}\), the semilinear Cartier iteration on this matrix is represented by its usual powers; nilpotence proves that the stable Frobenius rank, hence the Jacobian \(13\)-rank, is zero.

To determine the Newton polygon, note that \(C_0:y^3=x^5+1\) is an abelian cover with commuting \(\mu_3\) and \(\mu_5\) actions. Its first cohomology has eight one-dimensional character components indexed by \((u,v)\), where \(u\in\{1,2\}\) modulo three and \(v\in\{1,2,3,4\}\) modulo five. Since \(13\) has multiplicative order four modulo fifteen, all relevant characters are defined over \(\mathbf F_{13^4}\). The standard Jacobi-sum description of the zeta function, together with Stickelberger's valuation formula, gives for the eigenvalue associated to \((u,v)\) the normalized \(13\)-adic slope
\[
\frac14\sum_{i=0}^{3}\left\lfloor
\left\{\frac{13^iu}{3}\right\}+\left\{\frac{13^iv}{5}\right\}
\right\rfloor.
\]
For fixed \(u=1\), each \(v\) yields exactly one carry in four steps, hence slope \(1/4\). For fixed \(u=2\), each \(v\) yields exactly three carries, hence slope \(3/4\). These account for all eight eigenvalues, proving the claimed Newton polygon. Here the Jacobi-sum valuation formula is used as a classical external theorem; the eight finite carry computations are independently reproducible.

The extra order-five automorphism at \(a=0\) is immediate from \(x^5+1\); for nonzero \(a\), the same transformation preserves the defining polynomial only if \(\zeta_5^2=1\), which excludes primitive fifth roots. This establishes an automorphism-enhancement point coinciding with the unique nonordinary coefficient value; no assertion about the full automorphism group is needed.

## Verification
The accompanying standalone `verify.py` uses exact integer multinomial expansions modulo thirteen to reconstruct the complete Cartier coefficient matrices and their determinant, verify smoothness and exceptional ranks, and enumerate all eight Jacobi-sum carries. It also checks, for every \(a\in\mathbf F_{13}\), that the rank classification agrees with direct specialization. Execution prints `VERIFY_TRIGONAL13_OK`. All geometric conclusions use the symbolic determinant factorization, not merely finite-field enumeration.

## Relationship to prior work
Cavalieri and Pries (arXiv:2308.14891, first circulated August 28, 2023) study weighted nonordinary loci in one-dimensional families of cyclic covers and give full mass formulas for four-branch-point covers. Their formulas do not state this explicit six-branch-point characteristic-thirteen stratum or the Newton polygon of its exceptional fiber. The general Cartier coefficient extraction and classical Jacobi-sum/Stickelberger valuations are known tools; the contribution here is their exact synthesis for this marked pencil, including the unique exceptional parameter and its two distinct nonintegral slopes. Comparable cyclic-trigonal genus-four characteristic-seven and characteristic-eleven parameter classifications are separate coefficient families or characteristics and do not directly imply this statement.

## Limitations
This is a characteristic-thirteen and coefficient-marked pencil result, not a classification of all genus-four trigonal curves or all covers of six branch points. It does not determine the full zeta function of the exceptional curve. The Newton-slope calculation relies on the classical Jacobi-sum valuation theorem, while the Hasse--Witt and carry computations are self-contained. A historical equivalent computation of this particular parameter pencil cannot be excluded solely by database searching.

## References
1. R. Cavalieri and R. Pries, *Mass formula for non-ordinary curves in one dimensional families*, arXiv:2308.14891, first version August 28, 2023, https://arxiv.org/abs/2308.14891.
2. Classical Jacobi-sum description of the zeta function of diagonal cyclic covers and Stickelberger's valuation theorem; used for the explicit Newton-slope computation above.
