# Primitive one-edge persistence for induced-forest complexes of cocktail-party graphs

## Finding
For every integer \(m\ge2\), consider the cocktail-party graph \(G_m=K_{2,\ldots,2}\) on \(2m\) vertices, with independent parts \(P_i=\{a_i,b_i\}\). Remove one cross-edge \(a_1a_2\) to obtain \(G'_m\). The graph-edge deletion induces the simplicial inclusion
\[
j_m:K_m=\mathcal F_\infty(G_m)\longrightarrow L_m=\mathcal F_\infty(G'_m),
\]
where a face of \(\mathcal F_\infty(G)\) is a vertex set inducing an acyclic graph.

The complete integral persistence profile of this one-edge inclusion is:
\[
\begin{aligned}
\widetilde H_1(K_m;\mathbb Z)&\cong\mathbb Z^{\binom{m-1}{2}},&
\widetilde H_1(L_m;\mathbb Z)&\cong\mathbb Z^{\binom{m-2}{2}},\\
\ker(j_{m*}|_{\widetilde H_1})&\cong\mathbb Z^{m-2},&
\operatorname{coker}(j_{m*}|_{\widetilde H_1})&=0,\\
\widetilde H_2(K_m;\mathbb Z)&\cong\mathbb Z^{\binom m2},&
\widetilde H_2(L_m;\mathbb Z)&\cong\mathbb Z^{\binom m2+m-3},\\
\ker(j_{m*}|_{\widetilde H_2})&\cong\mathbb Z,&
\operatorname{coker}(j_{m*}|_{\widetilde H_2})&\cong\mathbb Z^{m-2}.
\end{aligned}
\]
Every kernel and image is primitive (the appropriate quotients are torsion-free), and all other reduced homology groups vanish. A basis of the first kernel consists of the loops \(\gamma_k=[a_1a_2]+[a_2a_k]-[a_1a_k]\) for \(3\le k\le m\), oriented by increasing labels. The degree-two kernel is the fundamental class of the tetrahedral boundary on \(\{a_1,b_1,a_2,b_2\}\). The degree-two cokernel has integral representatives given by the tetrahedral boundaries on \(\{a_1,a_2,a_k,b_k\}\), for \(3\le k\le m\). (The notation \([uv]\) denotes an oriented edge and the orientation of a loop may be reversed.)

For context, the absolute homotopy types are
\[
K_m\simeq\bigvee^{\binom{m-1}{2}}S^1\vee\bigvee^{\binom m2}S^2,
\qquad
L_m\simeq\bigvee^{\binom{m-2}{2}}S^1\vee\bigvee^{\binom m2+m-3}S^2.
\]
These absolute wedge counts are consistent with, and derivable from, established graph-join decompositions; the assertion here is the actual *natural integral map* under edge deletion.

## Assumptions and scope
All graphs are finite, simple, and undirected; all complexes contain the empty face and use the usual realization. The parameter is any integer \(m\ge2\). Binomial coefficients \(\binom{r}{2}\) are zero for \(r=0,1\). The exceptional smallest case \(m=2\) has contractible target. The claim concerns one deleted cross-edge between distinct two-vertex parts, and not arbitrary edge-fault sets. All homology is integral unless explicitly stated otherwise.

## Proof
**1. Complete face classification.** Denote by \(S_{ij}\) the four-triangle boundary of the tetrahedron with vertices \(P_i\cup P_j\). Every subset of at most two vertices is a forest. A three-set is a forest in \(G_m\) exactly when it contains a complete matched pair \(P_i\): three vertices from distinct parts form a triangle. Four vertices from only two parts induce a four-cycle, and every other four-set contains a triangle; larger sets contain forbidden triples or four-sets. Consequently
\[
K_m=T\cup\bigcup_{1\le i<j\le m} S_{ij},
\]
where \(T\) consists of all matched edges \(a_ib_i\) and one representative cross-edge \(a_ia_j\) for each \(i<j\); its realization is the complete graph \(K_m\) with one pendant edge at each vertex.

For distinct \(i,j\), the intersection \(S_{ij}\cap T\) is exactly the tree with three edges \(b_i-a_i-a_j-b_j\). For two different \(S_{ij}\), their intersection is either empty or a matched edge, hence lies in \(T\). Thus adjoining each sphere boundary along its contractible intersection with \(T\) gives the homotopy equivalence
\[
K_m\simeq T\vee\bigvee^{\binom m2}S^2,
\]
with each \(S_{ij}\) furnishing a primitive integral two-dimensional class. Moreover \(H_1(T;\mathbb Z)\cong\mathbb Z^{\binom{m-1}{2}}\).

Deleting precisely \(a_1a_2\) allows exactly these new faces: the full tetrahedron \(B=\Delta(P_1\cup P_2)\), and the \(2m-4\) triangles \(\{a_1,a_2,x\}\) for \(x\in P_k\), \(3\le k\le m\). No additional faces occur: every other four-subset either contains an undeleted triangle or, on two whole matched pairs, a four-cycle, and the only exception is \(P_1\cup P_2\). The tetrahedron \(B\) fills \(S_{12}\) and meets \(T\) in the same three-edge tree \(b_1-a_1-a_2-b_2\). Therefore, before attaching the new triangles, the enlarged complex has the homotopy type
\[
T\vee\bigvee_{(i,j)\ne(1,2)} S^2.
\]
The inclusion of the original complex kills precisely the old class \([S_{12}]\) in degree two, and preserves the other old two-sphere factors primitively.

**2. The integral attaching maps.** For each \(k\ge3\), first attach \(A_k=\Delta(a_1,a_2,a_k)\). Its boundary lies literally in \(T\) and is the graph cycle \(\gamma_k\). Choose the spanning tree of \(T\) consisting of all edges \(a_1a_j\) and all matched edges \(a_jb_j\). The non-tree edge \(a_2a_k\) appears with coefficient \(\pm1\) in \(\gamma_k\), and in none of the other \(\gamma_l\). Hence \(\{\gamma_k:3\le k\le m\}\) extends to an integral cycle basis of \(T\), and the attaching homomorphism has a unit diagonal block of size \(m-2\). Attaching these disks kills exactly that primitive subgroup of \(H_1(T)\), and one may collapse the corresponding triangle–edge pairs to see the remaining graph as \(K_{m-1}\) on representatives \(a_1,a_3,\ldots,a_m\) (with contractible pendant edges).

Now attach the other triangle \(B_k=\Delta(a_1,a_2,b_k)\) for each \(k\ge3\). The boundary cycles of \(A_k\) and \(B_k\) are homotopic inside the already existing union: their difference is the signed boundary of the two old triangles \(\Delta(a_1,a_k,b_k)\) and \(\Delta(a_2,a_k,b_k)\). Since \(A_k\) was already attached, the boundary of \(B_k\) is null-homotopic. The disk \(B_k\) therefore contributes an additional two-sphere, with explicit fundamental cycle the boundary of the unfilled tetrahedron \(\{a_1,a_2,a_k,b_k\}\). These spheres are mutually independent, and are independent of all remaining old \(S_{ij}\).

It follows that \(L_m\) is the wedge of \(\binom{m-2}{2}\) circles, \(\binom m2-1\) old spheres, and \(m-2\) new two-spheres, yielding the stated absolute type and integral maps. The natural map in degree one is the quotient by the primitive direct summand generated by the \(\gamma_k\); in degree two its kernel is \(\mathbb Z[S_{12}]\), while the new tetrahedral boundaries provide a free rank-\(m-2\) complement of its image. This proves all homology and primitivity assertions, including \(m=2\), where there are no \(\gamma_k\) or new two-spheres.

**3. Relative connecting maps.** As a further check, the simplicial quotient \(L_m/K_m\) has one three-cell (the filled old tetrahedron) and \(2m-4\) two-cells with all boundaries collapsed; hence it is homeomorphic as a CW quotient to \(S^3\vee\bigvee^{2m-4}S^2\). The long exact sequence sends the degree-three relative generator to \([S_{12}]\) with coefficient \(\pm1\), and the two relative degree-two generators in each pair \(\{A_k,B_k\}\) to the same integral graph loop \(\gamma_k\) up to consistent orientations. Thus the degree-two connecting matrix has \(m-2\) unit invariant factors, independently recovering the stated split kernel and cokernel ranks.

## Verification
The supplied standalone program `verify.py` reconstructs graph edges and *all* forest vertex sets without relying on the face formulas. For each \(m\in\{2,3,4,5,6\}\), it checks both exact predicted face sets, the single added three-cell and \(2m-4\) new two-faces, integral simplicial boundary identities for the primitive old and new tetrahedral cycles, and reduced homology ranks over \(\mathbb F_2,\mathbb F_3,\mathbb F_5\). Its recorded `verification_output.txt` is produced by executing that exact packaged program. These finite checks corroborate; the preceding combinatorial homotopy argument proves all integers \(m\ge2\).

## Relationship to prior work
Carnero Bravo's *The Forest Filtration of a Graph*, first posted 2023-07-25, gives the forest filtration and Corollaries 34–35 (graph-join and complete-multipartite wedge decompositions). Those statements, together with a finite two-factor calculation, also yield the **abstract** sphere-wedge counts here. We do not claim those absolute counts as a new result. They do not determine the maps induced by the *actual edge deletion* between the two different complexes. The new result calculates primitive integral kernels, images, cokernels and explicit cycle generators for that inclusion. Results about deleting an edge in a complete bipartite graph apply to the corner \(m=2\), but not the nonbipartite graphs \(m\ge3\). Clique-avoidance complexes of multipartite graphs are different: four vertices in two untouched matched parts form a four-cycle and therefore fail the induced-forest condition, although they are triangle-free.

## Limitations
The inclusion classification applies only to one deleted cross-edge from cocktail-party graphs, not to general multipartite parts or multiple faults. The nonequivariant homotopy types alone are implied by earlier graph-join theory; the map-level refinement is the scope of originality. Targeted literature and public mathematical-record searches cannot exclude every unindexed or inaccessible equivalent edge-relative theorem. No independent external audit has been performed.

## References
1. Andrés Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271 (first public 2023-07-25), especially Corollaries 34–35. https://arxiv.org/abs/2307.13271
2. A. Hatcher, *Algebraic Topology*, Sections 0 and 2, CW attachments and long exact sequences of pairs. https://pi.math.cornell.edu/~hatcher/AT/AT.pdf
