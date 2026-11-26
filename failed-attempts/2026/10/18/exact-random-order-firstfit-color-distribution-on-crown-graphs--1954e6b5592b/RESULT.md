# Exact random-order FirstFit color distribution on crown graphs

## Finding

For every integer \(n\ge 3\), let \(G_n\) be the crown graph with disjoint vertex sets \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), in which \(a_i\) is adjacent to \(b_j\) exactly when \(i\ne j\). Present its \(2n\) vertices in a uniformly random permutation, assign each arriving vertex the least positive integer color absent from its previously colored neighbors (FirstFit), and write \(C_n\) for the total number of used colors.

**Theorem (entire law).** For \(3\le k\le n\), write
\[
T_{n,k}=\frac{1}{n-k+3}\prod_{r=n-k+4}^{n}\frac{3}{2(2r-1)},
\]
with an empty product equal to \(1\). Then
\[
\Pr(C_n\ge k)=T_{n,k}.
\]
In addition, \(\Pr(C_n=2)=1-1/n\), \(\Pr(C_n=k)=T_{n,k}-T_{n,k+1}\) for \(3\le k<n\), and \(\Pr(C_n=n)=T_{n,n}\). No other values occur. In particular,
\[
\Pr(C_n=n)=\frac{40\,3^{n-3}\,n!}{(2n)!},
\qquad
\mathbb E[C_n]=2+\sum_{k=3}^{n}T_{n,k}
=2+\frac1n+\frac{3}{4n^2}+O(n^{-3}).
\]
The exact expectation therefore tends to \(2\), not merely to a constant bounded above by \(2.5\).

## Assumptions and scope

All graphs are finite, simple and labeled as above. Every vertex permutation is equally likely; edges are fixed. The coloring is the online FirstFit rule, not a random proper coloring, an adversarial-order Grundy maximum, or a random greedy independent-set process. The formula holds for every integer \(n\ge3\). At the disconnected boundary \(n=2\), the graph is two disjoint edges and \(C_2=2\) deterministically; \(n=1\) is not part of the theorem. The parameter \(k\) is an integer in the explicitly stated range, and all probabilities are over the permutation alone. The remainder term in the expectation is as \(n\to\infty\) along integers.

## Proof

By the automorphism interchanging the two bipartition classes, condition on the first vertex being \(a_i\). Among the remaining \(2n-1\) vertices, either a vertex \(a_j\), \(j\ne i\), precedes \(b_i\), or \(b_i\) precedes all those \(a_j\).

In the first event, \(a_i\) and the first such \(a_j\) both receive color \(1\): before \(b_i\), no vertex of \(B\) can receive color \(1\), since every \(b_h\) with \(h\ne i\) is adjacent to \(a_i\). Once two distinct vertices of \(A\) have color \(1\), no vertex of \(B\) can use it. Every vertex of \(B\) gets color \(2\), and every vertex of \(A\) gets color \(1\), regardless of subsequent arrival order. The final color count is exactly \(2\).

In the second event, \(b_i\) receives color \(1\) and closes this color forever, because every remaining vertex is adjacent to at least one of \(a_i,b_i\). Let \(r\) be the number of vertices of \(B\setminus\{b_i\}\) arriving between \(a_i\) and \(b_i\). All of these get color \(2\). If \(r\ge2\), the color-\(2\) class contains distinct vertices of \(B\); every remaining vertex of \(A\) is adjacent to at least one of them and must use color \(3\), while all vertices of \(B\) use color \(2\). The final count is exactly \(3\).

If \(r=0\) or \(r=1\), deleting the closed matched pair \(a_i,b_i\) leaves \(G_{n-1}\). The remaining arrival order is uniform: in the case \(r=0\) no remaining vertex has arrived; in the case \(r=1\) the single previously arrived vertex of \(B\) is the first vertex of this induced order, and its identity is exchangeable among the \(n-1\) pairs, with a uniform order on the others. Color \(1\) is unavailable to every remaining vertex; after subtracting one from their colors, their FirstFit dynamics are exactly those on a uniformly randomly ordered \(G_{n-1}\). Consequently, the conditional law is \(1+C_{n-1}\), where \(C_{n-1}\) denotes a fresh variable with that law. This reduction is valid regardless of whether the interposed vertex is present; crucially, no other vertex of the remaining graph can have appeared in either case.

The event that \(b_i\) precedes all \(n-1\) other vertices of \(A\) has probability \(1/n\). For \(r=0\), \(b_i\) is the next vertex, giving probability \(1/(2n-1)\). For \(r=1\), the next vertex is any of the \(n-1\) other vertices of \(B\) and the following vertex is \(b_i\), giving probability
\[
\frac{n-1}{(2n-1)(2n-2)}=\frac{1}{2(2n-1)}.
\]
Thus, with \(q_n=3/[2(2n-1)]\), the three mutually exclusive cases have probabilities \(1-1/n\) (color count \(2\)), \(1/n-q_n=(n-2)/[2n(2n-1)]\) (color count \(3\)), and \(q_n\) (law \(1+C_{n-1}\)). For \(n=3\), the law of \(C_2\) is concentrated at \(2\), hence \(\Pr(C_3\ge3)=1/3\). For all \(n\ge3\), the paired-color event yields at least \(3\) colors because \(G_{n-1}\) has an edge when \(n-1\ge2\). Hence
\[
\Pr(C_n\ge3)=\frac1n,
\qquad
\Pr(C_n\ge k)=q_n\Pr(C_{n-1}\ge k-1)
\quad(4\le k\le n).
\]
Iterating the second identity down to \(\Pr(C_{n-k+3}\ge3)=1/(n-k+3)\) proves the product formula. A graph of maximum degree \(n-1\) receives at most \(n\) FirstFit colors, giving the asserted support and the point probabilities.

For \(k=n\), simplify the product using \(\prod_{r=4}^{n}(2r-1)=(2n)!/[15\,2^n n!]\) to obtain the displayed extremal probability. For the expectation, use the tail-sum identity. Its first excess terms are \(T_{n,3}=1/n\) and \(T_{n,4}=3/[2(2n-1)(n-1)]=3/(4n^2)+O(n^{-3})\). For \(n\ge5\), the next term is \(T_{n,5}=9/[4(2n-1)(2n-3)(n-2)]=O(n^{-3})\). Moreover, successive remaining terms have ratio
\[
\frac{T_{n,k+1}}{T_{n,k}}=\frac{3m}{2(m-1)(2m-1)}\le\frac27,
\qquad m=n-k+3\ge4,
\]
so their sum is \(O(n^{-3})\). This establishes the asymptotic estimate.

## Verification

The accompanying self-contained Python 3 checker at `verification/verify.py` implements FirstFit directly on labeled vertex permutations and independently as a memoized exact enumeration over all prefix-coloring states. For \(n=2,3,4\), it also iterates all \((2n)!\) permutations directly. It compares exact rational distributions against the closed formula through \(n=7\). The \(n=7\) check covers \(14!=87,178,291,200\) orderings by an exact state-summing recurrence (not by listing all orders); it uses \(387,364\) memoized states. The checks agree and additionally verify normalization, expectation from tails, and the maximum-color probability. Run `python3 verification/verify.py` from the extracted file package. Output is recorded in `verification/expected_output.txt`. No exhaustive search over unbounded \(n\) is claimed; the all-\(n\) result is proved by the preceding case split and induction.

## Relationship to prior work

Ye, Xu, Wang, Zheng and Li (2026), Section 3.1, Theorem 3, prove the bound \(\mathbb E[C_n]\le2.5+O(1/n)\) for the same crown graph and uniformly random FirstFit vertex order, by bounding exceptional arrival blocks. Their paper does not state the full color-count law, the exact factorial expression for worst-case color probability, or the sharp mean limit and expansion obtained here. The general forest random-order bounds of Bosek, Gutowski, Lasoń and Przybyło (2024) concern a different graph class and do not imply these crown-graph probabilities. The present result is an exact-law refinement of the crown-graph analysis, not a claim to the invention of crown graphs or the FirstFit algorithm. The proof uses a distinct regenerative first-matched-pair decomposition; the earlier result provides motivation and a weaker bound.

## Limitations

The result applies only to the balanced crown graphs \(K_{n,n}\) with a perfect matching removed, for uniformly random vertex permutations and standard least-available-color FirstFit. It does not establish analogous laws for unbalanced matching-deleted bicliques, weighted/blown-up crowns, other arrival distributions or online coloring algorithms. Reproducible finite tests support the proof but are not an infinite certificate. The primary manuscript was inspected in HTML; there remains a possibility of independently discovered equivalent formulations in unindexed literature. No independent external mathematical audit has been performed.

## References

1. X. Ye, Y. Xu, Z. Wang, J. Zheng and Y. Li, *FirstFit online coloring in the random order model*, arXiv:2608.29603v1, first posted 2026-08-30, especially Section 3.1 and Theorem 3. https://arxiv.org/html/2608.29603v1
2. B. Bosek, G. Gutowski, M. Lasoń and J. Przybyło, *First-Fit Coloring of Forests in Random Arrival Model*, MFCS 2024, LIPIcs 306, Article 33, DOI:10.4230/LIPIcs.MFCS.2024.33. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2024.33
3. A. Gyárfás and J. Lehel, *On-Line and First Fit Colorings of Graphs*, J. Graph Theory 12 (1988), 217–227. https://www.renyi.hu/~gyarfas/Cikkek/33_GyarfasLehel_OnLineAndFirstFitColoringsOfGraphs.pdf
