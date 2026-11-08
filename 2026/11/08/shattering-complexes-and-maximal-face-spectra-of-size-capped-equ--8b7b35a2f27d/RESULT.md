# Shattering complexes and maximal-face spectra of size-capped equivalence relations

## Finding
For integers \(n\ge 1\) and \(r\ge 1\), consider all partitions of the labeled set \([n]\) into blocks of size at most \(r\). A binary query is an unordered pair \(\{u,v\}\), with response one exactly when its vertices lie in the same block. Regard a query support as the edge set of a spanning simple graph \(F\) on \([n]\).

**Complete shattering theorem.** The support is shattered if and only if \(F\) is a forest whose every component contains at most \(r\) vertices. In particular, its complete shattered-support polynomial \(\Phi_{n,r}(z)\) is determined by
\[
\sum_{n\ge 0}\Phi_{n,r}(z)\frac{x^n}{n!}
=\exp\!\left(\sum_{j=1}^{r}\frac{T_j}{j!}x^jz^{j-1}\right),
\qquad T_1=1,\quad T_j=j^{j-2}\ (j\ge2).
\]
The exact static and adaptive learning dimensions coincide:
\[
\operatorname{VCdim}(\mathcal P_{n,r})
=\operatorname{Ldim}(\mathcal P_{n,r})
=n-\left\lceil\frac nr\right\rceil.
\]

**Maximal-face theorem.** A shattered support is inclusion-maximal if and only if its forest component sizes \(s_1,\ldots,s_t\) satisfy \(s_i+s_j>r\) for every pair of different components. Put
\[
a=\lfloor r/2\rfloor+1,\qquad
\delta_r=\begin{cases}1&r\text{ even},\\0&r\text{ odd},\end{cases}
\qquad
T(n,r)=\max\{1,\lfloor(n+\delta_r)/a\rfloor\}.
\]
The cardinalities of the inclusion-maximal shattered supports comprise **every integer** in the exact interval
\[
\boxed{\ n-T(n,r)\ \le k\le\ n-\lceil n/r\rceil\ }.
\]
For example, for \(n=6,r=3\), a three-edge perfect matching and two disjoint three-vertex paths are both inclusion-maximal shattered supports, of cardinalities three and four. The maximal-face-size gap grows linearly in \(n\) for every fixed \(r\ge3\). At \(r=1\), only the empty support is shattered; at \(r\ge n\), every forest is shattered.

## Assumptions and scope
All partitions are **unlabeled collections of nonempty blocks** of a labeled finite set, including the all-singleton partition; block sizes are upper-bounded, not prescribed exactly. Pair queries are distinct unordered pairs. Shattering requires realization of all binary labelings of a fixed support by potentially different admissible partitions. Littlestone dimension means the deterministic realizable binary membership-query mistake-tree dimension. The empty ground set \(n=0\) is permitted only for the exponential generating function, with \(\Phi_{0,r}=1\).

## Proof
**Shattering necessity.** If a query graph contains a cycle, label all but one edges on that cycle one and the remaining edge zero. Transitivity of same-block equality makes the required zero impossible. If a connected component has more than \(r\) vertices, the all-positive labeling forces that entire component into one forbidden oversized block.

**Shattering sufficiency.** For any forest with component sizes at most \(r\) and any chosen subset \(A\) of its edges, form a partition from the connected components of the graph with edge set \(A\). All blocks have size at most \(r\). Every edge of \(A\) lies inside a block. Every edge of the original forest outside \(A\) joins *different* components: otherwise that edge together with the unique path in \(A\) would make a cycle. Thus this partition realizes precisely the given labeling.

**Polynomial.** In a forest, a component of size \(j\) is a labeled tree, with \(T_j\) possibilities by Cayley's formula; it contributes \(j-1\) edges. The exponential formula for sets of labeled components yields the displayed bivariate generating function. Equivalently, root-component decomposition gives the checkable recurrence
\[
\Phi_{0,r}(z)=1,\qquad
\Phi_{n,r}(z)=\sum_{j=1}^{\min(n,r)}\binom{n-1}{j-1}T_jz^{j-1}\Phi_{n-j,r}(z).
\]

**Learning dimensions.** Every spanning forest with \(t\) components has exactly \(n-t\) edges. Under the size bound, \(t\ge\lceil n/r\rceil\). A partition into blocks of size at most \(r\) attaining this minimum, with any tree on each block, gives a shattered support with \(n-\lceil n/r\rceil\) edges, proving the VC formula. For an online realizable sequence, predict equality if a queried pair is already connected by previous positively answered queries, and inequality otherwise. A prediction of equality can never be wrong by transitivity. Each mistaken inequality prediction is followed by an actual positive answer and merges two current connected components. All these components remain within true equality blocks; at least \(\lceil n/r\rceil\) components must survive. There are at most \(n-\lceil n/r\rceil\) mistakes. The standard equivalence between realizable mistake bounds and Littlestone depth gives the upper bound. A shattered support yields a complete fixed-order query tree of its cardinality, giving the matching lower bound.

**Maximal supports and full facet spectrum.** Adding an edge inside any forest component creates a cycle; adding it across two components preserves a forest and merges those components. Such an addition stays shattered precisely when the sum of the two component sizes is at most \(r\). Hence the pairwise strict-sum maximality criterion. For \(t\ge2\) sorted component sizes satisfying it, the minimum possible total size is
\[
m_r(t)=\begin{cases}ta,&r\text{ odd},\\ta-1,&r\text{ even}.\end{cases}
\]
Indeed, when \(r\) is odd, the two smallest sizes must sum to at least \(r+1\), minimizing the total with all sizes \(a\); when \(r\) is even, one size \(a-1\) and the others \(a\) attain the minimum and sorted-size inequalities exclude smaller totals. The maximum possible total is \(tr\). Every intermediate integer occurs by increasing some component sizes, one at a time, from a minimizing tuple to \((r,\ldots,r)\): increasing sizes cannot destroy strict pair sums. A single component is maximal exactly when its size is \(n\le r\). Thus the feasible component counts are exactly the integers from \(\lceil n/r\rceil\) through \(T(n,r)\). Since a forest with \(t\) components has \(n-t\) edges, the claimed full, gap-free facet-cardinality interval follows.

## Verification
Run the accompanying self-contained Python 3 program `verify.py` with the standard library. Its expected terminal marker is `BOUNDED_PARTITION_SHATTERING_PASS 22 202014 16 140`. It independently enumerates admissible set partitions and traces for all supported query subsets through six labeled vertices, compares 202,014 supports with the forest criterion and recurrence, computes exact online recursion for sixteen small parameter pairs, and tests 140 feasible maximal-face spectra. These are **finite corroborations only**; the unrestricted statements follow from the preceding proofs.

## Relationship to prior work
Pasteris, Vitale, Gentile, and Herbster (2018) study online pairwise-clustering prediction with bounded cluster sizes; a forest/union-find mistake estimate is related to their general mistake-bound methods. Their online bounds should not be counted as a novel ingredient here. Bényi, Méndez, Ramírez, and Wakhare (2018) enumerate set partitions with restricted block sizes; the present polynomial is instead a weighted count of **shattered query supports**, using labeled-tree rather than partition-block weights. Guingona, Kolesnikov, Nierwinski, and Soucy (2021) provide the model-theoretic VC/Littlestone framework for other concept classes. The standard Cayley and labeled-forest enumerations are prior knowledge. The present contribution is the exact identification of the query-support complex, its complete parameterized polynomial, and especially the all-parameter **inclusion-maximal-face spectrum** of bounded pair-equality concepts.

## Limitations
This concerns all set partitions with blocks of size **at most** \(r\), not exact-size partitions, ordered interval equivalences, or noncrossing partitions. The theorem does not determine a finer invariant for every adaptive labeling strategy, and the spectrum gives maximal-face sizes rather than a closed count by facet size. Prior equivalent formulations under bounded-size cluster forests or graphic simplicial complexes remain a historical-priority risk. No independent external mathematical audit has been performed.

## References
- G. Conant, A. Pillay, C. Terry, *Structure and regularity for subsets of groups with finite VC-dimension*, arXiv:1802.04246 (first public 2018-02-12); model-theoretic VC context, not a bounded-partition classification.
- S. Pasteris, F. Vitale, C. Gentile, M. Herbster, *On Similarity Prediction and Pairwise Clustering*, Proceedings of Algorithmic Learning Theory, PMLR 83 (2018), pp. 654–681; https://proceedings.mlr.press/v83/pasteris18a.html.
- B. Bényi, M. Méndez, J. L. Ramírez, T. Wakhare, *Restricted r-Stirling Numbers and their Combinatorial Applications*, arXiv:1811.12897 (first public 2018-11-30).
- V. Guingona, A. Kolesnikov, J. Nierwinski, R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805 (first public 2021-09-10).
- Cayley's classical enumeration of labeled trees, used here without a claim of novelty.
