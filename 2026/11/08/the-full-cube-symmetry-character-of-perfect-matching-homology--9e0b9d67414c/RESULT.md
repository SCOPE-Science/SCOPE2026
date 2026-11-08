# The full cube-symmetry character of perfect-matching homology

## Finding
Let \(Q_3\) be the graph with vertex set \(\{0,1\}^3\), adjacent when exactly one coordinate differs. Let \(K=\mathcal M_{\mathrm p}(Q_3)\) be the simplicial complex whose vertices are the graph edges and whose facets are the nine perfect matchings. The full cube automorphism group is
\[
G=\operatorname{Aut}(Q_3)\cong (C_2)^3\rtimes S_3.
\]
Write its elements as \(g_{b,\sigma}\), with \(b\in\{0,1\}^3\) and \(\sigma\in S_3\), acting on cube vertices by
\[
(g_{b,\sigma}x)_j=x_{\sigma(j)}\mathbin{\oplus} b_j\qquad (j=1,2,3).
\]
Let \(\varepsilon_{\mathrm{perm}}\) be the one-dimensional rational representation on which \(g_{b,\sigma}\) acts by \(\operatorname{sgn}(\sigma)\), and let \(V_{\mathrm{signed}}\) be the natural three-dimensional rational signed-coordinate representation with matrix entries \(T_{j,\sigma(j)}=(-1)^{b_j}\), all other entries zero. **The new claim** is the complete rational homology-module decomposition
\[
\boxed{H_1(K;\mathbb Q)\cong\varepsilon_{\mathrm{perm}}\oplus V_{\mathrm{signed}}\quad\text{as rational }G\text{-modules}.}
\]
Equivalently, for *all* \(48\) cube automorphisms,
\[
\boxed{\operatorname{tr}\bigl(g_{b,\sigma}\mid H_1(K;\mathbb Q)\bigr)
=\operatorname{sgn}(\sigma)+\sum_{j:\,\sigma(j)=j}(-1)^{b_j}.}
\]
The two summands are irreducible over \(\mathbb Q\), and there is no nonzero vector fixed by the entire group. The central antipodal involution fixes the one-dimensional first summand and acts as minus the identity on the three-dimensional second summand; its total trace is \(-2\).

The nonequivariant fact \(K\simeq\bigvee^4 S^1\) was already covered by a published homotopy classification of circular-ladder perfect-matching complexes [3, Theorem 25] after identifying \(Q_3\cong C_4\square K_2\). It is **not** claimed as new here.

## Assumptions and scope
The graph, perfect matching, complex, action, and coefficient field are specified above. All homology groups use the ordinary simplicial chain complex with ordered graph-edge vertices and boundary signs defined by vertex deletion. The group action on chains uses the corresponding reordering signs. The theorem concerns rational first homology under the *full* graph automorphism group, not merely the dihedral subgroup preserving a chosen four-cycle and not an integral lattice decomposition. The group has \(48\) elements because an automorphism is determined by the image of the zero vertex (eight choices) and the permutation of its three neighbors (six choices); all are realized by the stated signed-coordinate maps.

## Proof
**1. The underlying homology concentration.** The graph has twelve edges and precisely nine perfect matchings. Exhaustive enumeration by matching the least uncovered vertex and recursively matching its possible neighbors gives nine tetrahedral facets and the face counts \(1,12,42,36,9\), beginning with the empty face. Cover \(K\) by its nine facet simplices. Every nonempty intersection is a simplex, so the simplicial nerve lemma applies. Every graph edge occurs in exactly three perfect matchings, and the resulting twelve triples are distinct. The nerve therefore has face counts \(1,9,24,12\).

Order the nine perfect matchings lexicographically by their sorted graph-edge lists, and index them from zero through eight. A deterministic free-face procedure chooses the lexicographically first triangle admitting a free edge and then the lexicographically first such edge. It performs twelve elementary simplicial collapses (one free edge together with its unique containing triangle at each stage). No triangle remains, and the resulting graph has nine vertices, twelve edges, and one connected component. Hence \(K\simeq\bigvee^4 S^1\), so \(H_0(K;\mathbb Q)=\mathbb Q\), \(H_1(K;\mathbb Q)=\mathbb Q^4\), and all higher homology vanishes. The executable verifier independently checks every free pair and graph connectivity, rather than relying on the face counts alone.

**2. The entire homology character.** For any automorphism \(g\), let \(L_j(g)\) be the signed trace of the permutation induced on oriented \(j\)-simplices of the **original** perfect-matching complex. A simplex contributes \(+1\), \(-1\), or \(0\) according as it is preserved with even orientation permutation, preserved with odd orientation permutation, or not preserved as a set. The Hopf trace formula and the homology concentration from Step 1 give
\[
\operatorname{tr}(g\mid H_1)=1-\sum_{j=0}^3(-1)^j L_j(g).
\]
The enumeration is finite and exhaustive: there are exactly \(8\cdot6=48\) automorphisms and exactly \(99\) nonempty faces. Evaluating the displayed formula gives the following class table. A signed cycle type \((\lambda_+,\lambda_-)\) lists the lengths of coordinate-permutation cycles with even and odd parity, respectively, of the bit flips on that cycle. The classes in the table exhaust all ten signed-cycle types of \(G\).

| Signed cycle type \((\lambda_+,\lambda_-)\) | Class size | \(\operatorname{tr}(g\mid H_1)\) |
|---|---:|---:|
| \(((1,1,1),())\) | 1 | 4 |
| \(((1,1),(1))\) | 3 | 2 |
| \(((1),(1,1))\) | 3 | 0 |
| \(((),(1,1,1))\) | 1 | -2 |
| \(((2,1),())\) | 6 | 0 |
| \(((2),(1))\) | 6 | -2 |
| \(((1),(2))\) | 6 | 0 |
| \(((),(2,1))\) | 6 | -2 |
| \(((3),())\) | 8 | 1 |
| \(((),(3))\) | 8 | 1 |

For a signed cycle of length one, the trace of \(V_{\mathrm{signed}}\) is \(+1\) for even flips and \(-1\) for odd flips; longer cycles contribute zero. The permutation sign is negative precisely when the underlying coordinate permutation is odd. These observations reproduce every entry of the table and thus prove the asserted formula for all group elements. Over characteristic zero, group characters determine the representation. The signed-coordinate module is irreducible: the diagonal flip subgroup has three distinct weight lines, and \(S_3\) permutes these lines transitively. The sign representation is irreducible and distinct, completing the stated decomposition.

**3. Nontriviality of the refinement.** The identity trace is four. At the central involution \(b=(1,1,1)\), \(\sigma=\mathrm{id}\), the trace is \(-2\) because the two summands have eigenvalues \(+1\) (multiplicity one) and \(-1\) (multiplicity three). A single coordinate permutation of transposition type has trace zero. These actions cannot be recovered from the known Betti number or the ordinary wedge description.

## Verification
The standalone file `verify_cube_perfect_matching.py` uses only the Python standard library. It constructs every graph edge and perfect matching by the least-unmatched-vertex recurrence; constructs the original complex and nerve independently; certifies twelve genuine elementary collapses and residual connectivity; enumerates all forty-eight signed permutations; and compares for *each* automorphism three values: the signed Lefschetz character from original faces, the signed Lefschetz character from nerve faces, and the closed formula. It also checks direct mod-\(p\) boundary ranks on original faces for primes \(2,3,5,7\), as well as the sign/vector character inner products. Running `python3 verify_cube_perfect_matching.py` reproduces `verification_output.txt` without external data. These finite checks cover the complete stated finite domain; they are not extrapolations to higher hypercubes.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega [1, Sections 1.1 and 2] define perfect-matching complexes and use facet nerves for honeycomb graphs, but do not calculate this cube symmetry module. Chandrakar and Singh [2, Sections 1 and 3] study polygonal line tilings, particularly open two-row grids; their graphs are not the cubical *circular* ladder and they do not determine the full cube automorphism action.

The crucial stronger comparison is Agarwal and Basak [3, Main Theorem 2 and Theorem 25], which already covers the nonequivariant homotopy type of \(Q_3=C_4\square K_2\) as a wedge of four circles. The present result adds only the complete four-dimensional *rational automorphism representation*, including its exceptional full octahedral symmetry; [3] neither states nor implies which representation occurs. Published calculations for the ordinary matching complex of the cube concern a strictly larger complex, since perfect matchings generate a proper subcomplex, and their homology is in a different degree. No equivalent full-symmetry character was identified in the searched records, but the possibility of an unindexed or uninspected equivalent calculation remains.

## Limitations
The integral group-lattice structure is not classified; equality of rational characters does not imply an integral direct-sum decomposition. No equivariant homotopy splitting or result for higher-dimensional cubes is proved. The nonequivariant wedge is previously known. Claims of originality are limited to the inspected sources and indexed comparisons; absence from search results is not a proof of novelty. All computational assertions are for precisely twelve graph edges, nine perfect matchings, 99 nonempty faces and 48 automorphisms.

## References
[1] M. Bayer, M. Jelić Milutinović, J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803v1, public September 6, 2022; Electronic Journal of Combinatorics 30(2), P2.45 (2023). https://arxiv.org/html/2209.02803v1

[2] H. Chandrakar, A. Singh, *Perfect Matching Complexes of Polygonal Line Tiling*, arXiv:2407.05809, public July 8, 2024. https://arxiv.org/abs/2407.05809

[3] A. Agarwal, B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v2, revised September 14, 2026; original public August 31, 2026. https://arxiv.org/html/2608.30601v2
