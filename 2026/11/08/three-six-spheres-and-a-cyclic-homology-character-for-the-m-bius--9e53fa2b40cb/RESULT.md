# Three six-spheres and a cyclic homology character for the Möbius–Kantor two-independence complex

## Finding
For the sixteen-vertex Möbius–Kantor graph \(M=\operatorname{GP}(8,3)\), its two-independence complex has the **integral homotopy type**
\[
\operatorname{Ind}_2(M)\simeq S^6\vee S^6\vee S^6.
\]
Moreover, let \(r\) rotate both vertex octagons by one step. The character of its induced action on rational sixth homology satisfies
\[
\bigl(\operatorname{tr}(r^k\mid \widetilde H_6(\operatorname{Ind}_2(M);\mathbb Q))\bigr)_{k=0}^{7}
=(3,-1,-1,-1,3,-1,-1,-1).
\]
Thus this rational cyclic representation decomposes as \(\varepsilon\oplus V_4\), where \(\varepsilon(r)=-1\) is the one-dimensional sign character of \(C_8\), and \(V_4\) is the two-dimensional rational representation of \(C_8\) with minimal polynomial \(t^2+1\) for \(r\). In particular its space of cyclically invariant vectors is zero.

## Assumptions and scope
Write the vertices \(u_0,\ldots,u_7,v_0,\ldots,v_7\), indexed modulo eight, and take precisely these twenty-four undirected edges:
\[
\{u_i,u_{i+1}\},\qquad\{u_i,v_i\},\qquad\{v_i,v_{i+3}\}\quad (i\in\mathbb Z/8\mathbb Z).
\]
All sixteen vertices are distinct and every vertex has degree three. Define \(\operatorname{Ind}_2(M)\) as the abstract simplicial complex of subsets \(S\) for which every connected component of the induced subgraph \(M[S]\) has at most two vertices. Equivalently, each vertex of \(M[S]\) has induced degree at most one. This is the **higher two-independence complex**, also known as the complex of dissociation sets; it is not the ordinary independence, matching, clique, or graph-metric Vietoris–Rips complex.

A \(j\)-simplex is a subset of exactly \(j+1\) vertices, with the empty face understood as a formal face of dimension minus one. We orient an ordered vertex subset in increasing numerical order after assigning \(u_i=i\) and \(v_i=8+i\). The cyclic symmetry is \(r(u_i)=u_{i+1}\), \(r(v_i)=v_{i+1}\).

## Proof
**Two independent exhaustive face tests.** A brute force check of all \(2^{16}\) subsets keeps precisely those inducing degree at most one. A second procedure grows all faces one vertex at a time, checking connected-component sizes by breadth-first search. Both yield the same \(6813\) faces, including the empty face, with counts by dimensions \(-1,0,1,2,3,4,5,6,7\):
\[
(1,16,120,512,1324,2064,1840,816,120).
\]
Its maximal faces consist of exactly \(96\) six-simplices and \(120\) seven-simplices, so the complex is nonpure.

**Exact acyclic matching.** For a reproducible bit-mask encoding \(m(S)=\sum_{u_i\in S}2^i+\sum_{v_i\in S}2^{8+i}\), process the vertices in the fixed order
\[
(4,0,6,11,2,9,14,8,12,13,3,15,7,10,1,5).
\]
At a stage for vertex \(j\), pair every *currently unmatched* face \(m\) not containing \(j\) with \(m+2^j\), if the latter is also a currently unmatched face, visiting candidate lower masks in increasing numerical order. Include the empty face at this stage. Exactly \(3405\) pairs arise; the first critical pair is \((0,16)\), consisting of the empty face and vertex \(u_4\). After removing that augmented pair, the ordinary simplicial matching has \(3404\) pairs and four critical cells: the vertex \(u_4\) and precisely three six-simplices with masks \(29834\), \(50474\), and \(57514\).

To verify acyclicity, orient every covering incidence between nonempty faces from upper simplex to lower simplex, except reverse the matched incidences. There are exactly \(35104\) such incidences. The standalone verifier constructs all of them and finds a topological ordering containing all \(6812\) nonempty faces. Thus this directed graph is acyclic; the augmented graph likewise sorts all \(6813\) faces over \(35120\) incidences. These are exhaustive finite checks, not a random search. By the discrete-Morse CW theorem, the complex is homotopy equivalent to a CW complex having one zero-cell, exactly three six-cells and no positive-dimensional cells of other dimensions. Every six-cell attaches to that single point because the five-skeleton is a point. It follows *integrally and at the homotopy level*, without reliance on field-homology ranks, that
\[
\operatorname{Ind}_2(M)\simeq \bigvee^3S^6.
\]

**Cyclic symmetry character.** The simultaneous rotation \(r\) is verified to preserve every graph edge and hence the entire simplicial complex. For each \(k=0,\ldots,7\), the exact signed trace of \(r^k\) on oriented simplicial \(j\)-chains is the sum of permutation parities over all setwise fixed \(j\)-simplices. The verifier enumerates all such fixed faces, computes their parity from vertex permutations, and forms the reduced alternating Lefschetz trace (subtracting the ordinary connected \(H_0\) contribution). Since the just-proved homotopy type has reduced homology only in even degree six, the resulting eight traces are precisely the degree-six character
\[
(3,-1,-1,-1,3,-1,-1,-1).
\]
The order-eight rational irreducible characters \(\varepsilon=(1,-1,1,-1,1,-1,1,-1)\) and \(\chi_{V_4}=(2,0,-2,0,2,0,-2,0)\) add to this trace, proving the stated rational-module decomposition by semisimplicity over \(\mathbb Q\). Character averaging gives invariant dimension \(\frac18\sum_{k=0}^7\chi(r^k)=0\).

## Verification
With Python 3.9 or later, run `python3 verify.py` in the same directory as this document. The program uses the standard library only and is fully self-contained. It reconstructs the labeled graph, validates the 24 undirected edges and three-regularity, performs both exhaustive face-enumeration algorithms, creates the fixed-order matching, topologically sorts all directed Hasse incidences, and independently checks the mod-two simplicial boundary ranks and Betti numbers. It then checks every rotation as a graph automorphism, evaluates signed fixed-face traces, verifies the rational character decomposition and the vanishing invariant dimension. The exact expected transcript is `verification_output.txt`, ending `ALL_CHECKS_PASS`.

The unreduced mod-two Betti numbers by dimensions zero through seven are \((1,0,0,0,0,0,3,0)\); these are an independent consistency check, not a substitute for the discrete-Morse homotopy proof.

## Relationship to prior work
Deshpande and Singh [2] introduce higher independence complexes with the same connected-component definition and determine homotopy types for complete multipartite graphs, fully whiskered graphs, cycles and perfect rooted trees. Their general method and listed classifications do not include this nonchordal generalized Petersen graph. Deshpande, Shukla and Singh [3] give further connectivity criteria and a wedge result for chordal graphs, but the Möbius–Kantor graph has induced cycles and is not chordal.

The previously determined ordinary independence complex of this graph has homotopy type \(\bigvee^4S^3\vee S^4\); this is the **one-independence** complex, which is a strict subcomplex of the two-independence complex considered here [4]. Another published calculation concerns the same graph's ordinary matching complex [5], whose vertices are graph edges, not the vertices used here. An existing computation of \(\operatorname{Ind}_2\) of the Petersen graph [6] studies a different ten-vertex generalized Petersen graph and has no implication determining this sixteen-vertex case. Previously published cyclic-homology calculations for the ordinary independence complex also do not determine the present higher-independence character [7]. The result is not claimed as a consequence of any of those calculations.

## Limitations
This exact result is confined to the specified \(\operatorname{GP}(8,3)\) graph and the first higher-independence parameter. It neither classifies higher parameters or generalized Petersen families nor supplies an equivariant wedge decomposition; the cyclic representation is determined over \(\mathbb Q\), not as a fully classified integral module. The exhaustive calculation is small enough to be reproduced but is not an infinite family proof. Searches and direct comparisons with indexed prior findings and accessible primary texts found no stronger covering statement; equivalent unindexed work and inaccessible portions of potentially relevant papers remain originality risks. The result has not been independently validated.

## References
1. A. Malnič, D. Marušič, Š. Miklavič and P. Potočnik, *Semisymmetric elementary abelian covers of the Möbius–Kantor graph*, arXiv:math/0510383v1, first public 2005-10-18. Identifies the graph as the generalized Petersen graph \(\operatorname{GP}(8,3)\).
2. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448v1, first public 2020-01-15. Complete first public preprint inspected.
3. P. Deshpande, S. Shukla and A. Singh, *Distance \(r\)-domination number and \(r\)-independence complexes of graphs*, arXiv:2001.06775v1, first public 2020-01-19; its chordal-graph theorem does not cover this graph.
4. *Integral homotopy type of the Möbius–Kantor independence complex*, publicly indexed mathematical result, 2026-10-11; claim concerns ordinary independence (one-independence). Stable identifier `b0d62cfde5f3`.
5. *The Möbius–Kantor matching complex is a mixed-dimensional sphere wedge*, publicly indexed mathematical result, 2026-10-04; stable identifier `4bfded76792e`.
6. *The 2-independence complex of the Petersen graph is a 3-sphere*, publicly indexed mathematical result, 2026-10-11; stable identifier `156dc9567f6a`.
7. *Cyclic symmetry on Möbius–Kantor independence homology*, publicly indexed mathematical result, 2026-10-11; stable identifier `1c198fd64c4e`.
