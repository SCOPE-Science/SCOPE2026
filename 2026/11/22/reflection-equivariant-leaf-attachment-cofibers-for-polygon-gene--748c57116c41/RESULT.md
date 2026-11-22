# Reflection-equivariant leaf-attachment cofibers for polygon general-position complexes

## Finding

**Theorem.** For every integer \(n\ge3\), take the ordinary unweighted cycle \(C_n\) with vertices \(0,1,\ldots,n-1\), attach one new leaf \(x\) at vertex \(0\), and call the resulting tadpole graph \(T_n\). For a graph \(H\), let \(\operatorname{GP}(H)\) be the abstract simplicial complex of vertex subsets with no three distinct vertices on one graph geodesic (equivalently, no distinct \(u,v,w\) in the subset with \(d(u,w)=d(u,v)+d(v,w)\)). Put \(A_n=|\operatorname{GP}(C_n)|\), \(X_n=|\operatorname{GP}(T_n)|\), and let \(\rho\) reflect the cycle by \(i\mapsto -i\pmod n\), fixing \(x\).

Set \(h=\lfloor(n-1)/2\rfloor\) and \(p=1\) for odd \(n\), \(p=2\) for even \(n\). The canonical inclusion \(A_n\hookrightarrow X_n\) has homotopy cofiber
\[
X_n/A_n\simeq \bigvee^{p} S^1\ \vee\ \bigvee^{(h-1)^2} S^2.
\]
Its entire positive-degree **integral relative homology representation** under \(\rho\) is
\[
H_1(X_n,A_n;\mathbb Z)\cong\mathbb Z^p\ \text{(trivial reflection)},\qquad
H_2(X_n,A_n;\mathbb Z)\cong U_h\otimes_{\mathbb Z}U_h,
\]
with all other relative homology zero. Here \(U_h=\ker(\mathbb Z^h\xrightarrow{\sum}\mathbb Z)\), and the involution on the second module is **minus the tensor-factor swap**: \(\rho(a\otimes b)=-b\otimes a\).

More strongly, the **genuine geometric reflection quotient of the cofiber** satisfies
\[
(X_n/A_n)/\langle\rho\rangle\simeq
\bigvee^{p}S^1\ \vee\ \bigvee^{\binom{h-1}{2}}S^2.
\]
Writing \(L=H_2(X_n,A_n;\mathbb Z)\) and \(L^{\pm}=\{v\in L:\rho(v)=\pm v\}\), the integral eigensublattices have ranks \(\binom{h-1}{2}\) and \(\binom{h}{2}\), respectively, but
\[
[\,L:L^+\oplus L^-\,]=2^{\binom{h-1}{2}}.
\]
Thus the integral reflection representation first fails to split into its rational eigenspaces at \(n=7\), and its gluing index grows with the polygon order.

## Assumptions and scope

All graphs are simple, finite, connected and unweighted. Geodesic collinearity includes **any** shortest path, including both possible routes to the antipode in an even cycle. The simplicial complex uses all general-position sets, including the empty face. The cofiber is a quotient of the **simplicial complex inclusion**, not the graph-theoretic quotient, and it is not asserted to classify the homotopy type of \(X_n\) itself. The reflection fixes the attachment vertex and the new leaf. For \(h=1\), the augmentation module is zero, and empty sphere wedges are understood as absent.

## Proof

**1. Leaf link and parity.** The original cycle is an isometric induced subgraph of \(T_n\), since entering and exiting a pendant edge cannot shorten a route between rim vertices. Consequently \(A_n\) is exactly the deletion of the leaf vertex \(x\) from \(\operatorname{GP}(T_n)\). For \(a,b\in\{1,\ldots,h\}\), write \(L_a=a\) and \(R_b=n-b\). Every nonzero rim vertex except the even-order antipode \(n/2\) lies in precisely one of these two arms.

For two distinct rim vertices on the same arm, the nearer one lies on a shortest path from \(x\) to the farther one, hence the triple containing \(x\) is forbidden. Any triple containing \(x,0\) and another rim vertex is forbidden. For even \(n\), the triple containing \(x,n/2\) and any other rim vertex is likewise forbidden, because one of the two shortest paths from \(0\) to its antipode passes through that vertex. Conversely, for \(L_a\) and \(R_b\), the unique shortest paths from \(0\) to these nonantipodal vertices go in opposite directions; neither lies on a geodesic from \(x\) to the other, and \(x\), being a leaf, cannot be internal to a rim-to-rim geodesic. Thus \(\{x,L_a,R_b\}\) is in general position. No three rim vertices can occur with \(x\), because the complete bipartite link has no triangles. It follows, exactly as an abstract complex, that
\[
\operatorname{link}_{\operatorname{GP}(T_n)}(x)
=K_{h,h}\ \sqcup\ pK_1,
\]
where the notation on the right denotes the **one-dimensional simplicial graph** of the complete bipartite graph, plus isolated vertices \(0\) and (if present) \(n/2\). Reflection interchanges the two bipartition shores by \(L_a\leftrightarrow R_a\), fixing the isolated vertices.

**2. Cofiber and relative homology.** Every simplicial complex decomposes into the deletion of a vertex together with the cone from that vertex over its link, meeting in the link. Since a simplicial inclusion is a cofibration,
\[
X_n/A_n\cong \operatorname{Cone}(K_{h,h}\sqcup pK_1)/(K_{h,h}\sqcup pK_1)
=\Sigma(K_{h,h}\sqcup pK_1).
\]
The bipartite graph is connected, with \(2h\) vertices and \(h^2\) edges, hence has integral cycle rank \(h^2-2h+1=(h-1)^2\). Suspension of a graph with \(p+1\) components is a wedge of \(p\) circles and one two-sphere per independent graph cycle. This establishes the first homotopy equivalence and, by the suspension isomorphism, every relative homology group including integrality and vanishing.

**3. The integral reflection action.** Orient each bipartite edge from \(L_a\) to \(R_b\). Its first graph cycle group consists of the integer \(h\)-by-\(h\) arrays having all row sums and all column sums equal to zero. This lattice is canonically \(U_h\otimes U_h\). Under reflection the edge \(L_aR_b\) maps to \(R_aL_b\), which is the reversed orientation of \(L_bR_a\); the action is therefore minus matrix transposition. The connected bipartite component and every isolated component are individually reflection-fixed, so \(\widetilde H_0\) of the link, and hence relative \(H_1\), is pointwise fixed.

**4. Geometric quotient.** Reflection respects the cone coordinate, so \((\Sigma K)/\langle\rho\rangle\cong\Sigma(K/\langle\rho\rangle)\) for the link \(K\) above. The quotient of \(K_{h,h}\) has one vertex for each orbit \(\{L_a,R_a\}\). For distinct indices \(a,b\), the two edges \(L_aR_b\) and \(L_bR_a\) form one ordinary edge orbit between these vertices. Each diagonal edge \(L_aR_a\) is reversed by reflection; its geometric quotient is a pendant interval terminating at the edge midpoint, **not a loop**. Thus the quotient graph consists of \(K_h\) and \(h\) contractible pendant intervals. Its cycle rank is \(\binom{h}{2}-h+1=\binom{h-1}{2}\). The isolated vertices remain separate. Suspending proves the second homotopy equivalence over the integers.

**5. Integral splitting obstruction.** Set \(k=h-1\) and choose any basis \(e_1,\ldots,e_k\) of \(U_h\). Under minus transposition, each diagonal tensor \(e_i\otimes e_i\) is a negative eigenvector. For each \(i<j\), the rank-two lattice spanned by \(e_i\otimes e_j\) and \(e_j\otimes e_i\) has positive and negative eigenvectors given by their difference and sum, with change-of-basis determinant of absolute value two. These rank-two blocks are independent. Multiplying their indices gives \(2^{\binom{k}{2}}\), while counting the blocks and diagonals gives the stated positive and negative ranks. The index is larger than one precisely for \(k\ge2\), or \(h\ge3\); the first polygon order is \(n=7\).

## Verification

The accompanying standalone Python checker reconstructs graph distances and all leaf-containing admissible triples directly for every \(3\le n\le80\), confirming the exact bipartite-plus-isolates link. It also independently checks relative boundary ranks for \(3\le n\le23\), the minus-transpose integral involution through rank ten, and the quotient graph cycle-rank formula. Run `python3 check.py` from the directory containing the packaged file. These finite checks support the all-order proof but are not substitutes for it. The proof requires no numerical inference.

## Relationship to prior work

Iršič, Klavžar, Rus and Tuite (2024) count general-position sets of cycles and other graphs, including exact cubic coefficients. Rather (first public 6 March 2026) develops general-position polynomials and corona operations, motivating the effect of pendant attachments. Neither cited counting result gives the topology of the leaf-attachment homotopy cofiber, the reflection-equivariant integral relative lattice, or the geometric quotient of that cofiber. Known calculations of absolute graph-geodesic general-position homotopy types for other graph families are not asserted to be new here. Standard cone/link and bipartite cycle-space facts are used openly; the contribution is their combined explicit parity-sensitive and integral equivariant classification for the cycle-to-tadpole inclusion.

## Limitations

The result determines the **homotopy cofiber and relative homology**, not the map from the link into the deletion; thus it does not determine the absolute homotopy type of the leafed-cycle complex or its full reflection quotient. The statement does not cover a pendant path longer than one edge or multiple leaves. The involution eigensublattices concern the relative second-homology lattice, and no claim of independent priority verification or independent mathematical audit is made.

## References

1. V. Iršič, S. Klavžar, G. Rus, J. Tuite, “General Position Polynomials,” *Results in Mathematics* **79**, article 110 (2024), https://doi.org/10.1007/s00025-024-02133-3 . First preprint: https://arxiv.org/abs/2401.05696 .
2. B. A. Rather, “Explicit Formulas and Unimodality Phenomena for General Position Polynomials,” arXiv:2603.06930 (first public 6 March 2026), https://arxiv.org/html/2603.06930v3 .
