# Disjoint quadrilateral edge defects in fourth robust clique complexes of bicliques

## Finding

For integers \(a,b\ge4\), let \(A\) and \(B\) be disjoint sets of cardinalities \(a\) and \(b\). Start with the complete bipartite graph \(K_{a,b}\) and remove the four cross-edges of each of \(m\) vertex-disjoint copies of \(K_{2,2}\), where \(0\le m\le\min(\lfloor a/2\rfloor,\lfloor b/2\rfloor)\). Write the resulting graph as \(G_m\), and let \(X_m=\mathsf{Cliq}_4(G_m)\) denote the complex of vertex subsets inducing no independent set of four vertices.

Set \(R=\binom{a-1}{3}\binom{b-1}{3}\) and \(d=(a-3)(b-3)\). **Theorem.** For all allowed parameters except \((a,b,m)=(4,4,2)\),

\[|X_m|\simeq\bigvee^{R-md}S^5.\]

A wedge with zero sphere summands denotes a contractible space. In the exceptional configuration, \(G_2\) is the disjoint union of two four-cycles, and

\[|X_2|\simeq S^4\qquad(a=b=4).\]

The result is integral: all reduced homology is free abelian, and no other nonzero reduced homology groups occur. With successive square-edge deletions there are inclusions \(X_m\subseteq X_{m-1}\subseteq\cdots\subseteq X_0\). Except at the last exceptional deletion, each inclusion induces an injection on fifth integral homology with free cokernel of rank \(d\), hence a split injection. In the exceptional \((4,4,2)\) case the source acquires \(\widetilde H_4\cong\mathbb Z\) while the preceding stage is contractible.

For example, on shores of size six, the fifth Betti numbers as the zero, first, second, and third disjoint quadrilateral edge blocks are deleted are \(100,91,82,73\). For shores of size four, the stages are \(S^5\), a point, and \(S^4\).

## Assumptions and scope

The deleted edge blocks are distinct complete bipartite graphs on exactly two vertices of each shore and have pairwise disjoint vertex sets. The four edges of each block are all removed; all other cross-edges remain. Isolated unused vertices in a shore are allowed. Both original shore sizes are at least four. All homotopy equivalences are ordinary nonequivariant equivalences, and all maps in the persistence statement are induced by the indicated simplicial inclusions.

The fourth robust clique complex uses the definition of Kim and Lew and of Filakovský: a simplex is a vertex subset containing no independent four-element set. It is **not** an ordinary clique complex, an independence complex, or a complex of induced subgraphs with maximum degree two.

## Proof

**1. Exact face classification.** Let the left and right vertex pairs of deleted block \(i\) be \(P_i\subset A\) and \(Q_i\subset B\), respectively, and write \(T_i=P_i\cup Q_i\). Every independent four-set entirely in one shore is forbidden. A mixed independent four-set with three vertices in one shore and one in the other is impossible: each graph vertex has at most two deleted cross-edges. Thus a mixed independent four-set necessarily has two vertices on each side, and all four crossing edges must be missing. Since the deleted blocks are vertex-disjoint, this happens exactly for \(T_1,\dots,T_m\).

Let \(L_A=\operatorname{sk}_2\Delta^{a-1}\) and \(L_B=\operatorname{sk}_2\Delta^{b-1}\). The intact-biclique complex is \(Y=L_A*L_B\), and the precise description is

\[X_m=\{\sigma\in Y:T_i\nsubseteq\sigma\text{ for all }1\le i\le m\}.\]

Both two-skeleta are wedges of, respectively, \(\binom{a-1}{3}\) and \(\binom{b-1}{3}\) two-spheres. Hence \(Y\simeq\bigvee^R S^5\). Because a face of \(Y\) has at most three vertices on either shore, it cannot contain two disjoint \(T_i\).

**2. Relative groups, with their integral generators.** Every relative face of \((Y,X_m)\) contains exactly one \(T_i\). Its other vertices constitute a face of \(\operatorname{lk}_Y(T_i)\). Consequently the relative augmented cellular chain groups split **on the chain level** as the direct sum of the augmented link chains, each shifted by four degrees, with compatible signed simplicial boundaries:

\[C_q(Y,X_m;\mathbb Z)\cong\bigoplus_{i=1}^{m}\widetilde C_{q-4}(\operatorname{lk}_Y(T_i);\mathbb Z).\]

Each link is the join of two discrete vertex sets, one of size \(a-2\), the other of size \(b-2\); it is the complete bipartite one-dimensional complex \(K_{a-2,b-2}\). It is connected and its first homology is the tensor product of the two reduced zeroth homologies:

\[H_5(Y,X_m;\mathbb Z)\cong\bigoplus_{i=1}^m\big(\widetilde H_0(A\setminus P_i;\mathbb Z)\otimes\widetilde H_0(B\setminus Q_i;\mathbb Z)\big)\cong\mathbb Z^{md}.\]

All other relative homology groups vanish. The long exact sequence is therefore

\[0\to H_5(X_m)\to\mathbb Z^{R}\xrightarrow{\Phi_m}\mathbb Z^{md}\to H_4(X_m)\to0,\]

with all reduced homology below degree four equal to zero.

**3. Integral surjectivity except at one boundary.** We use an explicit integral basis of \(H_2(L_A)\): fixing one vertex \(v_0\in A\), the oriented boundaries of the tetrahedra on \(\{v_0,i,j,k\}\) for triples of other vertices are a basis. The analogous classes form a basis on \(B\). Their joins generate \(H_5(Y)\) integrally.

More specifically, for any fixed block \(i\) and distinct \(x,y\in A\setminus P_i\), the oriented boundary of the tetrahedron \(P_i\cup\{x,y\}\) determines in the reduced zeroth homology of the left link the primitive difference \(\pm([x]-[y])\). Likewise a tetrahedral boundary on \(Q_i\cup\{u,v\}\) gives \(\pm([u]-[v])\) on the right. The join of these cycles has its relative \(i\)-component equal to their integral tensor product.

Suppose \(a\ge5\). On the \(a-2\) vertices outside \(P_i\), construct the graph containing every pair except the pairs \(P_j\) belonging to other removed blocks. This is a complete graph with a matching deleted and is connected, because it has at least three vertices. Hence the differences \([x]-[y]\) along its edges generate the **entire integral augmentation lattice** of the left link. For such an allowed pair \(x,y\), the tetrahedral boundary involving \(P_i,x,y\) contains no other removed left pair \(P_j\). Therefore its join with any right tetrahedral boundary has no relative component in any summand \(j\ne i\). The right differences generate the whole right augmentation lattice, so \(\Phi_m\) hits the complete integral tensor-product lattice in summand \(i\), and zero in all other summands. Repeating for each \(i\) shows \(\Phi_m\) is surjective as a homomorphism of free abelian groups. If \(b\ge5\), the same argument applies with the shores exchanged.

When \(a=b=4\), at most two blocks are possible. For one block, both residual links are \(K_{2,2}\) and a tetrahedral-boundary join maps to a generator of its \(H_1\); therefore the map is surjective. The case of zero blocks is tautological. When \(a=b=4\) and \(m=2\), the domain \(H_5(Y)\) has rank one, both relative link homology groups have rank one, and the unique domain generator maps to \((\pm1,\pm1)\). Hence \(\ker\Phi_2=0\) and \(\operatorname{coker}\Phi_2\cong\mathbb Z\), without torsion.

It follows that in the ordinary cases \(\widetilde H_5(X_m;\mathbb Z)\cong\mathbb Z^{R-md}\) and all other reduced homology groups vanish. In the exceptional case, the only reduced group is \(\widetilde H_4\cong\mathbb Z\).

**4. From integral homology to homotopy.** Every \(X_m\) contains the full two-skeleton of the simplex on \(a+b\) vertices: forbidden independent sets have four vertices. Hence \(X_m\) is simply connected. The vanishing of second and third homology, together with the Hurewicz theorem applied successively, implies that it is three-connected. In an ordinary case, its fourth homology vanishes as well, making it four-connected. Choose maps from a basis of its fifth homology represented by spheres; their wedge induces an integral homology isomorphism from \(\bigvee^{R-md}S^5\). The homology Whitehead theorem gives a homotopy equivalence. With rank zero, a simply connected integral-acyclic finite complex is contractible. In the exceptional case, the fourth-homology generator is spherical and yields a homology equivalence \(S^4\to X_2\), hence a homotopy equivalence. This also excludes higher nonzero attaching obstructions in these five-dimensional complexes.

**5. Inclusion-induced maps.** Let \(\Phi_t\) denote the homomorphism to the first \(t\) link summands. The natural map \(H_5(X_t)\to H_5(Y)\) identifies it with \(\ker\Phi_t\). These kernels form nested subgroups under restorations. The integral surjectivity above shows every ordinary successive quotient is a free group of rank \(d\); a subgroup of a free abelian group with torsion-free quotient is a direct summand. At \((4,4,2)\), the preceding first-defect complex is contractible, while the twice-defective complex has its single degree-four class, which maps to zero. This proves the complete inclusion statement.

## Verification

Two executable, independently structured finite checks accompany the proof. `verify_integral_maps.py` computes the integral relative boundary matrices of the joins of tetrahedral-boundary generators and their Smith normal forms for twenty finite configurations on shores of sizes four through seven. Every ordinary matrix has maximal row rank with all nonzero invariant factors one; the exceptional four-by-four two-block map has primitive rank one into a rank-two target.

`verify_finite_homology.py` builds the complex simplices directly from the forbidden mixed and monochromatic four-subsets, calculates complete mod-two reduced simplicial boundary ranks for every permitted block count at six pairs of shore sizes between four and six, and compares all homology groups to the theorem. This is a genuinely independent combinatorial calculation of the finite topology, not a certificate for all integers. Exact output from both current executions is included. The unrestricted proof is Steps 1–5, not numerical induction.

## Relationship to prior work

Filakovský introduced the robust-clique terminology and studied grid-like square-sequence graphs, proving fourth-threshold results under restrictive edge-gluing hypotheses. The present dense bicliques with missing vertex-disjoint edge squares are not such edge-glued square sequences and have a distinct deformation mechanism. Carnero Bravo's Proposition 37 determines bounded-independence complexes for **intact** complete multipartite graphs, including the formula \(R\) for \(m=0\), but does not calculate the deleted-square family or its integral inclusion maps. Kim and Lew studied collapsibility properties of the same bounded-independence construction rather than the present classification. These baseline results are credited, not claimed as new.

The distinct contributions are an all-width deletion formula, its exceptional four-dimensional sphere, a primitive integral relative-map splitting, and all inclusion-induced homology maps. Searches for the alternate terms bounded-independence complexes, complete-bipartite square-edge deletion, missing \(K_{2,2}\) blocks, Alexander-dual total cut complexes, and equivalent join-of-skeleta subcomplexes did not identify an implication-equivalent theorem. This does not establish absolute novelty.

## Limitations

The missing-edge four-cycles must be mutually vertex-disjoint. The theorem does not cover overlapping deleted bicliques, arbitrary degree-two missing-edge graphs, higher robust-clique thresholds, or equivariant homotopy. The examples are finite confirmation only. The classification has undergone a self-review, not an independent mathematical audit. Unindexed or differently phrased existing work may still overlap.

## References

1. M. Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first public 2026-02-11, https://arxiv.org/abs/2602.11365.
2. A. Carnero Bravo, *Total cut complexes and their duals*, arXiv:2602.21427, first public 2026-02-24; especially Proposition 37, https://arxiv.org/abs/2602.21427.
3. M. Kim and A. Lew, *Complexes of graphs with bounded independence number*, arXiv:1912.12605, first public 2019-12-29, https://arxiv.org/abs/1912.12605.
