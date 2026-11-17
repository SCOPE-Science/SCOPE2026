# Forty-one seven-spheres in the Desargues two-independence complex

## Finding
For the Desargues graph \(D=\operatorname{GP}(10,3)\), the complex of vertex subsets with induced connected components of order at most two has integral homotopy type
\[
\operatorname{Ind}_2(D)\simeq\bigvee^{41}S^7.
\]
In particular its only nonzero reduced integral homology is \(\widetilde H_7\cong\mathbb Z^{41}\). This is a homotopy classification, not merely a homology computation.

## Assumptions and scope
Take the vertex set to be \(\{u_i,v_i:i\in\mathbb Z/10\mathbb Z\}\), with edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\), indices modulo ten. The graph has twenty vertices, thirty undirected edges, and degree three at each vertex. Identify \(u_i\) with bit \(i\), \(v_i\) with bit \(10+i\), and a subset with the corresponding twenty-bit nonnegative integer.

A face \(F\) of \(X\) is a subset for which every vertex of the induced graph \(D[F]\) has degree at most one. This condition is equivalent to saying that every connected component has at most two vertices: every connected graph with three or more vertices has a path on three vertices. Equivalently, \(X\) is the \(P_3\)-devoid complex \(\mathcal D(D;P_3)\), in the sense that no three-vertex path occurs as a subgraph of an induced subgraph.

There is a second explicit realization as the incidence graph between the ten two-element and ten three-element subsets of a fixed five-element set; incidence means containment. The included checker verifies a full twenty-vertex graph isomorphism between that realization and the indicated generalized Petersen realization.

## Proof
**1. Exact face family.** All \(2^{20}\) vertex masks are tested, including the empty mask. For a nonempty mask \(s\), let \(v\) be its least significant selected vertex and \(t=s\setminus\{v\}\). The mask \(s\) belongs to \(X\) exactly when \(t\) belongs to \(X\) and (i) \(v\) has at most one neighbor in \(t\), and (ii) if that neighbor \(w\) exists, it has no neighbor in \(t\). This follows directly by adding a vertex to a graph whose components have order at most two. The recurrence produces \(62{,}048\) nonempty faces. The counts by face cardinality \(1,\ldots,12\) are
\[
(20,190,1080,3985,9784,15910,16600,10390,3460,564,60,5).
\]
There are no faces of cardinality larger than twelve. Independently, the incidence-graph realization lists all sixty unordered three-vertex paths (each centered at one of twenty degree-three vertices, with three neighbor pairs). The face membership condition is exactly the absence of each such three-element obstruction. The checker constructs this family independently, relabels it through the explicit isomorphism, and verifies equality for all \(2^{20}\) masks.

**2. Construct the Morse matching.** Work on the poset of all *nonempty* faces. For the twenty pivot vertices \(v_j=7j\bmod20\), \(j=0,\ldots,19\), in that order, scan masks \(s=1,\ldots,2^{20}-1\) in increasing numerical order. If \(s\) is an as-yet-unpaired face with pivot \(v_j\) absent, and \(t=s\cup\{v_j\}\) is also an as-yet-unpaired face, pair \(s\) and \(t\). Each pair is a genuine face-poset covering edge, and no face participates twice. The resulting matching has exactly \(31{,}003\) pairs. Its unmatched faces consist of precisely one vertex and forty-one eight-element faces (dimension seven), with no other critical faces.

**3. Check acyclicity completely.** For every pair \(T\subset S\) of nonempty faces differing by one vertex, orient its Hasse edge from \(S\) down to \(T\), except that matched edges are reversed. There are exactly \(400{,}760\) such edges. The included checker builds the indegree of every vertex in this directed graph, then performs complete Kahn topological sorting, following each unmatched edge downward and each matched edge upward. It processes all \(62{,}048\) faces. A finite directed graph has such a complete topological ordering if and only if it is acyclic, so this matching is an acyclic discrete-Morse matching. The same critical-cell profile and complete acyclicity test are verified for the independent pivot sequence \(v_j=3j\bmod20\).

**4. Infer the integral homotopy type.** Forman's discrete-Morse theorem gives a CW complex homotopy equivalent to \(X\), with one zero-cell, forty-one seven-cells, and no cells in other dimensions. Every seven-cell is necessarily attached to the sole zero-cell by a constant map from its boundary sphere. Hence this CW complex is a wedge of forty-one seven-spheres. No rational approximation, attaching-degree inference, or homology-to-homotopy converse is used.

## Verification
Run `g++ -O2 -std=c++17 verify_desargues.cpp -o verify_desargues` followed by `./verify_desargues`. The self-contained source computes both graph realizations, verifies their full adjacency-matrix correspondence, enumerates faces by two distinct criteria, constructs both deterministic matchings, and checks each complete directed face-poset graph for cycles. `verification_output.txt` is the recorded output. The essential output is \(62{,}048\) nonempty faces, \(31{,}003\) matched pairs, one critical zero-cell, forty-one critical seven-cells, \(400{,}760\) Hasse covering relations, and a topological ordering covering all faces for both matching orders. The reduced Euler characteristic is \(-41\), as a cross-check rather than the homotopy proof.

## Relationship to prior work
Taylan (first public version January 27, 2015) develops matching trees and computes \(P_3\)-devoid homotopy types for forests, together with path and cycle families. The Desargues graph is connected, cubic, and contains cycles, so those exact-family classifications do not apply. Deshpande and Singh's later treatment of higher independence complexes (2020 preprint) treats complete multipartite, fully whiskered, path, cycle, and perfect rooted-tree families. The Desargues graph is outside those families. Later chordal-graph results likewise do not specialize to this girth-six graph. Published calculations of the *ordinary* independence or edge-matching complexes of the Desargues graph concern different face conditions: they do not determine this vertex-based two-independence homotopy type. The comparison is with the theorems and objects, not just with titles or sphere counts.

## Limitations
The theorem concerns exactly the twenty-vertex Desargues graph and the second (component size at most two) independence complex. It does not establish any classification for larger generalized Petersen graphs, any integral equivariant homotopy type, or shellability. Exhaustive verification applies to all finite faces of this graph, not to an infinite graph family. Literature searches and inspected primary texts do not logically establish worldwide priority; equivalent unindexed work remains possible. The verification and review are not independent mathematical certification.

## References
1. D. Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs*, arXiv:1501.06754v1 (first public January 27, 2015), especially Theorems 3.10, 3.14, and 5.2. https://arxiv.org/html/1501.06754v1
2. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448v1 (January 15, 2020). https://arxiv.org/abs/2001.05448
3. F. M. Abdelmalek et al., *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863v1 (June 21, 2021). https://arxiv.org/abs/2106.10863
4. Y. Orlovich et al., *The complexity of dissociation set problems in graphs*, Discrete Applied Mathematics **159** (2011), 1352–1366, DOI 10.1016/j.dam.2011.04.023. This concerns combinatorial optimization of the same permitted subsets, not the present homotopy calculation.
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145.
