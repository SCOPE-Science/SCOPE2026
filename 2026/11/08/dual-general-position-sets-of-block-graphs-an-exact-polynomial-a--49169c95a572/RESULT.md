# Dual general-position sets of block graphs: an exact polynomial and hereditary boundary

## Finding
Let \(G\) be a finite simple connected **block graph**: every block (including each bridge as a two-vertex block) is a clique. Let \(S(G)\) be its set of simplicial vertices and \(s=|S(G)|\). A *dual general-position set* \(X\subseteq V(G)\) is one for which (i) no vertex of \(X\) lies internally on a shortest path between two other vertices of \(X\), and (ii) no vertex of \(X\) lies internally on a shortest path between two vertices of \(V(G)\setminus X\). The empty set is permitted.

A *qualified pendant block* is a block \(B\) containing precisely one articulation vertex \(c\) of \(G\), where \(c\) belongs to precisely two blocks of \(G\). Write \(\mathcal Q(G)\) for the family of these blocks, and let \(q_k(G)\) count those with \(|V(B)|=k\).

**Theorem (complete classification).** For every connected block graph \(G\), the dual general-position sets are exactly the sets of the following two disjoint types:

1. Arbitrary subsets of \(S(G)\).
2. The entire vertex set \(V(B)\) of one qualified pendant block \(B\in\mathcal Q(G)\).

Consequently their cardinality-generating polynomial is
\[
D_G(z):=\sum_{X\text{ dual general-position}}z^{|X|}
=(1+z)^s+\sum_{B\in\mathcal Q(G)}z^{|V(B)|}
=(1+z)^s+\sum_{k\ge2}q_k(G)z^k.
\]
Every \(k\) between \(0\) and \(s\) occurs. For every qualified block \(B\), \(|V(B)|\le s\); therefore \(\deg D_G=s\) and
\[
q_k(G)=[z^k]D_G(z)-\binom{s}{k}\qquad(k\ge2).
\]
Thus this polynomial recovers the complete size distribution of qualified pendant blocks. Moreover, the family of dual general-position sets is downward closed under taking subsets **if and only if** \(\mathcal Q(G)=\varnothing\); equivalently, \(D_G(z)=(1+z)^s\). This is an exact structural boundary for the non-hereditary phenomenon.

For a tree \(T\) of order at least three, let \(\ell(T)\) be its number of leaves and \(p_2(T)\) its number of edges joining a leaf to a vertex of degree two. Then the specialization is
\[
D_T(z)=(1+z)^{\ell(T)}+p_2(T)z^2.
\]
For complete graphs, all vertices are simplicial and the correction sum is empty; the formula also holds for the one-vertex graph.

## Assumptions and scope
All graphs are finite, simple, undirected, and connected. The block decomposition is the usual one: maximal 2-connected subgraphs and bridges, with one-vertex graphs treated separately. A cut vertex \(c\) belongs to exactly as many blocks as there are connected components of \(G-c\) when \(G\) is a block graph. Every non-cut vertex in a nontrivial connected block graph is simplicial, and conversely; the same statement holds vacuously for a complete graph. No assumptions are made on the number of blocks or their sizes.

The term *polynomial* means ordinary labeled-vertex-subset enumeration: two different vertex subsets are counted separately even if an automorphism interchanges them. The result does not enumerate isomorphism classes or graph-embedding choices.

## Proof
**1. Simplicial subsets work.** A simplicial vertex cannot occur internally on a geodesic: if the two adjacent vertices along that geodesic surround the simplicial vertex, they are adjacent to each other, shortening the route. Hence any subset of \(S(G)\) satisfies both defining conditions, regardless of the endpoints of the tested geodesic.

**2. A selected cut vertex leaves only two pure branches.** Suppose \(X\) is dual general-position and contains a cut vertex \(c\). Let \(C_1,\ldots,C_d\) be the nonempty components of \(G-c\), with \(d\ge2\). If two different components contain vertices of \(X\), then any path between such vertices passes through \(c\) internally, contradicting general position. Thus at most one component contains selected vertices. If two different components contain vertices of \(V(G)\setminus X\), the same path-through-\(c\) observation contradicts the dual condition. Hence at most one component contains unselected vertices. Since every \(C_i\) is nonempty and each vertex is either selected or unselected, \(d\le2\), so \(d=2\). Both components must be pure: after relabeling, \(C_1\subseteq X\) and \(C_2\subseteq V(G)\setminus X\). It follows that \(X=C_1\cup\{c\}\).

**3. The selected branch must be a whole pendant clique.** The induced subgraph \(G[C_1\cup\{c\}]\) is connected. If it contained two nonadjacent vertices \(u,v\), a shortest \(u,v\)-path would stay within \(C_1\cup\{c\}\) (a path cannot leave this side through \(c\), visit \(C_2\), and return without repeating \(c\)). Every internal vertex of such a path would be selected, violating general position. Thus \(C_1\cup\{c\}\) is a clique. In a block graph the entire branch \(C_1\cup\{c\}\) must therefore be a single maximal clique block \(B\). It has no other cut vertex (otherwise it would extend into another block within \(C_1\)), and \(c\) belongs to exactly two blocks, because \(G-c\) has two components. Hence \(B\) is qualified and \(X=V(B)\).

**4. Qualified blocks work.** Conversely, let \(B\) be qualified and \(c\) its unique cut vertex. The selected set \(X=V(B)\) is a clique and therefore general-position. Removing all of \(B\) leaves exactly the other component of \(G-c\). Any geodesic between vertices of that component stays in it: entering \(B\) would require entering and returning through \(c\), contradicting simplicity of a shortest path. Hence there is no selected internal vertex on any geodesic between unselected endpoints. Thus \(V(B)\) is dual general-position.

**5. Disjoint enumeration and consequences.** Every qualified \(V(B)\) contains a non-simplicial cut vertex, so it is not a subset of \(S(G)\); different blocks have different vertex sets. This proves the classification and polynomial. Any connected noncomplete block graph has at least two pendant blocks, each with at least one simplicial vertex. A qualified block of order \(k\) contains \(k-1\) simplicial vertices, and a distinct pendant block supplies at least one more; consequently \(k\le s\). The binomial term therefore gives the full support \(0,\ldots,s\), degree \(s\), and the coefficient recovery formula. If a qualified block exists, its full vertex set is dual general-position but its singleton cut-vertex subset is not (the cut vertex lies internally on a path between unselected vertices from the two components). Otherwise all dual sets are subsets of \(S(G)\), a hereditary family. In a tree, the only blocks are edges, and a qualified block is precisely an edge between a leaf and a degree-two vertex. This proves every assertion. \(\square\)

## Verification
The standard-library program `verify.py` independently constructs all connected labeled block graphs with at most six vertices by testing every possible edge set, and also constructs deterministic larger clique-glued examples of orders seven through eleven. For each graph, it enumerates **every** vertex subset, computes shortest-path distances using breadth-first search, and tests the two defining geodesic conditions without invoking the theorem's convexity characterization. It separately computes block decompositions, articulation vertices, the predicted coefficient polynomial, and the hereditary criterion. Its actual execution returned:

`VERIFY_OK graphs=4943 subsets=414102 dual_sets=89688 exceptional_sets=7822 all_labeled_n_le_6=PASS deterministic_glued_cliques_n_7_to_11=PASS hereditary_boundary=PASS`

The program requires only Python 3 standard-library modules. Finite enumeration is a cross-check and not an infinite proof; the unrestricted result follows from the five steps above. To reproduce, run `python3 verify.py` in the directory containing the extracted file.

## Relationship to prior work
Tian and Klavžar, *Variety of general position problems in graphs* (first public preprint February 27, 2024, arXiv:2402.17338v1), introduced the dual variant and proved that a general-position set is dual exactly when its complement is geodesically convex (Theorem 3.1). They also established the lower bound from simplicial sets (Corollary 3.2), equality of the four extremal general-position numbers on block graphs, and the maximum dual sets of paths. These are prior results and are **not** claimed as new. The contribution here is a complete necessary-and-sufficient enumeration for *all* vertex subsets of *arbitrary connected block graphs*, plus the precise hereditary/non-hereditary boundary. The complete-graph boundary is elementary and also covered by existing complete-multipartite dual-position enumerations; it is not claimed as new. In particular, the prior maximum-value equality does not determine the polynomial or its exceptional coefficients.

Manuel and Klavžar, *A general position problem in graph theory* (2018), proved that the ordinary general-position number of a block graph equals its number of simplicial vertices (Theorem 3.6); their subject is the ordinary rather than dual condition and they do not enumerate the latter. Tian, Klavžar, and Tan (2024) investigate **edge** general-position on block graphs, a different choice of objects. Dokyeesun, Klavžar, Kuziak, and Tian study general-position variants of strong and lexicographic graph products (first preprint 2024), not this complete block-graph subset distribution. No claim of novelty is made for the convex-complement characterization, the simplicial-set construction, or the maximum dual general-position number.

## Limitations
The theorem is restricted to block graphs; no formula is asserted for arbitrary chordal or cactus graphs. The polynomial does not recover the entire block graph, only its simplicial count and sizes of qualified pendant blocks. Publication priority is provisional: an unindexed or otherwise undiscovered equivalent enumeration remains possible. Finite tests do not certify all graph orders.

## References
- J. Tian and S. Klavžar, *Variety of general position problems in graphs*, arXiv:2402.17338v1, February 27, 2024; *Bull. Malays. Math. Sci. Soc.* 48 (2025), article 5, DOI: 10.1007/s40840-024-01788-z.
- P. Manuel and S. Klavžar, *A general position problem in graph theory*, *Bull. Aust. Math. Soc.* 98 (2018), 177–187, DOI: 10.1017/S0004972718000473.
- J. Tian, S. Klavžar, and E. Tan, *Extremal Edge General Position Sets in Some Graphs*, *Graphs and Combinatorics* 40 (2024), article 40, DOI: 10.1007/s00373-024-02770-z.
- P. Dokyeesun, S. Klavžar, D. Kuziak, and J. Tian, *General position problems in strong and lexicographic products of graphs*, *Computational and Applied Mathematics* 45 (2026), article 97, DOI: 10.1007/s40314-025-03547-7; first arXiv preprint August 28, 2024.
