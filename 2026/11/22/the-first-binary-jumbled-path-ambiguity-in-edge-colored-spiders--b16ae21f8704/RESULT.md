# The first binary jumbled-path ambiguity in edge-colored spiders

## Finding

Let \(T\) be an unrooted spider: a tree with exactly one vertex of degree at least three; all other vertices have degree at most two. Assign one of two *named* symbols \(0,1\) to every edge. The observation \(\mathcal P(T)\) is the multiset of binary Parikh vectors of all nonempty undirected simple paths, counting each unordered pair of distinct endpoints exactly once. The unlabeled arm lengths are supplied to the decoder; two edge colorings count as equivalent only if an automorphism of that fixed tree carries one to the other **without interchanging the two symbol names**.

**Sharp finite threshold.** For every spider with \(3\le m\le8\) edges, equality of the observations of two edge colorings implies their equivalence. For \(m=9\), ambiguity occurs **only** for the three-armed spider with arm lengths \((2,3,4)\). Its \(512\) colorings have \(510\) distinct path-composition observations: \(508\) singleton fibers and exactly two doubleton fibers. The two pairs, with each arm read from the degree-three vertex outwards, are

\[
\{(01,101,0010),(10,001,0101)\},\qquad
\{(01,110,1010),(10,010,1101)\}.
\]

The second pair is the image of the first under the global interchange \(0\leftrightarrow1\). Among **all** \(25\) unlabeled spider topologies with nine edges, there are \(5788\) colorings up to tree automorphism and \(5786\) observations when the topology is retained as part of the readout. These are sums of per-topology counts; they are **not** a count of mutually distinct profiles when topology is forgotten.

## Assumptions and scope

Every arm length is a positive integer, the spider has at least three arms, and the number of edges is between three and nine inclusive. The central vertex is the unique vertex of degree at least three. A coloring can be represented by its list of binary arm words, with arm words read outward from the center. Arms of a common length can be permuted, but cannot be reversed and color symbols are fixed. A path with \(\ell\) edges and \(s\) edges colored \(1\) contributes the Parikh vector \((\ell-s,s)\), represented computationally by \((\ell,s)\). The empty path is excluded. A tree on \(m+1\) vertices has \(\binom{m+1}{2}\) such paths.

## Proof

**1. Exhaustive indexing of the finite domain.** For fixed edge count \(m\), enumerate every integer partition \(m=\ell_1+\cdots+\ell_k\), with \(3\le k\le m\) and \(1\le\ell_1\le\cdots\le\ell_k\). This is a bijection onto the uncolored spider topologies with \(m\) edges. For a part of length \(d\) occurring \(r\) times, an arm word has \(2^d\) possibilities and a coloring up to permutations of these equal-length arms is a multiset of \(r\) such words. There are precisely

\[
\prod_{d\,\mathrm{distinct}}\binom{2^d+r_d-1}{r_d}
\]

such colorings, where \(r_d\) denotes the multiplicity of arm length \(d\). The supplied program enumerates them by lexicographically sorting the arm words first by length, then lexicographically. It independently checks the number found against this product, so no automorphism orbit is omitted or repeated.

**2. Exact observation formula.** For arm words \(a_i\), let \(I_i\) count the Parikh vectors of all its contiguous nonempty subwords and let \(R_i\) count the Parikh vectors of its nonempty prefixes (center-to-vertex segments). All simple paths either lie entirely in an arm or concatenate a nonempty prefix in each of two different arms. Therefore, identifying a multiset with its formal two-variable generating polynomial,

\[
P_{(a_i)}=\sum_i I_i+\sum_{i<j}R_iR_j.
\]

This decomposition is exact and disjoint: every nonempty path belongs to exactly one of these categories. In the program `via_segments` evaluates this formula using integer counters. Independently, `via_vertex_pairs` constructs the actual edge-colored tree and traverses the unique path between every unordered pair of distinct vertices; the two computations are asserted equal for **every** canonical coloring tested. This protects against an incorrect path decomposition or endpoint convention.

**3. Complete count.** The following rows are exact exhaustive results. For each edge count, columns give the number of spider shapes, edge-coloring isomorphism classes, topology-scoped path-observation classes, and non-singleton fibers:

| Edges | Shapes | Coloring classes | Observation classes | Non-singleton fibers |
|---:|---:|---:|---:|---:|
| 3 | 1 | 4 | 4 | 0 |
| 4 | 2 | 17 | 17 | 0 |
| 5 | 4 | 66 | 66 | 0 |
| 6 | 7 | 221 | 221 | 0 |
| 7 | 11 | 688 | 688 | 0 |
| 8 | 17 | 2034 | 2034 | 0 |
| 9 | 25 | 5788 | 5786 | 2 |

At nine edges the checker finds only the length partition \((2,3,4)\) with a non-singleton fiber. Since its lengths are pairwise different, each of its \(2^9=512\) binary colorings is a distinct labeled-tree isomorphism class. Its observation classes consist of \(508\) singletons and the two displayed doubletons, both of size exactly two. The code compares the set of *all* exceptional pairs with the displayed pairs, not merely their number, and checks that global color-complementation exchanges the two pairs.

**4. Direct witness.** For \((01,101,0010)\) and \((10,001,0101)\), the common path profile \((\ell,s)\mapsto\text{multiplicity}\) is exactly

`(1,0):5, (1,1):4, (2,0):2, (2,1):7, (3,0):1, (3,1):6, (3,2):2, (4,1):4, (4,2):4, (5,1):1, (5,2):4, (5,3):1, (6,2):2, (6,3):1, (7,3):1`.

The entries sum to \(45=\binom{10}{2}\). Because the three arm lengths differ and the arm words differ, the two colored spiders are not isomorphic. The complementary pair has the same property.

Steps 1–3 are a **finite computer-assisted exhaustive proof** of the stated cutoff; no extrapolation to ten or more edges is used.

## Verification

Run `python3 spider_verify.py` in an ordinary Python 3 installation (standard library only). The program regenerates every integer partition and every binary arm-word multiset, checks the Burnside/multiset orbit count separately for every shape, computes every path profile using both the arm-decomposition formula and independent generic graph traversal, checks the entire seven-row count table, compares the precise exceptional-pair set, and checks complementation. It terminates with the `VERIFY_OK` line only if all assertions pass. The exact verifier distributed in this package was executed successfully.

## Relationship to prior work

Bartha, Burcsi and Lipták (CPM 2016) introduce edge-labeled tree path-Parikh reconstruction and give a general path polynomial recurrence, as well as broader nonreconstructibility examples. These definitions and the polynomial technique are antecedents, **not** new here. Their reported three-way ambiguity example uses five two-edge arms and an alphabet of more than two labels; it does not supply this binary fixed-topology sharp first threshold or its two fibers. Bartha's 2021 thesis, §3.3.3, Table 3.5, tabulates the *aggregate* equivalence-class counts for all binary edge-labeled trees up to twelve vertices, including ten vertices. That stronger aggregate census is explicitly recognized; the present result refines a **specific natural topology class** into an exact first-failure classification, not a new global tree census. Dailly and Lehtilä (2026) study primarily **vertex-labeled connected-subgraph** composition queries rather than the binary edge-labeled path readout used here. Neither variant logically provides the claimed spider-local fibers.

## Limitations

The claim concerns only known-topology spiders with at most nine edges, two fixed named edge symbols, full multiplicity of all nonempty simple-path Parikh vectors, and exact/noiseless reads. It does not establish reconstructibility for larger spiders, topology-blind uniqueness, weighted sums alone, maximal paths alone, arbitrary subtrees, or vertex-colored trees. The external literature review cannot exclude unpublished or unindexed earlier exhaustive tables; the 2021 global census is the most important priority qualification. The theorem is a fully checkable finite classification, not an infinite theorem or an independent certification.

## References

1. D. Bartha, P. Burcsi and Z. Lipták, *Reconstruction of Trees from Jumbled and Weighted Subtrees*, CPM 2016, DOI [10.4230/LIPIcs.CPM.2016.10](https://doi.org/10.4230/LIPIcs.CPM.2016.10); OA full text https://drops.dagstuhl.de/storage/00lipics/lipics-vol054-cpm2016/LIPIcs.CPM.2016.10/LIPIcs.CPM.2016.10.pdf (public date 2016-06-27).
2. D. Bartha, *Reconstructibility of Tree Graphs*, PhD thesis, Eötvös Loránd University (2021), DOI [10.15476/ELTE.2021.095](https://doi.org/10.15476/ELTE.2021.095); relevant §3.3.3 and Table 3.5.
3. A. Dailly and T. Lehtilä, *Reconstructing graphs with subgraph compositions*, *Discrete Applied Mathematics* 390 (2026), 198–219, DOI [10.1016/j.dam.2026.04.023](https://doi.org/10.1016/j.dam.2026.04.023); related but different labeling/readout model.
