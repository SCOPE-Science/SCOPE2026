# Complete Boolean shattering of deranged pairings: a pure complex with an exact top-face correction

## Finding

Let \(n\ge 2\). Partition \(2n\) labeled vertices into \(n\) prescribed pairs \(F\), and delete the \(n\) pair edges from the complete graph. The resulting *cocktail-party graph* is \(G_n=K_{2n}\setminus F\). Let \(\mathcal P_n\) be the family of all perfect matchings of \(G_n\), viewed as Boolean concepts on its edges: a query at an edge asks whether it belongs to the unknown perfect matching. A support \(S\subseteq E(G_n)\) is *shattered* if every labeling of its edges is realized by a perfect matching.

**Complete criterion.** A support is shattered precisely if either

1. \(S\) is a matching of at most \(n-2\) edges; or
2. \(S\) is a matching of exactly \(n-1\) edges and its two unmatched vertices are **not** one of the deleted prescribed pairs.

The stronger local statement holds: for every edge-query support \(S\) with \(|S|\le n-2\), *whether or not \(S\) is itself a matching*, the trace family is exactly the set of matching subcollections of \(S\):
\[
\{P\cap S:P\in\mathcal P_n\}
 =\{T\subseteq S:T\text{ is a matching}\}.
\]

Consequently the shattered-support complex is pure of dimension \(n-2\), and both its VC and Littlestone dimensions equal \(n-1\). Write \(p_n=|\mathcal P_n|\), with the convention \((-1)!!=1\), and let \(m_{n,k}\) be the number of size-\(k\) matchings in \(G_n\). Then its entire face polynomial is
\[
\boxed{\Phi_n(z)=\sum_{k=0}^{n-2}m_{n,k}z^k+n p_nz^{n-1}},
\]
where both numerical terms have closed inclusion-exclusion expressions
\[
\boxed{m_{n,k}=\sum_{j=0}^{k}(-1)^j\binom nj
 \frac{(2n-2j)!}{2^{k-j}(k-j)!(2n-2k)!}},
\qquad
\boxed{p_n=\sum_{j=0}^{n}(-1)^j\binom nj(2n-2j-1)!!}.
\]
Here the formula for \(m_{n,k}\) is required only for \(0\le k\le n-2\), although it also counts matchings for other feasible \(k\). In particular, the number of facets is exactly \(n p_n\), not the number of arbitrary near-perfect matchings. For example,
\[
\Phi_5(z)=1+40z+500z^2+2240z^3+2720z^4.
\]

## Assumptions and scope

Graphs are finite, simple, undirected, and labeled; the prescribed pairing \(F\) is fixed. A *matching* is a set of pairwise vertex-disjoint edges; a *perfect matching* covers all \(2n\) vertices. The empty support is shattered and contributes the constant coefficient one. An edge-query support can contain arbitrary edges of \(G_n\), including intersecting edges, although such a support cannot be shattered when it has at least two intersecting edges. The asserted range includes \(n=2\), when \(G_2\) is a four-cycle and the polynomial is \(1+4z\). No claim is made for \(n=1\), when deleting the unique pair leaves no perfect matching.

## Proof

**1. Residual pairing lemma.** Let \(U\) be any set of \(2k\ge4\) vertices and let \(A\) be the restriction of the deleted pairing \(F\) to \(U\). If we forbid in addition at most \(k-2\) arbitrary edges on \(U\), the remaining graph has a perfect matching: each vertex loses at most one edge from \(A\) and at most \(k-2\) additional edges. Its degree is therefore at least \((2k-1)-1-(k-2)=k\), so Dirac's theorem supplies a Hamiltonian cycle and alternate cycle edges give a perfect matching. This includes the four-vertex case \(k=2\), where there are no additional forbidden edges.

A second version applies when the additional forbidden edges form **one matching** \(B\). For \(k\ge3\), the residual degree is at least \(2k-3\ge k\), so the same argument gives a perfect matching. For \(k=2\), the three perfect matchings of \(K_4\) partition its six edges. Each of the two forbidden matchings \(A\) and \(B\) occupies edges from at most one of those three perfect matchings; the third avoids both. Thus for any \(k\ge2\), the complement of the union of two matchings on \(2k\) vertices has a perfect matching.

**2. All traces on small supports.** Fix \(S\subseteq E(G_n)\) with \(|S|\le n-2\), and any matching \(T\subseteq S\). Prescribe all edges of \(T\) as positive. The residual unmatched vertex set \(U\) has \(2k=2(n-|T|)\) vertices, where \(k\ge2\). Forbidden residual edges consist of the prescribed-pair edges \(F\) and of the queried edges \(S\setminus T\) (edges having a removed endpoint are irrelevant). There are at most \(|S|-|T|\le k-2\) of the latter. By the first residual pairing lemma they admit a perfect matching on \(U\), which joined with \(T\) realizes exactly the desired trace. Conversely, the trace of a perfect matching is always a matching. This proves the trace identity, including for nonmatching \(S\).

**3. The sharp boundary.** If \(S\) is shattered, the all-positive labeling occurs, so \(S\) is a matching. A support of \(n\) edges would then itself be a perfect matching; setting any one edge negative and all the others positive is impossible, since only its two endpoints remain unmatched and the removed edge is forced. Hence \(|S|\le n-1\). Step 2 shatters all matching supports through \(n-2\). For \(|S|=n-1\), the all-positive labeling extends to a perfect matching exactly when the two unused vertices form an **allowed** edge. Conversely, assume that unused pair is allowed. The full trace occurs. For every strict subset \(T\subset S\), at least four vertices remain after fixing \(T\), while all forbidden queried edges \(S\setminus T\) still form a matching. The second residual pairing lemma supplies a completion avoiding every unselected queried edge. Every trace therefore occurs. This proves the criterion.

**4. Facets, purity, and static dimension.** Any shattered \(S\) with fewer than \(n-1\) edges extends to a perfect matching \(P\), by Step 2 with all its edges positive. Choose an edge \(e\in P\setminus S\). The set \(P\setminus\{e\}\) has \(n-1\) edges, contains \(S\), and is shattered by Step 3, because its unused vertices are joined by the legal edge \(e\). Thus every maximal shattered support has exactly \(n-1\) edges. There are such supports for every \(n\ge2\); hence the VC dimension is \(n-1\) and the complex is pure of dimension \(n-2\).

**5. Exact enumeration.** A size-\(k\) matching of the complete graph \(K_{2n}\) containing a fixed selection of \(j\) disjoint prescribed-pair edges is obtained by matching \(2(k-j)\) of the remaining \(2(n-j)\) vertices. The number of completions is \((2n-2j)!/[2^{k-j}(k-j)!(2n-2k)!]\). Inclusion-exclusion over the \(n\) forbidden edges yields the expression for \(m_{n,k}\); at \(k=n\), the same computation gives the standard deranged-pairing count \(p_n\). Every shattered support of size \(n-1\) has a **unique** completion to a perfect matching, by inserting the edge joining its two unused vertices. Conversely, deleting any one of the \(n\) edges of each perfect matching gives a shattered support of size \(n-1\). These two operations are mutually inverse between top supports and pairs \((P,e)\) with \(P\in\mathcal P_n\), \(e\in P\). Thus the top coefficient is exactly \(n p_n\). No further faces exist, yielding the polynomial.

**6. Exact online dimension.** In an arbitrary perfect-matching concept class on \(2n\) vertices, any complete adaptive shattered query tree of depth \(n\) would have a positive root subtree of depth \(n-1\). Once a root edge is declared positive, its endpoints are fixed and all remaining nonconstant queries concern a perfect matching on the other \(2n-2\) vertices. Inductively this residual class has Littlestone dimension at most \(n-2\); the base case is a single possible edge on two vertices and dimension zero. Thus every such concept class has Littlestone dimension at most \(n-1\). Since static VC shattering of \(n-1\) queries also supplies a depth-\((n-1)\) adaptive tree, equality holds here.

## Verification

The standalone script `verify_cocktail_shattering.py` constructs all perfect matchings independently by recursion on the least unused vertex and tests all edge-query supports of cardinality at most \(n-1\) for every \(2\le n\le5\). For supports of size at most \(n-2\), it separately checks that the **entire** realized trace family consists exactly of the matching subcollections, including on supports with intersecting edges. It compares all computed coefficients with the two independent inclusion-exclusion sums. Its run yielded **104,500 exhaustive direct support checks**, with coefficient vectors \((1,4)\), \((1,12,24)\), \((1,24,156,240)\), and \((1,40,500,2240,2720)\), and the terminal marker `COCKTAIL_TRACE_PASS 104500 direct support checks`. The universal result follows from the graph-theoretic proof, not from finite enumeration.

## Relationship to prior work

Chase and Freitag (2018) establish the general model-theoretic setting of VC dimension and Boolean concept classes; this supplies the foundational learning interpretation, not this exact matching trace theorem. Lu and Yu (2018) study the more general notion of positive-and-negative matching extension \(E(m,n)\), but their large-order sufficient conditions for fixed extension parameters do not determine all traces through the moving critical boundary \(m+n=n-1\) or enumerate the facets of this specific graph.

Bucić, Devlin, Hendon, Horne, and Lund (2019) study intersection probabilities of perfect matchings in bipartite and general graphs. Johnston, Kayll, and Palmer (2022) consider precisely the graph \(K_{2n}\setminus F\) and the number of its perfect matchings, including asymptotics. The standard closed formula for that number, \(p_n\), and its inclusion-exclusion proof are prior facts and are **not** claimed new. Neither inspected study states the Boolean trace classification, purity, or the formula for all shattered faces.

Previously recorded results for the *bipartite* crown graph \(K_{n,n}\setminus F\) prove that its derangement-assignment support complex has VC dimension \(n-2\), with no top faces of degree \(n-1\). The two graph families are not isomorphic, and the bipartite classification does not imply the present \(n-1\) dimensional law: the four-cycle \(G_2\) already has four shattered singleton edges, whereas the two-by-two crown graph has just one derangement matching. Another known result concerns noncrossing perfect matchings of convex points and their face-activity constraint; those concepts restrict crossings rather than a fixed set of disjoint edges and give a different top-face count. The present result isolates the **nonbipartite deranged-pairing** trace boundary and its exact face enumerator.

## Limitations

The proof applies to complete graphs with precisely one prescribed perfect matching deleted, not to arbitrary forbidden-edge sets, general multipartite graphs, or an arbitrary family of selected perfect matchings. It gives face counts, purity, and VC/Littlestone dimensions, but not a homotopy type, an algorithm for general matching-extension problems, or a classification of online trees. All external checks were limited to the literature and records accessed; a differently titled or unindexed prior statement might cover all or part of the finding. Finite computational verification does not constitute an independent mathematical audit.

## References

1. H. Chase and J. Freitag, *Model Theory and Machine Learning*, arXiv:1801.06566v1, first public 2018-01-19, https://arxiv.org/abs/1801.06566 .
2. H. Lu and Q. Yu, *Binding Number, Toughness and General Matching Extendability in Graphs*, arXiv:1807.11159v1, first public 2018-07-30, https://arxiv.org/abs/1807.11159 .
3. M. Bucić, P. Devlin, M. Hendon, D. Horne, and B. Lund, *Perfect matchings and derangements on graphs*, arXiv:1906.05908v1, first public 2019-06-13, https://arxiv.org/abs/1906.05908 .
4. D. Johnston, P. M. Kayll, and C. Palmer, *Deranged matchings: proofs and conjectures*, arXiv:2209.11319v1, first public 2022-09-22, https://arxiv.org/abs/2209.11319 .
