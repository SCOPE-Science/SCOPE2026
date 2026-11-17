# Puncturing a Boolean cube removes the same number of neighborhood spheres from both parity components
## Finding
Let \(Q_n\) denote the graph of the binary \(n\)-dimensional cube, and let \(G_n=Q_n-v\) be obtained by removing any one vertex. For every integer \(n\ge3\), the ordinary open Lovász neighborhood complex has exactly two connected components, each of integral homotopy type
\[
\bigvee^{\nu_n} S^2,\qquad
\nu_n=2^{n-3}(n^2-5n+8)-1-\binom{n-1}{2}.
\]
A wedge of zero spheres here means a point. Thus both components are contractible at \(n=3\), and the multiplicities for \(n=4,5,6,7\) are respectively \(4,25,101,336\). For comparison, each component for the unpunctured cube has \(\mu_n=2^{n-3}(n^2-5n+8)-1\) two-spheres, so a single graph-vertex puncture destroys exactly \(\binom{n-1}{2}\) homology generators in **each** parity component, although the combinatorial alterations on the two shores are different.

## Assumptions and scope
Write \(V(Q_n)=\mathbf F_2^n\), with adjacent vertices differing in exactly one coordinate. The even and odd vertices are the two bipartition classes. For any graph \(G\) without isolated vertices, its open-neighborhood complex \(\mathcal N(G)\) consists of the nonempty finite subsets of \(V(G)\) that admit a common vertex adjacent to all of them, together with the empty face. All homotopy equivalences and sphere counts are integral and nonequivariant; no filling of higher-dimensional cells is implicit in the graph. The integer \(n\) ranges over all \(n\ge3\). The choice of deleted vertex does not matter by cube translation symmetry. The statement concerns the open neighborhood complex and not a Vietoris–Rips or closed-neighborhood complex.

## Proof
**1. Parity separation and a useful shore.** By a coordinate translation, delete \(0\in\mathbf F_2^n\), an even vertex. Each nonempty face has a common neighbor and hence lies on one bipartition shore. Denote the resulting disjoint subcomplexes by \(K_O\) (on odd vertices) and \(K_E\) (on the remaining even vertices). The cubical graph has minimum degree at least two after puncturing, so every remaining vertex occurs in the neighborhood complex. We first classify \(K_O\).

For any even cube vertex \(y\), write
\[
F_y=\{y+e_i:1\le i\le n\},
\]
where \(e_i\) are standard basis vectors. In the intact cube the facets of the odd neighborhood component are precisely the simplices \(2^{F_y}\) over all even \(y\). In the punctured graph, the facets are precisely \(2^{F_y}\) for \(y\ne0\). Distinct centers have at most two common neighbors: two distinct cube vertices have common neighbors only at Hamming distance two, when there are exactly two. Consequently every face with at least three vertices belongs to a unique facet. Every edge of the deleted facet \(F_0=\{e_1,\ldots,e_n\}\) persists because the pair \(\{e_i,e_j\}\) also lies in \(F_{e_i+e_j}\), whose center is nonzero. In particular the intact odd component \(K_O^{\mathrm{full}}\) and the punctured \(K_O\) have identical one-skeleta, and their only difference is the removal of all faces of \(2^{F_0}\) with three or more vertices.

**2. A complete two-dimensional collapse.** In each remaining facet \(F_y\), select an apex \(a_y\in F_y\). For each nonempty \(\sigma\subseteq F_y\setminus\{a_y\}\) with \(|\sigma|\ge3\), pair \(\sigma\) with \(\sigma\cup\{a_y\}\). Perform these elementary simplicial collapses in descending order of \(|\sigma|\), within each facet. At the time of each pairing all larger cofaces have already gone, and no outside facet contains a face of size three, so \(\sigma\) is free with unique surviving coface \(\sigma\cup\{a_y\}\). The pairs do not cross facets. All remaining faces have at most three vertices. Hence \(K_O\) simplicially collapses onto a two-dimensional complex \(L\).

**3. Fundamental group after puncturing.** First, the intact odd component \(K_O^{\mathrm{full}}\) is simply connected. Here is an explicit argument independent of the known numerical sphere count. Fix coordinate one and put \(g_j=e_1+e_j\) for \(2\le j\le n\). Its one-skeleton has an edge between odd vertices exactly when they differ in two coordinates. Every edge not of type \(g_j\) has difference \(e_i+e_j=g_i+g_j\), with \(i,j>1\). A triangle with a suitable nonzero common-neighbor center (the intact case permits all centers) homotopes that edge to a path consisting of two edges of types \(g_i,g_j\). Thus every edge loop is homotopic to a loop in the \((n-1)\)-cube graph on the odd shore with generators \(g_2,\ldots,g_n\). Every coordinate square in that graph is filled by two triangles of \(K_O^{\mathrm{full}}\): for each odd \(x\), the two triangles \(\{x,x+g_i,x+g_j\}\) and \(\{x+g_i,x+g_j,x+g_i+g_j\}\) share the square diagonal. The cubical two-skeleton is simply connected because adding higher-dimensional cells yields the contractible cube and does not change \(\pi_1\). Therefore \(\pi_1(K_O^{\mathrm{full}})=0\).

Now remove the vertex \(0\) from the graph. The only lost two-simplices are \(\{e_i,e_j,e_k\}\), for triples of distinct indices, because the only deleted facet is \(2^{F_0}\). The boundary of every such triangle is still nullhomotopic: put \(w=e_i+e_j+e_k\), an odd vertex not among these three, and use the three available triangles
\[
\{e_i,e_j,w\},\quad\{e_j,e_k,w\},\quad\{e_k,e_i,w\}.
\]
Their centers are respectively \(e_i+e_j\), \(e_j+e_k\) and \(e_k+e_i\), all nonzero even cube vertices. They form a simplicial disk filling the missing triangular boundary. Since intact and punctured components have the same one-skeleton and every lost two-cell relator is a consequence of retained two-cell relators, the Seifert–van Kampen presentations give the same trivial fundamental group. Higher missing faces do not affect \(\pi_1\). Thus \(K_O\), and consequently its two-dimensional collapse \(L\), are simply connected. The same edge description shows \(K_O\) is connected.

**4. Euler characteristic and integral homotopy.** In the intact odd component the face numbers are
\[
f_0=2^{n-1},\quad f_1=2^{n-2}\binom n2,
\quad f_{r-1}=2^{n-1}\binom nr\ (3\le r\le n).
\]
The unique-facet property proves the last formula. Summing their alternating signs gives
\[
\chi(K_O^{\mathrm{full}})=2^{n-3}(n^2-5n+8)=\mu_n+1.
\]
The puncture removes exactly \(\binom nr\) faces of cardinality \(r\), for every \(3\le r\le n\), and removes none of lower dimension. Therefore
\[
\chi(K_O^{\mathrm{full}})-\chi(K_O)
=\sum_{r=3}^{n}(-1)^{r-1}\binom nr
=\binom{n-1}{2}.
\]
Because \(L\) is a finite, connected, simply connected two-complex, its integral \(H_2\) is free, all positive homology other than \(H_2\) vanishes, and the rank of \(H_2\) is \(\chi(L)-1=\nu_n\). By Hurewicz, a basis is represented by maps of two-spheres; a wedge of these spheres maps by an integral homology isomorphism to \(L\). Both spaces are simply connected CW complexes, so Whitehead's theorem makes the map a homotopy equivalence. The case \(\nu_3=0\) gives a contractible complex.

**5. The other parity component.** Cover \(K_O\) by the full neighborhood simplices \(2^{F_y}\), indexed by surviving even vertices \(y\ne0\). Every nonempty finite intersection is a simplex and hence contractible. The nerve has the surviving even vertices as vertices, and a collection of them spans a face exactly when they share an odd graph neighbor. This nerve is **exactly \(K_E\)**. The simplicial nerve theorem (or the bipartite Dowker duality theorem) gives \(K_E\simeq K_O\). The two nonempty shores are disconnected from each other, so \(\mathcal N(G_n)=K_E\sqcup K_O\) with the claimed homotopy type. This completes the proof for every \(n\ge3\).

## Verification
The standalone dependency-free Python checker `artifacts/verify.py` constructs both neighborhood-complex shores directly from the graph, not from the proposed formula, for every \(3\le n\le7\). It verifies the actual facet lists, all faces and Euler characteristics, connectivity, and the rank of the mod-two second boundary; its computed first Betti number is zero and the Euler-derived second Betti number equals \(\nu_n\) in both shores. For \(3\le n\le6\) it also exhaustively replays explicit elementary collapses, checking unique cofaces at every removal, to a two-dimensional complex. The output in `artifacts/verification_output.txt` is reproducible with `python3 artifacts/verify.py`. These finite checks do **not** replace the unrestricted symbolic proof and do not constitute an independent mathematical audit.

## Relationship to prior work
A previously published hypercube-neighborhood theorem gives the intact \(Q_n\) sphere-wedge multiplicity \(\mu_n\) and a related facetwise two-dimensional collapse. The present theorem does **not** claim that parent result as new; it proves the separate vertex-deletion formula, local nullhomotopies for all lost triangles, and the equivalence of the combinatorially different punctured parity shores. The intact theorem's numerical homotopy classification alone does not imply the effect of deleting a vertex. Kozlov supplies the general neighborhood-complex background. Shukla treats maximum-degree-three graphs and certain four-regular circulants, rather than the arbitrary-dimensional vertex-punctured cube family. Arana–Stehlík's recent first-public 2025 paper concerns Lovász complexes of nonbipartite quadrangulations whose Lovász complexes are surfaces, whereas these graphs are bipartite and their neighborhood components are higher-rank sphere wedges for growing \(n\). Search comparisons against published mathematical records did not identify an equivalent full-puncture classification; absence of indexed matches does not prove uniqueness.

## Limitations
The theorem concerns deletion of **one graph vertex** and the ordinary open-neighborhood complex. It does not classify multiple removed vertices, graph-edge defects, induced subcomplex vertex deletion in place of graph vertex deletion, equivariant actions, or canonical sphere bases. The two shores are homotopy equivalent, not necessarily isomorphic as simplicial complexes. The computation checks only \(3\le n\le7\); the infinite conclusion is established by the proof. The main remaining scientific risk is an equivalent result formulated in inaccessible or unindexed literature. No independent audit or certification has been performed.

## References
1. C. Arana and M. Stehlík, *Quadrangulations and the Lovász complex*, arXiv:2510.03698v1, first public 2025-10-04, https://arxiv.org/html/2510.03698v1. A recent source on neighborhood/Lovász complexes, not the puncture claim.
2. *Neighborhood complexes of hypercubes collapse to explicit 2-sphere wedges*, published research record 2026-10-11, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-neighborhood-complexes-of-hypercubes-collapse-to-explicit-2-sphe--344271f4218a/RESULT.md. Gives the **intact** cube theorem, whose proof and claim were directly examined.
3. D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613v1, 2005-03-28, https://arxiv.org/abs/math/0503613.
4. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526v1, 2018-02-13, https://arxiv.org/abs/1802.04526.
