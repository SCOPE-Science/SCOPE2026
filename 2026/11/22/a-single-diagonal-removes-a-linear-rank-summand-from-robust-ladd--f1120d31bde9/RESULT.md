# A single diagonal removes a linear-rank summand from robust ladder homotopy

## Finding
For integers \(n\ge 3\) and \(0\le i\le n-2\), let \(L_n=P_n\square K_2\), with upper vertices \(u_0,\ldots,u_{n-1}\) and lower vertices \(v_0,\ldots,v_{n-1}\), and let \(D_{n,i}\) be obtained by adding exactly one diagonal edge \(u_iv_{i+1}\). Write \(\operatorname{RC}_3(G)\) for the simplicial complex of vertex subsets \(S\) satisfying \(\alpha(G[S])\le 2\). Then
\[
\operatorname{RC}_3(D_{n,i})\simeq\bigvee^{\binom{n-2}{2}}S^3,
\]
with a zero-fold wedge interpreted as a point. The inclusion from the unmodified ladder induces a split surjection on integral third homology whose kernel is the rank-\(n-2\) primitive direct summand spanned by square-pair cycles \(c_i\wedge c_j\) for \(j\ne i\).

## Assumptions and scope
Graphs are finite and simple. \(L_n\) has rail edges \(u_ju_{j+1}\), \(v_jv_{j+1}\) and rung edges \(u_jv_j\). The new edge \(u_iv_{i+1}\) creates precisely two graph triangles in the \(i\)-th unit square. For the standard oriented square one-cycles \(c_j\), the notation \(c_j\wedge c_k\) is the oriented simplicial join product, an integral three-cycle in the robust complex; indices refer to distinct unit squares. This is a homotopy statement over the integers, not merely an equality of Betti numbers.

## Proof
Let \(K=\operatorname{RC}_3(L_n)\) and \(K'=\operatorname{RC}_3(D_{n,i})\). The integral square-pair cycle-basis theorem in the references gives
\[
K\simeq\bigvee^{\binom{n-1}{2}}S^3,\qquad
\widetilde H_3(K;\mathbb Z)=\bigoplus_{0\le j<k\le n-2}\mathbb Z[c_j\wedge c_k].
\]
The basis is primitive over \(\mathbb Z\).

We calculate the relative face poset \(K'\setminus K\), where only a change in independence of the newly adjacent endpoints \(a=u_i\) and \(b=v_{i+1}\) is possible. Consequently every relative face contains \(a,b\), has exactly three, four or five vertices, and can be characterized by checking the independent triples after removing the diagonal.

Here is an all-length acyclic relative matching, with full local face lists that make the construction independently checkable. Write \(p=u_{i+1}\), \(q=v_i\). Start with the two columns at indices \(i,i+1\), where the relative face set is empty. Add columns one by one outward, first toward the right and then toward the left (the left cases follow by reversing column order and exchanging the upper and lower labels). At the first rightward new column \(X=u_{i+2}\), \(Y=v_{i+2}\), the seven new relative faces are
\[
abX;\quad abqX,abpX,abXY;\quad abpqX,abqXY,abpXY.
\]
Match the pairs \((abX,abpX)\), \((abqX,abpqX)\), and \((abXY,abpXY)\); the unique critical face is \(abqXY\), of dimension four. Each subsequent outward addition has a previous terminal rung \(R,S\) and a new rung \(X,Y\), with exactly fifteen new relative faces:
\[
\begin{gathered}
abX,abY;\\
abqX,abqY,abpX,abpY,abRX,abSY,abXY;\\
abqRX,abqSY,abqXY,abpRX,abpSY,abpXY.
\end{gathered}
\]
Pair by toggling \(p\) in \((abX,abpX)\), \((abY,abpY)\), \((abRX,abpRX)\), \((abSY,abpSY)\), \((abXY,abpXY)\), then toggle \(R\) in \((abqX,abqRX)\) and \(S\) in \((abqY,abqSY)\). Exactly \(abqXY\) survives, again in dimension four. The stated local lists result directly by checking whether each triple of a candidate face is independent: a relative face must contain \(a,b\), include a vertex nonadjacent to both of them in the old graph, but have no independent triple in the new graph. No more remote old vertices can occur. Within an addition stage, the pairs are acyclic by successive fixed-vertex toggling; the filtration by the furthest outward column is order preserving, so the patchwork lemma gives a global acyclic matching. There are exactly \(i+(n-i-2)=n-2\) critical relative four-faces and no other relative critical cells. Thus \(H_4(K',K;\mathbb Z)\cong\mathbb Z^{n-2}\), while the remaining relative homology groups vanish. This also gives a relative CW model of \(K'\) obtained from \(K\) by attaching \(n-2\) four-cells.

Let \(t_i=[a,p,b]+[a,b,q]\), with orientations chosen so \(\partial t_i=c_i\). These are the two new graph triangles. For each \(j\ne i\), the integral join chain \(w_j=t_i\wedge c_j\) lies in \(C_4(K')\): a graph triangle has independence number one and an edge has independence number one, so any five-vertex union has independence number at most two. Its boundary is \(\partial w_j=c_i\wedge c_j\), with the conventional oriented sign. It therefore defines a relative four-class whose connecting image is \([c_i\wedge c_j]\). Those \(n-2\) images are distinct members of the known integral basis of \(H_3(K;\mathbb Z)\). Since the domain \(H_4(K',K;\mathbb Z)\) has rank \(n-2\), the classes \([w_j]\) exhaust a free integral basis, and the connecting map identifies that group with the primitive direct summand spanned by the \(c_i\wedge c_j\). The long exact sequence now yields
\[
H_4(K';\mathbb Z)=0,\qquad H_3(K';\mathbb Z)\cong\mathbb Z^{\binom{n-2}{2}},
\]
and all lower reduced groups vanish.

Finally, the relative CW model attaches four-cells to the wedge of three-spheres \(K\). By the integral Hurewicz theorem, \(\pi_3(K)\to H_3(K;\mathbb Z)\) is an isomorphism. The attaching classes form a primitive subset of a basis, so a change of wedge generators and elementary cell cancellations kill exactly \(n-2\) of the three-spheres and leave the asserted wedge. This argument also proves the stated split surjection and its kernel.

## Verification
The accompanying `verify.py` reconstructs every relative face by testing every independent triple, constructs a global sequential toggle matching, and verifies the predicted \(n-2\) unmatched four-faces for every diagonal position and \(3\le n\le 12\). Its output is in `expected_output.txt`. Direct finite integral homotopy is obtained from the proof, not inferred from this bounded experiment. The relative matching construction and square-pair boundary calculations above apply to all parameters in the stated scope.

## Relationship to prior work
The February 2026 paper introducing robust clique complexes supplies the original ladder motivation. The existing all-bipartite homotopy theorem gives the unmodified ladder; the published primitive integral square-pair basis identifies the exact summand removed. Neither applies to the new graph, which contains two triangles. A triangle-chorded single-cycle stability theorem concerns a different graph family and does not imply the result. Originality remains subject to priority risk from unindexed or inaccessible publications.

## Limitations
Only one diagonal in a rectangular two-row ladder, with the three-robust threshold, is treated. No assertion is made about multiple diagonals, arbitrary widths, other thresholds, or equivariant lifts. The proof relies on the cited integral square-pair basis for unmodified ladders. A separate independent mathematical audit has not been performed.

## References
1. Marek Filakovský, *The topology of robust clique complexes in grid-like graphs*, first posted 2026-02-11. https://arxiv.org/abs/2602.11365
2. *A three-sphere wedge theorem for robust clique complexes of all connected bipartite graphs*, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-three-sphere-wedge-theorem-for-robust-clique-complexes-of-all--8d06720b1a2b
3. *Primitive square-pair cycle basis for three-robust clique homology of rectangular grids*, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-primitive-square-pair-cycle-basis-for-three-robust-clique-homolo--c8dc5451add0
4. *A sharp simple-homotopy stability threshold for triangle-chorded cycles*, 2026-10-11. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-simple-homotopy-stability-threshold-for-triangle-chorded--e00e94e8e078
