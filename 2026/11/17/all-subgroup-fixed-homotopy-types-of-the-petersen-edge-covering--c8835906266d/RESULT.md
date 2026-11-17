# All subgroup-fixed homotopy types of the Petersen edge-covering complex

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph on the two-subsets of a five-set, with disjointness adjacency. Let \(K=\operatorname{EC}(P)=M_2(P)\): its vertices are the fifteen graph edges, and an edge set is a simplex precisely when no Petersen vertex is incident with all three of its graph edges. The natural group \(S_5\) acts on \(|K|\).

**The geometric fixed-point spaces \(|K|^H\) for all 156 subgroups \(H\le S_5\) realize precisely six homotopy types:**

| Fixed-space homotopy type | Number of subgroups | Conjugacy classes |
| --- | ---: | ---: |
| \(\bigvee^4 S^7\) | 1 | 1 |
| \(S^3\vee S^3\) | 10 | 1 |
| \(S^1\) | 20 | 2 |
| \(S^0\) | 48 | 6 |
| A point | 75 | 7 |
| Empty | 2 | 2 |
| **Total** | **156** | **19** |

In particular, a transposition has fixed space \(S^3\vee S^3\); a three-cycle has fixed space \(S^1\); a five-cycle has fixed space \(S^0\); and the only subgroups with empty fixed space are \(A_5\) and \(S_5\).

## Assumptions and scope
The geometric fixed space \(|K|^H\) is the set of points fixed by **every** member of \(H\), not the orbit quotient \(|K|/H\), a homotopy-fixed-point construction, or the subcomplex of individually fixed graph edges. Empty fixed space is distinct from a contractible fixed space. All assertions concern this explicitly labeled Petersen graph and its canonical five-letter automorphism action. The nonequivariant wedge of four seven-spheres and the rational standard homology representation are prior results, not new claims.

## Proof
**1. Exact orbit-compression lemma.** Let \(H\) permute the vertices of any finite simplicial complex \(T\). A point of \(|T|\), written in barycentric coordinates, is fixed by \(H\) exactly when its coordinates are constant on each \(H\)-orbit \(O\) of vertices. Thus \(|T|^H\) is PL-homeomorphic to the realization of the simplicial complex with one vertex for each orbit \(O\) that is a face of \(T\), and with a collection of orbit-vertices forming a face exactly when the union of the corresponding orbits forms a face of \(T\). The homeomorphism sends an orbit-vertex to the barycenter of its original orbit. This proves equality of the geometric fixed space with the explicit orbit-union complex, including the empty case.

**2. Full finite enumeration, without unexamined cases.** Label the ten graph vertices lexicographically by pairs from \(\{0,1,2,3,4\}\), and label graph edges lexicographically by disjoint endpoint pairs. Enumerate the 120 permutations of the five labels and their induced permutations of the fifteen graph edges. Starting with the identity subgroup, repeatedly adjoin each group element and close under multiplication and inverses, retaining each new subgroup. This generates exactly 156 distinct subgroups, closed under conjugation. Partitioning them into conjugacy classes gives exactly 19 classes. Every subgroup belongs to one of these computed classes because every generated subgroup has been compared with all conjugates; moreover, conjugate subgroups have homeomorphic fixed spaces via the ambient action.

**3. Acyclic discrete-Morse certificates on all 19 representative fixed complexes.** For each representative subgroup, find its graph-edge orbits. Enumerate every union of those orbits and retain it precisely when it contains none of the ten three-edge stars. On this augmented face poset, apply the successive vertex-toggle matching in the specified order from `verify.py`: pair each remaining face not containing a chosen orbit-vertex with its coface obtained by adding that vertex whenever both remain; remove the pair before the next toggle. There are only five nonstandard toggle orders, explicitly listed in the verifier as `orders`; every other representative uses increasing orbit order. For every representative, the code checks each matched cover relation and topologically sorts the **entire** Hasse graph, with matched cover edges reversed and all other covers pointing downward. Every vertex of every directed graph is visited, so all 19 matchings are acyclic.

The resulting unreduced critical cardinality profiles, by representative index from zero to eighteen, are respectively
`8:4; 4:2; none; 2:1; none; none; none; 1:1; 1:1; 1:1; 2:1; none; 1:1; 1:1; none; 1:1; none; 0:1; 0:1`.
Here a critical face of cardinality \(j\) is a reduced critical cell of dimension \(j-1\); cardinality zero denotes the empty face. This displays exactly the six homotopy types in the table. An acyclic augmented matching with no critical faces yields a contractible nonempty complex; one critical \(j\)-face yields a \((j-1)\)-sphere for \(j\ge1\); several critical faces all in dimension at least two yield their sphere wedge, because the associated ordinary Morse CW complex has one zero-cell and no intermediate cells. For \(j=1\), the result is two-point \(S^0\). Only the empty face surviving means the geometric fixed space is empty. The two empty cases have respective group orders 60 and 120 and are \(A_5\) and \(S_5\).

**4. Complete class multiplicities.** The 19 representatives, in the verifier's deterministic order, have subgroup-order/conjugacy-class-size pairs
`1/1, 2/10, 2/15, 3/10, 4/15, 4/5, 4/15, 5/6, 6/10, 6/10, 6/10, 8/15, 10/6, 12/10, 12/5, 20/6, 24/5, 60/1, 120/1`.
Summing their class sizes in each critical-profile category gives \(1,10,20,48,75,2\), respectively, and the sum across categories is 156. This exhausts all subgroups.

## Verification
Run `python3 verify.py` with Python 3 and only the standard library. It rebuilds the graph, all permutations, multiplication and inverses, all 156 subgroups and 19 conjugacy classes; constructs every orbit-union fixed complex; checks the matching orders and all pairs; constructs and topologically sorts the full directed Hasse graph for every representative; and tests the exact final category census. The deterministic output in `verification_output.txt` ends in `PETERSEN_M2_FIXED_LOCI_ALL_SUBGROUPS_PASS`. All calculations are finite and exhaustive; no sampled computations or unproved infinite extrapolations are used.

## Relationship to prior work
Marietti and Testa (arXiv:0705.1461, §4.5) define edge covering complexes for any graph, and prove homotopy theorems for **forests**, not for this cubic Petersen graph and its fixed loci. Kawamura (2011) gives general homology comparisons for edge covering and independence complexes, not geometric fixed-set homotopy classifications. Existing public calculations of this exact Petersen \(2\)-matching complex already give \(K\simeq\bigvee^4 S^7\) and its standard \(S_5\)-module in degree seven, including rational homology of subgroup **quotients**. They do not determine the geometry of subgroup **fixed-point spaces**. In particular, averaging rational homology of \(K\) to obtain quotient invariants cannot imply that a transposition's geometric fixed space is two three-spheres or that five-cycle fixed space consists of two points.

## Limitations
This is a complete fixed-space classification only for this graph and the specified \(S_5\) action. It does not give equivariant attaching maps, all equivariant homotopy groups, or an analogous classification for larger Kneser graphs. Finite exhaustive verification establishes the stated cases, but cannot prove nonexistence of equivalent unindexed literature; independent validation and publication-priority assessment remain outstanding.

## References
1. M. Marietti and D. Testa, *A simple uniform approach to complexes arising from forests*, arXiv:0705.1461, first posted 2007-05-10, §4.5, https://arxiv.org/abs/0705.1461.
2. K. Kawamura, *Independence Complexes and Edge Covering Complexes via Alexander Duality*, *Electron. J. Combin.* 18 (2011), P39, first published 2011-02-14, https://doi.org/10.37236/526.
3. *The Petersen 2-matching complex is a wedge of four 7-spheres*, published 2026-10-04, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-the-petersen-2-matching-complex-is-a-wedge-of-four-7-spheres--c0442780c8c1/RESULT.md.
4. *The Petersen two-matching homology realizes the standard five-letter module*, published 2026-10-18, https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-the-petersen-two-matching-homology-realizes-the-standard-five-le--784054f0ca41/RESULT.md.
