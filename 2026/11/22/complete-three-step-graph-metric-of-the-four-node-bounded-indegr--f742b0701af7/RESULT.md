# Complete three-step graph metric of the four-node bounded-indegree characteristic-imset polytope

## Finding
Let \(P=\mathrm{CIM}_{4,2}\) be the convex hull of the characteristic imsets of all directed acyclic graphs on four labelled vertices of maximum in-degree at most two. For the graph \(G(P)\) of its vertices and edges, the unordered-pair graph-distance distribution is exactly
\[
\#\{\{u,v\}:d_G(u,v)=r\}=\begin{cases}2508&r=1,\\7666&r=2,\\1001&r=3,\\0&r>3.\end{cases}
\]
Every one of the \(150\) vertices has eccentricity \(3\), hence \(\operatorname{rad}G(P)=\operatorname{diam}G(P)=3\), despite nonconstant vertex degrees. The Wiener index is \(20843\). The vertex-degree spectrum, written as (degree : multiplicity), is
\[
(14:3,15:4,16:6,18:1,20:12,25:12,27:12,29:6,30:40,42:12,47:6,49:24,50:12).
\]
The \(150\) vertices and \(2508\) edges are previously known from the published face vector; their inclusion here enables the complete distance census, not a claim of discovery of those counts.

## Assumptions and scope
A directed graph on \(\{1,2,3,4\}\) is *admissible* if it is acyclic and has at most two parents at each node. List the six unordered pairs in lexicographic order, followed by the four unordered triples in lexicographic order. The corresponding characteristic imset \(c_D\in\{0,1\}^{10}\) has
\[
c_D(S)=1\quad\Longleftrightarrow\quad\exists v\in S:\ S\setminus\{v\}\subseteq\operatorname{pa}_D(v).
\]
All vertex labels and all ten coordinates are fixed; the polytope is the convex hull of these points, not the polytope for a fixed underlying undirected skeleton and not the full eleven-coordinate \(\mathrm{CIM}_4\). Graph distance permits traversal of every polytope edge, not only moves of a particular statistical algorithm.

## Proof
Enumerate the three possible states (absent, forward, backward) of each of the six unordered pairs. Reject directed cycles and nodes with more than two parents. There are precisely \(443\) admissible directed acyclic graphs and exactly \(150\) distinct ten-coordinate characteristic imsets. Every distinct imset is a vertex: for a zero-one vector \(v\), the linear functional \(\sum_{k}(2v_k-1)x_k\) is uniquely maximized at \(v\) among distinct zero-one points.

We now give a finite, exact edge test. Fix distinct vertices \(u,v\) and let \(J=\{k:u_k=v_k\}\). Intersecting \(P\) with the coordinate equalities \(x_k=u_k\) for \(k\in J\) gives a face \(F_{uv}\), since each zero-one coordinate is bounded between zero and one. Write the differing coordinates in increasing order and complement each where \(u_k=1\). Then the transformed endpoints are the all-zero and all-one vectors. For a certified edge, the attached integer vector \(a\) satisfies \(\sum a_k=0\), and \(a\cdot w<0\) for every other transformed vertex of \(F_{uv}\). This exhibits \(u,v\) as exactly the maximizers of a linear functional on the face, hence their segment is a polytope edge. If no other vertex lies in the face, this last argument applies without an additional vector.

For a certified nonedge, the attached positive integers \(q_s\), denominator \(Q\), and other vertex indices \(s\notin\{u,v\}\) satisfy \(\sum_s q_s=Q\) and, coordinatewise,
\[
2\sum_s q_s s_k=Q(u_k+v_k).
\]
Thus the midpoint of \([u,v]\) is a convex combination of vertices other than the endpoints. The segment cannot then be an edge, since a supporting hyperplane exposing an edge would force all contributing vertices onto it. These two conditions are sufficient in their respective directions; no assertion that all nonedges necessarily admit midpoint witnesses is needed.

The accompanying `imset_certs.json` contains an exact certificate for each of the \(\binom{150}{2}=11175\) unordered pairs: \(2508\) exposing certificates and \(8667\) other-vertex midpoint certificates. The independent standard-library `imset_verify.py` reconstructs the vertices from the definition, checks every integer inequality or exact midpoint equation, builds the certified graph, and performs exact breadth-first searches from all \(150\) vertices. The BFS results give all distances, eccentricities, degrees, radius, diameter, and Wiener index stated above. In particular, the \(1001\) distance-three pairs prove the sharp lower bound \(3\), and the absence of other distances proves the upper bound \(3\).

## Verification
Place `imset_verify.py` and `imset_certs.json` in one directory and run `python imset_verify.py` using Python 3 and no nonstandard dependencies. The checker verifies \(443\) admissible DAGs, \(150\) distinct imsets, every certificate for all \(11175\) pairs, \(2508\) graph edges, and the exact three-distance distribution. The producer used numerical linear programming solely to *discover* certificates; the final verifier uses only Python integer arithmetic, so its correctness is independent of solver tolerances. The certificate file is part of this package, not referenced from another source.

## Relationship to prior work
Coons, Hollering and Paul [1, Example 3.9] first give the bounded-in-degree polytope, prove its full dimensionality, and publish its full face vector, including the vertex and edge counts \(150\) and \(2508\). Their paper does not state a complete distance or eccentricity census. Restadh [2, Proposition 2.14 and surrounding discussion] proves \(\operatorname{diam}(\mathrm{CIM}_n)\le2n-2\), and reports the exact diameter \(n-1\) for the unrestricted \(\mathrm{CIM}_n\) for \(n\le4\). Even the precise unrestricted diameter at \(n=4\) does not imply the diameter of the proper face \(\mathrm{CIM}_{4,2}\): shortest paths in the full graph may leave that face. Restadh's skeleton-fixed face bounds also concern a different polytope. Linusson, Restadh and Solus [3] classify edges for certain fixed-skeleton faces (trees and cycles), rather than the full mixed-skeleton degree-bounded polytope. These implications explain why the exact bounded-indegree distance distribution is not subsumed by the inspected results.

## Limitations
This is a certified finite classification for exactly four labelled nodes and parent bound two; it provides no all-node theorem, no statistical sample-complexity statement and no guarantee for greedy score-increasing paths. A shortest undirected edge path need not be monotone for an objective. The exhaustive certificate is substantial; independent mathematical and historical-priority assessment have not been performed. A published or unpublished existing enumeration of the same graph could subsume this claim even though the inspected sources did not contain it.

## References
[1] J. I. Coons, B. Hollering and N. C. Paul, *Polyhedral Geometry of Degree-Bounded Characteristic Imset Polytopes*, arXiv:2611.09633v1, first public 2026-11-06, https://arxiv.org/html/2611.09633v1 .

[2] P. Restadh, *Diameters of the Characteristic Imset Polytopes*, arXiv:2302.03647v2, https://arxiv.org/pdf/2302.03647 .

[3] S. Linusson, P. Restadh and L. Solus, *On the Edges of Characteristic Imset Polytopes*, arXiv:2209.07579, https://arxiv.org/abs/2209.07579 .
