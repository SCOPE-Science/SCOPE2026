# Integral stabilizer coinvariants of the Fano cap-complex homology

## Finding
Let \(V=\mathbb F_2^3\setminus\{0\}\), and let \(K\) be the simplicial complex of subsets of \(V\) containing no Fano line \(\{a,b,a+b\}\). The natural action of \(G=\operatorname{GL}_3(\mathbb F_2)\), of order \(168\), preserves \(K\). Write \(L=\widetilde H_2(K;\mathbb Z)\) and, for a subgroup \(H\leq G\), write \(L_H=L/\langle hx-x:h\in H,\ x\in L\rangle\) for the **integral coinvariant group**.

Then \(L\cong\mathbb Z^6\), and its coinvariants under five canonical symmetry groups are
\[
\boxed{L_{G_p}\cong L_{G_\ell}\cong\mathbb Z/2\mathbb Z,\qquad
L_{C_7}\cong\mathbb Z/7\mathbb Z,\qquad
L_{N_G(C_7)}=0,\qquad L_G=0.}
\]
Here \(G_p\) fixes any Fano point, \(G_\ell\) stabilizes any Fano line setwise, \(C_7\) is any subgroup of order seven, and \(N_G(C_7)\) is its normalizer of order twenty-one. Both point and line stabilizers have order twenty-four. Transitivity and conjugation show that these isomorphism types are independent of the choices.

The meaningful integral distinction is the order-two obstruction for either natural index-seven stabilizer, despite vanishing coinvariants for the whole group and for the order-twenty-one normalizer. The previously known rational \(G\)-character does not encode this integral torsion.

## Assumptions and scope
The seven nonzero vectors are encoded by integers \(1,\ldots,7\), with binary-vector addition denoted by bitwise xor. The seven Fano lines are precisely the distinct triples \(\{a,b,a\mathbin\oplus b\}\). An oriented simplex is ordered increasingly, and simplicial boundary uses alternating signs. All homology and coinvariants are over \(\mathbb Z\); in particular, a rational or mod-two dimension is not substituted for an integral invariant. The normalizer is taken inside the point-collineation group \(G\), not the larger group allowing point-line dualities.

## Proof
**Integral homology lattice.** The complex \(K\) has face numbers \((f_0,f_1,f_2,f_3)=(7,21,28,7)\), and no higher-dimensional faces. Every allowed triangle lies in exactly one four-point cap: if its points are noncollinear \(a,b,c\), the fourth point is \(a+b+c\). Hence the seven oriented tetrahedron boundaries have disjoint, nonempty triangle supports, so the third boundary is injective.

The one-skeleton is the complete graph on seven vertices. Use the fifteen edges not incident to vertex \(1\) as coordinates for its integral cycle lattice \(Z_1\cong\mathbb Z^{15}\). In the lexicographic list of twenty-eight allowed triangles, the fifteen indices
\[
(0,1,2,3,4,5,6,7,8,9,10,11,12,16,19)
\]
select a fifteen-by-fifteen minor of the triangle-to-cycle boundary of determinant \(+1\). Therefore the triangle boundary surjects onto \(Z_1\) integrally, and its kernel \(Z_2\) is a free group of rank thirteen. The seven tetrahedron boundaries form a primitive rank-seven sublattice: after choosing the thirteen complementary triangle coordinates, each tetrahedron relation has a private coordinate with coefficient \(\pm1\) and those seven private coordinates are distinct. The resulting quotient is \(L=Z_2/\partial_3 C_3\cong\mathbb Z^6\). This also proves that the reduced integral homology in other degrees vanishes.

**Exact symmetry matrices.** Enumerate the \(168\) invertible binary matrices by the images of basis vectors, lexicographically over ordered triples \((a,b,c)\) of distinct integers in \(\{1,\ldots,7\}\) with \(a\mathbin\oplus b\ne c\). Use zero-based indices for this list. Each such matrix permutes the twenty-eight ordered triangle generators with the sign of the resulting vertex permutation. Taking the integral cycle basis from the unimodular minor, and reducing modulo the seven primitive tetrahedron boundaries, gives an explicit integral six-by-six matrix \(\rho(g)\) for the action on \(L\). All \(168\) matrices have determinant \(\pm1\), and the integral matrix identity \(\rho(gh)=\rho(g)\rho(h)\) holds for all \(168^2\) ordered pairs.

**Exact coinvariant-index certificates.** For any subgroup \(H\) listed above, make the six-row integral relation matrix \(R_H\) whose columns are \((\rho(g)-I)e_j\) for every \(g\in H\) and basis index \(0\le j<6\). Six selected columns are enough to supply sharp upper bounds on the subgroup-relation index. The table records the ordered pairs \((i,j)\) specifying group-element index \(i\) and basis column \(j\); their six-by-six determinant is the listed signed integer. The corresponding full relation matrix has the stated rank over the residue field.

| Subgroup | Six witness columns \((i,j)\) | Determinant | Modular rank |
| --- | --- | ---: | --- |
| Point stabilizer | \((18,0),(14,3),(11,2),(16,0),(3,4),(16,2)\) | \(-2\) | \(5\) modulo \(2\) |
| Line stabilizer | \((28,2),(49,4),(52,0),(54,4),(53,5),(29,2)\) | \(-2\) | \(5\) modulo \(2\) |
| Order-seven subgroup | \((160,2),(143,5),(67,0),(67,2),(33,3),(143,1)\) | \(7\) | \(5\) modulo \(7\) |
| Order-twenty-one normalizer | \((104,3),(158,5),(137,2),(68,4),(85,0),(46,0)\) | \(-1\) | \(6\) modulo \(2\) |
| Full group | \((116,3),(117,2),(142,5),(92,2),(4,4),(85,4)\) | \(-1\) | \(6\) modulo \(2\) |

For an integer rank-six relation lattice, a nonzero six-by-six minor of absolute value \(m\) forces the index to divide \(m\). In the first two cases, a modular rank deficit of one proves that the index is divisible by two, while the determinant-two minor proves the index is at most two; thus the quotient is exactly \(\mathbb Z/2\mathbb Z\). The same argument at the prime seven gives \(\mathbb Z/7\mathbb Z\) for the Singer subgroup. A determinant-one minor proves zero coinvariants for each of the last two subgroups. These are complete integral conclusions, without inference from rational character values.

## Verification
Run `python3 verify.py` from the package directory. The standard-library-only program reconstructs all Fano faces, the unimodular triangle-boundary basis, the seven independent tetrahedron boundaries and the six-dimensional integral homology lattice. It enumerates all binary collineations, computes every signed induced matrix and checks every pairwise group multiplication identity. It constructs the five relation matrices, recomputes the exact Bareiss determinants of the six-column witnesses, and checks the appropriate modular rank deficits. The full output is recorded in `verification_output.txt` and ends in `VERIFY_OK`. No floating-point arithmetic is used.

## Relationship to prior work
The general 2024 hypergraph independence-complex investigation by Jinha Kim motivates the topological setting but does not compute a Fano-plane integral homology representation or stabilizer coinvariants. Tsukuda's 2017 result relating incidence-graph independence complexes to Alexander dual hypergraph complexes is relevant: it warns that the **rational** Fano action should not be claimed as a newly discovered isolated representation. A previously published calculation already determines the six-dimensional rational exceptional \(\operatorname{GL}_3(\mathbb F_2)\)-character on the Heawood incidence graph independence complex. The present result instead computes the previously unreported **integral** quotient groups for canonical subgroups of the Fano collineation group, including order-two torsion not recoverable from that rational character. Superdock's finite-projective-plane complexes use line-facet constructions; the inspected results do not calculate these coinvariants for the line-avoiding cap complex.

## Limitations
This is a finite, exact computation for the projective plane of order two and its indicated subgroups. No uniform theorem for larger projective planes or integral isomorphism with the Heawood lattice is asserted. An equivalent integral calculation under other representation-theoretic terminology might exist outside the inspected sources. The quotient data do not determine the full isomorphism class of the \(\mathbb Z[G]\)-lattice.

## References
- Jinha Kim, *Star clusters in independence complexes of hypergraphs*, arXiv:2408.14321 (first public posting 2024-08-26), https://arxiv.org/abs/2408.14321.
- Shuichi Tsukuda, *Independence complexes and incidence graphs*, Contributions to Discrete Mathematics **12** (2017), 28–46, https://cdm.ucalgary.ca/article/download/62277/46773/178118.
- Matt Superdock, *Simplicial complexes from finite projective planes and colored configurations*, arXiv:2110.12314, https://arxiv.org/abs/2110.12314.
- *The exceptional rational homology representation of the Heawood independence complex*, published mathematical computation, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-the-exceptional-rational-homology-representation-of-the-heawood--213fded46807/RESULT.md.
