# Natural equivariant sphere models for acyclic directed-subgraph complexes

## Finding

For every finite nonempty **loop-free simple directed graph** \(G=(V,E)\), let \(K(G)\) be the simplicial complex whose nonempty faces are the nonempty arc sets \(F\subseteq E\) for which \((V,F)\) has no directed cycle. Let \(\Gamma=\operatorname{Aut}(G)\), and let \(\mathcal C\) be the partition of \(V\) into strongly connected components (SCCs), including singleton components. Put
\[
W_G=\left\{x\in\mathbb R^V:\sum_{v\in C}x_v=0\ \text{for every}\ C\in\mathcal C\right\}.
\]
The coordinate-permutation action of \(\Gamma\) preserves this Euclidean space. Write \(S(W_G)\) for its unit sphere, with the convention \(S(0)=\varnothing\).

**Equivariant classification.** If \(G\) has an arc between distinct SCCs, \(|K(G)|\) is \(\Gamma\)-equivariantly contractible. Otherwise there is a \(\Gamma\)-homotopy equivalence
\[
|K(G)|\simeq_\Gamma S(W_G).
\]
The equivalence is natural under digraph isomorphisms. In particular, for **every** subgroup \(H\leq\Gamma\), if no inter-SCC arc exists, then
\[
|K(G)|^H\simeq S^{o_V(H)-o_{\mathcal C}(H)-1},\qquad
|K(G)|/H\simeq S(W_G)/H,
\]
where \(o_V(H)\) is the number of \(H\)-orbits on vertices and \(o_{\mathcal C}(H)\) is the number of its orbits on SCCs; \(S^{-1}\) means the empty space. If inter-SCC arcs exist, every subgroup fixed space and quotient is contractible. If \(\dim W_G=|V|-|\mathcal C|>0\), the integral top reduced homology is a rank-one \(\Gamma\)-module with character
\[
\chi_G(g)=\operatorname{sgn}(g\text{ on }V)\,\operatorname{sgn}(g\text{ on }\mathcal C).
\]
These are ordinary geometric fixed spaces and quotients, not homotopy fixed points or Borel constructions.

## Assumptions and scope

The graph is finite, directed, nonempty at the vertex level, without loops or repeated ordered arcs; opposite arcs are allowed. Its automorphism group acts on arcs by relabeling their endpoints. A directed path of length zero establishes self-reachability, so isolated vertices count as singleton SCCs. Geometric realization of the complex with only the empty simplex is taken to be the empty space. All equivalences are in the usual topological sense for finite \(\Gamma\)-CW spaces, and the group action is the *actual* simplicial action. No assertion of a PL homeomorphism to the representation sphere is made.

## Proof

**1. Cross-component contraction.** Let \(T\subseteq E\) consist of every arc between distinct SCCs. The condensation digraph on SCCs is acyclic. Thus adjoining all of \(T\) to any acyclic \(F\subseteq E\) cannot introduce a directed cycle: any cycle would either project to a directed condensation cycle or lie wholly inside one component, where \(F\) is already acyclic. When \(T\ne\varnothing\), the map \(F\mapsto F\cup T\) shows that \(K(G)\) is a cone in the equivariant sense: every simplex and the simplex \(T\) have a common simplex. The affine homotopy from each point to the barycenter of \(T\) stays inside their common simplex. As \(T\) is \(\Gamma\)-invariant, this contraction is \(\Gamma\)-equivariant. Its restriction to \(H\)-fixed spaces and descent to \(H\)-quotients are also contractions.

**2. A natural equivariant sink equivalence on a strongly connected component.** Assume first that \(G\) is strongly connected with \(n=|V|\geq2\). Let \(P\) be the inclusion poset of nonempty acyclic arc sets. Let \(Q\) be the poset of proper nonempty vertex subsets ordered by **reverse inclusion**. For \(F\in P\), define \(s(F)\) to be the vertices with no outgoing arc in \(F\) (isolated vertices are included). A finite DAG has a sink, and since \(F\) is nonempty it also has the tail of an arc; hence \(\varnothing\subsetneq s(F)\subsetneq V\). As arcs are added, sinks can only disappear, so \(s:P\to Q\) is order preserving. This construction commutes with every graph automorphism.

Fix \(S\subsetneq V\), \(S\ne\varnothing\), and write \(Q_{\leq S}\) for the lower interval in reverse inclusion. Its inverse image under \(s\) consists exactly of those \(F\) containing **no arc whose tail lies in \(S\)**. Let \(A(S)\) be the set of all arcs in \(G\) entering \(S\) from \(V\setminus S\). Strong connectivity implies \(A(S)\ne\varnothing\). If \(F\) belongs to the fiber, \(F\cup A(S)\) is acyclic: any new arc enters \(S\), and \(F\cup A(S)\) has no arc leaving \(S\), so no new directed cycle is possible. The monotone poset maps
\[
F\subseteq F\cup A(S)\supseteq A(S)
\]
are order homotopies furnishing a contraction of the fiber to \(A(S)\). They commute with every automorphism stabilizing \(S\); therefore this fiber is contractible **equivariantly under its stabilizer**. The equivariant poset fiber theorem of Thévenaz and Webb now proves that \(s\) induces a \(\Gamma\)-homotopy equivalence of order complexes
\[
|\operatorname{sd}K(G)|\simeq_\Gamma |\Delta(Q)|.
\]
The latter is the barycentric subdivision of the boundary of the simplex on \(V\). Translating the simplex barycenter to the origin and radially normalizing gives a \(\Gamma\)-equivariant homeomorphism to the unit sphere of \(\{x\in\mathbb R^V:\sum_{v\in V}x_v=0\}\), completing the strongly connected case. Barycentric subdivision is naturally \(\Gamma\)-homeomorphic to the original realization.

**3. Disjoint SCCs and permutations of factors.** If no arcs join SCCs, the acyclic-set complex is the abstract join of the corresponding component complexes; singleton components contribute no arc vertices and are omitted from the join. For each nontrivial component, step 2 gives a natural equivariant equivalence to its vertex-augmentation sphere. These maps form an equivariant join even when \(\Gamma\) permutes isomorphic components, because the sink map and radial projection commute with all component isomorphisms. The standard join-of-unit-spheres homeomorphism identifies this join with the unit sphere of their orthogonal direct sum, precisely \(W_G\). If all components are singletons, both the original realization and \(S(W_G)\) are empty. This proves the classification without requiring components to be individually preserved by each automorphism.

**4. Fixed spaces, quotients, and the orientation character.** Equivariant homotopy equivalences restrict to ordinary \(H\)-fixed spaces and descend to ordinary \(H\)-quotients. Every vector of \(W_G^H\) is constant on vertex orbits. The SCC-sum constraints have exactly one independent equation per orbit of SCCs, giving \(\dim W_G^H=o_V(H)-o_{\mathcal C}(H)\). Consequently \(S(W_G)^H=S(W_G^H)\) has the stated sphere dimension, including the empty case. Finally, the orthogonal \(\Gamma\)-module splitting
\[
\mathbb R^V=W_G\oplus\operatorname{span}\{\mathbf{1}_C:C\in\mathcal C\}
\]
has the second summand isomorphic to the SCC permutation module (normalized indicator vectors give an orthonormal permuted basis). Taking determinants gives \(\det(g\mid W_G)=\operatorname{sgn}(g\mid V)\operatorname{sgn}(g\mid\mathcal C)\). This determinant is the top reduced integral homology action of the representation sphere when \(\dim W_G>0\).

## Verification

A standalone checker is supplied at `checks/verify.py`. Running `python3 checks/verify.py` outputs `VERIFY_OK` and the tested instance and face counts. It exhaustively enumerates every labeled loopless digraph on two and three vertices and each of their cyclic automorphism actions. It additionally tests a reproducible, seeded collection of four- and five-vertex digraphs, skipping samples with over sixteen eligible arc orbits. For each included case, it explicitly forms allowed arc orbits, verifies directed acyclicity of all orbit-set combinations, computes the reduced Euler characteristic of the actual fixed-orbit triangulation, and compares it to the SCC and vertex-orbit formula. The program also cross-checks SCC orbit counts against the quotient digraph. These finite checks are consistency tests only: the infinite generality and actual equivariant homotopy type are established by the proof above, not by enumeration.

## Relationship to prior work

Hultman's 2003 dissertation, Paper 3, Theorem 3.3.3, and the published version's Theorem 3.3 (2004) **already determine the nonequivariant** sphere-or-contractible classification for exactly these acyclic directed-subgraph complexes. The sphere dimension \(|V|-|\mathcal C|-1\), the ordinary contractible case, and the component join are prior results, not new claims here. Hultman explicitly attributes the complete-digraph strongly connected predecessor to Björner–Welker (1999). The present contribution is the natural, group-equivariant **representation-sphere model** for an arbitrary digraph and its consequences for every automorphism subgroup's geometric fixed spaces, ordinary quotient model, and integral orientation character. A nonequivariant homotopy equivalence alone neither supplies the equivariant model nor determines fixed-point homotopy types. The equivariant Quillen fiber criterion used here is established in Thévenaz–Webb (1991); the original application to this sink-poset map is what is being asserted. A literature-search failure is not a proof of priority, and the 1999 article's complete full text was not accessible for detailed comparison.

## Limitations

The classification assumes loopless simple digraphs and *graph automorphisms*; arbitrary arc-permuting simplicial symmetries are not covered. Its quotient conclusion is a representation-sphere quotient, not a uniform wedge-of-spheres decomposition for every subgroup. No PL homeomorphism between \(|K(G)|\) and \(S(W_G)\) is asserted. The empty-space convention matters when all SCCs are singleton. Although the main structural proof is self-contained modulo the cited equivariant poset fiber theorem, the article by Björner and Welker (1999) was accessible only through its abstract and the full-text Hultman citation; previously unindexed equivariant results remain possible. The finite checker is not an exhaustive validation of all four- or five-vertex digraphs.

## References

1. Axel Hultman, *Combinatorial complexes, Bruhat intervals and reflection distances*, Royal Institute of Technology dissertation (Stockholm, publicly defended October 21, 2003), Paper 3, §3.3, Theorem 3.3.3. https://www.diva-portal.org/smash/get/diva2%3A9451/FULLTEXT01.pdf
2. Axel Hultman, “Directed Subgraph Complexes,” *Electronic Journal of Combinatorics* 11 (2004), R75, published October 26, 2004, Theorem 3.3. https://doi.org/10.37236/1828
3. Anders Björner and Volkmar Welker, “Complexes of Directed Graphs,” *SIAM Journal on Discrete Mathematics* 12 (1999), 413–424, Theorem 2.2 as cited by Hultman. https://doi.org/10.1137/S0895480198338724
4. Jacques Thévenaz and Peter J. Webb, “Homotopy equivalence of posets with a group action,” *Journal of Combinatorial Theory, Series A* 56 (1991), 173–181, Theorem 1. https://doi.org/10.1016/0097-3165(91)90030-K ; author's copy: https://www-users.cse.umn.edu/~webb/Publications/posets.pdf
