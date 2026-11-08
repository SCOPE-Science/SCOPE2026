# Two-sphere homotopy after deleting a rung of a Möbius ladder

## Finding
Let \(n\ge5\) be congruent to \(1\) or \(2\) modulo \(4\). Let \(M_{2n}\) have vertices \(\mathbb Z/(2n)\) and edges between consecutive residues and between antipodal residues. Delete exactly the antipodal edge \(\{0,n\}\), obtaining \(R_n\). Then the ordinary (integral) homotopy type of its independence complex is
\[
\boxed{\operatorname{Ind}(R_n)\simeq S^{\lfloor(n-1)/2\rfloor}\vee S^{\lfloor(n-1)/2\rfloor}.}
\]
In particular, for \(n=4k+1\) or \(4k+2\), with \(k\ge1\), the sphere dimension is \(2k\). The theorem asserts no classification for the other two residue classes.

## Assumptions and scope
For a finite simple graph \(G\), \(\operatorname{Ind}(G)\) is the simplicial complex of independent vertex sets. For a vertex \(v\), \(N_G[v]\) is the closed neighborhood. The edge removed is a rung (an antipodal edge), *not* a cycle edge; the two edge types are different for the general Möbius ladder. Geometric homotopy equivalences, integral homology, and ordinary, not equivariant, homotopy types are asserted. A disjoint union of \(m\) edges has independence complex \(S^{m-1}\), since its complex is a join of \(m\) copies of \(S^0\).

## Proof
**1. Two standard homotopy operations.** For distinct vertices \(u,v\) of \(G\), if \(N_G(u)\subseteq N_G(v)\), then deleting \(v\) induces a homotopy equivalence of independence complexes (the fold lemma). The independence complex is the mapping cone of the natural inclusion
\[
\operatorname{Ind}(G-N_G[v])\longrightarrow\operatorname{Ind}(G-v).
\]
When the target is contractible, the result is the suspension of the source; when the inclusion is nullhomotopic, the result is the wedge of the target with the suspension of the source. In the lists below, \((u,v)\) means that \(v\) is deleted using \(u\) as witness, so the required check is \(N(u)\subseteq N(v)\) in the graph *at that stage*. All indices in the displayed sequences are taken from \(0\) to \(2n-1\), without modular reinterpretation beyond the original graph.

**2. Case \(n=4k+1\).** Put \(G=R_n\) and choose the vertex \(0\). Because the removed rung is incident to \(0\), the deletion \(G-0\) is exactly \(M_{2n}-0\). The vertex-deletion calculation of Agarwal and Basak (arXiv:2608.30601v1, Lemma 9) reduces its independence complex to that of the path on \(6k+1\) vertices, which is contractible by the classical path formula.

The link graph \(G-N_G[0]\) is obtained by deleting the three vertices \(\{2n-1,0,1\}\). Perform the following \(2k-1\) valid graph folds, in order. First delete \(n-3\) with witness \(2n-2\). Then, for \(j=0,1,\ldots,k-2\), delete \(n+4j+3\) with witness \(4j+2\), followed by deleting \(4j+5\) with witness \(n+4j+4\). The remaining graph is connected, has \(6k\) vertices, and every vertex has degree two; direct substitution in the cycle-and-antipode adjacency rule shows that it is \(C_{6k}\). Each stated fold satisfies the open-neighborhood inclusion by the same adjacency rule; all the index ranges are valid for \(k\ge1\). Consequently the link complex has homotopy type
\[
\operatorname{Ind}(C_{6k})\simeq S^{2k-1}\vee S^{2k-1},
\]
by the classical cycle formula. The mapping-cone description over the contractible deletion now gives \(\operatorname{Ind}(G)\simeq S^{2k}\vee S^{2k}\).

**3. Case \(n=4k+2\).** Choose vertex \(1\) in \(G=R_n\). Let \(D=G-1\) and \(L=G-N_G[1]\). We give completely explicit fold certificates for both graphs. All pairs below are ordered \((\text{witness},\text{removed vertex})\).

For \(D\), start with the two pairs
\[
(0,n-1),\qquad(n,n+2).
\]
For \(j=0,\ldots,k-2\), use the following four pairs in this exact order:
\[
(4j+2,4j+4),\quad(4j+2,n+4j+3),\quad
(n+4j+4,4j+5),\quad(n+4j+4,n+4j+6).
\]
Finish with
\[
(4k-2,4k),\quad(4k-2,n+4k-1),\quad(2n-2,0).
\]
The remaining graph has exactly the disjoint edges \(\{4j+2,4j+3\}\), for \(0\le j<n/2\), so it is \((n/2)K_2\).

For \(L\), note that the initially removed closed neighborhood is \(\{0,1,2,n+1\}\). First use
\[
(n+2,3),\qquad(n+2,n+4).
\]
For \(j=0,\ldots,k-2\), use
\[
(4j+4,4j+6),\quad(4j+4,n+4j+5),\quad
(n+4j+6,4j+7),\quad(n+4j+6,n+4j+8).
\]
Finish with
\[
(4k,4k+2),\qquad(4k,n+4k+1).
\]
The remaining graph consists exactly of the edges \(\{4j,4j+1\}\), for \(1\le j<n/2\), and is therefore \((n/2-1)K_2\).

Each pair in these lists satisfies the fold condition in the graph remaining at its occurrence. This is a uniform, elementary check: a vertex has only the neighbors at cyclic offsets \(\pm1\) and (unless it is \(0\) or \(n\)) the antipodal offset \(n\); evaluating those three possibilities after earlier deletions establishes every inclusion. The lists are valid for every \(k\ge1\), including the empty middle loops at \(k=1\). The included program directly reconstructs and checks every pair for arbitrary supplied parameters, and checks the final graph as well.

It follows that \(\operatorname{Ind}(D)\simeq S^{2k}\) and \(\operatorname{Ind}(L)\simeq S^{2k-1}\). The attaching map from the latter sphere to the former is nullhomotopic because \(\pi_{2k-1}(S^{2k})=0\). The vertex-deletion mapping cone therefore splits as \(S^{2k}\vee\Sigma S^{2k-1}\), completing the proof.

## Verification
The standalone `verify.py` rebuilds the graphs from their modular edge definitions, checks every neighborhood-inclusion step of the three closed-form fold sequences, checks the final disjoint-edge and cycle graphs, and independently computes simplicial homology over \(\mathbb F_2\) for small parameters. Invoke `python verify.py` with a standard Python interpreter; the observed run and its exact counts appear in `verification_output.txt`. The finite homology tests corroborate but do not replace the uniform fold proof and cited path/cycle homotopy theorems. The proof establishes the full integral homotopy type without torsion assumptions.

## Relationship to prior work
Agarwal and Basak, arXiv:2608.30601 (first public version 2026-08-31), classify the independence complexes of the *unmodified* Möbius ladders and provide the vertex-deletion lemma used above. Their result does not give the homotopy type after removing an antipodal edge. A published computation of dihedral rational homology representations of the unmodified complexes similarly retains every rung and does not imply this one-edge perturbation theorem. The published computation of the matching complex of the Wagner graph uses edges as vertices of its simplicial complex, whereas this theorem uses independent sets of graph vertices; its edge-orbit result does not imply the present classification. The new proof explicitly tracks the modified link and its fold certificates.

## Limitations
Only the two congruence classes \(n\equiv1,2\pmod4\) are proved; the other two classes, removal of cycle edges, integral equivariant structures, and more general missing-rung sets are not classified here. Literature and record searches cannot exclude an unindexed equivalent theorem. Independent mathematical audit has not been performed.

## References
1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v1 (2026-08-31), especially Lemma 9 and Theorem 12; revised v2 posted 2026-09-14.
2. D. Kozlov, *Complexes of directed trees*, Journal of Combinatorial Theory, Series A **88** (1999), 112–122, for independence complexes of paths and cycles.
3. *Dihedral rational homology representations of Möbius-ladder independence complexes*, published-finding corpus mathematical record, 2026-10-11, publicly accessible at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-dihedral-rational-homology-representations-of-m-bius-ladder-inde--baaa00f0cf91.
4. *The Wagner graph matching complex and its two edge-orbit splittings*, published-finding corpus mathematical record, 2026-10-11, publicly accessible at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-wagner-graph-matching-complex-and-its-two-edge-orbit-splitti--1b0ec7f839cb.
