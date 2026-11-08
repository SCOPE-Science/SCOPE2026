# Contractibility of the truncated-cube perfect-matching complex

## Finding
Let \(Q_3\) be the graph on \(\{0,1\}^3\) with edges of Hamming length one, and let \(T\) be the truncated-cube graph obtained by replacing every vertex of \(Q_3\) by a triangle and joining the corresponding triangle corners along the original cube edges. Let \(\mathcal M_{\mathrm p}(T)\) be the simplicial complex whose vertices are edges of \(T\) and whose facets are perfect matchings of \(T\). Then
\[
\boxed{\mathcal M_{\mathrm p}(T)\simeq *.}
\]
The complex has exactly 32 facets, each of dimension 11, and 118,096 faces including the empty face. It is not a cone. In contrast, the ordinary matching complex \(\mathcal M(T)\) has Euler characteristic \(-331\), so it is not contractible and is not homotopy equivalent to \(\mathcal M_{\mathrm p}(T)\).

## Assumptions and scope
All graphs are finite, simple, and undirected. For an explicit model, label the vertices of \(Q_3\) by the integers \(0,\ldots,7\), viewed as binary triples. For every oriented cube edge \((u,v)\), introduce one vertex of \(T\). Two such vertices are adjacent if they are distinct darts with common initial vertex, or if they are the opposite orientations of the same cube edge. Thus \(T\) has 24 vertices and 36 edges. This is the one-skeleton of the Archimedean truncated cube, with eight triangular and six octagonal faces.

In the verifier, the 24 darts are ordered by initial vertex \(u\) and then by increasing terminal vertex \(v\); the 36 graph edges are lexicographically ordered pairs of dart indices. Each simplex is represented by a 36-bit integer identifying a subset of these graph edges. The empty face is included only for counting; the discrete-Morse pairing uses nonempty faces.

## Proof
**Perfect matchings and odd subgraphs.** In a perfect matching of \(T\), each triangle replacing a cube vertex uses either all three external edges or one external edge and the unique internal edge joining the other two corners. Consequently, the selected external edges correspond to a spanning edge subset \(A\subseteq E(Q_3)\) whose degree at every original cube vertex is odd (one or three). Conversely, every such \(A\) uniquely determines a perfect matching by inserting the internal edge at each vertex of degree one. The incidence matrix of the connected cube has rank seven over \(\mathbb F_2\). Since the all-ones vertex parity vector is admissible, the number of odd-degree edge subsets is \(2^{12-7}=32\). An independent vertex-covering backtracking enumerator also produces precisely these 32 perfect matchings.

**Complete simplicial enumeration.** Taking all subsets of these 32 twelve-edge matchings gives 118,096 distinct faces, including the empty face, with nonempty face vector, by dimensions zero through eleven,
\[
(36,510,3492,11865,22920,28700,25176,15828,7040,2112,384,32).
\]
The Euler characteristic is one. Each of the 24 edges inside the eight triangles belongs to eight facets, and each of the twelve external edges belongs to sixteen; hence no vertex of the simplicial complex belongs to every facet, so the complex is not a cone.

**Acyclic Morse pairing.** Order the graph-edge vertices as specified above. Starting with all nonempty simplices, for each of the 36 graph edges in order, pair every still-unpaired simplex \(\sigma\) not containing that edge with \(\sigma\) plus the edge whenever both are still unpaired. Each stage is an element pairing on the unmatched cells; the union is acyclic by the standard sequential element-pairing lemma. An independent directed-Hasse topological sort checks acyclicity of the entire pairing over all 737,700 covering incidences. It produces exactly 59,036 pairs, leaving one critical zero-cell, eleven critical three-cells, and eleven critical four-cells, and no other critical cells.

**Integral attaching boundary.** Orient every simplex by increasing graph-edge index. The cellular degree-three-to-four Morse boundary is evaluated exactly using the standard signed gradient-path substitution. In particular, write \(P(\tau)\) for the image of an oriented three-simplex in the free abelian group on critical three-simplices. It is its basis generator if critical, zero if matched upward from dimension two, and, if paired as a lower face with an oriented four-simplex \(\eta\), satisfies
\[
P(\tau)=-[\eta:\tau]^{-1}\sum_{\substack{\rho\subset\eta,\,\dim\rho=3\\\rho\ne\tau}}[\eta:\rho]P(\rho).
\]
Here every incidence coefficient is \(\pm1\). Summing the projections of the signed faces of each critical four-simplex gives the integral \(11\times11\) Morse boundary matrix, whose determinant is \(+1\). The complete computation, including every incidence sign and memoized recursion, is reproduced by `verify.py`. Thus the Morse CW model has no reduced integral homology. Since it has one zero-cell and cells only in dimensions three and four, it is simply connected. The Hurewicz and Whitehead theorems then show that it is contractible, as is the original complex.

**Independent ordering.** Repeating the full construction with the 36 graph edges considered in reverse order yields a second acyclic pairing with 59,024 pairs, one critical zero-cell, 23 critical three-cells, and 23 critical four-cells. The independent integral Morse boundary has determinant \(+1\) again. It therefore gives the same conclusion.

**Ordinary matching-complex contrast.** For the original 24-vertex graph \(T\), let \(Z(U)\) denote the alternating sum of all matchings in the induced graph on vertex subset \(U\). For any \(u\in U\), the matching recurrence is
\[
Z(U)=Z(U\setminus\{u\})-\sum_{v\in N(u)\cap U}Z(U\setminus\{u,v\}),\qquad Z(\varnothing)=1.
\]
Exact memoized evaluation gives \(Z(V(T))=332\). Thus \(\chi(\mathcal M(T))=1-332=-331\). This distinguishes the ordinary and perfect-matching complexes without claiming an ordinary-matching homotopy classification.

## Verification
Run `python3 verify.py` with a standard-library Python 3 interpreter. The script independently enumerates the 32 perfect matchings both as exact graph matchings and as parity-constrained cube edge subsets, constructs all 118,096 simplices, checks the full Hasse directed graph for both element-pairing orders, evaluates both integer Morse matrices with exact rational elimination, and computes the ordinary matching Euler characteristic by a graph-vertex recurrence. No randomized assumptions, floating-point arithmetic, hidden files, or external mathematical software are used. A successful execution prints `TRUNCATED_CUBE_PM_COMPLEX_CONTRACTIBLE_VERIFIED`; the associated output is supplied as `verify_output.txt`.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega [1] defined and calculated perfect-matching complexes for honeycomb graphs. Chandrakar and Singh [2] classified such complexes for polygonal line tilings and two-row square grids. Their graph-family hypotheses do not include this truncated-cube graph, which has eight vertex-disjoint triangle faces linked into a non-line polyhedral graph. The complete-bipartite chessboard result discussed in [1] also does not apply: the truncated cube is cubic, not complete bipartite. Existing calculations of the truncated cube's independence and Vietoris–Rips complexes concern different face predicates, and no implication of this perfect-matching contractibility has been identified.

## Limitations
The theorem concerns only the graph \(T\) and its specified simplicial complex; it gives no general theorem for truncations of arbitrary cubic graphs. It establishes homotopy contractibility, not an explicit sequence of elementary simplicial collapses or an equivariant contraction. The ordinary matching complex is distinguished by Euler characteristic only. The finite computation is exhaustive for these exact graph and complex definitions, but this does not establish bibliographic uniqueness; an unindexed equivalent calculation may exist. Independent external audit has not been performed.

## References
[1] M. Bayer, M. Jelić Milutinović, and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803, first publicly posted 2022-09-06; Electronic Journal of Combinatorics 30(2), P2.45 (2023). https://arxiv.org/pdf/2209.02803

[2] H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809, first publicly posted 2024-07-08. https://arxiv.org/pdf/2407.05809

[3] R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145; standard discrete-Morse and CW homotopy principles.
