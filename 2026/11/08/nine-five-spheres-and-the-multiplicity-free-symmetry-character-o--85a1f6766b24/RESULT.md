# Nine five-spheres and the multiplicity-free symmetry character of the Franklin dominance complex

## Finding
Let \(F\) be the Franklin graph, defined on vertices \(0,1,\ldots,11\) by the twelve cyclic edges \(\{i,i+1\pmod {12}\}\) and the six distinct chords \(\{i,i+5(-1)^i\pmod {12}\}\), where the index \(i\) in the chord expression is taken through all twelve vertices. Let \(X=\operatorname{Dom}(F)\) denote the simplicial complex whose faces are complements of dominating vertex sets. Then

\[
X\simeq\bigvee^{9}S^5,
\qquad \widetilde H_k(X;\mathbb Z)=\begin{cases}\mathbb Z^9&k=5,\\0&k\ne5.\end{cases}
\]

The full automorphism group \(G=\operatorname{Aut}(F)\) has order \(48\) and is isomorphic to \(S_4\times C_2\). Its action on \(\widetilde H_5(X;\mathbb Q)\) is multiplicity-free: for the splitting of \(G\) explicitly constructed and verified by the accompanying program,

\[
\widetilde H_5(X;\mathbb Q)\cong
\bigl(S^{(2,1,1)}\oplus\operatorname{sgn}\bigr)\boxtimes\mathbf 1
\;\oplus\;
\bigl(\mathbf 1\oplus S^{(2,1,1)}\oplus\operatorname{sgn}\bigr)\boxtimes\varepsilon.
\]

Here \(S^{(2,1,1)}\) is the three-dimensional irreducible \(S_4\)-module, \(\operatorname{sgn}\) the sign module, and \(\varepsilon\) the nontrivial character of \(C_2\). Equivalently, the character values on the \(48\) elements are \(-3,-1,1,3,9\), with multiplicities \(6,24,9,8,1\), respectively. The invariant subspace is zero. The central involution \(i\mapsto i+6\pmod{12}\) has trace \(-1\), so it has rational eigenspaces of dimensions \(4\) and \(5\).

## Assumptions and scope
All graphs are finite simple undirected graphs. The displayed labeled edge set is the definition, not a choice of an unrecorded database graph. For a vertex \(v\), write \(N[v]\) for its closed neighborhood. A subset \(\sigma\subseteq V(F)\) is a face precisely when no closed neighborhood \(N[v]\) is contained in \(\sigma\). This is equivalent to the complement \(V(F)\setminus\sigma\) dominating every vertex. The empty set is a face; ordinary reduced simplicial homology is used, over \(\mathbb Z\) and \(\mathbb Q\) as specified. The result concerns this individual twelve-vertex graph and its natural vertex-action, not all cubic graphs.

## Proof
**(1) Face system and matching.** For each of the \(2^{12}=4096\) vertex masks, membership is decided by checking the twelve closed-neighborhood masks. An independent dominating-complement predicate agrees on every mask. The numbers of faces by dimension \(-1,0,\ldots,7\) are
\[
(1,12,66,220,483,696,612,276,51),
\]
with \(2416\) nonempty faces. On the nonempty face poset take the following deterministic partial matching: begin with all nonempty faces unmatched; for \(v=0,1,\ldots,11\), in increasing integer-mask order, pair each still-unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) whenever both faces are still unmatched, and remove both from further consideration. This produces \(1203\) distinct covering pairs. The remaining faces are one vertex and nine five-simplices.

To certify acyclicity, orient every nonempty face-poset covering relation from the larger face to the smaller, except reverse each matched incidence. There are exactly \(12216\) such incidences. Construct the complete directed graph of these incidences, and perform topological sorting, repeatedly removing all vertices of indegree zero. The supplied standalone integer-mask verifier explicitly checks every incidence and records that all \(2416\) vertices are removed, proving that the directed graph is acyclic. Thus the matching is an acyclic discrete-Morse matching, not merely a list of pairs. Forman's discrete-Morse theorem yields a CW model with one zero-cell and nine five-cells and no cells in other dimensions. All attaching maps of these five-cells have target a point, so that model is precisely \(\bigvee^9 S^5\).

**(2) Symmetry and character.** Enumerate vertex bijections by adjacency-compatible backtracking and verify that every resulting permutation preserves all eighteen edges. There are exactly \(48\) such permutations. For any such \(g\), the *reduced* alternating simplicial trace is computed by summing over \(g\)-fixed faces (including the empty face with the reduced augmentation sign) the parity of the vertex-order permutation induced on each face, times the alternating dimension sign. This is the reduced Lefschetz number \(L(g)\). Since the only reduced rational homology is in odd degree five, \(\chi(g)=-L(g)\). Independent algorithms (fixed-face iteration and complete-cycle-union iteration) give the same value for each of the \(48\) permutations. Their value multiset is \(\{9^{\times1},3^{\times8},1^{\times9},(-1)^{\times24},(-3)^{\times6}\}\). Consequently \(\sum_g\chi(g)=0\) and \(\sum_g\chi(g)^2=240\); dividing by \(|G|=48\) gives zero invariants and character inner product \(5\).

For an explicit group splitting, the verifier constructs a homomorphism \(G\to C_2\) taking the central involution \(z(i)=i+6\) to the nontrivial value and checks all \(48^2\) products. Its kernel \(H\) has order \(24\), intersects \(\langle z\rangle\) trivially and therefore yields \(G=H\times\langle z\rangle\). Conjugation of \(H\) on its four order-three Sylow subgroups is faithful, giving an isomorphism \(H\cong S_4\). The trace pairs on representatives of the five \(S_4\) cycle types are:

| \(S_4\) cycle type | Class size | \(\chi(h)\) | \(\chi(zh)\) |
|---|---:|---:|---:|
| \((1,1,1,1)\) | 1 | 9 | -1 |
| \((2,1,1)\) | 6 | -3 | -1 |
| \((2,2)\) | 3 | 1 | -1 |
| \((3,1)\) | 8 | 3 | -1 |
| \((4)\) | 6 | 1 | -1 |

Inner products with the ten characters of \(S_4\times C_2\), computed exactly from the five \(S_4\) class sizes and the signed \(C_2\) coordinate, give multiplicity one for exactly the five representations displayed in the finding and zero otherwise. This establishes the complete rational character and multiplicity-free decomposition; it does not assert a canonical choice of the \(S_4\) complement.

## Verification
Run `python3 franklin_dom_verify.py` with Python \(3.10\) or later (standard library only). The program reconstructs the graph and every face rather than loading a purported result, checks two independent face criteria on all \(4096\) masks, produces the specified matching, tests all \(12216\) Hasse incidences for acyclicity, and independently calculates mod-two simplicial boundary ranks. It enumerates and verifies all \(48\) automorphisms, computes Lefschetz traces by two algorithms, constructs and checks the stated direct-product splitting, and evaluates the full irreducible character decomposition. Its expected output is included as `verification_output.txt`; the final line is `FRANKLIN_DOMINANCE_TOPOLOGY_CHARACTER_PASS`. The mod-two ranks are corroboration: the integral homotopy assertion follows from the complete acyclic matching and discrete-Morse theorem, not from finite-field ranks alone.

## Relationship to prior work
Marietti and Testa introduce and study this dominance-complex construction and classify the case of **forest graphs** in *A Simple Uniform Approach to Complexes Arising from Forests*, arXiv:0705.1461, Section 4.3. The Franklin graph contains cycles and is not a forest. Taylan's *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs*, arXiv:1501.06754, treats broader matching-tree methods and the **chordal** setting, but Franklin is not chordal. Matsushita and Wakatsuki's *Dominance Complexes, Neighborhood Complexes and Combinatorial Alexander Duals*, arXiv:2312.02639, gives a general duality of \(\operatorname{Dom}(F)\) with the open-neighborhood complex of the **complement graph**. That duality gives a potential alternative way to derive this case but does not itself specify its nine generators or automorphism character.

Published exact results for the same Franklin graph concern its ordinary matching complex (an edge-vertex complex on eighteen graph edges) or graph-theoretic paired domination; their conclusions do not determine the twelve-vertex dominance complex. Results for domination complexes whose *simplicial vertices are entire graphs* concern a different construction. A targeted literature and mathematical-result comparison found no inspected earlier theorem determining both the homotopy type and complete character here; such negative search evidence does not establish definitive publication priority.

## Limitations
The computation and complete finite certificate apply only to the labeled Franklin graph (up to relabeling), not to all cubic, bipartite, or Klein-bottle graphs. The \(S_4\) splitting used for the displayed decomposition is constructed explicitly and is not claimed canonical. The rational irreducible character does not specify integral irreducible lattices or an equivariant sphere-wedge homotopy splitting. Complete absence of equivalent unindexed or unpublished work has not been demonstrated. No independent mathematical audit is claimed.

## References
1. M. Marietti and D. Testa, *A Simple Uniform Approach to Complexes Arising from Forests*, arXiv:0705.1461, initially public May 10, 2007. Section 4.3.
2. E. Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs*, arXiv:1501.06754, initially public January 27, 2015.
3. T. Matsushita and S. Wakatsuki, *Dominance Complexes, Neighborhood Complexes and Combinatorial Alexander Duals*, arXiv:2312.02639, initially public December 5, 2023.
4. Wolfram MathWorld, *Franklin Graph*, https://mathworld.wolfram.com/FranklinGraph.html, graph description and LCF notation.
