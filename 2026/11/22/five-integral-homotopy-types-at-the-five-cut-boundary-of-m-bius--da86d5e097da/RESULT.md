# Five integral homotopy types at the five-cut boundary of Möbius ladders

## Finding
For the ordinary five-cut complexes of the Möbius ladder \(M_{2n}\), the **complete finite classification for \(4\le n\le8\)** is
\[
\begin{aligned}
\Delta_5(M_8)&\simeq S^1,\
\Delta_5(M_{10})&\simeq\bigvee^{41}S^4,\
\Delta_5(M_{12})&\simeq\bigvee^{216}S^6,\
\Delta_5(M_{14})&\simeq\bigvee^{582}S^8,\
\Delta_5(M_{16})&\simeq\bigvee^{1213}S^{10}.
\end{aligned}
\]
These are integral **homotopy equivalences**, not just Betti-number assertions. The eight-vertex Wagner graph is exceptional: its five-cut complex is a pure two-dimensional complex but is homotopy equivalent to a circle. At all four larger listed sizes the nonzero homology lies in the top simplicial dimension. No statement for larger sizes is asserted.

## Assumptions and scope
For an integer \(n\ge4\), define \(M_{2n}\) on \(V=\mathbb Z/(2n)\mathbb Z\) with edges between \(i\) and \(i\pm1\) and between \(i\) and \(i+n\), indices taken modulo \(2n\). For any finite graph \(G\), its **ordinary** \(5\)-cut complex \(\Delta_5(G)\) is the simplicial complex whose facets are exactly \(V(G)\setminus T\) for five-vertex subsets \(T\) for which the induced subgraph \(G[T]\) is disconnected. It must not be confused with the total five-cut complex, whose facets are the complements of independent five-sets.

The theorem covers the five integers \(n\in\{4,5,6,7,8\}\), and uses ordinary geometric realizations and integral homotopy. Each complex is pure of dimension \(2n-6\), even when its homotopy dimension is smaller. Its face complex includes the empty face in the standard way; discrete-Morse matchings below are on nonempty faces.

## Proof
The following exact, finite, reproducible combinatorial proof is implemented completely in `verify_cut5.py`. Every hypothesis about the resulting discrete Morse matching is checked on the **entire** corresponding face poset, rather than inferred from finite sampling or a homology rank alone.

**1. Graph construction and all facets.** For each of the five prescribed integers \(n\), represent every subset of \(\mathbb Z/(2n)\mathbb Z\) by a \(2n\)-bit integer. Generate the graph-adjacency masks directly from the three edge rules above. Exhaustively iterate all \(\binom{2n}{5}\) five-vertex subsets, using breadth-first connectivity in the induced graph to retain exactly those that are disconnected. For each such set \(T\), enumerate all subfaces of its complement \(V\setminus T\) by the decreasing-submask recurrence `s = (s-1) & facet`, adding the empty face. There are precisely \(8,152,672,1862,4208\) disconnected five-sets for \(n=4,5,6,7,8\), respectively. As an independent generation check, every one of the \(2^{2n}\) possible subsets \(\sigma\) is tested against the direct defining criterion that \(V\setminus\sigma\) contains a disconnected five-set. The two sets of faces agree identically.

**2. Deterministic complete face-poset matching.** Initially every nonempty simplex is unmatched. For each vertex \(v=0,\ldots,2n-1\) in order, inspect the still-unmatched lower simplices \(\sigma\) in ascending bitmask order and, when both \(\sigma\) and \(\sigma\cup\{v\}\) belong to the complex and are unmatched, pair them and mark both as unavailable. Every pair is an immediate codimension-one incidence and no simplex appears twice.

**3. Exhaustive acyclicity certificate.** Enumerate each Hasse cover relation \(\eta\supset\sigma\) obtained by deleting one vertex from a nonempty simplex \(\eta\). Orient it from \(\eta\) toward \(\sigma\), except that matching incidences point upward. Kahn's exact topological sort visits **every** nonempty face in each case, establishing that the orientation has no directed cycles. The inspected face, matching and incidence counts are:

| \(n\) | Nonempty simplices | Morse pairs | Oriented Hasse incidences | Remaining critical cells |
|---:|---:|---:|---:|---|
| 4 | 32 | 15 | 56 | one vertex and one one-cell |
| 5 | 522 | 240 | 1,990 | one vertex and 41 four-cells |
| 6 | 3,175 | 1,479 | 16,944 | one vertex and 216 six-cells |
| 7 | 14,765 | 7,091 | 98,056 | one vertex and 582 eight-cells |
| 8 | 62,850 | 30,818 | 491,376 | one vertex and 1,213 ten-cells |

Every numerical assertion in this table is recomputed by the provided program from the graph definition and matching rules, including complete directed-acyclicity checks. The matching contains **no other critical cells**.

**4. Integral homotopy conclusion.** By the discrete-Morse acyclic matching theorem, the realization has the homotopy type of a CW complex with exactly the critical cells listed. In each of the five cases there is a single zero-cell and only \(m\) cells in one strictly positive degree \(d\). Since all attaching maps have the point as their target at the stage where the \(d\)-cells are attached, the resulting CW space is the wedge \(\bigvee^m S^d\). This proves the claimed *integral* homotopy types; it requires no inference from field-valued homology.

**5. Separate boundary-rank check.** For each case, the program independently constructs each ordinary mod-two simplicial boundary matrix, computes its rank by binary Gaussian elimination, and confirms that the only nonzero reduced Betti number equals the critical sphere count in its claimed degree. Euler characteristics agree as well. The mod-two computation is a consistency check and is **not** treated as sufficient evidence for an integral homotopy theorem; the latter follows from the verified acyclic matching.

## Verification
Using Python 3 and the standard library only, execute `python3 verify_cut5.py` and compare its output byte-for-byte with `expected_output.txt`. It takes every graph and face from definitions; no cached certificate, random choice, external data file or network connection is needed. Its final line is `ALL FIVE EXACT MATCHING AND DAG CHECKS PASSED`. For the largest case it exhaustively checks \(65,536\) candidate vertex subsets, \(62,850\) nonempty faces, \(491,376\) Hasse incidences and the \(30,818\) matched pairs. The mod-two ranks are independently computed for all five cases. The exhaustive range is exactly those five prescribed graph sizes.

## Relationship to prior work
The foundational work of Bayer et al. [1] defines ordinary cut complexes and proves results for cycles, complete multipartite graphs, prisms over cliques and other families, but its family theorems do not state five-cut homotopy types for Möbius ladders. Agarwal and Basak [2] classify independence and perfect-matching complexes for Möbius ladders and explicitly pose their cut-complex topology as a further direction. Published work [3] already gives the **ordinary four-cut** classification for every \(n\ge5\), which is distinct from the five-cut family here: its missing-set cardinality, facets, simplicial dimension and homotopy ranks differ. Likewise [4] concerns ordinary three-cuts and [5] concerns **total four-cuts**, not ordinary five-cuts. The cited full-text and database comparisons did not identify an equivalent five-cut classification for these five parameter values, but unindexed or inaccessible work remains a priority uncertainty.

## Limitations
Only the finite range \(4\le n\le8\) and ordinary five-cut complexes are classified. No formula for all \(n\), homotopy classification for other cut parameters, symmetry action, shellability conclusion for the four larger cases, or independence from unpublished equivalent work is claimed. While the finite exhaustive checker is proof-complete on its stated inputs, this is not an externally independently audited result.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first available 2023-04-26), https://arxiv.org/abs/2304.13675.
2. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601 (first available **2026-08-31**; later title revision), https://arxiv.org/abs/2608.30601.
3. *Ordinary four-cut complexes of Möbius ladders form uniform sphere wedges*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-ordinary-four-cut-complexes-of-m-bius-ladders-form-uniform-spher--44c11dd77c6b.
4. *Ordinary three-cut complexes of Möbius ladders are sphere wedges*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-ordinary-three-cut-complexes-of-m-bius-ladders-are-sphere-wedges--74e8b58d248f.
5. *Four exact total-four-cut homotopy types of Möbius ladders*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-four-exact-total-four-cut-homotopy-types-of-m-bius-ladders--1b8923a23d15.
