# Seven integral rational-point groups of the quartic del Pezzo sixteen-curve boundary

## Finding
Let \(k=\mathbb F_q\) be any finite field, and let \(S/k\) be the blowup of \(\mathbb P^2_k\) in a Frobenius-stable set of five distinct geometric points in general position. Let \(D\subset S\) be the reduced union of all sixteen geometric exceptional curves, descended as a divisor over \(k\). Write \(T=\operatorname{Pic}^{0}_{D/k}\), and write \(C_m=\mathbb Z/m\mathbb Z\). Then \(T\) is a torus of rank \(25\), and the **complete finite abelian group** \(T(k)\) is given by the following table, according to the seven cycle types of Frobenius acting on the five blown-up points:

| Cycle type | Exact group \(T(\mathbb F_q)\) |
|:--|:--|
| \((1^5)\) | \(C_{q-1}^{25}\) |
| \((2,1^3)\) | \(C_{q-1}^{5}\oplus C_{q^2-1}^{10}\) |
| \((2^2,1)\) | \(C_{q+1}^{3}\oplus C_{q^2-1}^{11}\) |
| \((3,1^2)\) | \(C_{q-1}\oplus C_{q^3-1}^{8}\) |
| \((3,2)\) | \(C_{q^3-1}\oplus C_{(q^3-1)(q+1)}\oplus C_{q^6-1}^{3}\) |
| \((4,1)\) | \(C_{q^2+1}\oplus C_{(q+1)(q^2+1)}\oplus C_{q^4-1}^{5}\) |
| \((5)\) | \(C_{q^5-1}^{5}\) |

The five-cycle row is established prior work and is included for completeness. The other six rows constitute the present classification. In the mixed types \((3,2)\) and \((4,1)\), the displayed product factors retain an integral gluing invisible in the factorization of the rational Frobenius characteristic polynomial. For odd \(q\), a naive direct sum of the obvious induced and sign character lattices has respectively one more dimension of rational \(2\)-torsion than the actual \(T(k)\). No assertion of a corresponding direct-product isomorphism of algebraic tori is made for these six new rows.

## Assumptions and scope
The five points may have any of the stated Frobenius cycle types, provided they are distinct and no three are collinear. This is a conditional classification and does not assert realization of every type for every small field. The blowup is smooth of anticanonical degree four. In the geometric Picard lattice, the sixteen exceptional curves have classes
\[
E_i\ (0\le i<5),\qquad L_{ij}=H-E_i-E_j\ (0\le i<j<5),\qquad Q=2H-\sum_{i=0}^{4}E_i.
\]
Their distinct transverse intersection pairs are exactly \(E_i\) with \(Q\) (five pairs), \(E_r\) with \(L_{ij}\) for \(r\in\{i,j\}\) (twenty pairs), and \(L_{ij}\) with \(L_{kl}\) for disjoint index pairs (fifteen pairs). These intersections are distinct ordinary nodes: for example, the conic \(Q\) and a joining line meet at their two distinct base points before blowup, so their strict transforms do not meet. Three joining lines cannot pairwise have disjoint two-element index sets among five indices. Therefore the dual graph \(\Gamma\) is connected, triangle-free, five-regular, and has \(16\) vertices and \(40\) edges. Thus \(p_a(D)=40-16+1=25\). All normalized components are rational, so the identity-component Picard scheme is purely toric.

Here \(\Gamma\) is the **five-regular** Clebsch graph (not its ten-regular complement). The theorem concerns the ordinary permutation subgroup \(\mathfrak S_5\) realized by permuting five blown-up points. It does not classify all signed \(W(D_5)\) Frobenius forms.

## Proof
**1. Integral graph lattice.** Order the vertices as \(E_0,\ldots,E_4\), the ten \(L_{ij}\) in lexicographic order, then \(Q\). Orient every edge from the earlier to the later vertex, and let \(\partial:\mathbb Z^{40}\to\mathbb Z^{16}\) be the signed incidence matrix. A spanning tree has fifteen edges. Each of the other twenty-five edges yields one fundamental cycle whose coefficient on its own non-tree edge is one and on all other non-tree edges is zero. These cycles give a unimodular basis of
\[
X=H_1(\Gamma,\mathbb Z)=\ker\partial\cong\mathbb Z^{25}.
\]
The normalization gluing sequence identifies \(X\), with its Galois action, as the **character** lattice of \(T\). The action of a vertex permutation on an oriented edge includes a minus sign precisely when the edge orientation is reversed. Thus a permutation of the five blowup labels induces an explicit integral \(25\)-by-\(25\) matrix \(G\) on \(X\).

**2. Rational points from the integral matrix.** Since the torus has character group \(X\), its geometric points are \(\operatorname{Hom}(X,\overline{k}^{\times})\). Frobenius invariance means that a homomorphism annihilates \((qI-G)X\), up to replacing \(G\) by its conjugate inverse. The inverse is integrally conjugate here because every permutation of five symbols is conjugate to its inverse. The determinant of \(qI-G\) is nonzero and prime to the characteristic, hence \(T(k)\) is noncanonically isomorphic to the finite cokernel
\[
T(k)\cong\operatorname{coker}(qI-G:\mathbb Z^{25}\to\mathbb Z^{25}).
\]
In particular, a calculation of eigenvalues or group orders alone is insufficient to identify its invariant factors.

**3. Integral polynomial Smith reduction.** Write \(u\) for an indeterminate. Apply exact elementary row and column operations over \(\mathbb Z[u]\) to \(uI-G\), using only swaps, sign changes, and additions of integer-polynomial multiples of rows or columns. The resulting diagonal entries, omitting unit factors, are:

| Frobenius type | Nonunit diagonal polynomials, with multiplicities |
|:--|:--|
| \((1^5)\) | \((u-1)^{[25]}\) |
| \((2,1^3)\) | \((u-1)^{[5]},\ (u^2-1)^{[10]}\) |
| \((2^2,1)\) | \((u+1)^{[3]},\ (u^2-1)^{[11]}\) |
| \((3,1^2)\) | \((u-1),\ (u^3-1)^{[8]}\) |
| \((3,2)\) | \((u^3-1),\ (u^3-1)(u+1),\ (u^6-1)^{[3]}\) |
| \((4,1)\) | \((u^2+1),\ (u+1)(u^2+1),\ (u^4-1)^{[5]}\) |
| \((5)\) | \((u^5-1)^{[5]}\) |

Here the bracketed superscript denotes **multiplicity of a diagonal entry**, not a polynomial power. Each listed entry divides the next in \(\mathbb Z[u]\). Every row or column operation is invertible over \(\mathbb Z[u]\), so specialization \(u=q\) preserves the equivalence integrally, for **every** prime power \(q\). Replacing each specialized positive diagonal polynomial by the cyclic group of that order proves all seven group formulas. An executable implementation of the complete integer-polynomial elimination, including graph generation and its cycle basis, is supplied in `verify.py`; see the verification section.

**4. Mixed-type integral obstruction.** The rational characteristic polynomials in the two mixed cases factor as
\[
\chi_{(3,2)}(u)=(u^6-1)^3(u^3-1)^2(u+1),
\qquad
\chi_{(4,1)}(u)=(u^4-1)^5(u^2+1)^2(u+1).
\]
It would be invalid to infer an integral splitting into the corresponding induced and norm-one tori merely from these rational factors. For odd \(q\), those hypothetical direct products have respectively six and eight cyclic factors of even order, whereas the actual groups have only five and seven. The stronger, correct nontrivial invariant factors contain \((q^3-1)(q+1)\) and \((q^2+1)(q+1)\), respectively. Thus the integral point groups detect a genuine \(2\)-primary gluing not visible from rational Frobenius representations.

## Verification
Install the dependency in `requirements.txt`, and run `python3 verify.py`. The self-contained script constructs the divisor-intersection graph from the displayed classes, checks all 40 edges, its five-regularity and absence of triangles, derives a fundamental integral cycle basis, and verifies Frobenius action matrices for the seven permutations. It performs the entire symbolic diagonalization over \(\mathbb Z[u]\) by explicitly invertible row and column operations; it asserts all 25 polynomials and their divisibility chain in each case, then compares exact integer Smith forms for five numerical specializations. It terminates with `QUARTIC_DEL_PEZZO_ALL_SEVEN_PICARD_POINT_GROUPS_OK`.

The symbolic diagonalizations prove the all-field group statements. The five numerical specializations are independent regression checks, not a replacement for the symbolic argument. Verification does not establish the absence of an earlier equivalent theorem.

## Relationship to prior work
Batyrev–Popov describe the exceptional-curve classes of del Pezzo blowups, and Hassett–Kresch–Tschinkel treat quartic del Pezzo geometry and the larger \(W(D_5)\) Galois action. Geisser's corrected treatment of the affine Picard scheme supplies general theory of torus Galois modules. Those sources establish the prerequisites, not the six new finite abelian groups here. A published five-cycle study, *Five induced quintic tori for the sixteen-line boundary of a quartic del Pezzo surface*, already proves the \((5)\) row as an integral torus isomorphism and is explicitly excluded from the originality claim. Earlier complete rational-point spectra for the open del Pezzo complement can imply orders in several cases, but not the displayed Smith invariant factors. Critical-group calculations of the same graph concern the distinct graph Jacobian and do not yield \(\operatorname{coker}(qI-G)\) for all prime powers. No inspected source provided the remaining six-group classification.

## Limitations
The result is a group classification of the identity-component Picard torus, not a claim of explicit isomorphisms of algebraic tori for all types. It excludes other signed-Weyl Frobenius actions not realized by the given five-point permutation model. It makes no universal realizability claim for small finite fields and no claim about smoothing Néron component groups. Integral gluing statements concern odd \(q\); for even \(q\), relatively prime factors can yield abstractly isomorphic groups despite the different presentations. Historical priority remains provisional pending exhaustive independent literature review.

## References
1. V. V. Batyrev and O. N. Popov, *The Cox ring of a Del Pezzo surface*, arXiv:math/0309111v1, first submitted 2003-09-05; Section 2 and Theorem 2.1. https://arxiv.org/abs/math/0309111
2. B. Hassett, A. Kresch, and Y. Tschinkel, *On the moduli of degree 4 Del Pezzo surfaces*, arXiv:1312.6734v1, first submitted 2013-12-24; Sections 2 and 4. https://arxiv.org/abs/1312.6734
3. T. Geisser, *The affine part of the Picard scheme (corrected)*, arXiv:0704.0479v4, corrected 2021 version of the original 2007 preprint, especially Theorem 1. https://arxiv.org/html/0704.0479v4
4. *Five induced quintic tori for the sixteen-line boundary of a quartic del Pezzo surface*, published mathematical finding, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-five-induced-quintic-tori-for-the-sixteen-line-boundary-of-a-qua--5411549db544
