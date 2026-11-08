# Four-way rerouting cliques and sharp diameter for Johnson-graph geodesics

## Finding
Let \(N,k\) be integers with \(1\le k<N\), and let \(A\ne B\) be two \(k\)-element subsets of \([N]\). Put \(d=|A\setminus B|=|B\setminus A|\ge1\). Form the *geodesic rerouting graph* \(\mathcal R(A,B)\): its vertices are all shortest paths from \(A\) to \(B\) in the Johnson graph \(J(N,k)\); two paths are adjacent if they differ in exactly one intermediate vertex.

Write \(s_i\) for the transposition of adjacent positions \(i,i+1\) in \(S_d\), and \(e\) for the identity. Then
\[
\mathcal R(A,B)\cong\operatorname{Cay}\left(S_d\times S_d,\ \{(s_i,e),(e,s_i),(s_i,s_i):1\le i<d\}\right).
\]
Consequently, its isomorphism type depends only on \(d\), not on \(N\), \(k\), or the placement of the endpoints. It is vertex-transitive and connected, with
\[
|V|=(d!)^2,\qquad \deg=3(d-1),\qquad |E|=\frac{3(d-1)(d!)^2}{2},\qquad
\operatorname{rad}=\operatorname{diam}=\binom d2.
\]
For \(d\ge2\), every edge lies in exactly one maximal four-vertex clique; these are **all** maximal cliques, and their number is \((d-1)(d!)^2/4\). The graph has exactly \((d-1)(d!)^2\) triangles, each contained in one of those four-cliques. For \(d=1\) it consists of one vertex.

## Assumptions and scope
The Johnson graph \(J(N,k)\) has all \(k\)-subsets of \([N]\) as vertices, with an edge when exactly one element is removed and another inserted. An \(A\)-to-\(B\) shortest path has length \(d\). Paths are ordered vertex sequences with fixed endpoints, and a rerouting edge changes one internal vertex while leaving the other \(d\) vertices unchanged. All graphs here are undirected and simple; a four-clique is a copy of \(K_4\). The assertions cover every \(N,k,A,B\) satisfying the stated conditions, not merely antipodal endpoints in \(J(2d,d)\).

## Proof
**1. Parametrization.** A Johnson-graph step changes overlap with \(B\) by at most one. A shortest \(A\)-to-\(B\) path uses exactly \(d\) steps, so at each step it must remove an element of \(X=A\setminus B\) and insert an element of \(Y=B\setminus A\). Each element of \(X\) is removed once, each element of \(Y\) inserted once, and common elements are unchanged. Hence a shortest path is uniquely encoded by an ordering \(\sigma=(x_1,\ldots,x_d)\) of \(X\) and an ordering \(\tau=(y_1,\ldots,y_d)\) of \(Y\). Its vertex after step \(j\) is
\[
(A\setminus\{x_1,\ldots,x_j\})\cup\{y_1,\ldots,y_j\}\qquad(0\le j\le d).
\]
Thus there are exactly \((d!)^2\) paths.

**2. Exact one-step adjacency.** Fix consecutive paths which differ only at the vertex after step \(i\), where \(1\le i<d\). Their vertices at steps \(i-1\) and \(i+1\) agree. Between these fixed vertices, exactly two elements of \(X\) are removed and two of \(Y\) inserted. Choosing the first removed element and the first inserted element gives exactly four valid intermediate vertices, all different. The four paths form a \(K_4\), and their pairs of orderings differ by swapping the entries at positions \(i,i+1\) in the first ordering, the second ordering, or both. Conversely, those three swaps change just the step-\(i\) vertex. This proves the Cayley-graph isomorphism and the degree formula.

Each rerouting edge has a unique changed step \(i\); its two endpoint paths uniquely determine the fixed step-\(i-1\) and step-\(i+1\) vertices. Therefore it lies in precisely one such \(K_4\). In a triangle, the indices on consecutive edges must agree: otherwise the first and third paths differ in two intermediate vertices and cannot be adjacent. The same holds for any clique. Every clique with at least two vertices is contained in one of the described four-cliques, which are consequently exactly the maximal cliques for \(d\ge2\). Each vertex belongs to exactly one four-clique for each \(i\); each four-clique has four vertices. This gives \((d-1)(d!)^2/4\) maximal cliques. They partition the edges, so the edge and triangle counts are respectively \(6\) and \(4\) times that number.

**3. Sharp distance bound.** Relabelling the elements of \(X\) and \(Y\) independently acts transitively on ordered pairs \((\sigma,\tau)\) and preserves moves, so the graph is vertex-transitive. To reach any chosen target, first relabel its two orderings to the identity; it suffices to sort an arbitrary pair of permutations into their respective identities. Use the same fixed bubble-sort comparator schedule on both lists: compare positions \(1,2\), then \(2,3\), up to \(d-1,d\), then compare positions \(1,2\) through \(d-2,d-1\), and continue with successively shorter passes. In each comparison, swap the out-of-order pair in the first list, in the second, in both, or in neither. Every nontrivial stage is exactly one permitted rerouting move by Step 2. The schedule uses \(\sum_{j=1}^{d-1}j=\binom d2\) comparisons, and bubble sorting puts both lists in increasing order. Hence every two vertices are at distance at most \(\binom d2\).

For equality, consider a target whose first ordering reverses that of the source while its second ordering is unchanged. The inversion number of the first ordering relative to its target is \(\binom d2\), and each rerouting move changes that permutation by at most one adjacent transposition, altering its inversion count by at most one. Therefore at least \(\binom d2\) moves are necessary. The diameter is exactly this value. Vertex-transitivity makes every eccentricity equal to the diameter, proving the radius formula and connectedness.

## Verification
The standalone script `verify_direct.py` constructs the underlying Johnson-graph vertices as sets and every shortest path as an explicit sequence. For \(1\le d\le4\) it independently compares all pairs of paths for one-vertex rerouting adjacency, counts triangles by common-neighbor intersections, and checks the graph size, degree, edge count, and diameter. Its final output is `DIRECT_ALL_PASS`.

The separate script `verify_cayley.py` constructs the paired-permutation graph directly, independently computes its eccentricity for \(1\le d\le5\), and checks the comparator sorting construction on 400 seeded pairs at each order \(2\le d\le10\). Its final output is `CAYLEY_ALL_PASS`. Both scripts require only Python's standard library. These are finite cross-checks: the quantified theorem follows from the proof above.

## Relationship to prior work
Bonsma's earliest arXiv version (2010) establishes the shortest-path rerouting model and general complexity results, but not this Johnson-graph classification. Zara's 2003 paper studies *relevant ascending paths* in Johnson graphs and their Bruhat-order parametrization, not the all-geodesic one-vertex rerouting adjacency or its sharp diameter. Asplund and collaborators (2017) develop structure of shortest-path graphs and identify the permutohedron as the reconfiguration graph of antipodal hypercube paths; that one-permutation model does not furnish the simultaneous two-permutation Johnson moves. Gajjar and collaborators (2024) give the exact Kendall-tau metric for hypercube path rerouting, but do not provide the four-way Johnson cliques or the two-coordinate diameter theorem.

A direct analogy does not prove the claimed diameter: a Johnson rerouting step may exchange one, the other, or both adjacent positions, but *only at the same index*. For example, independent adjacent transpositions at two different indices require two moves even though either coordinate individually needs only one. The common comparator network resolves this synchronization constraint at the diameter level.

## Limitations
This theorem gives the exact graph model, local clique structure, degree/count invariants, and radius/diameter. It does **not** give a closed formula for every individual shortest rerouting distance between arbitrary pairs of paths or a count of shortest rerouting sequences. The original-priority comparison is based on the named accessible literature and database searches; it cannot exclude unpublished or differently indexed equivalent theorems. No external independent review has been performed.

## References
1. C. Zara, *Parking Functions, Stack-Sortable Permutations, and Spaces of Paths in the Johnson Graph*, Electronic Journal of Combinatorics 9(2), R11 (public 2003-04-23), DOI `10.37236/1683`.
2. P. Bonsma, *The Complexity of Rerouting Shortest Paths*, earliest arXiv `1009.3217v1` (2010-09-16); Theoretical Computer Science 510 (2013), 1–12.
3. J. Asplund, K. Edoh, R. Haas, Y. Hristova, B. Novick and B. Werner, *Reconfiguration graphs of shortest paths*, arXiv `1705.09385v1` (2017-05-25), Discrete Mathematics 341 (2018), 2938–2948.
4. K. Gajjar, A. V. Jha, M. Kumar and A. Lahiri, *Reconfiguring Shortest Paths in Graphs*, Algorithmica 86 (2024), 3309–3338, DOI `10.1007/s00453-024-01263-y`.
