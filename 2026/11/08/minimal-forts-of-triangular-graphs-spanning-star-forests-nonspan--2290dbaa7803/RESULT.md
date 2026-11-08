# Minimal forts of triangular graphs: spanning star forests, nonspanning cycles, and an exact enumerator

## Finding

For each integer \(n\geq3\), let \(T_n=J(n,2)=L(K_n)\) denote the triangular graph whose vertices are the two-element subsets of \([n]\), adjacent when they intersect. A **fort** is a nonempty vertex set \(F\subseteq V(T_n)\) for which each vertex outside \(F\) has either zero or at least two neighbors inside \(F\). A fort is **inclusion-minimal** when no proper nonempty subset is a fort.

**Classification.** Regard \(F\) as the edge set of a simple graph \(H_F=([n],F)\). Then \(F\) is an inclusion-minimal fort of \(T_n\) if and only if exactly one of the following holds:

* \(H_F\) is a spanning star forest with no isolated vertices (its components are stars \(K_{1,r}\), \(r\geq1\)); or
* \(H_F\) consists of a single simple cycle of length \(k\) with \(3\leq k\leq n-1\), together with the \(n-k\) isolated vertices.

Here \(K_{1,1}\) is a single edge and is counted only once, not twice as a choice of center. The two types are disjoint.

Let \(f_{n,j}\) count inclusion-minimal forts of cardinality \(j\), and let \(\mathcal F_n(z)=\sum_j f_{n,j}z^j\). Then, for every \(n\geq3\),

\[
\boxed{\mathcal F_n(z)=n![t^n]\exp\!\left(\frac{zt^2}{2}+\sum_{k\geq3}\frac{z^{k-1}t^k}{(k-1)!}\right)
+\frac12\sum_{k=3}^{n-1}\binom nk(k-1)!z^k.}
\]

The cardinality spectrum is exactly \(\{2\}\) for \(n=3\), exactly \(\{2,3\}\) for \(n=4\), and exactly \(\{3,4,\ldots,n-1\}\) for all \(n\geq5\). In particular, all minimal forts have the same size only when \(n=3\).

## Assumptions and scope

All graphs are finite, simple, undirected, and labeled by \([n]\); no asymptotic or genericity assumptions are imposed. A fort is minimal by **full set inclusion**, not merely the absence of a fort after deleting a single vertex. The coefficient-extraction variable \(t\) is formal, so the infinite series is interpreted coefficientwise: only \(k\leq n\) contributes to \([t^n]\). For the cycle term, \(\binom nk=0\) outside its usual range and the sum is empty for \(n=3\).

## Proof

**1. Exact fort criterion.** Let \(H=([n],F)\) and write \(d_H(u)\) for the degree of label \(u\). For an unselected pair \(uv\notin F\), its neighbors in the selected vertex set of the line graph are precisely the selected edges incident with \(u\) or \(v\). Since \(uv\) itself is absent, these collections are disjoint. Hence

\[
|N_{T_n}(uv)\cap F|=d_H(u)+d_H(v).
\]

The fort condition fails exactly when \(H\) has both a degree-zero vertex and a degree-one vertex: if such vertices \(u,v\) exist, \(uv\) is necessarily absent and has exactly one selected neighbor; conversely, degrees summing to one must be zero and one. Therefore every nonempty fort is of one of two forms: **(A)** \(H\) covers all \(n\) vertices (every vertex has positive degree), or **(B)** \(H\) has at least one isolated vertex, and all its nonisolated vertices have degree at least two.

**2. The spanning case.** Suppose \(F\) is a minimal fort and \(H\) has no isolated vertices. If there were an edge \(e\in F\) whose deletion left all vertices covered, then \(F\setminus\{e\}\) would be another fort by (A), contradicting minimality. Thus \(F\) is an inclusion-minimal edge cover of the complete graph on \([n]\). For every selected edge, at least one endpoint must consequently have degree one: otherwise deleting it preserves the edge cover. A graph in which every edge has a degree-one endpoint is a disjoint union of stars (including \(K_{1,1}\)). Hence \(H\) is a spanning star forest.

Conversely, let \(H\) be a spanning star forest with no isolated vertices. Every proper nonempty edge subset \(F'\subsetneq F\) misses at least one of the original vertices, since each component edge of a star touches a leaf, which becomes isolated if that edge is removed. Meanwhile \(([n],F')\) is a nonempty forest, so it contains a degree-one vertex. The simultaneous degree-zero and degree-one vertices violate the exact fort criterion. Thus \(F\) is a minimal fort, not merely single-deletion critical.

**3. The nonspanning case.** Suppose \(F\) is a fort whose root graph has at least one isolated vertex. By (B) all positive degrees are at least two, so a nonempty connected component contains a simple cycle \(C\). The edges of this cycle themselves form a fort: they have no degree-one/degree-zero mixture, and they retain at least one originally isolated vertex. If \(F\) is minimal, it must consist exactly of the cycle edges. Conversely, if \(F\) is a simple cycle of length at most \(n-1\), every nonempty proper edge subset is a forest with a leaf and an isolated original label, so it is not a fort. This establishes the classification in both directions.

**4. Enumeration.** A labeled spanning star forest is a set partition of \([n]\) into blocks of size at least two, with a chosen star on each block. A block of size two supports exactly one star edge set and contributes \(zt^2/2\) to its exponential generating function. A block of size \(k\geq3\) supports exactly \(k\) different stars (choice of center), each having \(k-1\) edges; its contribution is \(k z^{k-1}t^k/k!=z^{k-1}t^k/(k-1)!\). The exponential formula yields the first term in \(\mathcal F_n(z)\).

For each \(k\in\{3,\ldots,n-1\}\), choosing the support of a simple cycle gives \(\binom nk\) choices, and an undirected labeled cycle on \(k\) vertices has \((k-1)!/2\) edge sets (cyclic orders modulo reversal). This yields the second term. The two types cannot overlap, since the first spans \([n]\) and is acyclic, whereas the second omits a label and is cyclic.

**5. Spectrum.** For \(n=3\), the only possible spanning star forest is a two-edge path, and no proper-support cycle exists. For \(n=4\), the perfect matchings give cardinality two, while stars and proper triangles give cardinality three. For every \(n\geq5\), the nonspanning cycles alone produce each cardinality from three through \(n-1\), while every spanning star forest has at least \(\lceil n/2\rceil\geq3\) edges and at most \(n-1\) edges. There are no other types by the classification. Thus the spectrum and the exceptional uniform case follow.

## Verification

The supplied standalone file `verify_forts.py` constructs the triangular graph directly and tests every nonempty vertex subset for \(3\leq n\leq7\) (\(2,131,011\) tested subsets in total). The test determines inclusion-minimality by a dynamic program over **all proper subsets** and independently compares both the predicted structural types and the full coefficient distributions. The calculation returned `VERIFY_OK`, with \(2,007,472\) forts and \(2,041\) inclusion-minimal forts counted across those five orders. For instance,

\[
\mathcal F_4(z)=3z^2+8z^3,\qquad
\mathcal F_5(z)=40z^3+20z^4,\qquad
\mathcal F_6(z)=35z^3+195z^4+78z^5.
\]

These exact finite checks do not prove the unrestricted statement; the preceding arguments do.

## Relationship to prior work

Becker, Cameron, Hanely, Ong, and Previte (arXiv:2404.05963v1, first posted 2024-04-09) study minimal-fort counts and give formulas for paths, cycles, spiders, and other families. The original full-text preprint discusses general bounds and constructions, but does not give this triangular-graph classification or its counting polynomial. Cameron, Hogben, Kenter, Mojallal, and Schuerger (arXiv:2310.17904v1, first posted 2023-10-27) develop fort hypergraphs, fractional zero forcing, and Cartesian-product results. Their general fort-hypergraph framework supplies motivation but not the above two-family classification of \(L(K_n)\). The claim is the graph-family-specific classification and enumerator, not the definition of forts, the general transversal characterization of zero forcing, or the general exponential formula.

## Limitations

This is a theorem about the entire triangular-graph family, not a characterization of forts in arbitrary line graphs. The enumerator counts inclusion-minimal forts and does not count all forts, nor does it classify which of the minimal-fort inequalities define facets of a zero-forcing polytope. No new formula for the ordinary zero forcing number is claimed. Priority against inaccessible or unindexed equivalent results remains an external-literature risk, and no independent mathematical audit is represented.

## References

1. P. Becker, T. R. Cameron, D. Hanely, B. Ong, J. P. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963v1 (2024), https://arxiv.org/abs/2404.05963, subsequently *Graphs and Combinatorics* 41 (2025), article 25.
2. T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal, H. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904v1 (2023), https://arxiv.org/abs/2310.17904.
