# Geometric fixed-point homotopy of clique-free complexes of multipartite graphs

## Finding

Let \(G=K_{a_1,\ldots,a_m}\) have \(m\ge2\) nonempty independent parts, let \(t\ge2\), and let \(H\le\operatorname{Aut}(G)\) be any subgroup, including those permuting equal-size parts. Let \(P_1,\ldots,P_k\) be the orbits of \(H\) on the set of parts and let \(w_j=|P_j|\), sorted so that \(w_1\le\cdots\le w_k\). Put \(T=t-1\). If \(w_1>T\), then \(|\mathsf{CF}_t(G)|^H=\varnothing\). Otherwise its homotopy type is
\[|\mathsf{CF}_t(G)|^H\simeq\bigvee_{\substack{\varnothing\ne S\subseteq\{2,\ldots,k\}\\T-w_1<\sum_{j\in S}w_j\le T}}S^{|S|-1}.\]
An empty wedge here denotes a point. Thus all nonempty fixed-point spaces have torsion-free reduced integral homology and the number of degree-\(d\) generators is the number of such subsets of cardinality \(d+1\). In particular, for seven equal nontrivial parts and \(t=5\), the involution interchanging two disjoint pairs of parts has fixed-point homotopy type \(S^1\vee S^2\vee S^2\), whereas the ambient complex is \(\bigvee^{15}S^3\).

The formula determines the **actual geometric fixed-point locus**, not only the subcomplex of individually fixed vertices. Its numerical input consists solely of orbits on the multipartition classes, irrespective of the subgroup action within each class.

## Assumptions and scope

The graph is finite, simple, and complete multipartite, with a specified partition into \(m\ge2\) nonempty pairwise nonadjacent classes. Automorphisms can permute classes of equal size. The integer \(t\) satisfies \(t\ge2\), including \(t>m\), when the clique-free complex is a simplex. The simplicial complex \(\mathsf{CF}_t(G)\) consists of all subsets of graph vertices with no \(t\)-clique. Its geometric realization is the ordinary affine realization, and fixed points are fixed pointwise by **every** element of \(H\). The empty realization is distinguished from a contractible nonempty one. Each sphere wedge is an ordinary homotopy equivalence, not an equivariant wedge decomposition for a normalizer action.

## Proof

1. In a complete multipartite graph, a chosen vertex subset contains a clique of order \(t\) if and only if it meets at least \(t\) parts. Therefore the face condition is that its support on the set of parts has cardinality at most \(T=t-1\).

2. A point in the affine realization is fixed by \(H\) exactly when its barycentric coefficients are constant on each orbit of \(H\) on the original graph vertices. Consequently the fixed-point locus is canonically homeomorphic to the realization of the **orbit complex**: a collection of vertex orbits is a simplex precisely when their full union is an allowed face. This orbit construction includes barycenters of permuted vertices and is not the usual induced subcomplex on individually fixed vertices.

3. Any vertex orbit contained over a part orbit \(P_j\) necessarily meets every class of that part orbit, by transitivity of \(H\) on \(P_j\). No vertex orbit meets classes from different part orbits. Thus selecting even one vertex orbit over \(P_j\) contributes exactly \(w_j\) distinct graph parts to the forbidden-clique count; selecting additional such vertex orbits contributes no more graph parts. The orbit complex has one nonempty group of mutually interchangeable vertices for each \(P_j\), and a face exists precisely if the sum of the weights of the groups it uses is at most \(T\).

4. Choose one representative vertex orbit from each group. Mapping every orbit-complex vertex to its group's representative is simplicial, and this map is contiguous to the identity because the union of any face with its image occupies the same part orbits. Therefore the orbit complex is homotopy equivalent to the weighted threshold complex \(K_{T}(w_1,\ldots,w_k)\), whose faces are exactly subsets with total weight at most \(T\). The same argument handles all within-part and part-permuting actions.

5. If \(w_1>T\), there is no nonempty allowable orbit simplex, so the geometric fixed-point locus is empty. Otherwise let \(A\) be the closed star of the first vertex in \(K_T\), consisting of faces containing it and faces of weight at most \(T-w_1\) on the remaining vertices. This is a nonempty contractible simplicial subcomplex. Every face of \(K_T\) outside \(A\) is a nonempty subset \(S\subseteq\{2,\ldots,k\}\) with \(T-w_1<\sum_{j\in S}w_j\le T\). For every such \(S\) and every \(j\in S\), removing \(j\) lowers its weight by at least \(w_1\), so **every proper face** of \(S\) lies in \(A\). Hence no two faces outside \(A\) can contain one another; each is a simplex attached entirely along its boundary to \(A\).

6. Because \(A\) is a nonempty contractible subcomplex of a CW complex, the quotient map induces a homotopy equivalence \(|K_T|\simeq |K_T|/|A|\). The quotient is exactly one sphere of dimension \(|S|-1\) for every indicated \(S\), wedged at the collapsed star. This proves the formula and integral homology statement, including zero-dimensional wedges and the contractible case.

For the example, the seven part-orbits before quotient each have weight one. The simultaneous swap of the fourth/fifth and sixth/seventh parts has orbit weights \((1,1,1,2,2)\). At \(T=4\), the qualifying subsets of the four weights after the first one are the two groups of weights \((1,1,2)\) and the pair \((2,2)\), yielding two \(2\)-spheres and one \(1\)-sphere. With the trivial subgroup, the qualifying subsets are the \(\binom{6}{4}=15\) four-subsets, yielding the ambient bouquet of fifteen \(3\)-spheres.

## Verification

The companion `verify.py` uses ordinary graph adjacency to enumerate forbidden-clique-free unions of vertex orbits under explicitly generated permutation subgroups, computes all nonempty faces of the resulting orbit complex, and calculates its reduced simplicial homology over \(\mathbb F_2\). It independently compares those ranks with the formula for the weighted threshold complex, including trivial groups, within-part swaps, permutations of equal-size parts, a mixed-dimensional fixed locus and an empty fixed locus. The recorded output `verify_output.txt` reports 124 parameter/subgroup instances and 20,554 orbit-complex faces, with `ALL_VERIFY_OK`. Finite verification is auxiliary: the proof above establishes all cases integrally and for arbitrarily large graphs and finite subgroups.

Reproduce from the package directory with `python3 verify.py` using only the Python 3 standard library. The verifier returns nonzero if a comparison fails.

## Relationship to prior work

Ghosh and Selvaraja [1] introduced systematic shellability and decomposability results for \(t\)-clique-free graph complexes, especially chordal/diamond-free graphs and clique-whiskering. Their results do not provide the fixed-point homotopy classification of unmodified complete multipartite graphs under arbitrary part-permuting automorphisms. The simple weighted-threshold calculation is an explicit structural argument rather than an invocation of shellability. The trivial-subgroup case is the classical skeleton-of-a-simplex homotopy formula and is **not** presented as an original nonequivariant classification. Earlier split-graph symmetry calculations for another special graph family do not determine these arbitrary multipartite fixed spaces. The new statement determines all subgroup-fixed homotopy types at once, including mixed-dimensional fixed-point homology, and is not a claim about residual equivariance.

## Limitations

No explicit normalizer-equivariant wedge splitting is established, nor any simultaneous compatibility of homotopy equivalences across inclusions of subgroups. The formula describes finite complete multipartite graphs only. An equivalent result outside the searched literature could exist. Independent review has not been performed.

## References

[1] Rakesh Ghosh and S Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1, first posted 2026-02-10, https://arxiv.org/abs/2602.09623 .

[2] Classical facts: contiguity of simplicial maps, CW quotient by a contractible subcomplex, and simplicial homology over the integers; used with explicit proofs of their applicability above.
