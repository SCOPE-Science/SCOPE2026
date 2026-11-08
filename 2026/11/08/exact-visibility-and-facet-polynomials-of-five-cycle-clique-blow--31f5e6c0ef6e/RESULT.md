# Exact visibility and facet polynomials of five-cycle clique blowups

## Finding
For every integer \(m\ge 2\), let \(H_m=C_5\boxtimes K_m\), equivalently the lexicographic product \(C_5[K_m]\). Partition its vertices into five cyclically indexed cliques \(V_0,\ldots,V_4\), each of cardinality \(m\). Define an ordinary mutual-visibility set \(S\) to mean that every pair of its vertices admits a shortest path with all internal vertices outside \(S\). Write \(\mathcal V_m(z)=\sum_{S\text{ visible}}z^{|S|}\) and \(\mathcal M_m(z)=\sum_{S\text{ inclusion-maximal visible}}z^{|S|}\).

Put
\[
A=(1+z)^m-1-z^m,\quad B=z^m,\quad T=1+A.
\]
Then the exact cardinality polynomials are
\[
\boxed{\mathcal V_m(z)=T^5+5B(1+4A+5A^2+2A^3)+5B^2(2+4A+A^2)+5B^3},
\]
\[
\boxed{\mathcal M_m(z)=m^5z^{5m-5}+5m^2z^{4m-2}+5mz^{3m-1}+5z^{3m}}.
\]
Equivalently, exactly four cyclic types of inclusion-maximal sets occur (some cardinalities may coincide): the five nonempty-proper fibers; five rotations of two full, two proper, and one empty fiber; five rotations of two full, one proper, and two empty fibers; and five rotations of three full and two empty fibers. Each proper fiber of an inclusion-maximal set contains exactly \(m-1\) vertices. The complementary positions in the last three types are constrained as described in the proof.

All minimal nonfaces of the visibility complex are exactly the \(5m^2\) sets
\[
V_i\cup\{u,v\},\quad u\in V_{i-1},\quad v\in V_{i+1},\quad i\in\mathbb Z/5\mathbb Z.
\]
The visibility complex is nonpure for every \(m\ge2\). Its least facet cardinality is \(3m-1\); its largest facet cardinality is \(\max\{3m,4m-2,5m-5\}\). In particular, \(\mu(H_2)=6\), \(\mu(H_3)=10\), and \(\mu(H_m)=5m-5\) for \(m\ge4\).

## Assumptions and scope
Graphs are finite, simple, undirected. Indices on the five cliques are cyclic modulo five. In the strong product with \(K_m\), every \(V_i\) is a clique and every pair of consecutive fibers is completely joined; nonconsecutive fibers have no edges. The parameter \(m\) is any integer at least two; singleton fibers are deliberately outside the theorem. A visibility set may be empty, counted by the constant coefficient one. Inclusion-maximal refers to vertex-set containment, not only largest cardinality.

## Proof
**Visibility criterion.** Distinct vertices from the same fiber or consecutive fibers are adjacent and hence visible for every selected set. Suppose instead \(u\in V_{i-1}\) and \(v\in V_{i+1}\). Their graph distance is two, and their common-neighbor set is exactly \(V_i\): the base cycle has exactly one common neighbor for vertices at base distance two, and the complete fibers do not create extra two-edge routes. Therefore \(u,v\) are visible relative to \(S\) if and only if \(V_i\setminus S\ne\varnothing\). Thus \(S\) is visible precisely when, for every cyclic \(i\),
\[
V_i\subseteq S\ \Longrightarrow\ (S\cap V_{i-1}=\varnothing)\ \text{or}\ (S\cap V_{i+1}=\varnothing).\tag{1}
\]
The implication gives all minimal forbidden sets: the full middle fiber and one selected endpoint from each neighboring fiber. Every displayed forbidden set is inclusion-minimal because deleting any constituent destroys that complete obstruction; conversely any nonvisible set contains one. The five disjoint choices of middle fiber and \(m^2\) endpoint choices give \(5m^2\) distinct minimal nonfaces, since \(m\ge2\).

**All visible sets.** Encode each fiber by \(E\) (empty), \(P\) (nonempty proper), or \(F\) (full). Their weight polynomials are \(1,A,B\), respectively. Criterion (1) says precisely that every \(F\) in a cyclic word of length five has at least one neighboring \(E\). If the word has no \(F\), its total weight is \(T^5\). With exactly one \(F\), choose its position in five ways and require at least one of its two neighbors to be \(E\): the weight is \(5B(T^4-A^2T^2)=5B(1+4A+5A^2+2A^3)\). With exactly two \(F\)'s, the choices are five adjacent pairs and five nonadjacent pairs. For an adjacent pair the two exterior neighbors are \(E\) and the remaining position is \(E\) or \(P\), giving \(5B^2T\). For a nonadjacent pair, their shared neighbor is either \(E\), in which case both other positions are \(E\) or \(P\), or it is \(P\), in which case their two other neighboring positions must be \(E\); hence \(5B^2(T^2+A)\). These add to \(5B^2(2+4A+A^2)\). Exactly three full fibers are possible only in the five rotations of \(FFEFE\), contributing \(5B^3\). Four or five full fibers cannot satisfy (1). Summation yields \(\mathcal V_m\).

**Maximal sets.** The criterion is hereditary. If an included proper fiber contains at most \(m-2\) vertices, an additional vertex in that fiber changes neither its state nor (1), so such a set is not maximal. Hence every \(P\) in a facet has exactly \(m-1\) vertices. A \(P\) can be upgraded to \(F\) while preserving (1) if and only if at least one neighboring fiber is \(E\); consequently maximality requires both its neighbors to be nonempty. An \(E\) can be changed to \(P\) without violating (1) unless it is the *only* empty neighbor of an adjacent full fiber; thus maximality also requires each \(E\) to serve as the only empty neighbor of some adjacent \(F\).

These two local tests classify all maximal words. With no full fibers, any empty fiber can be augmented, leaving only \(PPPPP\). With exactly one full fiber there can be no maximal word: an empty site not adjoining that full fiber is augmentable unless occupied, but occupying all such sites creates a proper fiber adjacent to an empty neighbor and hence upgradable. With exactly two full fibers, adjacent full fibers cannot produce a maximal word: their exterior neighbors must be empty, and their remaining site is either an augmentable empty site or an upgradable proper site. Therefore the full fibers are nonadjacent, say at indices \(0,2\). Their common neighbor (index \(1\)) is either empty, forcing indices \(3,4\) to be proper and yielding the rotations of \(FEFPP\); or proper, forcing indices \(3,4\) empty and yielding rotations of \(FPFEE\). A third full fiber cannot occupy index \(1\), since then it would have two full neighbors. With three full fibers all other fibers must be empty, and admissibility forces the rotations of \(FFEFE\). There can be no four or five full fibers. Every word listed passes the two augmentation tests, and so is maximal.

There is one \(PPPPP\) word, carrying \(m^5\) labelled choices of a missing vertex and size \(5(m-1)\). The type \(FEFPP\) has five cyclic rotations, each with \(m^2\) choices and size \(2m+2(m-1)\). The type \(FPFEE\) has five rotations, each with \(m\) choices and size \(2m+(m-1)\). The type \(FFEFE\) has five rotations, each with one choice and size \(3m\). Their enumerator is \(\mathcal M_m\) as stated. Every displayed type exists for all \(m\ge2\) and two of their sizes are \(3m-1\) and \(3m\), so the complex is never pure. The extremal size formula follows directly; checking \(m=2,3\) gives \(6,10\), while \(5m-5\) dominates the other terms when \(m\ge4\). \(\square\)

## Verification
The standalone file `verify_c5.py` constructs the simple graph by adjacency, derives each nonedge's common neighbors, and directly checks mutual visibility for all \(2^{5m}\) subsets at \(m=2,3\). It compares each coefficient with the formulas, checks inclusion-maximal subsets directly by one-vertex extensions, and enumerates all minimal nonfaces by deleting each member. It examined \(33{,}792\) subsets and identified \(375\) inclusion-maximal sets, with all comparisons passing. Separate symbolic arithmetic sanity checks run for \(2\le m\le29\). These are finite tests and do not establish the unrestricted theorem, which is proved above.

To reproduce, run `python3 verify_c5.py` in the directory containing this manuscript and the verifier. It uses only Python standard-library modules.

## Relationship to prior work
Di Stefano introduced mutual visibility in graphs (arXiv:2105.02722, 2021). Cicerone, Di Stefano, Klavžar, and Yero analyzed mutual-visibility numbers of strong products and strong grids (arXiv:2210.07835, first public October 14, 2022). This work addresses their natural graph-product setting but counts all visible and inclusion-maximal configurations for a different diameter-two family. The preprint on diameter-two visibility problems (arXiv:2401.02373) treats scalar parameters, products of complete graphs, cographs and selected other graph classes, rather than the complete cardinality distributions of these true-twin five-cycle expansions. Bujtás, Klavžar, and Tian introduced general visibility polynomials (DOI:10.1007/s00010-025-01197-y), including balanced complete bipartite examples and a general inclusion-exclusion relation between all sets and maximal sets. That general relation does not enumerate the maximal sets of \(C_5[K_m]\). The former classification of arbitrary clique-expanded trees is a different family: the base \(C_5\) is not a tree and has no leaf fibers. These are implication comparisons, not an assertion of exhaustive publication priority.

## Limitations
The theorem concerns five base-cycle fibers of equal cardinality \(m\ge2\), and ordinary (not total, outer or dual) mutual visibility. It does not classify unequal fiber sizes or longer base cycles, nor determine the homotopy type of the complex. While primary-source and research-record searches did not locate a covering statement, an unindexed equivalent formula or deduction from broader machinery remains possible. The result has undergone mathematical review in this package, but has not received independent mathematical audit. The finite verifier alone cannot establish the infinite-parameter claim.

## References
1. G. Di Stefano, *Mutual visibility in graphs*, arXiv:2105.02722 (2021); https://arxiv.org/abs/2105.02722.
2. S. Cicerone, G. Di Stefano, S. Klavžar, I. G. Yero, *Mutual-visibility in strong products of graphs via total mutual-visibility*, arXiv:2210.07835 (first public October 14, 2022); https://arxiv.org/abs/2210.07835.
3. S. Cicerone, G. Di Stefano, S. Klavžar, I. G. Yero, *Mutual-visibility problems on graphs of diameter two*, arXiv:2401.02373 (2024); https://arxiv.org/abs/2401.02373.
4. C. Bujtás, S. Klavžar, J. Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, Aequationes Math. 99 (2025), 1883–1901; https://doi.org/10.1007/s00010-025-01197-y.
5. D. Kuziak, J. A. Rodríguez-Velázquez, *Total mutual-visibility in graphs with emphasis on lexicographic and Cartesian products*, Bull. Malays. Math. Sci. Soc. 46 (2023), article 197; arXiv:2306.15818.
