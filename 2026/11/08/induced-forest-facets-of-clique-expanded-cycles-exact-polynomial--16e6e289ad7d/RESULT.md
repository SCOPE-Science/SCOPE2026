# Induced-forest facets of clique-expanded cycles: exact polynomials and exceptional purity

## Finding

For every pair of integers \(n\ge4\), \(m\ge2\), let \(H_{n,m}=C_n[K_m]\), the graph formed by replacing each vertex of the labelled cycle \(C_n\) with a clique of order \(m\), with complete joins between neighboring cliques. A forest set is a vertex subset whose induced graph is acyclic; a facet is a forest set maximal by inclusion. Put \(u=mz\), \(v=\binom m2 z^2\), and
\[
B=\begin{pmatrix}1&u&v\\1&u&0\\1&0&0\end{pmatrix}.
\]
The polynomial \(F_{n,m}(z)\) of **all** forest sets and the polynomial \(M_{n,m}(z)\) of **all facets** are exactly
\[
F_{n,m}(z)=\operatorname{tr}(B^n)-u^n,
\]
\[
\boxed{M_{n,m}(z)=nu^{n-1}+\sum_{k=1}^{\lfloor n/2\rfloor}
\frac nk\,v^k[x^{n-k}]
\left(x+x^2+\frac{u^2x^4}{1-ux}\right)^k.}
\]
The coefficient-extraction formula is polynomial in \(z\) and has nonnegative integer coefficients; \(x\) is an auxiliary formal variable. Every facet cardinality is between the following sharp endpoints:
\[
\min|S|=\min\!\left\{n-1,\,2\left\lceil\frac n3\right\rceil\right\}
=\begin{cases}3,&n=4,\\2\lceil n/3\rceil,&n\ge5,\end{cases}
\]
\[
\max|S|=\begin{cases}n,&n\text{ even},\\n-1,&n\text{ odd}.\end{cases}
\]
Consequently the induced-forest simplicial complex is **pure exactly at** \(n=5\) and \(n=7\), for every \(m\ge2\). In particular, writing \(a=\binom m2\),
\[
M_{5,m}(z)=5(m^4+am^2+a^2)z^4,
\qquad
M_{7,m}(z)=7(m^6+am^4+a^2m^2+a^3)z^6.
\]
A set is a minimal feedback vertex set precisely when its complement is one of these facets. Thus its full cardinality polynomial is \(z^{nm}M_{n,m}(1/z)\).

## Assumptions and scope

All graphs are finite, undirected, simple, and labelled. The cycle has length \(n\ge4\); the homogeneous replacement cliques have size \(m\ge2\). A forest subset includes the empty set. Maximal means inclusion-maximal, not largest possible cardinality. A cyclic word records the number \(0\), \(1\), or \(2\) of vertices chosen from each replacement clique. Each occurrence of \(1\) has \(m\) label choices; each occurrence of \(2\) has \(\binom m2\) label choices. These choices distinguish different labelled vertex subsets.

## Proof

**Fiber reduction.** More generally, in a clique substitution of any simple base graph, an induced forest uses at most two vertices from each fiber: three form a triangle. A fiber containing two selected vertices cannot have a selected vertex in any neighboring fiber, since the three vertices would form a triangle. Once these double fibers are isolated, the singleton fibers induce the base graph restricted to their indices; acyclicity of that induced graph is necessary and sufficient. For the base cycle \(C_n\), every proper induced vertex subgraph is a disjoint union of paths. Therefore a cyclic \(\{0,1,2\}\)-word is admissible exactly when every \(2\) has two neighboring \(0\)'s and the word is not all \(1\)'s.

**All-forest polynomial.** In the matrix \(B\), rows and columns represent consecutive fiber counts \(0,1,2\). Its entry from state \(i\) to state \(j\) is the weight of count \(j\), except that an adjacent pair involving a \(2\) and a positive count is forbidden. Closed walks of length \(n\) encode and weight each admissible cyclic word exactly once at its fixed labelled starting fiber. The sole additional forbidden word is all \(1\)'s, contributing \(u^n\). This proves the formula for \(F_{n,m}\).

**Maximality.** Suppose the cyclic word is admissible. A fiber of size \(1\) admits a second selected vertex if and only if both its neighboring fiber counts are \(0\). A zero fiber admits its first vertex unless one of its neighboring fiber counts is \(2\), or filling it would complete the all-singleton cycle. The latter possibility occurs exactly when there is one \(0\) and all other entries are \(1\). A double fiber admits no further vertex. Hence there is one exceptional family with a single zero, of total weight \(nu^{n-1}\). Every other facet has at least one \(2\) and is characterized by three local conditions: each \(2\) has neighboring \(0\)'s; each \(1\) has a neighboring \(1\); each \(0\) has a neighboring \(2\). These conditions are both necessary and sufficient by the preceding one-vertex extension tests. In particular, no run of \(1\)'s has length one.

**Cyclic gaps.** Consider a locally maximal word with exactly \(k\ge1\) occurrences of \(2\), and mark one of them. Between successive occurrences of \(2\), read the intervening gap in cyclic order. Its only permitted forms are \(0\), \(00\), and \(0\,1^\ell\,0\) for integers \(\ell\ge2\). Indeed, every intervening zero needs a neighboring two, while a run of singleton fibers must have length at least two. Conversely, any cyclic concatenation of such gaps and doubled fibers satisfies all local conditions. The gap-length and weight generating series is
\[
A(x,z)=x+x^2+\sum_{\ell\ge2}u^\ell x^{\ell+2}
=x+x^2+\frac{u^2x^4}{1-ux}.
\]
The \(k\) doubled fibers contribute \(v^k\), while the \(k\) gaps occupy \(n-k\) positions. There are \(n\) choices for the starting labelled position of a marked doubled fiber and exactly \(k\) possible marks of any resulting labelled word. Dividing by \(k\) gives \(\frac nk v^k[x^{n-k}]A(x,z)^k\). The sum over \(1\le k\le\lfloor n/2\rfloor\), together with the exceptional family, proves the complete facet polynomial.

**Sharp cardinality bounds.** For any locally maximal word containing a \(2\), write \(q,s,t\) for its numbers of double, singleton, and zero fibers. Each double fiber has two zero neighbors; each zero has at least one double neighbor and at most two, hence \(q\le t\le2q\). The facet has \(j=2q+s=n-t+q\) vertices and \(n=q+s+t\le3q+s=j+q\). Let \(p=\lceil n/3\rceil\). If \(j<2p\) is even, write \(j=2h\); then \(q\le h\) implies \(n\le j+q\le3h\le3(p-1)<n\), a contradiction. If \(j<2p\) is odd, write \(j=2h+1\). Since every singleton run has length at least two, the odd number \(s\) cannot be one; therefore \(s\ge3\), \(q\le h-1\), and \(n\le j+q\le3h\le3(p-1)<n\), another contradiction. Thus \(j\ge2p\). This bound is attained by choosing \(p\) doubled fibers and gaps consisting solely of one or two zeros: the required gap lengths exist because \(2p\le n\le3p\). The exceptional family has size \(n-1\), yielding the asserted minimum including \(n=4\).

For the upper bound, \(t\ge q\) gives \(j=n-t+q\le n\). Equality forces every zero to have two doubled neighbors, hence perfect alternation of doubled and zero fibers, possible only for even \(n\). If \(n\) is even, the alternating word attains \(n\); if \(n\) is odd, the exceptional word attains \(n-1\), the largest possible. The lower and upper endpoints coincide precisely at \(n=5\) or \(7\). At \(n=4\) or any even \(n\ge6\) the endpoints differ, and for odd \(n\ge9\), \(2\lceil n/3\rceil<n-1\). This proves the purity classification.

**Minimal feedback deletion.** Complementation is a bijection between maximal induced-forest sets and inclusion-minimal feedback vertex sets, reversing their sizes relative to the \(nm\) graph vertices. This gives the reciprocal polynomial.

## Verification

Run the accompanying standalone `verify.py` with Python 3. Its independent graph-level cycle detector enumerates all vertex subsets in eight profiles, checks facet maximality by explicitly adding every omitted vertex, and compares both polynomials with the cyclic-word description. A separate gap-composition enumerator checks the exact coefficient formula across 24 additional parameter pairs, and small lengths check the sharp cardinality bounds and purity exceptions. The documented run returned:

```text
GRAPH_OK 4 2 sets 79 facets 34 facet_sizes [3, 4]
GRAPH_OK 5 2 sets 261 facets 105 facet_sizes [4]
GRAPH_OK 6 2 sets 850 facets 245 facet_sizes [4, 5, 6]
GRAPH_OK 7 2 sets 2717 facets 595 facet_sizes [6]
GRAPH_OK 8 2 sets 8607 facets 1386 facet_sizes [6, 7, 8]
GRAPH_OK 4 3 sets 241 facets 126 facet_sizes [3, 4]
GRAPH_OK 5 3 sets 1066 facets 585 facet_sizes [4]
GRAPH_OK 4 4 sets 561 facets 328 facet_sizes [3, 4]
VERIFY_OK direct_graph_profiles 8 candidate_masks 189696 facets 3404 cyclic_counts_and_purity=PASS
GAP_FORMULA_OK profiles 24
```

Finite checks corroborate the result but do not substitute for the general combinatorial proof.

## Relationship to prior work

Jafarpour-Golzari introduced well-\(f\)-covered graphs, in which all maximal induced forests have equal order [1], and studied necessary conditions for this property in lexicographic graph products [2]. In particular, Theorem 3.5 of [2] imposes conditions on the two factors, but does not provide a sufficient condition for nonempty lexicographic products or the complete facet-counting polynomial. The theorem here gives an exact all-parameter classification and all facet coefficients for the cycle–clique subclass; it is not claimed as a characterization for all lexicographic products. Gunderson et al. [3] study maximum induced forests of distance-regular graphs, rather than the maximal-family polynomial in this cycle–clique product. Dyer and Müller [4] study thick-graph recognition and counting independent sets and colorings, a different counting problem. The degree-two cyclic transfer is a new specialization developed here; standard symbolic transfer-matrix methodology is not claimed as new.

## Limitations

The theorem concerns labelled undirected cycles with \(n\ge4\) and uniform clique size \(m\ge2\). It does not classify general lexicographic products, nonuniform clique sizes, or the homotopy type of the induced-forest complex. The extreme-cardinality formulas do not assert every intermediate cardinality occurs. The full text of [1] could not be inspected through the available public access routes; only its verified abstract was checked, leaving a residual equivalence-priority risk. Searches and comparisons cannot prove absolute publication novelty, and independent mathematical review has not occurred.

## References

[1] R. Jafarpour-Golzari, *Graphs whose all maximal induced forests are of the same order*, arXiv:2105.14339, first public 2021-05-29. https://arxiv.org/abs/2105.14339

[2] R. Jafarpour-Golzari, *On well-f-coveredness of lexicographic products of graphs*, arXiv:2108.09146, first public 2021-08-20. https://arxiv.org/abs/2108.09146

[3] K. Gunderson, K. Meagher, J. Morris, and V. R. T. Pantangi, *Induced forests in some distance-regular graphs*, arXiv:2301.05207, first public 2023-01-12. https://arxiv.org/abs/2301.05207

[4] M. Dyer and H. Müller, *Thick Forests*, arXiv:2309.01482, first public 2023-09-04. https://arxiv.org/abs/2309.01482
