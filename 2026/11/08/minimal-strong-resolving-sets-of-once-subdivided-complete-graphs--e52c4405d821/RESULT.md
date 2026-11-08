# Minimal strong resolving sets of once-subdivided complete graphs

## Finding

Fix any integer \(n\ge4\). Let \(H_n=S(K_n)\) be obtained by subdividing once each edge of the complete graph on the labelled vertices \(1,\dots,n\). Write \(v_i\) for the original vertices and \(q_{ij}=q_{ji}\) for the degree-two vertex on the old edge \(ij\). Put \(Q_n=\{q_{ij}:1\le i<j\le n\}\) and \(m=\binom n2\).

**Theorem.** The complete family of inclusion-minimal strong resolving sets of \(H_n\) consists precisely of the \(n\) sets
\[
Q_n\setminus\{q_{ij}:j\ne i\}\quad(1\le i\le n)
\]
and the \(\binom n3\) sets
\[
Q_n\setminus\{q_{ij},q_{ik},q_{jk}\}\quad(1\le i<j<k\le n).
\]
The displayed sets are distinct, and none contains an original vertex. Consequently the cardinality polynomial is
\[
R_n(z)=n z^{\binom n2-n+1}+\binom n3 z^{\binom n2-3}.
\]
If the exponents agree (only at \(n=4\)), their coefficients are added. There are \(n+\binom n3\) such sets. The strong metric dimension is \(\binom n2-n+1\); the largest cardinality of an inclusion-minimal strong resolving set is \(\binom n2-3\). For \(n\ge6\), exactly \(n-5\) consecutive intervening cardinalities, from \(\binom n2-n+2\) to \(\binom n2-4\), are absent. In particular the gap between the two attainable cardinalities is \(n-4\) and is unbounded.

## Assumptions and scope

All graphs are finite, simple and undirected, and distances are shortest-path lengths. A vertex \(w\) *strongly resolves* distinct \(u,v\) if one lies on a shortest path from the other to \(w\), equivalently if \(d(w,u)=d(w,v)+d(u,v)\) or \(d(w,v)=d(w,u)+d(u,v)\). A set is *strong resolving* if every unordered pair is strongly resolved by one of its vertices. Minimal always means inclusion-minimal, not minimum-cardinality. Vertices \(x,y\) are *mutually maximally distant* (MMD) if every neighbor of either is at distance at most \(d(x,y)\) from the other. The *strong resolving graph* has the same vertex set as the original graph and joins precisely MMD pairs; isolated vertices are retained. The general strong resolving graph theorem says strong resolving sets are exactly vertex covers of this graph [1,2]. We prove the needed special graph identification directly.

## Proof

**1. Distances.** For distinct original vertices, \(d(v_i,v_j)=2\). For an original vertex \(v_i\) and an edge vertex \(q_{jk}\), distance is \(1\) if \(i\in\{j,k\}\) and \(3\) otherwise. Two distinct edge vertices have distance \(2\) if their old edges share an endpoint and distance \(4\) if those edges are disjoint. These formulas follow from the bipartite incidence structure and completeness of the unsubdivided graph.

**2. Exactly the disjoint-edge pairs are MMD.** If \(\{i,j\}\cap\{k,l\}=\varnothing\), then \(d(q_{ij},q_{kl})=4\). Every neighbor of either edge vertex is an original endpoint and has distance \(3\) from the other edge vertex, so the pair is MMD. Every other pair has a witness violating the MMD condition:

* For \(v_i,v_j\), choose \(l\notin\{i,j\}\); neighbor \(q_{il}\) of \(v_i\) is distance \(3>2\) from \(v_j\).
* For incident \(v_i,q_{ij}\), choose \(l\notin\{i,j\}\); neighbor \(q_{il}\) is distance \(2>1\) from \(q_{ij}\).
* For nonincident \(v_i,q_{jk}\), choose \(l\notin\{i,j,k\}\) (possible because \(n\ge4\)); neighbor \(q_{il}\) is distance \(4>3\) from \(q_{jk}\).
* For distinct edge vertices \(q_{ij},q_{ik}\) sharing \(i\), neighbor \(v_j\) of \(q_{ij}\) has distance \(3>2\) from \(q_{ik}\).

Thus the strong resolving graph is the Kneser graph \(KG(n,2)\) on the edge vertices \(q_{ij}\), with its edges joining disjoint two-subsets, together with \(n\) isolated original vertices.

**3. All minimal covers.** By the strong resolving graph/vertex-cover equivalence [1,2], inclusion-minimal strong resolving sets of \(H_n\) are exactly inclusion-minimal vertex covers of \(KG(n,2)\), with no isolated original vertices. Complements within \(Q_n\) of such covers are precisely inclusion-maximal families of pairwise-intersecting two-subsets of \(\{1,\dots,n\}\).

Any such family either has a common element \(i\), in which case maximality makes it the entire star \(\{\{i,j\}:j\ne i\}\), or has no common element. In the second case take two distinct intersecting pairs \(\{i,j\},\{i,k\}\). Some family member omits \(i\); to intersect both it must be \(\{j,k\}\). Every two-subset meeting all three sides of this triangle is itself one of those three sides. Maximality therefore makes the family exactly that triangle. Conversely, full stars and triangles are both maximal intersecting families for every \(n\ge4\). These are the two asserted forms of the omitted edge vertices.

**4. Sizes and gaps.** A star omits \(n-1\) of the \(m\) edge vertices, and a triangle omits three. There are exactly \(n\) labelled stars and \(\binom n3\) labelled triangles. They are distinct even when \(n=4\) (all have three edges then). Hence the polynomial, total count, lower and upper extremal cardinalities, and absent intervals follow. No other minimal sets exist.

## Verification

Run `python3 verify_strong_subdiv.py` (Python 3.9+; no nonstandard dependencies). The verifier builds each subdivided graph directly for \(4\le n\le7\), computes all distances by breadth-first search, verifies the exact MMD graph against the disjointness graph, and exhaustively evaluates every subset of old edges to test the proposed maximal-intersecting family classification. Independently, for \(n=4,5\), it exhaustively tests the original strong-resolving condition for each vertex subset and its inclusion-minimality. The checked counts by \(n=4,5,6,7\), respectively, are \(8,15,26,42\) minimal sets; altogether \(2{,}131{,}008\) candidate edge families and \(33{,}792\) candidate strong-resolving vertex sets are examined. The output is `VERIFY_OK`. Computation corroborates finite orders only; steps 1--4 prove every \(n\ge4\).

## Relationship to prior work

The strong resolving graph/vertex-cover characterization is an established theorem of Oellermann and Peters-Fransen, described explicitly by Kuziak et al. [1]. Bergougnoux, Defrain, and Mc Inerney [2] prove polynomial-delay enumeration of arbitrary minimal strong resolving sets using this relationship. The elementary star/triangle classification of maximal intersecting two-set families is also classical. The claim here is the identification of the strong resolving graph of the full edge subdivision of a complete graph with \(KG(n,2)\), and its consequent exact **minimal-set distribution and unbounded gap**. The cited general results alone do not specify the MMD relation for this particular family. An earlier equivalent specialized classification not indexed by the searches remains a possibility.

## Limitations

The classification is for a once-subdivided complete graph, not arbitrary subdivisions or arbitrary incidence graphs. The two-term formula is not a new general algorithm for minimal strong resolving set enumeration, and no novelty is claimed for the general vertex-cover theorem or the intersecting-family lemma. Infinite correctness is analytical, not certified by the finite computations. An independent mathematical and publication-priority audit has not been performed.

## References

[1] D. Kuziak, M. L. Puertas, J. A. Rodríguez-Velázquez, I. G. Yero, *Strong resolving graphs: the realization and the characterization problems* (first arXiv posting 8 December 2016), arXiv:1612.02843v1, https://arxiv.org/html/1612.02843v1.

[2] B. Bergougnoux, O. Defrain, F. Mc Inerney, *Enumerating minimal solution sets for metric graph problems* (first arXiv posting 29 September 2023), arXiv:2309.17419v1, https://arxiv.org/html/2309.17419v2 (revised full text consulted).
