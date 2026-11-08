# The first nonrefinable connected proper interval graph

## Finding

A finite simple graph is **refinable** if the stable partition obtained by ordinary uncolored one-dimensional Weisfeiler–Leman color refinement coincides with its automorphism-orbit partition. A **proper interval graph** is the intersection graph of a finite family of intervals, none properly containing another; equivalently, it is a unit interval graph.

**Theorem.** Every connected proper interval graph on at most seven vertices is refinable. Among the **232** isomorphism types of connected proper interval graphs on eight vertices, **exactly one** is nonrefinable. The exception consists of two vertex-disjoint triangles joined by a path of three edges between one designated vertex of each triangle.

A further finite-order distinction holds: for every order at most eight, **joint** one-dimensional color refinement distinguishes all nonisomorphic connected proper interval graphs of that order from one another. Hence the eight-vertex failure concerns vertex-orbit recovery, not graph identification *within this class* at these orders.

## Assumptions and scope

The graphs are finite, simple, undirected, uncolored, nonempty and connected. The quantifier ranges over all connected proper interval graphs of orders one through eight. Refinement starts from one uniform vertex color and iteratively replaces a color by the pair consisting of its current color and the multiset of its neighbors' colors. Comparisons of two graphs use a **common** refinement palette on their disjoint union. Two vertices lie in the same automorphism orbit if some adjacency-preserving permutation sends one to the other. The theorem does not assert relative graph identification or refinability for arbitrary larger orders.

Write the vertices of the exceptional graph as \(0,1,\ldots,7\). Its edge set is the union of the two triangles on \(\{0,1,2\}\) and \(\{5,6,7\}\), and the connecting edges \(\{2,3\},\{3,4\},\{4,5\}\). Its proper interval ordering has the rightmost adjacent-or-self index sequence

\[
(2,2,3,4,5,7,7,7).
\]

## Proof

**1. Exhaustive parametrization.** A connected proper interval graph has a straight ordering \(0,\ldots,n-1\) in which, for each vertex \(i\), its neighbors to its right are exactly the vertices \(i+1,\ldots,r_i\). The sequence \(r_0,\ldots,r_{n-1}\) is nondecreasing, satisfies \(r_i\geq i+1\) for \(i<n-1\) (connectedness), and has \(r_{n-1}=n-1\). Conversely, each such sequence defines a connected proper interval graph. This follows from the proper-interval/Dyck-path representation in Saitoh–Yamanaka–Kiyomi–Uehara, especially their Observation 1 and Lemma 1. The same lemma states uniqueness of the representation up to reversal; thus two such sequences encode isomorphic graphs precisely when one is the reflection of the other. The verifier builds both mirrored adjacency rows and recomputes their right endpoints before choosing the lexicographically smaller representative.

For completeness, the counts of straight-order sequences for orders one through eight are \(1,1,2,5,14,42,132,429\). After reflection they become \(1,1,2,4,10,26,76,232\), agreeing with the published Catalan/binomial enumeration:

\[
N_n=\frac12\left(C_{n-1}+\binom{n-1}{\lfloor(n-1)/2\rfloor}\right)
\quad(n\geq2),
\]

where \(C_k=\frac1{k+1}\binom{2k}{k}\). The case \(n=1\) has a single graph.

**2. Exact partition checks.** For each resulting graph the verifier performs ordinary color refinement using exact tuples and integer multisets. Independently, it enumerates **every** adjacency-preserving permutation, by a backtracking bijection search restricted only by the necessary degree equality and previously assigned adjacency relations. It unites each mapped pair to obtain the true automorphism orbits. Thus no approximate isomorphism routine, random sampling, or guessed orbit formula is used. The program tests equality of these two partitions for each of the \(352\) isomorphism types of orders at most eight. Its result is zero nonrefinable graphs for each of the first seven orders, and exactly one at order eight.

For each fixed order, the verifier also refines every isomorphism representative in a shared palette, then counts the distinct stable global color histograms. Those counts equal the number of isomorphism types at every order through eight, proving the relative identification assertion.

**3. Direct check of the unique obstruction.** In the displayed eight-vertex graph, the two bridge endpoints \(2,5\) have degree three; the six other vertices have degree two. Every degree-three vertex has exactly three degree-two neighbors and no degree-three neighbor. Every degree-two vertex has one degree-two and one degree-three neighbor. Therefore the degree partition of sizes \(2\) and \(6\) is equitable. Color refinement separates these two degree classes after one round and never splits them further.

But the two internal path vertices \(3,4\) lie in no triangle, whereas the four triangle-wing vertices \(0,1,6,7\) each lie in a triangle. Triangle containment is invariant under automorphisms, so these vertices cannot belong to one orbit. In fact the automorphism orbits are \(\{2,5\}\), \(\{3,4\}\), and \(\{0,1,6,7\}\): reflection exchanges ends, and each pair of triangle wings may be interchanged. Thus the stable coloring has two cells, while the true orbit partition has three.

Combining the complete census with the explicit obstruction proves all assertions. The exhaustive finite cutoff is the entire asserted classification; no larger-order inference is made.

## Verification

Run `python3 verify.py` with Python 3.8 or newer. The program uses only the Python standard library and prints the count table and `VERIFY_OK`. Its algorithm checks the exact set of monotone right endpoints, reversal/canonicalization, all color classes, all adjacency-preserving automorphisms and, separately, simultaneous-refinement signatures across the graph types at each order. A recorded run is provided in `output.txt`; correctness relies on the executable and the proof of exhaustion, not on the log alone.

At order eight the implementation generates \(429\) straight representations and \(232\) reflected isomorphism representatives. Exactly one graph fails orbit-color equality, and joint color refinement yields \(232\) distinct signatures. The exceptional adjacency bit masks are provided by the program to facilitate a second implementation.

## Relationship to prior work

Saitoh, Yamanaka, Kiyomi and Uehara (2010) prove the canonical string representation and enumeration of connected proper interval graphs; their result supplies the rigorous enumeration framework and the known \(232\) graph count, **not** a classification by refinability. Arvind, Köbler, Rattan and Verbitsky (2015) define *refinable* graphs and establish general relationships with amenability, compactness and color refinement; the relevant inspected text does not classify proper interval graphs by their orbit-color agreement, or provide the first failure order. Their equivalence between color refinement and two-variable counting logic explains the logical motivation.

The new assertion is the exact first threshold, unique forbidden example at that threshold, and its contrast with complete relative identification through eight vertices. These comparisons are restricted to accessible, inspected literature; a universal historical-priority guarantee is not asserted.

## Limitations

The result does not characterize all nonrefinable connected proper interval graphs at greater orders, nor assert that all proper interval graphs are distinguishable from arbitrary graphs by one-dimensional refinement. The verifier's finite search is exhaustive only through order eight. The two principal published sources concern a stronger general framework and enumeration, respectively; unindexed or inaccessible prior work could contain the exact threshold. Independent mathematical review has not been performed.

## References

1. T. Saitoh, K. Yamanaka, M. Kiyomi, R. Uehara, “Random Generation and Enumeration of Proper Interval Graphs,” *IEICE Transactions on Information and Systems* E93-D(7), 1816–1823 (2010), DOI: 10.1587/transinf.E93.D.1816. Publicly available 2010-07-01. https://www.jstage.jst.go.jp/article/transinf/E93.D/7/E93.D_7_1816/_pdf/-char/en
2. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, “Graph Isomorphism, Color Refinement, and Compactness,” arXiv:1502.01255, first posted 2015-02-04; relevant definitions in Section 8, especially the refinability hierarchy. https://arxiv.org/abs/1502.01255
