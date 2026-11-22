# Five minimal finite-space models realizing the seven-antihole

## Finding

Let \(H=\overline{C_7}\) be the complement of the chordless seven-cycle. For a finite topological space \(X\), write \(\operatorname{Ins}(X)\) for the graph whose distinct vertices are adjacent exactly when their open neighborhoods cannot be separated by disjoint open sets. If \(\operatorname{Ins}(X)\) contains an **induced** copy of \(H\), then \(|X|\ge 14\). At equality, \(X\) is necessarily a height-one \(T_0\) space, and all such spaces are classified by vertex covers of a seven-cycle.

More precisely, fix the induced seven vertices \(x_i\), indexed by \(i\in\mathbb Z/7\mathbb Z\), so that \(x_i\) and \(x_j\) are adjacent precisely when \(j-i\notin\{0,1,-1\}\). There are precisely seven further vertices \(m_j\), all minimal and mutually incomparable. Their strict order relations are exactly
\[
 m_j<x_j,\qquad m_j<x_{j+4},\qquad
 m_j<x_{j+2}\quad\text{if }j\in S,
\]
where \(S\subseteq\mathbb Z/7\mathbb Z\) obeys
\[
 \text{for every }i\in\mathbb Z/7\mathbb Z,\qquad
 i\in S\quad\text{or}\quad i-2\in S.
\]
The last condition says that \(S\) is a vertex cover of the step-two seven-cycle. Conversely, every such \(S\) produces an extremal finite \(T_0\) space. For the prescribed cyclic labels there are exactly \(29\) choices of \(S\), with cardinality distribution \(7,14,7,1\) at sizes \(4,5,6,7\). Under relabeling, the resulting spaces form exactly **five homeomorphism types**, with orbit sizes \(7,7,7,7,1\).

For every such space, the order complex is a connected graph and has homotopy type
\[
 |\Delta(X)|\simeq\bigvee^{|S|+1}S^1.
\]
Consequently the finite space itself is **weakly homotopy equivalent**, through its order complex, to bouquets of respectively \(5,6,7,8\) circles. The five distinct homeomorphism types split into four weak homotopy types; two distinct homeomorphism types have six circles.

## Assumptions and scope

Finite spaces need not initially satisfy the \(T_0\) separation axiom. The specialization order is \(u\le v\) when every open set containing \(v\) contains \(u\); in a finite \(T_0\) space it is a partial order, with minimal elements called open points. In the induced-graph assertion, all adjacencies and non-adjacencies are required only among the specified seven \(x_i\); there is no assertion that the full inseparability graph equals \(H\). The classification concerns minimum-cardinality realizations \(|X|=14\), not larger realizations.

## Proof

**Reduction to \(T_0\).** Points topologically indistinguishable in a finite space become closed twins in its inseparability graph. Distinct vertices of \(H\) have distinct closed neighborhoods (each has degree four, and no two closed neighborhoods are equal); thus the seven vertices remain distinct in the Kolmogorov quotient. The induced \(H\) survives this quotient, whose cardinality is no greater. It suffices to prove the lower bound for a \(T_0\) space. Once the bound is proved, an equality case has a quotient of size at least fourteen and is therefore itself \(T_0\).

**Seven forced minimal witnesses.** In a finite \(T_0\) space, two points are adjacent in \(\operatorname{Ins}(X)\) exactly when some minimal point lies below both. For any minimal point \(m\), its upper set among the specified seven points, \(A_m=\{i:m\le x_i\}\), is a clique in \(H\). No \(x_i\) is minimal: if it were, its inseparability closed neighborhood would be a clique, whereas the induced neighborhood in \(H\) is not.

There are seven distinguished edges
\[
 e_j=\{x_j,x_{j+4}\},\qquad j\in\mathbb Z/7\mathbb Z.
\]
A clique of \(H\) can contain at most one \(e_j\). Indeed the maximum cliques of \(H\) are the seven triples
\[
 T_j=\{x_j,x_{j+2},x_{j+4}\},
\]
and \(T_j\) is the **unique** maximal clique containing \(e_j\). Choose a minimal common lower bound \(m_j\) for the two endpoints of \(e_j\). The seven \(m_j\) are distinct, lie outside the seven \(x_i\), and hence \(|X|\ge14\).

**Rigidity at equality.** Suppose \(|X|=14\). Then the only points are the seven minimal points \(m_j\) and the seven distinguished points \(x_i\). There is no order relation between two distinct \(x_i,x_k\): if \(x_i\le x_k\), every minimal witness for an induced neighbor of \(x_i\) also witnesses adjacency to \(x_k\), hence \(N_H[x_i]\subseteq N_H[x_k]\). Both closed neighborhoods have five vertices and are distinct, contradiction. Thus all strict relations run from the \(m_j\) to the \(x_i\). For each \(j\), the upper fiber \(A_{m_j}\) contains \(x_j,x_{j+4}\), and, because it is a clique, may additionally contain only \(x_{j+2}\). Define \(S\) by the presence of that optional relation.

The remaining seven edges of \(H\) are \(\{x_i,x_{i+2}\}\), each appearing in exactly two of the triples, namely \(T_i\) and \(T_{i-2}\). Such an edge has a minimal common lower bound if and only if \(i\in S\) or \(i-2\in S\). Therefore the induced seven-vertex graph is exactly \(H\) if and only if \(S\) covers every edge of the step-two seven-cycle. Conversely, specifying these mandatory and optional relations defines a height-one partial order, and the preceding test verifies all \(14\) edges and all \(7\) nonedges of the induced \(H\).

**Counting and homeomorphism.** Since \(2\) generates \(\mathbb Z/7\mathbb Z\), the step-two graph is an ordinary \(C_7\). A vertex cover is the complement of an independent set. Its independent-set polynomial is \(1+7z+14z^2+7z^3\), yielding the \(29\) labeled covers. An isomorphism must permute the \(x_i\) by an automorphism of \(H\), exactly the dihedral group of order \(14\), and must carry \(m_j\) to the unique minimal witness for the image of \(e_j\). Its action on optional indices is the induced dihedral action. There is one orbit of size seven for four optional relations, two orbits of size seven for five, one orbit of size seven for six, and the fixed full set for seven: five homeomorphism types. Explicit orbit representatives are listed in `checks.json`.

**Weak homotopy types.** The order complex of this height-one poset is its bipartite incidence graph. The fourteen mandatory relations form a spanning \(14\)-cycle (because repeatedly adding \(4\) visits all seven indices); the \(|S|\) optional relations add exactly \(|S|\) further graph edges without changing connectivity. Thus its vertex and edge counts are \(14\) and \(14+|S|\), so its cycle rank is \(|S|+1\). Every connected graph has the homotopy type of a bouquet of as many circles as its cycle rank. McCord's theorem gives a weak homotopy equivalence from the realization of the order complex to the finite \(T_0\) space, proving the asserted *weak*, not ordinary, homotopy classification.

## Verification

`verify.py` (Python 3 standard library only) exhaustively constructs the seven maximal cliques, checks the uniqueness of every distinguished edge witness, verifies all \(128\) optional subsets against the induced graph, tests connectivity and cycle ranks for all \(29\) valid cases, and partitions the \(29\) cases under the actual dihedral action. Reproduce from the same directory with `python3 verify.py`; the exact structured output is `checks.json`. The finite enumeration verifies the base combinatorics; the reduction and rigidity proofs are independent arguments applying to every finite space.

## Relationship to prior work

Cameron and Kumar's *Graphs on Topological Spaces* (2026), Theorem 7.3, characterizes finite-space inseparability graphs via simplicial edge covering; Proposition 7.6 proves the induced-cycle lower bound and a coarser \(n+5\) lower bound for an induced odd antihole. This work uses their finite-space framework and refines the **extremal-poset classification** for the smallest genuine odd antihole. The numerical seven-clique edge-cover bound for \(\overline{C_7}\) is **not new**: it appears in Kim, Park and Sano (2009), Theorem 2.4, and, combined with general finite-space reasoning, already yields the fourteen-point lower bound. Accordingly the priority claim here is the exhaustive structure of equality cases, five homeomorphism types, and their weak homotopy ranks—not independent discovery of that clique-cover number or bound. Chen, DeLeo and Henderschedt (2025) give a related general characterization of finite-topology graph classes, not these specific extremal-poset types.

## Limitations

The classification concerns the induced \(\overline{C_7}\) threshold only; no corresponding classification for longer odd antiholes is claimed. The bouquet statement is about the homotopy type of the order complex and the **weak** homotopy type of the finite space, not about a homeomorphism or ordinary homotopy equivalence of finite spaces with CW bouquets. The seven-clique cover number and general graph-topology correspondence predate this classification. Full historical priority cannot be excluded by database searches; independent mathematical review has not been performed.

## References

1. P. J. Cameron and V. Kumar P. B., *Graphs on Topological Spaces*, arXiv:2610.14783, first posted 10 October 2026, especially Theorem 7.3 and Proposition 7.6. https://arxiv.org/abs/2610.14783
2. S.-R. Kim, B. Park and Y. Sano, *Cycles and p-competition graphs*, arXiv:0905.3942 (2009), especially Theorem 2.4 on the clique edge cover of \(\overline{C_7}\). https://arxiv.org/abs/0905.3942
3. K. Chen, J. DeLeo and O. Henderschedt, *Graphs generated from minimal sets of finite point-set topologies*, arXiv:2503.22490 (2025), especially Theorem 5.1. https://arxiv.org/abs/2503.22490
4. M. C. McCord, *Singular homology groups and homotopy groups of finite topological spaces*, Duke Math. J. 33 (1966), 465–474.
