# Morse–Bott normal forms on the singular components of a hexagonal universal adjoint

## Finding
Let \(X\subset\mathbb P^5_{\mathbb C}\) be the hexagonal universal-adjoint quartic
\[
F(x_0,\ldots,x_5)=\sum_{i\in\mathbb Z/6\mathbb Z}\ \prod_{j\notin\{i,i+1\}}x_j=0.
\]
Its reduced singular locus has precisely **20 irreducible components**: the two alternating coordinate planes, nine mixed-parity coordinate lines, and nine further noncoordinate lines. Along a dense Zariski-open subset of each plane, the completed hypersurface germ is an ordinary double point in three transverse variables times a smooth two-dimensional factor. Along a dense open subset of each of the 18 lines, it is an ordinary double point in four transverse variables times a smooth one-dimensional factor. In particular, the Jacobian singular scheme is generically reduced along every component and the generic transverse Hilbert–Samuel multiplicity is two.

## Assumptions and scope
All schemes and analytic germs are over \(\mathbb C\). Indices are taken modulo six, with \(x_0,\ldots,x_5\) cyclically ordered. A coordinate line is *mixed-parity* if it is spanned by two standard coordinate points with one even and one odd index. The two alternating planes are
\[
P_E=V(x_1,x_3,x_5),\qquad P_O=V(x_0,x_2,x_4).
\]
Write \(C_{ij}\) for the coordinate line spanned by the \(i\)-th and \(j\)-th coordinate points, with \(i\) even and \(j\) odd. For each unordered nonadjacent pair \(\{i,j\}\subset\mathbb Z/6\mathbb Z\), let \(L_{ij}\) be the unique line of singular points whose generic member has precisely \(x_i=x_j=0\). Two representatives suffice under the dihedral action on the cyclic indices:
\[
L_{35}=V(x_3,x_5,x_0+x_4,x_2+x_4),\quad
L_{25}=V(x_2,x_5,x_0+x_4,x_1+x_3).
\]
There are six nonadjacent index pairs at cyclic distance two and three at distance three. The full set-theoretic reduced singular locus is
\[
\operatorname{Sing}(X)_{\rm red}=P_E\cup P_O\cup
\bigcup_{i\ \mathrm{even},\ j\ \mathrm{odd}} C_{ij}
\cup\bigcup_{\{i,j\}\ \mathrm{nonadjacent}} L_{ij}.
\]
The normal forms asserted below hold at points in a dense open of each component, outside the other components and the vanishing locus of a suitable Hessian minor; no assertion is made about transverse types at their intersections.

## Proof
**1. Exhaustive support stratification.** For a projective point \(p\), let \(S(p)=\{i:x_i(p)\ne0\}\). The six monomials of \(F\) have support the complements of the cyclic edges \(\{i,i+1\}\).

If \(|S|\le2\), all partial derivatives of \(F\), which have degree three and are squarefree, vanish. These points belong to an alternating plane if their support has a single parity, and otherwise to one of the nine mixed-parity lines \(C_{ij}\).

If \(|S|=3\), some partial derivative is a nonzero scalar multiple of the product of the three nonzero coordinates unless the complement of \(S\) contains no adjacent pair. Indeed that derivative has one such contribution per complementary edge and all six monomial coefficients are \(+1\), so cancellation is impossible on this support. The only independent three-vertex sets of the six-cycle are the alternating sets. Hence the singular points with three nonzero coordinates lie in \(P_E\cup P_O\).

If \(|S|=4\), let \(\{i,j\}\) be the missing pair. For adjacent missing indices, exactly one monomial survives in \(F\), so \(p\notin X\). For nonadjacent missing indices, all monomials vanish, and the only potentially nonzero gradient entries are those corresponding to the two missing indices. There are two dihedral orbits. For \(x_3=x_5=0\), the nontrivial partials are
\[
\partial_3F=x_1x_2(x_0+x_4),\qquad
\partial_5F=x_0x_1(x_2+x_4).
\]
On the four-support torus these give exactly \(L_{35}\). For \(x_2=x_5=0\), they are
\[
\partial_2F=x_1x_3(x_0+x_4),\qquad
\partial_5F=x_0x_4(x_1+x_3),
\]
whose common zeros on the four-support torus are exactly \(L_{25}\). Dihedral symmetry gives the other seven lines.

For \(|S|=5\), cyclic symmetry reduces to \(x_5=0\), where \(F=x_1x_2x_3(x_0+x_4)\). Thus a point of this stratum belonging to \(X\) has \(x_0+x_4=0\), while \(\partial_0F=x_1x_2x_3\ne0\). Finally, for \(|S|=6\), put \(y_i=x_i^{-1}\). On the torus \(F=(\prod_i x_i)Q\), with \(Q=\sum_i y_iy_{i+1}\). A singular point would satisfy all equations \(\partial Q/\partial y_i=y_{i-1}+y_{i+1}=0\). These imply \(y_{i+2}=-y_i\) and, after three steps, \(y_i=-y_i\), impossible over \(\mathbb C\) when all \(y_i\ne0\). Thus the displayed union is exhaustive. Distinct lines of type \(L_{ij}\) have different generic missing pairs; mixed coordinate lines have a different generic support; the two planes have generic support of size three. No one of the listed 20 linear spaces contains another, proving irreducible minimality.

**2. Generic Hessian rank.** Set \(H(p)=(\partial_i\partial_jF(p))_{0\le i,j\le5}\). At each singular point the homogeneous Euler identity gives \(H(p)p=0\). At any point of a linear singular component of projective dimension \(d\), differentiating the gradient identities along its affine cone shows that the \((d+1)\)-dimensional cone tangent space is in \(\ker H(p)\). Hence \(\operatorname{rank}H(p)\le5-d\). The dihedral group acts by permuting coordinates and leaves \(F\) invariant. The following exact rational witnesses attain the bound in every orbit (coordinates are in order \(0,\ldots,5\)):

| Stratum orbit | Witness | Hessian rank | Nonzero principal minor (zero-based indices; determinant) |
|---|---|---:|---|
| Alternating plane | \((1,0,2,0,3,0)\) | 3 | \((1,3,5);720\) |
| Adjacent mixed coordinate line | \((1,2,0,0,0,0)\) | 4 | \((2,3,4,5);16\) |
| Opposite mixed coordinate line | \((1,0,0,2,0,0)\) | 4 | \((1,2,4,5);16\) |
| Noncoordinate line, distance two | \((-1,2,-1,0,1,0)\) | 4 | \((0,2,3,5);16\) |
| Noncoordinate line, distance three | \((-1,-2,0,2,1,0)\) | 4 | \((0,1,2,5);16\) |

Each witness lies on the indicated singular component; every relevant orbit is represented. Rank is maximal at a nonempty Zariski-open subset of each component, since the displayed minors do not vanish identically.

**3. Analytic normal forms.** Off the intersections of singular components, the singular support is smooth, and the Hessian kernel is exactly the affine tangent to its cone. In local affine coordinates split into parameters \(u_1,\ldots,u_d\) along the singular locus and \(5-d\) transverse coordinates, the differential of \(F\) vanishes along \(\{z=0\}\), and the transverse Hessian is nondegenerate. The complex analytic Morse–Bott lemma with parameters gives a local analytic equation \(z_1^2+\cdots+z_{5-d}^2=0\). This yields three square variables for planes and four for lines. The transverse partial derivatives form a regular system of parameters normal to each component, so the Jacobian singular scheme is generically reduced and has generic transverse multiplicity two.

## Verification
Run `python3 verify.py` using Python 3 without third-party dependencies. The program reconstructs the six quartic monomials, checks the gradient identities identically on the complete 20-component list by comparing polynomial coefficients, confirms that the dihedral orbits yield exactly nine distinct noncoordinate lines, and evaluates Hessian ranks by exact rational elimination at generic rational witnesses. The program is an independent finite certificate for the explicit linear spaces and witness ranks; the unrestricted support argument and openness reasoning are given in the proof, not inferred from sampled computations.

## Relationship to prior work
Simon Telen, *Toric Amplitudes and Universal Adjoints* (arXiv:2504.00897, v1 dated April 1, 2025; subsequently Journal of the London Mathematical Society, 2026), Example 7.6, already determines the singular locus of this same hexagonal adjoint set-theoretically, describing a covering by thirty lines and two planes, and Proposition 7.4 / Corollary 7.11 provide general structural methods. The **newly asserted result is not prior discovery of singular points**: it is the minimal 20-component irreducible organization together with the uniform generic analytic normal forms, maximal transverse Hessian ranks, and generic scheme-theoretic reducedness. The article treats Hessian rank for the pentagonal Segre cubic in Section 2.2, but does not give the corresponding generic transverse analytic analysis for its hexagonal quartic in Example 7.6. The original article was read in the open-access full HTML representation, not inferred from its abstract.

## Limitations
The classification is for the specified cyclic six-term quartic over \(\mathbb C\); it does not extend automatically to arbitrary weighted six-ray polygons or positive characteristic. The Jacobian scheme may have embedded components or nonreduced structure at component intersections, which are not classified here. The claim excludes the local analytic type at all such intersections. Historical priority under alternative names for the quartic remains a possibility, and no independent mathematical audit has been performed.

## References
1. S. Telen, *Toric Amplitudes and Universal Adjoints*, arXiv:2504.00897, original submission 2025-04-01; J. Lond. Math. Soc. 113 (2026), e70468, https://doi.org/10.1112/jlms.70468. Primary text: https://arxiv.org/html/2504.00897v3, especially Sections 2.2 and 7, Example 7.6 and Proposition 7.4.
2. The complex analytic Morse–Bott lemma, in its standard local holomorphic form with parameters; the only application is to a hypersurface with a smooth critical locus and nondegenerate normal Hessian.
