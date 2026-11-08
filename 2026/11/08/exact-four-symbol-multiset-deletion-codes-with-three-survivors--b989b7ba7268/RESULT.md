# Exact four-symbol multiset deletion codes with three survivors

## Finding

Let \(\mathcal S_{n,4}=\{(x_0,x_1,x_2,x_3)\in\mathbb Z_{\geq 0}^4:\sum_{i=0}^3x_i=n\}\). For every integer \(n\geq 3\), let \(S_4(n,n-3)\) denote the maximum cardinality of a subset of \(\mathcal S_{n,4}\) from which an unknown source can be uniquely recovered after exactly \(n-3\) multiset deletions. Then

\[
S_4(n,n-3)=\begin{cases}
20,&n=3,\\
11,&n=4,\\
6,&n=5,\\
5,&6\leq n\leq 8,\\
4,&n\geq 9.
\end{cases}
\]

Thus the first blocklength at which only the four single-symbol constant multisets can achieve the optimal *cardinality* is not asserted; rather, the optimal cardinality first stabilizes at four when \(n=9\). There may be nonconstant members in other optimum codes.

## Assumptions and scope

The alphabet consists of four distinct symbols, order is discarded, the source is a multiset of precisely \(n\) symbols, and the adversary deletes exactly \(n-3\) symbols. An observation is an arbitrary three-symbol submultiset. Distinct codewords \(x,y\) have disjoint observation sets exactly when

\[
\Omega(x,y):=\sum_{i=0}^{3}\min(x_i,y_i)\leq2.
\]

Indeed the greatest size of a common submultiset is \(\Omega(x,y)\), and a common three-symbol output exists if and only if \(\Omega(x,y)\geq3\). With fixed source cardinality, the same separation condition corrects any **at-most** \(n-3\) deletions: every received output then contains at least three symbols, so a common output would itself contain a common three-symbol submultiset.

## Proof

**Lower bounds, all lengths.** The four pure vectors \(ne_i\), for \(0\leq i\leq3\), are pairwise disjoint. For \(n=3\), every vector in \(\mathcal S_{3,4}\) is compatible with every other distinct vector, because two distinct size-three multisets cannot have an intersection of size three. There are \(\binom{6}{3}=20\) such vectors. At \(n=4\), take the four pure vectors, the six permutations of \((2,2,0,0)\), and \((1,1,1,1)\). Their pairwise intersections have size at most two, yielding eleven vectors. At \(n=5\), add \((0,2,2,1)\) and \((2,0,1,2)\) to the four pure vectors. These two additional vectors have intersection size two, and each overlaps any pure vector in at most two places, giving six. For each \(n\in\{6,7,8\}\), add \((2,2,2,n-6)\) to the four pure vectors. Every coordinate of the fifth vector is at most two, so all five are compatible.

**Infinite upper bound.** For \(n\geq9\), every member of \(\mathcal S_{n,4}\) has at least one coordinate of size three or greater: otherwise its total would be at most eight. Two compatible vectors cannot both have any fixed coordinate three or greater, as their intersection would already contain three copies of that symbol. Therefore the nonempty sets \(H(x)=\{i:x_i\geq3\}\) associated with distinct codewords are pairwise disjoint subsets of a four-element set. Hence any code has at most four codewords. The four pure vectors attain this bound.

**Finite upper bounds at \(4\leq n\leq8\).** For each such \(n\), enumerate the \(\binom{n+3}{3}\) nonnegative four-compositions of \(n\) in lexicographic order. Form a simple graph with an edge between vectors \(x,y\) precisely when \(\Omega(x,y)\leq2\). Any feasible code of cardinality \(r\) corresponds exactly to a clique of size \(r\). The standalone `checker.py` implements an exhaustive integer-bitmask recursion searching for cliques with targets \(12,7,6,6,6\) at lengths \(4,5,6,7,8\), respectively; it proves that none exists. To see why this is exhaustive, at a recursive node all future vertices have greater indices than the chosen vertices and are adjacent to every chosen vertex. Taking the lowest remaining candidate and recursively intersecting with its neighborhood enumerates every increasing-index clique once; omitting it explores the complementary branch. The sole pruning rule eliminates a node only when fewer eligible vertices remain than are needed. Exact visit counts, respectively \(7056,13027,14895,16825,19450\), are emitted by replay. Thus the stated feasible witnesses attain the exact upper bounds.

The finite exhaustive part is a complete finite search *by a proved exhaustive algorithm*, not an extrapolation from small instances; the infinite tail has the independent combinatorial argument above.

## Verification

Run `python3 checker.py` with Python 3.10 or later; no external packages or downloads are required. The script checks the number of compositions, all pairwise intersections of explicit witnesses, and disjointness of their three-symbol descendant sets through a second direct generation routine. It then exhaustively rules out the next-higher clique sizes for all finite exceptional lengths, printing the visit counts in the proof. Its final output is `PASS: all finite exhaustive upper bounds and witnesses verified`.

The checker additionally enumerates the pigeonhole property for \(n=9,10,11,12\); the proof for all \(n\geq9\) does not depend on that sample. The finite clique proof depends on correctly executing the provided integer enumeration on the explicitly defined graph; the independent witness test checks the graph's interpretation against deletion outputs.

## Relationship to prior work

Kreindel, Essayag and Zabokritskiy (2026, arXiv:2601.05636v1, §3.5, Theorem 9) explicitly study the three-survivor regime \(t=n-3\), derive the common-intersection criterion, and give an upper bound \(M\leq q^2(n-2)/(n-1-q)\) for \(n\geq q+2\). This is in general much weaker than the exact quaternary optimum determined here. Their §3.6 gives a general puncturing upper bound \(S_q(n,n-3)\leq q^3\). Their later paper arXiv:2603.18322v1 develops multiset-ball enumerators and general code bounds rather than this fixed quaternary profile. Kovačević and Tan (2016, arXiv:1612.08837, §§II and IV) develop the simplex metric, lattice/Sidon constructions, and general bounds, which do not imply the five-piece exact profile.

The published finding *Exact ternary multiset deletion codes when three multiset elements survive* gives an analogous three-letter result and a related large-length heavy-coordinate argument. That ternary conclusion does not yield the exceptional quaternary maxima, nor the location of the quaternary stabilization threshold. In particular, the finite upper-bound certificates and witnesses at \(n=4,5,6,7,8\) address genuinely different finite graphs. The extension of the large-length heavy-coordinate argument alone is not presented as the original mathematical core.

## Limitations

Only the four-symbol alphabet and outputs of size three are classified. This does not classify all maximum codes up to symbol relabeling, determine other alphabet sizes, or give formulas for outputs of different cardinalities. The five exceptional finite upper bounds rely on a complete, reproducible enumeration rather than a short human-only inequality proof. Historical priority has been checked against cited accessible papers and related indexed findings, but an older unindexed exact table or implicit consequence of a stronger classification remains possible. No independent mathematical audit has been conducted.

## References

1. A. Kreindel, I. B. Essayag and A. L. Zabokritskiy, *Multiset Deletion-Correcting Codes: Bounds and Constructions*, arXiv:2601.05636v1 (first posted 2026-01-09), https://arxiv.org/html/2601.05636v1 .
2. A. Kreindel, I. B. Essayag and A. L. Zabokritskiy, *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322v1 (first posted 2026-03-18), https://arxiv.org/html/2603.18322v1 .
3. M. Kovačević and V. Y. F. Tan, *Codes in the Space of Multisets—Coding for Permutation Channels with Impairments*, arXiv:1612.08837 (2016), https://arxiv.org/abs/1612.08837 .
4. *Exact ternary multiset deletion codes when three multiset elements survive*, indexed published finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-ternary-multiset-deletion-codes-when-three-multiset-elemen--d3a62a71c505 (indexed description checked; complete underlying text not retrieved).
