# Exact quadratic-band Slepian spectrum of a spherical octant

## Finding

Let \(S^2=\{(x,y,z)\in\mathbb R^3:x^2+y^2+z^2=1\}\), let \(\sigma\) be its normalized area measure, and let \(R=\{(x,y,z)\in S^2:x>0,y>0,z>0\}\). Let \(V=\mathcal H_0\oplus\mathcal H_1\oplus\mathcal H_2\), the nine-dimensional complex space of spherical harmonics of degrees zero through two. Define the Slepian concentration operator \(K\) on \(V\) by
\[
\langle Kf,g\rangle_{L^2(S^2,\sigma)}=\int_R f\overline g\,d\sigma.
\]
Its **complete spectrum** is the six numbers \(t/8\), where \(t\) runs through the three real roots of each of the exact generalized characteristic polynomials
\[
P_{\mathrm{sym}}(t)=\det(C_{\mathrm{sym}}-t B_{\mathrm{sym}}),\qquad
P_{\mathrm{std}}(t)=\det(C_{\mathrm{std}}-t B_{\mathrm{std}}),
\]
with multiplicity one for each root of \(P_{\mathrm{sym}}\) and multiplicity two for each root of \(P_{\mathrm{std}}\). All six values are distinct and strictly between zero and one. The matrices, with \(p=\pi\), are
\[
B_{\mathrm{sym}}=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1/5\end{pmatrix},\quad
C_{\mathrm{sym}}=\begin{pmatrix}
1&3/2&2/p\\
3/2&1+4/p&3(1+p)/(4p)\\
2/p&3(1+p)/(4p)&(p+4)/(5p)
\end{pmatrix},
\]
\[
B_{\mathrm{std}}=\begin{pmatrix}2/3&0&0\\0&4/15&0\\0&0&2/15\end{pmatrix},\quad
C_{\mathrm{std}}=\begin{pmatrix}
2(p-2)/(3p)&1/4&(p-2)/(4p)\\
1/4&4/15&4/(15p)\\
(p-2)/(4p)&4/(15p)&2(p-2)/(15p)
\end{pmatrix}.
\]
There is a **unique most-concentrated complex line** and a **unique least-concentrated complex line**: both lie in the permutation-symmetric subspace. The two sharp energy fractions and the squared-energy condition ratio are
\[
\lambda_{\max}=0.680691506535312\ldots,\quad
\lambda_{\min}=0.00000517687224732976\ldots,\quad
\frac{\lambda_{\max}}{\lambda_{\min}}=131487.020350\ldots.
\]
Consequently the restriction map \(V\to L^2(R,\sigma)\) is injective and has **sharp singular-value condition number** \(\sqrt{\lambda_{\max}/\lambda_{\min}}=362.611390265\ldots\). These decimals illustrate exact root-defined quantities, not substitute definitions.

## Assumptions and scope

The restriction is continuous on the **surface** of the two-sphere, not discrete sampling and not volume integration in the ball. All degrees \(0,1,2\) are included, with complex coefficients and the full-sphere probability inner product. The orthant has probability \(1/8\); \(C\) above denotes *conditional* orthant moments, so its generalized eigenvalues must be divided by eight. Any simultaneous rotation of the mask and the harmonics preserves the spectrum. The two unique lines are complex one-dimensional, not independent real-and-imaginary degeneracies. No statement is made for other bandwidths, dimensions, spherical triangles, or sampling noise distributions.

## Proof

**1. Harmonic-polynomial model.** On \(S^2\), restrictions of polynomials of total degree at most two coincide with \(V\), because the quadratic trace is a multiple of \(x^2+y^2+z^2=1\). The symmetric group on the three coordinates preserves \(R\) and \(\sigma\). Its action splits \(V\) into three copies of the trivial representation and three copies of its two-dimensional standard representation. There is no alternating component. Thus every invariant Hermitian form is represented by one three-by-three scalar block and one three-by-three block repeated twice.

For the trivial multiplicity space choose \(u_0=1\), \(u_1=x+y+z\), \(u_2=xy+yz+zx\). For one fixed standard coordinate choose \(v_0=x-y\), \(v_1=x^2-y^2\), \(v_2=z(x-y)\). The last triple is the \((1,-1,0)\) component of three equivariant copies of the standard representation; invariance makes its generalized eigenvalues occur twice. Direct sign or permutation symmetry gives full-sphere orthogonality among each triple's three basis elements, and cross-orthogonality between the trivial and standard sectors.

**2. Exact moments and blocks.** If \(X\) is uniform on \(S^2\), the magnitudes \((|X_1|,|X_2|,|X_3|)\) have the same law as uniform coordinates conditioned to \(R\). For nonnegative integers \(a,b,c\),
\[
\mathbb E_R[X_1^aX_2^bX_3^c]
=\frac{\Gamma(3/2)}{\Gamma((3+a+b+c)/2)}
\prod_{j=1}^3\frac{\Gamma((e_j+1)/2)}{\Gamma(1/2)},
\quad(e_1,e_2,e_3)=(a,b,c).
\]
On the full sphere, the moment is zero if any exponent is odd; if all are even it is the same gamma product. Expanding the products of the displayed basis functions of degrees at most four yields the matrices \(B_{\mathrm{sym}},C_{\mathrm{sym}},B_{\mathrm{std}},C_{\mathrm{std}}\) stated above. Here \(B\) is the full-sphere Gram matrix and \(C\) the conditional-orthant Gram matrix. Therefore the actual Slepian eigenproblem is \((C/8)w=\lambda Bw\). Representation theory and the dimension count \(3+2\cdot3=9\) prove that the two generalized cubics constitute the entire spectrum with their stated multiplicities. The independent monomial-moment reconstruction in `orthant_band2_verify.py` verifies each displayed matrix entry exactly.

**3. Rigorous root separation and sharp extrema.** Let \(t^{(0)}_1<t^{(0)}_2<t^{(0)}_3\) denote roots of \(P_{\mathrm{sym}}\) and \(t^{(1)}_1<t^{(1)}_2<t^{(1)}_3\) roots of \(P_{\mathrm{std}}\). Exact rational sign calculations certify the disjoint isolating intervals
\[
\begin{array}{c|ccc}
&1&2&3\\\hline
\mathrm{sym}&(1/25000,1/20000)&(1/10,11/100)&(5,6)\\
\mathrm{std}&(2/1000,3/1000)&(12/100,14/100)&(3/2,17/10)
\end{array}.
\]
For each cubic the determinant changes sign at the endpoints of each interval. Since a cubic has at most three roots, this proves exactly three simple real roots in those intervals. The intervals are disjoint and give the strict global ordering
\[
t^{(0)}_1<t^{(1)}_1<t^{(0)}_2<t^{(1)}_2<t^{(1)}_3<t^{(0)}_3.
\]
Thus the least and greatest eigenvalues are the two extreme trivial-sector roots, both simple. All eigenvalues satisfy \(0<\lambda<1\), because every interval lies in \((0,8)\) before division by eight. The determinant signs are certified over rational upper and lower bounds for \(\pi=16\arctan(1/5)-4\arctan(1/239)\), using alternating series with thirty terms; no floating-point root search is used in this separation proof. The exact checker reproduces the rational sign certificates.

**4. Stability interpretation.** With the full-sphere norm on the domain, \(\|f\|_{L^2(R)}^2=\langle Kf,f\rangle\). Hence the squared singular values of restriction are precisely the eigenvalues of \(K\), with no zero singular value, and the sharp restriction condition number is \(\sqrt{\lambda_{\max}/\lambda_{\min}}\). The Shannon trace is \(\operatorname{tr}K=9/8\), independently corroborated by the spherical addition theorem and by the exact block traces.

## Verification

Run `python orthant_band2_verify.py` with Python 3 and SymPy installed. It independently expands a nine-element Cartesian polynomial basis, checks the full-sphere and conditional-orthant moment matrices, verifies the permutation blocks exactly, checks the Shannon trace, and isolates all six generalized roots with rational arithmetic. It computes the \(\pi\) enclosure via Machin's identity and the alternating-series remainder, then evaluates determinant-sign bounds using rational interval Horner arithmetic. The executed checker reports `OCTANT_BAND2_EXACT_CHECKS_PASS`. The proof above supplies the representation-theoretic completeness and the spectral interpretation; numerical approximations alone do not establish the result.

## Relationship to prior work

Roddy and McEwen (arXiv:2106.02023, sections II-C and III) define the spherical Slepian eigenproblem and construct wavelets for incomplete spherical observations, but their inspected full text does not compute the all-right octant spectrum for the nine-dimensional quadratic band. Michel, Plattner, and Seibert (arXiv:2103.14650, section 3.1 and section 5) give the general spherical concentration eigenmatrix and cap-specific constructions, not the explicit octant eigenvalues. These frameworks motivate the exact finite-matrix problem but do not state the two evaluated cubic blocks or the sharp minimum/maximum here.

The published mathematical result *Exact quadratic spherical-orthant concentration and a sharp dimension-squared stability law* treats **pure degree-two** spherical harmonics in arbitrary dimensions, rather than the low-pass direct sum of degrees zero, one and two. Its spectral blocks therefore omit mixed-degree couplings, including the very small symmetric eigenvalue here. *The complete quadratic hemispherical Slepian spectrum in every sphere dimension* includes all three degrees but uses a **hemisphere**, whose reflection symmetry gives a different eigenvalue structure; its closed values cannot specialize to an octant by parameter choice. These are scientifically close but neither implication covers the stated six-level octant spectrum. The distinction is by operators and invariant subspaces, not by title alone.

## Limitations

The result concerns exactly the lowest nontrivial full harmonic band on a single all-right spherical triangle. Its extreme eigenvalues can be obtained numerically from general Slepian software, but the contribution claimed is their complete exact analytic specification, multiplicities, sharp ordering, and rationally certified stability value. It is not a general recovery theorem for arbitrary masks or higher bandlimits. Earlier specialized finite-band spherical-triangle tables or an equivalent algebraic calculation could exist outside the inspected literature; historical priority is not independently established. The reported condition number assumes ideal continuous restriction with the full-sphere input norm and is not a statement about discretized sampling or a stochastic noise model.

## References

1. P. J. Roddy and J. D. McEwen, *Slepian Scale-Discretised Wavelets on the Sphere*, arXiv:2106.02023, first posted 2021-06-03, https://arxiv.org/abs/2106.02023.
2. V. Michel, A. Plattner and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650, first posted 2021-03-26, https://arxiv.org/abs/2103.14650.
3. F. J. Simons, F. A. Dahlen and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424, https://arxiv.org/abs/math/0408424.
4. *Exact quadratic spherical-orthant concentration and a sharp dimension-squared stability law*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-quadratic-spherical-orthant-concentration-and-a-sharp-dime--043aca2fd738.
5. *The complete quadratic hemispherical Slepian spectrum in every sphere dimension*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-complete-quadratic-hemispherical-slepian-spectrum-in-every-s--b091257c4da7.
