# Fifty-five three-spheres and two invariant homology classes in the Pappus non-matching complex

## Finding

Let \(P\) be the eighteen-vertex Pappus graph, the Levi graph of the \((9_3)\) Pappus point–line configuration. Define the **third non-matching complex**
\[
X=\operatorname{NM}_3(P)=\{F\subseteq E(P):\nu(F)<3\},
\]
where \(\nu(F)\) is the maximum size of a set of pairwise vertex-disjoint edges in the spanning graph with edge set \(F\). Then the ordinary integral homotopy type is
\[
\boxed{|X|\simeq\bigvee^{55}S^3.}
\]
In particular, \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z^{55}\), all other reduced integral homology groups vanish, and \(\pi_1(X)=0\).

The full group \(\operatorname{Aut}(P)\), of order \(216\), acts on \(\widetilde H_3(X;\mathbb Q)\). Its complete rational character is given below; in particular,
\[
\boxed{\dim_{\mathbb Q}\widetilde H_3(X;\mathbb Q)^{\operatorname{Aut}(P)}=2.}
\]
Thus two linearly independent rational third-homology classes survive all Pappus graph symmetries.

For each group element, classify its action by the cycle partition of its permutation of the eighteen original vertices and the cycle partition of the twenty-seven graph edges. The following eleven pairs exhaust the group; equal cycle-type pairs have equal computed trace. Superscripts denote multiplicity in a cycle partition.

| Original-vertex cycle type | Graph-edge cycle type | Group elements | \(\operatorname{tr}(g\mid\widetilde H_3(X;\mathbb Q))\) |
|---|---|---:|---:|
| \(1^{18}\) | \(1^{27}\) | 1 | 55 |
| \(1^6 2^6\) | \(1^3 2^{12}\) | 9 | 7 |
| \(1^4 2^7\) | \(1^3 2^{12}\) | 18 | 5 |
| \(1^3 3^5\) | \(3^9\) | 12 | 1 |
| \(1\,2\,3\,6^2\) | \(3\,6^4\) | 36 | -1 |
| \(2^9\) | \(1^3 2^{12}\) | 18 | 7 |
| \(2^3 4^3\) | \(1^3 4^6\) | 18 | 1 |
| \(3^6\) | \(3^9\) | 14 | 1 |
| \(3^2 6^2\) | \(3\,6^4\) | 18 | 1 |
| \(6^3\) | \(3\,6^4\) | 36 | 1 |
| \(6\,12\) | \(3\,12^2\) | 36 | 1 |

The counts sum to \(216\), and the trace sum is \(432\), giving the invariant dimension \(432/216=2\) by character averaging.

## Assumptions and scope

The labeled graph has vertex set \(\{0,1,\ldots,17\}\) and includes the eighteen cycle edges \(\{i,i+1\pmod{18}\}\), together with the nine undirected chords specified by the length-eighteen LCF sequence \([5,7,-7,7,-7,-5]^3\): at each vertex \(i\), add \(\{i,i+s_i\pmod{18}\}\), discarding duplicate undirected edges. This gives exactly twenty-seven graph edges, ordered lexicographically in the verifier. It is cubic, bipartite and has girth six. A **simplicial vertex of \(X\)** is an edge of \(P\), not a vertex of \(P\). All complexes are finite and include the empty simplex for reduced-chain bookkeeping. Homology is integral unless another coefficient ring is specified.

The homotopy statement is nonequivariant. The automorphism character statement is an additional rational equivariant-homology calculation; no integral representation-lattice decomposition or equivariant homotopy equivalence is asserted.

## Proof

**1. Exact face set.** The Pappus graph is bipartite. For any \(F\subseteq E(P)\), Kőnig's matching–vertex-cover theorem gives \(\nu(F)<3\) if and only if all edges in \(F\) are incident to at most two vertices of \(P\). Thus \(X\) is the union of the full simplices on \(\operatorname{star}_P(u)\cup\operatorname{star}_P(v)\), as \(\{u,v\}\) ranges over distinct original graph vertices. Exhaustive enumeration of their subsets (all masks on twenty-seven indexed graph edges) gives the augmented face numbers
\[
(f_{-1},f_0,f_1,f_2,f_3,f_4,f_5)
=(1,27,351,1206,1593,783,126).
\]
The reduced Euler characteristic is \(\widetilde\chi(X)=-55\). As an independent face-membership test, the verifier enumerates all \(1719\) three-edge matchings and checks selected masks against the absence of forbidden matching triples. The exact vertex-cover theorem, not the sample checks, supplies the all-subsets equivalence.

**2. Explicit complete acyclic matching.** Start with all \(4087\) augmented faces. Shuffle the indices \(0,\ldots,26\) by the precisely specified Python `random.Random(0).shuffle` operation; for each index \(i\) in that resulting order, traverse all faces in increasing cardinality and then increasing bitmask order. If a currently unmatched face \(S\) omits \(i\) and \(S\cup\{i\}\) is also currently unmatched, match this covering pair and remove both faces from further stages. The verifier implements this rule independently of any precomputed certificates. It produces \(2011\) matched pairs, leaving exactly five critical two-simplices and sixty critical three-simplices, with no other critical faces in the augmented poset.

Orient each of the \(15390\) covering edges of the augmented face-poset Hasse diagram from a higher-dimensional face to its codimension-one face, except reverse the orientation on matched covers. The standalone code constructs **every** one of these directed covers and topologically sorts all \(4087\) vertices successfully. The matching is therefore acyclic. Discard the unique pair involving the empty simplex and retain its singleton as a critical zero-cell. The remaining \(2010\) pairs form an acyclic **ordinary non-augmented** face-poset matching (a restriction of the verified acyclic matching); the ordinary Hasse diagram has \(15363\) covers. Standard discrete Morse theory therefore gives a CW model with one zero-cell, five two-cells and sixty three-cells, and no one-cells or cells in dimensions above three.

**3. Integral three-cell attaching maps.** Sort the critical two- and three-simplices by their face bitmasks. Orient each simplex by ascending edge index. The integral cellular boundary \(B\) from the sixty critical three-cells to the five critical two-cells is determined by exact gradient-path elimination. If an oriented two-simplex \(\sigma\) is matched upward to a three-simplex \(\tau\), write
\[
\partial\tau=\epsilon\sigma+\sum_{\rho\ne\sigma}\epsilon_\rho\rho,
\qquad \epsilon\in\{+1,-1\},
\]
and replace \(\sigma\) recursively by \(-\epsilon\sum_{\rho\ne\sigma}\epsilon_\rho\rho\). Critical two-simplices project to their own basis vectors, while two-simplices matched downward project to zero. Acyclicity ensures the recursion terminates. Applied to every facet of each critical three-simplex, this yields an exact \(5\times60\) integer matrix with twenty-eight nonzero entries, all of absolute value one. The submatrix in zero-based critical-three-cell columns \((1,5,12,18,48)\) has determinant \(+1\), computed by exact integer Bareiss elimination in `verify.py`.

Consequently \(B\) has rank five and primitive image in \(\mathbb Z^5\): the integral Smith diagonal has five unit entries. The two-skeleton of the Morse CW model is \(\bigvee^5S^2\). Under \(\pi_2(\bigvee^5S^2)\cong\mathbb Z^5\), every three-cell attaching map is completely described by its degree vector, a column of \(B\). Unimodular row and column changes, realized by homotopy equivalences and elementary cellular changes, transform the attaching vectors into five coordinate vectors plus fifty-five zeros. The five corresponding two-/three-cell pairs cancel up to homotopy. Therefore the remaining model is \(\bigvee^{55}S^3\), proving the asserted **integral homotopy type**, not just rational Betti numbers.

**4. Exact full symmetry character.** The checker generates all graph automorphisms by backtracking on partial vertex permutations, requiring preservation of every adjacency and nonadjacency relation to previously assigned vertices. This enumerates exactly \(216\) distinct permutations, independently corroborating the full group size. For each original-graph automorphism \(g\), let \(\overline g\) be its induced permutation of the twenty-seven edges. For each setwise fixed simplex \(F\subseteq E(P)\), its oriented cellular-chain contribution is the sign of \(\overline g\) restricted to the sorted vertices of \(F\). Summing these contributions with signs \((-1)^{\dim F}\), **including the empty face with sign minus one**, computes the reduced Lefschetz number. Because the previous part proves that only \(\widetilde H_3\) survives,
\[
\operatorname{tr}(g\mid\widetilde H_3(X;\mathbb Q))
=-\sum_{F=\overline gF}(-1)^{\dim F}\operatorname{sgn}(\overline g\mid F).
\]
Every summand is computed directly as an integer. The eleven resulting cycle-type rows are those given in the theorem. Character averaging gives exactly two invariant rational classes.

## Verification

Run `python3 verify.py` using Python 3.9 or later; it uses only the standard library. The graph is reconstructed both from its explicit edge list and from its LCF convention, and the two descriptions must agree. The program verifies the face counts, forbidden three-matchings, all discrete-Morse pairings, all directed Hasse incidences and acyclicity, signed integral gradient-path boundaries, the explicit determinant-one minor, the complete graph-automorphism enumeration and the eleven rational character rows. The deterministic output is included in `verification_output.txt`. The terminal line begins `VERIFY_OK` and reports the sphere-wedge and symmetry conclusions.

The numerical calculations exhaust the **specific finite complex**: there is no extrapolation to graph families or infinitely many parameters. The theoretical implications of a complete acyclic matching, the primitive attaching matrix, and the Lefschetz formula are supplied above rather than inferred merely from ranks over finite fields.

## Relationship to prior work

Shan and Wang [1], first publicly released September 2, 2026, study precisely the edge-based non-matching complexes and prove injectivity of top homology under bipartite edge additions (Theorems 2.1 and 2.3). That broad result predicts persistence of a nonzero top class for Pappus, but supplies neither its exact rank and homotopy type nor its \(216\)-element character. Holmsen and Lee [2] provide general bipartite vanishing bounds, not this classification.

An exact earlier computation of \(\operatorname{NM}_3\) for the Heawood incidence graph gives thirty-six three-spheres [3]. The Heawood graph is not isomorphic to Pappus, and this computation does not determine the present attaching map or equivariant character. The previously calculated **ordinary matching complex** of Pappus is \(\bigvee^{40}S^5\) [4], but it consists of pairwise disjoint edge sets, the opposite face condition to excluding three disjoint edges.

The universal bipartite robust-clique theorem [5] concerns \(I_3(H)=\{S\subseteq V(H):\alpha(H[S])\le2\}\). Although \(\operatorname{NM}_3(P)\cong I_3(L(P))\) for the line graph \(L(P)\), the line graph is **not bipartite**: three edges incident to a Pappus vertex form a triangle in \(L(P)\). Hence [5] does not cover the present complex. Its coincidental rank fifty-five for the different vertex-based complex \(I_3(P)\) does not imply this claim. The complete-bipartite hook-tensor theorem [6] does not apply to the sparse Pappus graph either. The comparison is at the level of mathematical implication, not title matching.

## Limitations

The theorem treats only the canonical eighteen-vertex Pappus graph and the third non-matching threshold. It gives an exact homotopy type and rational full-automorphism character, not a uniform theorem for all cubic bipartite graphs, not other matching thresholds, and not the integral automorphism representation lattice. Bibliographic searches cannot rule out unindexed equivalent work. Independent mathematical validation has not been performed.

## References

[1] Jiawen Shan and Zexin Wang, *Homology of non-matching complexes under edge additions and applications to their Stanley-Reisner ideals*, arXiv:2609.02621, first public version September 2, 2026. https://arxiv.org/abs/2609.02621

[2] Andreas F. Holmsen and Seunghun Lee, *Leray numbers of complexes of graphs with bounded matching number*, arXiv:2003.11270, first posted March 25, 2020. https://arxiv.org/abs/2003.11270

[3] *Complete integral non-matching homotopy filtration of the Heawood graph*, research result with full proof and checker, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-integral-non-matching-homotopy-filtration-of-the-heawoo--8c61a8d39b4a

[4] *Integral homotopy type of the Pappus graph matching complex*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-integral-homotopy-type-of-the-pappus-graph-matching-complex--db6c6c11f317

[5] *A three-sphere wedge theorem for robust clique complexes of all connected bipartite graphs*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-three-sphere-wedge-theorem-for-robust-clique-complexes-of-all--8d06720b1a2b

[6] *The integral hook-tensor theorem for bipartite three-matching avoidance*, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-the-integral-hook-tensor-theorem-for-bipartite-three-matching-av--f6ab14dd0ec4

[7] *Pappus Graph*, Wolfram MathWorld, graph definition and LCF representation. https://mathworld.wolfram.com/PappusGraph.html
